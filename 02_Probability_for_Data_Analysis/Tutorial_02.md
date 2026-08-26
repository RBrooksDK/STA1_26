# Tutorial 2 — Probability tools for automated inspection

## 1. Problem / context

An automated vision system flags possible solder defects on circuit boards. Historically, 2% of boards are defective. The system flags 95% of defective boards, but it also flags 8% of good boards.

We will use this one engineering case to practise the complete Session 2 workflow:

1. define outcomes and events;
2. use complements, unions, and intersections;
3. read conditional probabilities from a contingency table;
4. distinguish independence from mutual exclusivity;
5. combine paths with total probability;
6. reverse the conditioning with Bayes' theorem;
7. verify the calculation in Python and by simulation.

Let \(D\) mean that a board is defective and \(F\) mean that it is flagged. The model inputs are

\[
P(D)=0.02,\qquad P(F\mid D)=0.95,\qquad P(F\mid D^c)=0.08.
\]

## 2. Events and probability rules

If we record both the physical condition and the system decision, a suitable sample space is

\[
S=\{D\cap F,\ D\cap F^c,\ D^c\cap F,\ D^c\cap F^c\}.
\]

The complement \(F^c\) means “not flagged”. The union \(D\cup F\) means “defective or flagged, including both”, while \(D\cap F\) means “defective and flagged”.

The multiplication rule gives the four path probabilities. The addition rule then combines mutually exclusive paths.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p_defect = 0.02
sensitivity = 0.95
false_positive_rate = 0.08

p_defect_and_flag = p_defect * sensitivity
p_good_and_flag = (1 - p_defect) * false_positive_rate
p_flag = p_defect_and_flag + p_good_and_flag
p_not_flag = 1 - p_flag
p_defect_or_flag = p_defect + p_flag - p_defect_and_flag

pd.Series(
    {
        "P(D and F)": p_defect_and_flag,
        "P(F)": p_flag,
        "P(not F)": p_not_flag,
        "P(D or F)": p_defect_or_flag,
    }
)
```

Before continuing, explain why \(P(D\cup F)\) is not \(P(D)+P(F)\). Which boards would otherwise be counted twice?

## 3. Natural frequencies and a contingency table

Probabilities are often easier to interpret as expected counts. For a hypothetical batch of 10,000 boards, the model gives 200 defective and 9,800 good boards. These are model-based expected counts, not newly observed data.

```python
n = 10_000
n_defective = round(n * p_defect)
n_good = n - n_defective

true_positive = round(n_defective * sensitivity)
false_negative = n_defective - true_positive
false_positive = round(n_good * false_positive_rate)
true_negative = n_good - false_positive

table = pd.DataFrame(
    {
        "flagged": [true_positive, false_positive],
        "not_flagged": [false_negative, true_negative],
    },
    index=["defective", "good"],
)
table["total"] = table.sum(axis=1)
table.loc["total"] = table.sum(axis=0)
table
```

A conditional probability restricts the denominator to the stated reference group. Compare the denominators below.

```python
sensitivity_from_table = (
    table.loc["defective", "flagged"] / table.loc["defective", "total"]
)
false_positive_rate_from_table = (
    table.loc["good", "flagged"] / table.loc["good", "total"]
)
positive_predictive_value = (
    table.loc["defective", "flagged"] / table.loc["total", "flagged"]
)

pd.Series(
    {
        "P(F | D), sensitivity": sensitivity_from_table,
        "P(F | not D), false-positive rate": false_positive_rate_from_table,
        "P(D | F), positive predictive value": positive_predictive_value,
    }
)
```

The same numerator, 190, appears in both \(P(F\mid D)\) and \(P(D\mid F)\), but their denominators answer different questions.

## 4. Independence is not mutual exclusivity

If \(D\) and \(F\) were independent, learning that a board is defective would not change its probability of being flagged:

\[
P(F\mid D)=P(F),
\]

or equivalently \(P(D\cap F)=P(D)P(F)\). Check both sides.

```python
independence_check = pd.Series(
    {
        "P(F | D)": sensitivity,
        "P(F)": p_flag,
        "P(D and F)": p_defect_and_flag,
        "P(D)P(F)": p_defect * p_flag,
    }
)
independence_check
```

The events are clearly dependent. They are not mutually exclusive either: a board can be both defective and flagged, so \(P(D\cap F)>0\).

## 5. Total probability and Bayes' theorem

The flagged boards arrive through two mutually exclusive paths:

\[
P(F)=P(F\mid D)P(D)+P(F\mid D^c)P(D^c)=0.0974.
\]

Bayes' theorem reverses the conditioning:

\[
P(D\mid F)
=\frac{P(F\mid D)P(D)}{P(F)}
=\frac{0.95(0.02)}{0.95(0.02)+0.08(0.98)}
\approx 0.195.
\]

```python
ppv = sensitivity * p_defect / p_flag
print(f"P(flag) = {p_flag:.4f}")
print(f"P(defect | flag) = {ppv:.4f}")
```

Although sensitivity is 95%, a flagged board has only about a 19.5% probability of being defective. The large population of good boards produces many more false alarms than the small population of defective boards produces true alarms.

## 6. The base-rate effect

Hold sensitivity and false-positive rate fixed, and vary only the defect base rate.

```python
base_rates = np.linspace(0.0, 0.20, 401)
ppv_curve = (
    sensitivity * base_rates
    / (sensitivity * base_rates + false_positive_rate * (1 - base_rates))
)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(base_rates, ppv_curve, label="Positive predictive value")
ax.scatter([p_defect], [ppv], color="tab:orange", zorder=3, label="Worked example")
ax.axvline(p_defect, color="0.35", linestyle="--", linewidth=1)
ax.set(xlabel="Defect base rate", ylabel="Positive predictive value")
ax.set_xlim(0, 0.20)
ax.set_ylim(0, 0.80)
ax.grid(alpha=0.2)
ax.legend()
plt.show()
```

The detector has the same sensitivity and false-positive rate throughout the plot, yet its predictive value changes substantially. Performance measures must therefore be interpreted together with the population in which the system is used.

## 7. Exact probability and simulation

Simulation checks the long-run interpretation; it does not replace the exact calculation.

```python
rng = np.random.default_rng(2026)
n_sim = 100_000

defective = rng.random(n_sim) < p_defect
flagged = np.where(
    defective,
    rng.random(n_sim) < sensitivity,
    rng.random(n_sim) < false_positive_rate,
)

simulated_ppv = defective[flagged].mean()
print(f"Exact P(defect | flag) = {ppv:.4f}")
print(f"Simulated P(defect | flag) = {simulated_ppv:.4f}")
print(f"Number of simulated flags = {flagged.sum():,}")
```

Run the cell again with \(n_{\mathrm{sim}}=1{,}000\), \(10{,}000\), and \(1{,}000{,}000\). The estimates fluctuate, but the fluctuation generally becomes smaller as the sample size grows.

## 8. Engineering improvement and interpretation

Suppose the false-positive rate is reduced from 8% to 1%, while sensitivity remains 95%.

```python
improved_fpr = 0.01
improved_p_flag = (
    sensitivity * p_defect + improved_fpr * (1 - p_defect)
)
improved_ppv = sensitivity * p_defect / improved_p_flag

print(f"Original PPV = {ppv:.3f}")
print(f"Improved PPV = {improved_ppv:.3f}")
```

A flag is evidence, not proof. Whether a board should be scrapped, retested, or accepted also depends on the costs of missed defects, unnecessary scrap, and confirmation.

## 9. Check your understanding

1. Use the table to compute \(P(F^c\mid D)\) and \(P(D^c\mid F^c)\). State each denominator in words.
2. Explain why \(F\) and \(F^c\) are mutually exclusive but not independent.
3. Change the defect base rate to 10% without changing the detector. Recompute \(P(F)\) and \(P(D\mid F)\).
4. A colleague claims: “The detector is 95% accurate, so 95% of its flags are correct.” Correct the statement using the appropriate probability notation.
5. Describe one piece of real operating data you would monitor before trusting this model in a new production line.

**Conclusion:** Tables, trees, and Bayes' theorem are three views of the same probability model. The essential discipline is to identify the event after the conditioning bar and use the correct reference group.
