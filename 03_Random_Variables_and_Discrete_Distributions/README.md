# 03 — Random Variables and Discrete Distributions

## Session preparation

Read Ross 4.1–4.2, 4.4, 4.6 and 5.1–5.2. The binomial coefficient is introduced here, where the binomial model uses it.

**Syllabus and input**

- Ross 4.1 Random variables
- Ross 4.2 Types of random variables
- Ross 4.4 Expectation
- Ross 4.6 Variance
- Ross 5.1 Bernoulli and binomial
- Ross 5.2 Poisson
- Optional: selected parts of 5.3 (hypergeometric)
- [Session material](https://github.com/RBrooksDK/STA1_26/tree/main/03_Random_Variables_and_Discrete_Distributions/session_material)

---

## Session focus

A random variable is a numerical description of a random experiment. We use PMFs, expectation, and variance, then choose among Bernoulli, binomial, and Poisson models for engineering counts.

By the end of the session, you should be able to:

- distinguish the random variable \(X\) from an observed value \(x\);
- read a PMF and a CDF, and compute \(E[X]\) and \(\operatorname{Var}(X)\);
- decide when a binomial or Poisson model is plausible;
- compute probabilities with SciPy rather than by expanding every term by hand;
- explain the binomial coefficient as “the number of ways to place \(k\) successes among \(n\) trials”.

<p align="left">
  <a href="Tutorial_03_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Tutorial 3: Packet loss and failure counts</strong>
  </a>
</p>

[Download notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA1_26/main/03_Random_Variables_and_Discrete_Distributions/Tutorial_03_notebook.ipynb)
&nbsp;·&nbsp;
[Read as markdown](Tutorial_03.md/)

---

## What we do not do

- Geometric and negative binomial as core syllabus (they may appear as extras)
- Jointly distributed random variables, covariance of sums, MGFs (Ross 4.3, 4.7–4.8)
- Deriving PMFs from first principles for every named family

---

## Assignments

This session completes **[Assignment 2](../pages/assignments.md)**: probability and discrete models.

Exercises will be added later in [Exercises.md](Exercises.md).
