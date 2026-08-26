# STA1 intro animation

Manim Community (ManimCE) is **not** installed by the site `requirements.txt`. Use a separate virtual environment.

```powershell
cd C:\GitHub\STA1_26
python -m venv .venv-manim
.\.venv-manim\Scripts\Activate.ps1
pip install -r manim\requirements-manim.txt
```

LaTeX (MiKTeX or TeX Live) is required for `MathTex`.

Preview (480p15):

```powershell
manim -ql manim\sta_intro.py StatsIntroLight
manim -ql manim\sta_intro.py StatsIntroDark
```

Production (1080p60):

```powershell
manim -qh manim\sta_intro.py StatsIntroLight
manim -qh manim\sta_intro.py StatsIntroDark
```

Copy the merged files:

```text
manim\media\videos\sta_intro\1080p60\StatsIntroLight.mp4  ->  figures\sta_intro_light.mp4
manim\media\videos\sta_intro\1080p60\StatsIntroDark.mp4   ->  figures\sta_intro_dark.mp4
```

The two scenes share timing and motion; only background and colours change.
