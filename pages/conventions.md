<h1 align="center">Conventions</h1>

STA1 uses one notation and one Python style across sessions, tutorials, and assignments. If a library uses a different convention, we translate it explicitly.

## Mathematical notation

| Concept | Symbol |
| --- | --- |
| Sample space | \(S\) |
| Events | \(A, B, \ldots\) |
| Conditional probability | \(P(A \mid B)\) |
| Random variable | capital letter: \(X\) |
| Observed value | lower-case letter: \(x\) |
| Sample observations | \(x_1, \ldots, x_n\) |
| Population mean | \(\mu\) |
| Population variance | \(\sigma^2\) |
| Population standard deviation | \(\sigma\) |
| Sample mean (observed) | \(\bar{x}\) |
| Sample variance | \(s^2\) |
| Sample standard deviation | \(s\) |
| Random sample statistics | \(\bar{X}\), \(S^2\) |
| PMF | \(p_X(k) = P(X = k)\) |
| PDF | \(f_X(x)\) |
| CDF | \(F_X(x) = P(X \le x)\) |

### Normal distribution

Always parameterise the normal by mean and **variance**:

\[
X \sim N(\mu, \sigma^2),
\qquad
\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right).
\]

The standard error is written separately:

\[
\operatorname{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}.
\]

SciPy uses the standard deviation: `norm(loc=mu, scale=sigma)`.

### Exponential and Poisson

The exponential uses **rate** \(\lambda\):

\[
T \sim \operatorname{Exp}(\lambda),
\qquad
f_T(t) = \lambda e^{-\lambda t},
\qquad
E[T] = \frac{1}{\lambda}.
\]

If events occur at rate \(\lambda\), then

\[
N(t) \sim \operatorname{Poisson}(\lambda t).
\]

In Python never use the name `lambda`. Write `rate` and convert to SciPy's scale:

```python
from scipy.stats import expon, poisson

rate = 25
waiting_time = expon(scale=1 / rate)
counts = poisson(mu=rate * time)
```

### Sample variance

The sample variance divides by \(n-1\):

\[
s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2.
\]

Pandas uses \(n-1\) by default. NumPy uses \(n\) unless you set `ddof=1`:

```python
df["response_time"].std()      # sample SD
np.std(x, ddof=1)
np.var(x, ddof=1)
```

### Binomial coefficient

Count successes with \(k\):

\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}.
\]

## Python style

Use this import block unless a tutorial needs extra libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("../data")   # from a session folder; Path("data") from the repo root
rng = np.random.default_rng(42)
```

Rules:

- Set a seed or `random_state` whenever you simulate.
- Prefer `scipy.stats` named distributions (`binom`, `poisson`, `norm`, `expon`, `t`) over ad-hoc formulas when computing probabilities.
- Use **statsmodels** for inference (tests, confidence intervals, ANOVA, regression summaries).
- Use **scikit-learn** in Session 10 to fit a prediction model and to illustrate train/test split — not as a substitute for statistical inference.
- Label axes with units.
- End every analysis with a sentence in ordinary language, not only a number.

## Terminology

- **Population** vs **sample**: the complete set of relevant items versus the observed subset.
- **Sample space** vs **sample**: all possible outcomes of a random experiment versus the data you actually collected. These two uses of “sample” are distinguished explicitly in Session 03.
- **Estimator** vs **estimate**: a random variable computed from a sample versus the number you obtained.
- **Statistical significance** vs **practical importance**: a small \(p\)-value is not automatically an engineering problem, and a large effect can fail to be significant in a small sample.
