---
tags:
    - Regression
    - Least Squares
    - Residuals
    - R-squared
---

<h1 align="center">Simple Linear Regression</h1>

Regression models how a response changes with a predictor: energy use with load, a calibrated reading with a reference, a quality measure with a process setting. We fit least squares, interpret slope and intercept with units, and inspect residuals.

\(R^2\) measures the fraction of observed squared variation accounted for by the line; it is not causation. Statsmodels is used for inference: a test of the slope, a confidence interval for the mean response, and a prediction interval for a new observation. This session is a statistical regression analysis, not a machine-learning prediction lab.

#### Key Concepts

- Least squares: \(\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x\)
- Interpretation of slope and intercept
- \(R^2\) and correlation
- Residual and QQ-plots
- Confidence interval for the mean versus prediction interval
- Statsmodels for fitting, inference, diagnostics, and intervals

!!! tip "Learning Objectives"

    - Fit \(\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x\) and interpret the coefficients with units.
    - Report \(R^2\) without treating it as proof of causation.
    - Test whether the slope differs from zero.
    - Read residual and QQ-plots.
    - Distinguish a confidence interval for the mean response from a prediction interval for one new observation.

<hr/>

### Session Preparation:

Brooks: [Chapter 10](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/IgCTZYJOjiA6T7ahrSfe-UpnAQBFfuCv1R0c3l5R4tzvYpY)

[Tutorial 10: Energy use and processor load](Tutorial_10_notebook.ipynb)

[Assignment 5 — ANOVA and Regression](../assignments/assignment_05_anova_and_regression.md) — due 17 Nov. 2026, 12:45
