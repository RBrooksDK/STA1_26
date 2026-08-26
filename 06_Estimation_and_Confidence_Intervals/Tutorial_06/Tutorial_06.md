# Tutorial 6 — How precise is this measurement?

## 1. Problem / context

Quality reports a mean thickness from a sample of plates. A single number is not enough: we need an interval that communicates precision. We also check, by simulation, that a 95% interval covers the true mean about 95% of the time.

## 2. Core theory

An **estimator** \(\hat\theta\) is a random variable; an **estimate** is the number we got.

A confidence interval for a normal mean with unknown \(\sigma\) uses Student's \(t\):

\[
\bar{x}\pm t_{n-1,1-\alpha/2}\,\frac{s}{\sqrt{n}}.
\]

A 95% interval does **not** mean “the probability that \(\mu\) lies in this realised interval is 0.95”. After the data are seen the interval either covers \(\mu\) or it does not. The 95% refers to the **procedure**.

For a proportion, a simple approximation is

\[
\hat p \pm z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}.
\]

A **bootstrap** interval resamples the data and uses percentiles of the resampled means as a computational check.

## 3. From mathematics to Python

`scipy.stats.t.interval` and `norm.interval` take `loc` and `scale`, where `scale` is the standard error.

## 4. Python implementation

```python
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import t, norm, bootstrap

candidates = [Path("data"), Path("../data")]
DATA = next(p for p in candidates if p.exists())
x = pd.read_csv(DATA / "sensor_thickness.csv")["thickness_um"].to_numpy()

n = x.size
mean = x.mean()
s = x.std(ddof=1)
se = s / np.sqrt(n)
ci = t.interval(0.95, df=n - 1, loc=mean, scale=se)
print(f"n={n}, mean={mean:.3f} µm, s={s:.3f} µm")
print("95% t-interval:", ci)
```

Coverage simulation from a known normal:

```python
rng = np.random.default_rng(0)
mu_true, sigma_true, n_sim, n_rep = 250.0, 4.2, 20, 2000
covers = 0
for _ in range(n_rep):
    sample = rng.normal(mu_true, sigma_true, size=n_sim)
    m, ss = sample.mean(), sample.std(ddof=1)
    lo, hi = t.interval(0.95, df=n_sim - 1, loc=m, scale=ss / np.sqrt(n_sim))
    covers += lo <= mu_true <= hi
print("Estimated coverage:", covers / n_rep)
```

Bootstrap percentile interval:

```python
res = bootstrap((x,), np.mean, confidence_level=0.95, random_state=42, method="percentile")
print("Bootstrap 95% interval:", (res.confidence_interval.low, res.confidence_interval.high))
```

Proportion of plates above 255 µm:

```python
phat = (x > 255).mean()
se_p = np.sqrt(phat * (1 - phat) / n)
z = norm.ppf(0.975)
print("hat p =", phat, "  95% interval:", (phat - z * se_p, phat + z * se_p))
```

## 5. Interpretation

The \(t\)-interval is a statement about the **mean thickness**, not about an individual plate. Individual plates vary by about \(s\), which is much wider. The coverage experiment should land near 0.95 if the normal model and the \(t\) procedure are appropriate. Bootstrap is a check, not a second official syllabus chapter.

## 6. Common mistakes / things to notice

- Interpreting 95% as a probability about this one interval after seeing the data.
- Using \(z\) with a small sample and unknown \(\sigma\).
- Reporting a tiny interval for the mean as if every plate lay in that interval.

## 7. Short worked example

How does doubling \(n\) change the half-width of a \(z\)-interval? It scales by \(1/\sqrt{2}\approx 0.71\), not by \(1/2\).

```python
print("Half-width ratio if n doubles:", 1 / np.sqrt(2))
```

**Conclusion in one sentence:** The mean thickness is estimated with a \(t\)-interval whose width is governed by \(s/\sqrt{n}\); 95% describes the long-run coverage of the method, not a probability attached to \(\mu\) after the sample is in hand.
