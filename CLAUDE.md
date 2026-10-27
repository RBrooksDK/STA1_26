# STA1_26 – Statistics and Data Analysis for Engineers

Kursusside (engelsk) for STA1, efterår 2026 (start 1. september 2026). Kursussiden og bogen i `C:\GitHub\STA_book_v1` udvikles som ét sæt materialer.

## Styrende dokumenter (læs før ændringer i indhold eller scope)

- `source_map.md` – redaktionelt kildekort for kursusside og bog. Scope-ændringer registreres her og i kontrakten, før de rulles ud.
- `planning/CHAPTER_SESSION_CONTRACT.md` – én-til-én-kobling: session NN ↔ bogens kapitel NN ↔ Tutorial NN. Session 00 ↔ Appendix A.
- `planning/STYLE_AND_NOTATION.md` – stemme, notation og Python-konventioner for side, tutorials, opgaver og bog.
- `planning/PROJECT_PLAN.md` – leveranceplan og faste beslutninger.
- `pages/conventions.md` – den notation, de studerende ser (fx \(N(\mu, \sigma^2)\) med varians, eksponential med rate \(\lambda\)).

Kopier af kontrakt, stilguide og kildekort ligger også i `STA_book_v1/planning/`. De to sæt er ikke ens; versionerne her er senest ændret (31.08.2026 mod 29.08.2026). Spørg, før de synkroniseres.

Sessionsmappen `09_Analysis_of_Variance` er en del af kursussiden. Reglen om ingen ANOVA gælder kun den generelle kursusbeskrivelse.

## Struktur

- `00_...` til `12_...`: hver session har `README.md`, `Tutorial_NN.md`, `Tutorial_NN_notebook.ipynb` og evt. `session_material/`.
- `assignments/` (seks gruppeopgaver), `pages/` (exam, project, datasets, faq, recording m.fl.), `blog/`, `data/`.
- `Sessions/README.md` – oversigt over sessioner og hvilke opgaver de fører til.

## Tutorials og notebooks

- `Tutorial_NN.md` er kilden; notebooken genereres med `python tools/md_to_notebook.py` (alle) eller `--file <sti>`. Ret i markdown-filen, ikke direkte i notebooken.
- `Tutorial_[0-9][0-9].md` er udelukket fra bygget; siden linker til notebooken.
- `mkdocs-jupyter` kører med `execute: false`, så output skal være gemt i notebooken. Afvikl den, før den committes.
- Datasæt genereres reproducerbart med `python tools/generate_datasets.py` (seed 2026). De sande parametre står i `data/generation_log.json`.

## Må ikke publiceres

- `instructor_material/` og `/manim/` er ignoreret af git og må aldrig committes.
- `.gitignore` holder noter (`*Notes*`, `*Annote*`) ude af `session_material/`.
- `planning/`, `tools/`, `source_map.md`, `pages/literature.md` og `pages/conventions.md` er udelukket fra bygget via `exclude_docs`. Nye interne filer i roden skal også tilføjes dér, fordi `docs_dir: .` ellers udgiver dem.

## Byg og CI

- Lokalt: `.venv\Scripts\mkdocs build --strict` (Python 3.12-miljø; Python 3.14 giver template-fejl i mkdocs-jupyter).
- CI (`ci.yml`) bygger med `--strict` og deployer med `mkdocs gh-deploy`.
