---
tags:
    - Categorical Data
    - Chi-square
    - Goodness-of-fit
    - Independence
    - Homogeneity
    - Cramér's V
---

<h1 align="center">Categorical Data and Chi-Square Tests</h1>

Not every engineering measurement is a real number. Defect types, line IDs, and pass/fail labels are categorical. Chi-square tests compare observed counts with expected counts, either against a specified distribution or in a two-way table.

A goodness-of-fit test asks whether one set of counts matches a claimed distribution. Tests of independence and homogeneity use the same Pearson calculation but answer different questions because their study designs differ. Expected counts should not be too small; conditional proportions and adjusted residuals locate the important patterns, while Cramér's \(V\) describes their magnitude. Sparse tables may require pooling based on subject-matter meaning, simulation, or an exact alternative. The conclusion is stated in terms of the engineering categories, not only \(\chi^2\).

#### Key Concepts

- Contingency tables and expected counts
- Goodness-of-fit tests
- Tests of independence and homogeneity
- The guideline on expected counts
- Pearson and adjusted residuals
- Cramér's \(V\) and sparse-table alternatives

!!! tip "Learning Objectives"

    - Form a contingency table and compute expected counts.
    - Distinguish goodness-of-fit, independence, and homogeneity from the study design.
    - Perform a goodness-of-fit test and a contingency-table test.
    - Check the guideline that expected counts should not be too small.
    - Interpret adjusted residuals and Cramér's \(V\).
    - Explain when pooling, simulation, or an exact alternative may be needed.
    - State a conclusion in terms of the engineering categories, not only \(\chi^2\).

<hr/>

### Session Preparation:

Brooks: [Chapter 11](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/11_Categorical_Data_and_Chi_Square_Tests/session_material)

[Tutorial 11: Defect types across production lines](Tutorial_11_notebook.ipynb)
