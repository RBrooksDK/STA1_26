# 00 — Getting Started with Python and Data

## Session preparation

This page is **self-study**. There is no classroom session 00. Work through it before Session 01 so that class time can be spent on statistics, not on installing packages.

**Syllabus and input**

- [Conventions](../pages/conventions.md): notation and Python style used in every later notebook
- [Datasets](../pages/datasets.md): where files live and what they contain
- [Literature](../pages/literature.md): which book belongs to which session

---

## Session focus

The aim is a working analysis environment and a shared language for the rest of the course.

By the end of this page, you should be able to:

- run Python 3.10+ with Jupyter in VS Code or Anaconda;
- import NumPy, Pandas, SciPy, and Matplotlib;
- load a CSV file from the course `data/` folder;
- distinguish a random variable \(X\) from an observed value \(x\);
- compute a sample standard deviation with \(n-1\) degrees of freedom.

---

## Setup

1. Install [Anaconda](https://www.anaconda.com/products/distribution) or a Python 3.10+ interpreter with the Jupyter extension in VS Code.
2. Create a notebook and run:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print(np.__version__, pd.__version__)
```

3. From a session folder, the data directory is one level up:

```python
DATA = Path("../data")
df = pd.read_csv(DATA / "sensor_thickness.csv")
df.head()
```

If you work from the repository root, use `Path("data")` instead.

## Packages used in the course

| Library | Role |
| --- | --- |
| NumPy | Arrays, simulation, numerical summaries |
| Pandas | Tables, import, grouping |
| Matplotlib | Plots |
| SciPy (`scipy.stats`) | Distributions, tests, and probabilities |
| statsmodels | Inference: intervals, ANOVA, regression summaries |
| scikit-learn | Session 10 only: `LinearRegression` and a train/test split |

Install extras if needed:

```text
pip install numpy pandas matplotlib scipy statsmodels scikit-learn openpyxl
```

`openpyxl` is required for `.xlsx` files.

## Notebook hygiene

- Keep a seed whenever you simulate: `rng = np.random.default_rng(42)`.
- Write `ddof=1` when you use `np.std` or `np.var` on a **sample**.
- Never name a Python variable `lambda`.
- Put interpretation in a markdown cell after the code, not only in a `print`.

## What we do not do

- We do not teach a full programming course. If Python is new, use Session 01's tutorial as extra practice on tables and plots.
- We do not use R or Excel as the primary analysis tool.

## Assignments

No assignment is attached to this page. A working setup is assumed from Assignment 1 onwards.
