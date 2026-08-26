---
tags:
    - Regression
    - Least Squares
    - Residuals
    - R-squared
---

<h1 align="center">Simple Linear Regression</h1>

Regression models how a response changes with a predictor: energy use with load, a calibrated reading with a reference, a quality measure with a process setting. We fit least squares, interpret slope and intercept with units, and inspect residuals.

\(R^2\) measures fit, not causation. Statsmodels is used for inference: a test of the slope, a confidence interval for the mean response, and a prediction interval for a new observation. Scikit-learn is used for fitting and a simple train/test split; it does not replace a statistical summary for intervals and tests.

#### Key Concepts

- Least squares: \(\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x\)
- Interpretation of slope and intercept
- \(R^2\) and correlation
- Residual and QQ-plots
- Confidence interval for the mean versus prediction interval
- Statsmodels for inference; scikit-learn for fitting

!!! tip "Learning Objectives"

    - Fit \(\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x\) and interpret the coefficients with units.
    - Report \(R^2\) without treating it as proof of causation.
    - Test whether the slope differs from zero.
    - Read residual and QQ-plots.
    - Explain why scikit-learn does not replace a statistical summary for intervals and tests.

<hr/>

### Session Preparation:

Brooks: [Chapter 10](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/10_Simple_Linear_Regression/session_material)

[Tutorial 10: Calibration and energy use](Tutorial_10_notebook/)

[Calculating metrics](Calculating_metrics.md/) (optional derivation sheet)

<hr/>

### Exercises
