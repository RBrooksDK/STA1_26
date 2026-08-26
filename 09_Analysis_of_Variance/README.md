# 09 — Analysis of Variance

## Session preparation

Read Ross 10.1–10.3. Only one-way ANOVA is core syllabus.

**Syllabus and input**

- Ross 10.1–10.3: one-way ANOVA, the \(F\)-test, and pairwise comparisons
- [Session material](https://github.com/RBrooksDK/STA1_26/tree/main/09_Analysis_of_Variance/session_material)

---

## Session focus

Comparing three or more groups with many \(t\)-tests inflates the type I error. ANOVA tests whether group means differ, using variation between and within groups. Tukey HSD then locates which pairs differ.

By the end of the session, you should be able to:

- explain why many pairwise \(t\)-tests are a poor default;
- read an ANOVA table (between, within, \(F\), \(p\));
- state the assumptions: independence, approximate normality, similar variances;
- run one-way ANOVA and Tukey HSD in Python;
- reuse boxplots from Session 01 as a diagnostic, not as a new plot type.

<p align="left">
  <a href="Tutorial_09_notebook/">
    <img src="../figures/Python-logo-notext.svg.png" alt="Python tutorial" width="100" />
    <br>
    <strong>Tutorial 9: Several suppliers, one quality measure</strong>
  </a>
</p>

[Download notebook (.ipynb)](https://raw.githubusercontent.com/RBrooksDK/STA1_26/main/09_Analysis_of_Variance/Tutorial_09_notebook.ipynb)
&nbsp;·&nbsp;
[Read as markdown](Tutorial_09.md/)

---

## What we do not do

- Two-way ANOVA and interactions
- Treating a significant \(F\)-test as identifying *which* groups differ without a post-hoc analysis

---

## Assignments

This session completes **[Assignment 5](../pages/assignments.md)**: comparing two and several groups.

Exercises will be added later in [Exercises.md](Exercises.md).
