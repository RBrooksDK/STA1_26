---
tags:
    - ANOVA
    - F-test
    - Tukey HSD
---

<h1 align="center">Analysis of Variance</h1>

Comparing three or more groups with many \(t\)-tests inflates the type I error. One-way ANOVA tests whether group means differ, using variation between groups relative to variation within groups. Only one-way ANOVA is core syllabus.

A significant \(F\)-test does not identify *which* groups differ. Tukey HSD then locates the pairs. Assumptions are independence, approximate normality, and similar variances; boxplots from Session 01 are reused as a diagnostic, not as a new plot type.

#### Key Concepts

- Why many pairwise \(t\)-tests are a poor default
- Between-group and within-group variation
- The ANOVA table, \(F\), and \(p\)
- Assumptions of one-way ANOVA
- Tukey HSD for pairwise comparisons

!!! tip "Learning Objectives"

    - Explain why many pairwise \(t\)-tests are a poor default.
    - Read an ANOVA table (between, within, \(F\), \(p\)).
    - State the assumptions: independence, approximate normality, similar variances.
    - Run one-way ANOVA and Tukey HSD in Python.
    - Reuse boxplots from Session 01 as a diagnostic, not as a new plot type.

<hr/>

### Session Preparation:

Brooks: [Chapter 9](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/09_Analysis_of_Variance/session_material)

[Tutorial 9: Several suppliers, one quality measure](Tutorial_09_notebook.ipynb)

<hr/>

### Exercises
