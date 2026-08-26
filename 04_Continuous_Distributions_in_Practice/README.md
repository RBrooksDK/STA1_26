# 04 — Continuous Distributions in Practice

## Session preparation

Read Ross 5.4–5.6 **selectively**. You must understand the models and compute probabilities in Python. You do not integrate densities by hand.

**Syllabus and input**

- Ross 5.4 Uniform
- Ross 5.5 Normal
- Ross 5.6 Exponential

---

## Session focus

Continuous measurements — thicknesses, times, noise — are described by densities. Probability is area. The working models are uniform, normal, and exponential.

By the end of the session, you should be able to:

- explain why \(P(X = x) = 0\) for a continuous variable;
- use PDF, CDF, survival function, and percent-point function in SciPy;
- standardise with a \(z\)-score and interpret it;
- choose among uniform, normal, and exponential for a practical problem;
- read a QQ-plot as a diagnostic, not as a proof of normality.

<p align="left">
  <a href="Tutorial_04_notebook.ipynb">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Tutorial 4: Response times and component lifetimes</strong>
  </a>
</p>

[Download notebook (.ipynb)](Tutorial_04_notebook.ipynb)
&nbsp;·&nbsp;
[Read as markdown](Tutorial_04.md)

---

## What we do not do

- Manual integration of a PDF, or deriving a CDF from a PDF by hand
- Deriving means and variances from integrals
- Gamma, Weibull, or logistic as core models
- The theory of Poisson processes (SMP1); we only use the practical link “Poisson counts, exponential waits”

---

## Assignments

This session feeds **[Assignment 3](../pages/assignments.md)** together with Session 05.

Exercises will be added later in [Exercises.md](Exercises.md).
