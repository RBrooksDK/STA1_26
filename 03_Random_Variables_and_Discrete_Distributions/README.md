---
tags:
    - Random Variables
    - PMF
    - Bernoulli
    - Binomial
    - Poisson
---

<h1 align="center">Random Variables and Discrete Distributions</h1>

A random variable is a numerical description of a random experiment. Once we have that language, packet-loss counts, defect counts, and other engineering tallies can be modelled rather than only listed.

We use PMFs, CDFs, expectation, and variance, then choose among Bernoulli, binomial, and Poisson models. The binomial coefficient is introduced here because the binomial model needs it: it counts the number of ways to place \(k\) successes among \(n\) trials. Probabilities are computed in SciPy rather than by expanding every term by hand.

#### Key Concepts

- Random variable \(X\) versus observed value \(x\)
- PMF, CDF, expectation, and variance
- Bernoulli and binomial models
- Poisson counts
- The binomial coefficient \(\binom{n}{k}\)

!!! tip "Learning Objectives"

    - Distinguish the random variable \(X\) from an observed value \(x\).
    - Read a PMF and a CDF, and compute \(E[X]\) and \(\operatorname{Var}(X)\).
    - Decide when a binomial or Poisson model is plausible.
    - Compute probabilities with SciPy rather than by expanding every term by hand.
    - Explain the binomial coefficient as the number of ways to place \(k\) successes among \(n\) trials.

<hr/>

### Session Preparation:

Brooks: [Chapter 3](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Tutorial 3: Packet loss and failure counts](Tutorial_03_notebook.ipynb)

[Assignment 2 — Discrete and Continuous Probability Models](../assignments/assignment_02_discrete_and_continuous_models.md) — due 29 Sept. 2026, 12:45
