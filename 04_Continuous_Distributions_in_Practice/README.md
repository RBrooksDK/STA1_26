---
tags:
    - Continuous Distributions
    - Normal
    - Exponential
    - Uniform
    - QQ-plot
---

<h1 align="center">Continuous Distributions in Practice</h1>

Continuous measurements — thicknesses, times, noise — are described by densities. Probability is area: for a continuous variable, \(P(X = x) = 0\). The working models in this course are uniform, normal, and exponential.

You must understand the models and compute probabilities in Python. You do not integrate densities by hand. SciPy supplies the PDF, CDF, survival function, and percent-point function. A \(z\)-score standardises a normal measurement, and a QQ-plot is a diagnostic of shape, not a proof of normality.

#### Key Concepts

- Probability as area; \(P(X = x) = 0\)
- PDF, CDF, survival function, and percent-point function
- Uniform, normal, and exponential models
- \(z\)-scores and percentiles
- QQ-plots as diagnostics

!!! tip "Learning Objectives"

    - Explain why \(P(X = x) = 0\) for a continuous variable.
    - Use PDF, CDF, survival function, and percent-point function in SciPy.
    - Standardise with a \(z\)-score and interpret it.
    - Choose among uniform, normal, and exponential for a practical problem.
    - Read a QQ-plot as a diagnostic, not as a proof of normality.

<hr/>

### Session Preparation:

Brooks: [Chapter 4](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/IgDSmYZksHCGRLhWixBdyOOdAWZM_5MGaFvdM7LAki33vQc)

[Tutorial 4: Response times and component lifetimes](Tutorial_04_notebook.ipynb)

[Assignment 2 — Discrete and Continuous Probability Models](../assignments/assignment_02_discrete_and_continuous_models.md) — due 29 Sept. 2026, 12:45
