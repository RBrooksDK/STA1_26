---
tags:
    - ANOVA
    - F-test
    - Welch ANOVA
    - Tukey HSD
    - Eta-squared
---

<h1 align="center">Analysis of Variance</h1>

Comparing three or more groups with many \(t\)-tests inflates the type I error. One-way ANOVA tests whether group means differ, using variation between groups relative to variation within groups. Only one-way ANOVA is core syllabus.

A significant \(F\)-test does not identify *which* groups differ. Tukey HSD then locates the pairs under the classical common-variance model. Welch's one-way ANOVA is the practical alternative when independent groups have materially unequal spreads, and \(\eta^2\) describes the observed effect magnitude. Assumptions concern independence and the within-group errors; boxplots from Session 01 are reused as a diagnostic, not as a new plot type.

#### Key Concepts

- Why many pairwise \(t\)-tests are a poor default
- Between-group and within-group variation
- The ANOVA table, \(F\), and \(p\)
- Classical versus Welch's one-way ANOVA
- Assumptions and diagnostics for within-group errors
- Tukey HSD for pairwise comparisons
- \(\eta^2\) as a descriptive effect magnitude

!!! tip "Learning Objectives"

    - Explain why many pairwise \(t\)-tests are a poor default.
    - Read an ANOVA table (between, within, \(F\), \(p\)).
    - Diagnose independence, within-group error shape, and the common-variance assumption.
    - Choose between classical and Welch's one-way ANOVA.
    - Run one-way ANOVA and, when compatible, Tukey HSD in Python.
    - Report \(\eta^2\) without treating it as causation.
    - Reuse boxplots from Session 01 as a diagnostic, not as a new plot type.

<hr/>

### Session Preparation:

Brooks: [Chapter 9](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/09_Analysis_of_Variance/session_material)

[Tutorial 9: Several suppliers, one quality measure](Tutorial_09_notebook.ipynb)
