"""Convert course tutorial markdown files to Jupyter notebooks.

A markdown file is split on fenced ```python code blocks. Surrounding
prose becomes markdown cells; each fence becomes a code cell.

Usage:
    python tools/md_to_notebook.py
    python tools/md_to_notebook.py --file 01_Data_and_Descriptive_Statistics/Tutorial_01.md
"""

from __future__ import annotations

import argparse
import json
import re
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FENCE = re.compile(r"^```(?:python)?\s*$", re.IGNORECASE)
DISPLAY_MATH = re.compile(r"\\\[([\s\S]*?)\\\]")
INLINE_MATH = re.compile(r"\\\(([\s\S]*?)\\\)")


def notebook_math_delimiters(text: str) -> str:
    """Use $ delimiters in notebooks so nbconvert HTML keeps math for MathJax."""

    def display_repl(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        return f"$$\n{body}\n$$"

    def inline_repl(match: re.Match[str]) -> str:
        return f"${match.group(1).strip()}$"

    text = DISPLAY_MATH.sub(display_repl, text)
    text = INLINE_MATH.sub(inline_repl, text)
    return text


def md_to_cells(text: str) -> list[dict]:
    lines = text.replace("\r\n", "\n").split("\n")
    cells: list[dict] = []
    buf: list[str] = []
    in_code = False

    def flush_md() -> None:
        content = "\n".join(buf).strip("\n")
        buf.clear()
        if content.strip():
            content = notebook_math_delimiters(content)
            cells.append(
                {
                    "cell_type": "markdown",
                    "id": uuid.uuid4().hex[:12],
                    "metadata": {},
                    "source": _as_source(content + "\n"),
                }
            )

    def flush_code() -> None:
        content = "\n".join(buf).strip("\n")
        buf.clear()
        cells.append(
            {
                "cell_type": "code",
                "id": uuid.uuid4().hex[:12],
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": _as_source((content + "\n") if content else ""),
            }
        )

    for line in lines:
        if FENCE.match(line):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_md()
                in_code = True
            continue
        buf.append(line)

    if in_code:
        flush_code()
    else:
        flush_md()
    return cells


def _as_source(text: str) -> list[str]:
    if not text:
        return []
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] != "" else [])


def write_notebook(md_path: Path, nb_path: Path | None = None) -> Path:
    cells = md_to_cells(md_path.read_text(encoding="utf-8"))
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "cells": cells,
    }
    if nb_path is None:
        nb_path = md_path.with_name(md_path.stem + "_notebook.ipynb")
        # Tutorial_01.md -> Tutorial_01_notebook.ipynb
        if md_path.stem.startswith("Tutorial_") and not md_path.stem.endswith("_notebook"):
            nb_path = md_path.with_name(md_path.stem + "_notebook.ipynb")
    nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return nb_path


def patch_notebook_math(nb_path: Path) -> bool:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        original = "".join(cell.get("source", []))
        updated = notebook_math_delimiters(original)
        if updated != original:
            cell["source"] = _as_source(updated)
            changed = True
    if changed:
        nb_path.write_text(
            json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    return changed


def discover() -> list[Path]:
    return sorted(ROOT.glob("*/Tutorial_*.md"))


def discover_notebooks() -> list[Path]:
    return sorted(ROOT.glob("*/Tutorial_*_notebook.ipynb"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, default=None)
    parser.add_argument(
        "--patch-math",
        action="store_true",
        help="Convert \\(...\\) and \\[...\\] to $ delimiters in existing notebooks",
    )
    args = parser.parse_args()

    if args.patch_math:
        paths = [args.file] if args.file else discover_notebooks()
        for nb in paths:
            nb = nb if nb.is_absolute() else ROOT / nb
            if patch_notebook_math(nb):
                print(f"patched {nb.relative_to(ROOT)}")
        return

    paths = [args.file] if args.file else discover()
    for md in paths:
        md = md if md.is_absolute() else ROOT / md
        out = write_notebook(md)
        print(f"{md.relative_to(ROOT)} -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
