# Tutorial 7 — Does the process meet the specification?

## 1. Problem / context

The specification for mean plate thickness is \(\mu=250\) µm. A sample mean of about 250.something does not automatically mean the process is on target. We test

\[
H_0:\mu=250
\quad\text{versus}\quad
H_1:\mu\neq 250
\]

and also look at a one-sided alternative if the concern is only “too thick”.

## 2. Core theory

- \(H_0\) is the default claim we will retain unless the data are unusual under it.
- The **\(p\)-value** is \(P(\text{data as extreme as observed or more}\mid H_0)\). It is not \(P(H_0\mid\text{data})\).
- **Type I error**: reject a true \(H_0\) (rate \(\alpha\), often 0.05). **Type II error**: fail to reject a false \(H_0\). **Power** is \(1-\beta\).
- One-sample \(t\)-test: \(t=\dfrac{\bar{x}-\mu_0}{s/\sqrt{n}}\), compared with \(t_{n-1}\).
- A two-sided test at level \(\alpha\) rejects \(H_0\) exactly when \(\mu_0\) lies outside a \((1-\alpha)\) confidence interval (duality).

For a proportion, `scipy.stats.binomtest` is the modern interface.

## 3. From mathematics to Python

| Test | SciPy |
| --- | --- |
| One-sample \(t\) | `ttest_1samp(x, popmean=mu0, alternative="two-sided")` |
| One-sided greater | `alternative="greater"` |
| Proportion | `binomtest(k, n, p=p0, alternative="two-sided")` |

## 4. Python implementation

```python
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import ttest_1samp, t, binomtest

candidates = [Path("data"), Path("../data")]
DATA = next(p for p in candidates if p.exists())
x = pd.read_csv(DATA / "sensor_thickness.csv")["thickness_um"].to_numpy()

mu0 = 250.0
res = ttest_1samp(x, popmean=mu0, alternative="two-sided")
print(res)

n, mean, s = x.size, x.mean(), x.std(ddof=1)
se = s / np.sqrt(n)
t_obs = (mean - mu0) / se
p_two = 2 * t.sf(abs(t_obs), df=n - 1)
print("manual t =", t_obs, " p =", p_two)
print("95% CI:", t.interval(0.95, df=n - 1, loc=mean, scale=se))
```

```python
# One-sided: is the mean greater than 250?
print(ttest_1samp(x, popmean=250, alternative="greater"))

# Proportion of plates above 258 µm versus p0 = 0.05
k = (x > 258).sum()
print("k =", k, " n =", n)
print(binomtest(int(k), n=n, p=0.05, alternative="two-sided"))
```

## 5. Interpretation

Report the test statistic, the \(p\)-value, the alternative, and a sentence about the specification. If \(p\) is small, the sample mean is hard to reconcile with \(\mu=250\) under the usual normal/\(t\) model. If \(p\) is large, we **do not prove** that \(\mu=250\); we only failed to detect a departure with this sample.

## 6. Common mistakes / things to notice

- “\(p=0.04\) means there is a 4% chance that \(H_0\) is true.”
- Equating “not significant” with “the process is exactly on target”.
- Mixing one-sided and two-sided after seeing the data.
- Ignoring the CI: it shows **how far** from 250 the plausible means are.

## 7. Short worked example

Five calibration voltages: 4.97, 5.01, 4.99, 5.03, 4.98. Test \(\mu=5.00\) at \(\alpha=0.05\).

```python
volt = np.array([4.97, 5.01, 4.99, 5.03, 4.98])
print(ttest_1samp(volt, popmean=5.00))
```

**Conclusion in one sentence:** A one-sample \(t\)-test asks whether the observed mean thickness is compatible with the 250 µm specification; the \(p\)-value is a tail probability under \(H_0\), and the confidence interval tells us which mean values remain plausible.
