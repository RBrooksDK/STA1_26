# Tutorial 2 — False positives in an automatic test

## 1. Problem / context

A vision system flags solder defects. Historically 2% of boards are defective. The detector catches 95% of defective boards (sensitivity) but also flags 8% of good boards (false-positive rate). If a board is flagged, what is the probability that it is actually defective?

This is Bayes' theorem in an engineering setting.

## 2. Core theory

Let \(D\) be the event that a board is defective and \(F\) the event that it is flagged.

\[
P(D\mid F)=\frac{P(F\mid D)P(D)}{P(F)},
\qquad
P(F)=P(F\mid D)P(D)+P(F\mid D^c)P(D^c).
\]

Here \(P(F\mid D)=0.95\) is **sensitivity**, and \(P(F\mid D^c)=0.08\) is the **false-positive rate**. The quantity we want, \(P(D\mid F)\), is the **positive predictive value**. These three numbers are not the same.

Independence would mean \(P(F\mid D)=P(F)\), which is false here: the flag is designed to depend on the defect.

## 3. From mathematics to Python

We can compute the formula directly, or simulate many boards and count.

| Piece | Symbol | Code idea |
| --- | --- | --- |
| Base rate | \(P(D)\) | `p_d = 0.02` |
| Sensitivity | \(P(F\mid D)\) | `sens = 0.95` |
| False-positive rate | \(P(F\mid D^c)\) | `fpr = 0.08` |
| PPV | \(P(D\mid F)\) | Bayes formula, or `defective[flagged].mean()` in a simulation |

## 4. Python implementation

```python
import numpy as np
import pandas as pd

p_d, sens, fpr = 0.02, 0.95, 0.08
p_f = sens * p_d + fpr * (1 - p_d)
ppv = sens * p_d / p_f
print(f"P(F) = {p_f:.4f}")
print(f"P(D | F) = {ppv:.4f}")
```

```python
rng = np.random.default_rng(42)
n = 100_000
defective = rng.random(n) < p_d
flagged = np.where(
    defective,
    rng.random(n) < sens,
    rng.random(n) < fpr,
)
sim_ppv = defective[flagged].mean()
print(f"Simulated P(D | F) = {sim_ppv:.4f} based on {flagged.sum()} flags")
```

A two-way table for 10,000 boards:

```python
n_table = 10_000
n_def = int(round(p_d * n_table))
n_ok = n_table - n_def
tp = int(round(sens * n_def))
fn = n_def - tp
fp = int(round(fpr * n_ok))
tn = n_ok - fp
table = pd.DataFrame(
    {"flagged": [tp, fp], "not flagged": [fn, tn]},
    index=["defective", "good"],
)
table.loc["total"] = table.sum()
table["total"] = table.sum(axis=1)
table
```

## 5. Interpretation

Even with 95% sensitivity, most flags can be **false** if defects are rare. The positive predictive value is far below 0.95. That is not a bug in Bayes' theorem; it is the base-rate effect. A process engineer who treats every flag as a confirmed defect will over-scrap good boards.

## 6. Common mistakes / things to notice

- Confusing sensitivity \(P(F\mid D)\) with PPV \(P(D\mid F)\).
- Saying “probability 0 means impossible”. For continuous measurements that will be false (Session 04); here the events are discrete and the warning is less urgent.
- Calling mutually exclusive events independent. If \(D\) and \(D^c\) both have positive probability they cannot be independent.

## 7. Short worked example

Suppose the false-positive rate is improved to 1% while everything else stays the same.

```python
fpr2 = 0.01
p_f2 = sens * p_d + fpr2 * (1 - p_d)
ppv2 = sens * p_d / p_f2
print(f"New P(D | F) = {ppv2:.4f}")
```

**Conclusion in one sentence:** After a flag, the probability that the board is actually defective is much lower than the 95% sensitivity, because defects are rare; reducing the false-positive rate is what raises the positive predictive value.
