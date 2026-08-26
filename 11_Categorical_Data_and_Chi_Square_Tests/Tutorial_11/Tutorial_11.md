# Tutorial 11 — Defect types across production lines

## 1. Problem / context

Each recorded defect is labelled solder, alignment, contamination, or other, and comes from line L1, L2, or L3 (`defect_types.csv`). Operations wants to know whether the **mix** of defect types differs by line. That is a test of independence in a contingency table, not a \(t\)-test on a mean.

## 2. Core theory

A **contingency table** counts observations in category pairs. Under independence, expected counts are

\[
E_{ij}=\frac{(\text{row \(i\) total})\times(\text{column \(j\) total})}{n}.
\]

The Pearson statistic is \(\chi^2=\sum\frac{(O_{ij}-E_{ij})^2}{E_{ij}}\). A common guideline is that expected counts should not be too small (a traditional rule of thumb is most \(E_{ij}\ge 5\)).

**Goodness-of-fit** compares one categorical variable with a specified (or estimated) distribution. **Independence** compares two categorical variables.

Standardised residuals show **which cells** drive a significant result.

## 3. From mathematics to Python

`scipy.stats.chi2_contingency` returns \(\chi^2\), \(p\), degrees of freedom, and expected counts.

## 4. Python implementation

```python
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import chi2_contingency, chisquare

candidates = [Path("data"), Path("../data")]
DATA = next(p for p in candidates if p.exists())
df = pd.read_csv(DATA / "defect_types.csv")
table = pd.crosstab(df["line"], df["defect_type"])
table
```

```python
chi2, p, dof, expected = chi2_contingency(table)
print("chi2 =", chi2, " p =", p, " dof =", dof)
print("Expected counts:\n", expected)
print("Min expected:", expected.min())
resid = (table.to_numpy() - expected) / np.sqrt(expected)
print("Pearson residuals:\n", np.round(resid, 2))
```

Goodness-of-fit against equal defect types overall:

```python
counts = df["defect_type"].value_counts().sort_index()
print(counts)
print(chisquare(counts))
```

## 5. Interpretation

If \(p\) is small, the defect-type profile is not the same across lines (under the usual chi-square model). Look at residuals: a large positive residual means more defects of that type than independence predicts. A significant result is not by itself a root-cause analysis.

## 6. Common mistakes / things to notice

- Chi-square on a table of **percentages** instead of **counts**.
- Treating a tiny expected count as harmless.
- Confusing GOF (one margin versus a theory) with independence (two margins).

## 7. Short worked example

A shift reports 50, 30, 20 defects of three types and claims they should be 40%, 40%, 20%. That is GOF, not independence.

```python
obs = np.array([50, 30, 20])
exp = np.array([0.4, 0.4, 0.2]) * obs.sum()
print(chisquare(obs, f_exp=exp))
```

**Conclusion in one sentence:** Use a chi-square test of independence on **counts** of defect type by line, check expected frequencies, and read residuals to see which combinations deviate from a common mix.
