# Tutorial 8 — A/B test of response times

## 1. Problem / context

We compare two server configurations. The file `response_times.csv` contains:

- `server_a_ms` and `server_b_ms`: two **independent** samples (different requests);
- `server_b_paired_ms`: a **paired** measurement on the same requests as A (e.g. replayed traffic).

The design decides the test.

## 2. Core theory

**Independent two-sample \(t\)** (equal variance) versus **Welch's \(t\)** (unequal variance). STA1 prefers Welch as the default for independent groups unless a pooled model is justified.

**Paired \(t\)**: analyse the differences \(d_i=A_i-B_i\), then a one-sample test on \(\bar{d}\).

Effect size (Cohen's \(d\)) and a CI for the difference keep “significant” from being confused with “large enough to matter”.

Battery lifetimes in `batteries.xlsx` are another independent two-group example.

## 3. From mathematics to Python

| Design | SciPy |
| --- | --- |
| Independent, Welch | `ttest_ind(a, b, equal_var=False)` |
| Independent, pooled | `ttest_ind(a, b, equal_var=True)` |
| Paired | `ttest_rel(a, b)` |
| Levene (variances) | `levene(a, b)` |

Always set `alternative=` explicitly.

## 4. Python implementation

```python
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import ttest_ind, ttest_rel, levene, t

candidates = [Path("data"), Path("../data")]
DATA = next(p for p in candidates if p.exists())
df = pd.read_csv(DATA / "response_times.csv")
a, b = df["server_a_ms"], df["server_b_ms"]
b_paired = df["server_b_paired_ms"]

print("Levene:", levene(a, b))
print("Welch:", ttest_ind(a, b, equal_var=False, alternative="two-sided"))
print("Pooled:", ttest_ind(a, b, equal_var=True, alternative="two-sided"))
print("Paired:", ttest_rel(a, b_paired, alternative="two-sided"))
```

CI for the Welch difference (approximate, Welch–Satterthwaite df from the test):

```python
res = ttest_ind(a, b, equal_var=False)
na, nb = a.size, b.size
se = np.sqrt(a.var(ddof=1) / na + b.var(ddof=1) / nb)
diff = a.mean() - b.mean()
df_w = res.df
ci = t.interval(0.95, df=df_w, loc=diff, scale=se)
print("Mean difference A-B:", diff)
print("95% CI:", ci)
```

```python
s_pooled = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
cohens_d = diff / s_pooled
print("Cohen's d (pooled SD):", cohens_d)
```

```python
batt = pd.read_excel(DATA / "batteries.xlsx")
print(ttest_ind(batt["Producer 1"], batt["Producer 2"], equal_var=False))
```

## 5. Interpretation

Independent and paired analyses answer different questions. Pairing removes request-to-request variation and is often more powerful **if** the pairing is real. Do not pair unrelated requests. A 9 ms mean drop can be statistically significant and still irrelevant if users cannot notice it — or the opposite.

## 6. Common mistakes / things to notice

- Running `ttest_ind` on paired data (wrong variance).
- Reporting only a \(p\)-value without the CI for the difference.
- Choosing the alternative after looking at which mean is larger.

## 7. Short worked example

If the paired improvement is the scientifically relevant design, the test is `ttest_rel(server_a, server_b_paired)`. State \(H_0: \mu_D=0\) for the mean difference.

**Conclusion in one sentence:** Compare servers with a test that matches the design — Welch for independent traffic, paired \(t\) for the same requests — and report the interval for the difference so that practical importance can be judged.
