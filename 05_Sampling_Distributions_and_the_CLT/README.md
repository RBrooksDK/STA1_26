---
tags:
    - Sampling Distributions
    - Standard Error
    - Central Limit Theorem
---

<h1 align="center">Sampling Distributions and the Central Limit Theorem</h1>

A statistic such as \(\bar{X}\) is itself a random variable. Its distribution — the sampling distribution — is the reason later confidence intervals and tests work. One sample gives one \(\bar{x}\); many samples give a distribution of \(\bar{x}\).

The standard error of the mean is \(\operatorname{SE}(\bar{X}) = \sigma / \sqrt{n}\). When the observations are i.i.d. normal, \(\bar{X} \sim N(\mu, \sigma^2 / n)\) for every \(n\). For a non-normal i.i.d. population the CLT gives \(\bar{X} \approx N(\mu, \sigma^2 / n)\), never \(N(\mu, \sigma / \sqrt{n})\). The theorem is demonstrated by simulation, not proved. It helps for means and reasonably large \(n\); it does not turn a single skewed observation into a normal one.

#### Key Concepts

- A statistic as a random variable
- Sampling distribution of \(\bar{X}\)
- Standard error \(\sigma / \sqrt{n}\)
- Notation \(N(\mu, \sigma^2 / n)\)
- When the CLT helps and when it does not

!!! tip "Learning Objectives"

    - Describe the sampling distribution of \(\bar{X}\) and write \(\operatorname{SE}(\bar{X}) = \sigma / \sqrt{n}\).
    - Use \(N(\mu, \sigma^2 / n)\) when the CLT applies.
    - Simulate repeated samples and watch the histogram of \(\bar{x}\) become approximately normal.
    - State when the CLT helps (means, large \(n\)) and when it does not (small \(n\), strong skew, a single observation).

<hr/>

### Session Preparation:

Brooks: [Chapter 5](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/05_Sampling_Distributions_and_the_CLT/session_material)

[Tutorial 5: From one sample to many](Tutorial_05_notebook.ipynb)
