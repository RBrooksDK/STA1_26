# 05 — Sampling Distributions and the Central Limit Theorem

## Session preparation

Read Ross 6.1–6.3 and selected parts of 6.4–6.5.

**Syllabus and input**

- Ross 6.1 Introduction
- Ross 6.2 The sample mean
- Ross 6.3 The central limit theorem
- Selected parts of 6.4–6.5 (sample variance; sampling from a normal population)
- [Session material](https://github.com/RBrooksDK/STA1_26/tree/main/05_Sampling_Distributions_and_the_CLT/session_material)

---

## Session focus

A statistic such as \(\bar{X}\) is itself a random variable. Its distribution — the sampling distribution — is the reason later confidence intervals and tests work. The CLT is demonstrated by simulation, not proved.

By the end of the session, you should be able to:

- describe the sampling distribution of \(\bar{X}\) and write \(\operatorname{SE}(\bar{X}) = \sigma / \sqrt{n}\);
- use \(N(\mu, \sigma^2 / n)\) when the CLT applies, never \(N(\mu, \sigma / \sqrt{n})\);
- simulate repeated samples and watch the histogram of \(\bar{x}\) become approximately normal;
- state when the CLT helps (means, large \(n\)) and when it does not (small \(n\), strong skew, interest in a single observation).

<p align="left">
  <a href="Tutorial_05_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Tutorial 5: From one sample to many</strong>
  </a>
</p>

[Download notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA1_26/main/05_Sampling_Distributions_and_the_CLT/Tutorial_05_notebook.ipynb)
&nbsp;·&nbsp;
[Read as markdown](Tutorial_05.md/)

---

## Scope boundary

- Finite-population corrections (Ross 6.6)
- Proving the CLT
- Confusing the distribution of the raw data with the distribution of the mean

---

## Assignments

This session completes **[Assignment 3](../pages/assignments.md)**: continuous models, sampling, and the CLT.

The [assessment page](Exercises.md) is reserved for Assignment 3 material,
which will be published during the semester.
