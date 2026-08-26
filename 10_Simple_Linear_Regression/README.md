# 10 — Simple Linear Regression

## Session preparation

Read Chapter 10, *Simple Linear Regression*, in the course textbook
[*Statistics and Data Analysis for Engineers*](https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).
The English note [Calculating_metrics.md](Calculating_metrics.md) can be used as an extra derivation sheet.

**Syllabus and input**

- Brooks, *Statistics and Data Analysis for Engineers*, Chapter 10
- [Calculating metrics](Calculating_metrics.md), optional derivation sheet
- [Session material](https://github.com/RBrooksDK/STA1_26/tree/main/10_Simple_Linear_Regression/session_material)

---

## Session focus

Regression models how a response changes with a predictor. We fit least squares, interpret slope and intercept, inspect residuals, and distinguish a confidence interval for the mean response from a prediction interval for a new observation. Statsmodels is used for inference; scikit-learn is used for fitting and a simple train/test split.

By the end of the session, you should be able to:

- fit \(\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x\) and interpret the coefficients with units;
- report \(R^2\) without treating it as proof of causation;
- test whether the slope differs from zero;
- read residual and QQ-plots;
- explain why scikit-learn does not replace a statistical summary for intervals and tests.

<p align="left">
  <a href="Tutorial_10_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Tutorial 10: Calibration and energy use</strong>
  </a>
</p>

[Download notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA1_26/main/10_Simple_Linear_Regression/Tutorial_10_notebook.ipynb)
&nbsp;·&nbsp;
[Read as markdown](Tutorial_10.md/)

---

## Scope boundary

- Multiple, polynomial, or logistic regression
- Causal claims from an observational scatterplot
- Using `sklearn.metrics` as the only report of a regression in this course

---

## Assignments

This session feeds **[Assignment 6](../pages/assignments.md)** together with Session 11. The [project](../pages/project.md) is introduced here.

The [assessment page](Exercises.md) is reserved for Assignment 6 material,
which will be published during the semester.
