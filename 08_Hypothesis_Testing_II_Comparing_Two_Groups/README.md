---
tags:
    - Two-sample t-test
    - Welch
    - Paired t-test
    - Two Proportions
    - Effect size
---

<h1 align="center">Hypothesis Testing II: Comparing Two Groups</h1>

Many engineering questions compare two conditions: two servers, two suppliers, before and after a change. The design — independent samples versus paired observations — decides the test.

Independent groups use **Welch's** two-sample \(t\) procedure as the default; a preliminary variance test is not used to choose automatically between pooled and Welch analyses. Paired observations use a paired \(t\)-test on the differences. For independent binary outcomes, we compare two proportions through a risk difference and its uncertainty. A confidence interval for the difference in engineering units keeps the result from collapsing to a single \(p\)-value. Statistical significance is not the same as practical importance.

#### Key Concepts

- Independent samples versus paired observations
- Two-sample \(t\)-test and Welch's \(t\)-test
- Paired \(t\)-test
- Comparison of two independent proportions
- Confidence interval for a difference
- Statistical significance versus practical importance

!!! tip "Learning Objectives"

    - Choose between independent and paired data.
    - Perform Welch's two-sample \(t\)-test as the default for independent groups.
    - Perform a paired \(t\)-test.
    - Compare two independent proportions and report a risk difference with uncertainty.
    - Report a confidence interval for the difference and an effect size.
    - Distinguish statistical significance from practical importance.

<hr/>

### Session Preparation:

Brooks: [Chapter 8](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Tutorial 8: A/B test of response times](Tutorial_08_notebook.ipynb)

[Assignment 4 — One- and Two-Sample Tests](../assignments/assignment_04_one_and_two_sample_tests.md) — due 3 Nov. 2026, 12:45
