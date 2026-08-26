---
tags:
    - Python
    - Jupyter
    - Pandas
    - NumPy
    - Data
---

<h1 align="center">Getting Started with Python and Data</h1>

This page is **self-study**. There is no classroom session 00. Work through it before Session 01 so that class time can be spent on statistics, not on installing packages.

The aim is a working analysis environment and a shared language for the rest of the course. Install Python 3.10+ with Jupyter — Anaconda or VS Code with the Jupyter extension is enough — and confirm that you can import NumPy, Pandas, SciPy, and Matplotlib, then load a CSV file from the course `data/` folder.

From a session folder the data directory is one level up:

```python
import pandas as pd
from pathlib import Path

DATA = Path("../data")
df = pd.read_csv(DATA / "sensor_thickness.csv")
df.head()
```

If you work from the repository root, use `Path("data")` instead. `openpyxl` is required for `.xlsx` files.

#### Key Concepts

- Python, Jupyter, and the course package stack
- Loading CSV and Excel files from `data/`
- Random variables versus observed values
- Sample standard deviation with \(n-1\)
- Seeds, `ddof=1`, and notebook hygiene

!!! tip "Learning Objectives"

    - Run Python 3.10+ with Jupyter in VS Code or Anaconda.
    - Import NumPy, Pandas, SciPy, and Matplotlib.
    - Load a CSV file from the course `data/` folder.
    - Distinguish a random variable \(X\) from an observed value \(x\).
    - Compute a sample standard deviation with \(n-1\) degrees of freedom.

<hr/>

### Session Preparation:

This is self-study. Complete it before Session 01.

Install extras if needed:

```text
pip install numpy pandas matplotlib scipy statsmodels scikit-learn openpyxl
```

When you simulate, keep a seed: `rng = np.random.default_rng(2026)`. Write `ddof=1` when you use `np.std` or `np.var` on a **sample**. Never name a Python variable `lambda`. Put interpretation in a markdown cell after the code, not only in a `print`.

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/00_Getting_Started_with_Python_and_Data/session_material)

[Datasets](../pages/datasets.md)

[Anaconda](https://www.anaconda.com/products/distribution)

<hr/>

### Exercises
