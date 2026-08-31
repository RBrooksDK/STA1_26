# Assignment 6 — Categorical Data and Chi-Square Analysis

In this mini-project, you will analyse counts and categorical outcomes. You will compare an observed event mix with a historical model, compare event distributions across sites, locate the cells driving a contingency-table result, and choose an exact alternative for a sparse \(2\times2\) table.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Session 11 and Brooks, Chapter 11
    - **Required method:** Python throughout

## Preparation, resources and AI

Review [Session 11 — Categorical Data and Chi-Square Tests](../11_Categorical_Data_and_Chi_Square_Tests/README.md), [Tutorial 11](../11_Categorical_Data_and_Chi_Square_Tests/Tutorial_11_notebook.ipynb), and [Brooks: Chapter 11](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use [assignment06_safety_events.csv](../data/assignment06_safety_events.csv). Begin with the title, group members, table of contents, imports, and the file loaded from a local data folder.

### How to present your work

Chi-square methods use counts. Show observed and expected counts before reporting a test. State the study design and statistical question, inspect expected counts, and supplement a global result with conditional proportions, residuals, and an effect magnitude.

### Working with AI

AI may help construct tables, calculate expected counts and residuals, implement simulations, identify an exact alternative, and critique interpretations. You remain responsible for checking that the question, design, and method match. Part 5 documents your use.

## Part 1 — Safety-event overview

The file [assignment06_safety_events.csv](../data/assignment06_safety_events.csv) contains recorded safety events from three sites. Each event has a `site` and an `event_type`: sensor, network, mechanical, or power.

Complete the following tasks:

1. Identify the observational unit, population of interest, variables, categories, and whether the data represent one jointly classified sample or separate site samples. State what additional sampling information is needed for broad generalisation.
2. Create overall frequency counts and percentages for event type. Create a site-by-type contingency table with row totals, column totals, and row percentages.
3. Create suitable bar charts for the overall distribution and the conditional event-type distributions by site. Explain why a histogram is not appropriate for unordered categories.
4. Describe the largest visible differences without yet treating them as statistically established or causal.

## Part 2 — Goodness of fit to the historical event mix

The historical reference model, specified before the new data were examined, is

\[
P(\text{sensor})=0.50,\quad
P(\text{network})=0.25,\quad
P(\text{mechanical})=0.15,\quad
P(\text{power})=0.10.
\]

Complete the following tasks:

1. State the goodness-of-fit hypotheses. Calculate expected counts as \(np_j\), show an observed-versus-expected table, and check the expected-count guideline.
2. Calculate each category's contribution \((O-E)^2/E\), their sum \(\chi^2\), and the degrees of freedom. Verify with `scipy.stats.chisquare` and report the \(p\)-value and decision at \(\alpha=0.05\).
3. Identify which categories contribute most and describe whether each is above or below its expected count. Explain why the global test alone does not provide this information.
4. State a contextual conclusion and explain why a difference from the historical mix does not identify its operational cause.

## Part 3 — Are event profiles homogeneous across sites?

Treat the site records as separate samples and ask whether the event-type distribution is the same at all three sites.

Complete the following tasks:

1. Explain why this is naturally a test of homogeneity. State \(H_0\) and \(H_1\), and explain how an independence study would differ in design even though the Pearson calculation can be identical.
2. Calculate every expected count using the row and column margins, check their minimum, and calculate the degrees of freedom \((r-1)(c-1)\).
3. Perform the Pearson chi-square test. Report \(\chi^2\), degrees of freedom, \(p\), decision, and a conclusion in terms of site event profiles.
4. Calculate Pearson and adjusted residuals and display the adjusted residuals as a labelled heatmap. Use their signs and magnitudes together with row percentages to identify the cells driving the global pattern.
5. Calculate Cramér's \(V\) and interpret it as a descriptive association magnitude without applying a universal engineering cutoff or treating it as causation.
6. With seed 2026 and at least 5,000 permutations, shuffle site labels while holding event types fixed. Compare the Monte Carlo tail probability with the chi-square reference result and explain what the simulation checks.

## Part 4 — A sparse \(2\times2\) safety table

A small pilot study compares an existing and a modified interlock. An unwanted trip occurred in 1 of 20 existing-system trials and 7 of 20 modified-system trials.

Complete the following tasks:

1. Construct the \(2\times2\) table of observed counts and calculate row percentages. State the comparison and hypotheses.
2. Calculate the expected counts under independence or homogeneity. Explain why the usual chi-square approximation is questionable here.
3. Use Fisher's exact test as the primary analysis. Report the odds ratio returned by SciPy, the two-sided \(p\)-value, decision, and contextual conclusion.
4. Explain why categories or outcomes must not be pooled merely to make a test significant or satisfy a rule. State what additional evidence or larger study you would recommend.

## Part 5 — AI-use and conclusion

### AI-use

State which AI tools you used, what they contributed, what you changed or rejected, and how you verified the work. A short paragraph or table is sufficient.

### Overall conclusion

Write approximately 150–250 words comparing the goodness-of-fit, homogeneity, and sparse-table questions. Include statistical evidence, the categories driving each result, effect magnitude where appropriate, assumptions, and practical limitations.

Do not use chi-square on binned continuous data as a normality test. Normality assessment for quantitative data remains a different question addressed with methods such as QQ-plots.

## Submission checklist

- [ ] Tests are calculated from counts, not percentages.
- [ ] Goodness of fit and two-way tables are distinguished.
- [ ] Observed and expected counts and degrees of freedom are shown.
- [ ] Expected-count adequacy is checked before using the approximation.
- [ ] Residuals and conditional proportions locate the important cells.
- [ ] Cramér's \(V\) is not interpreted causally.
- [ ] Fisher's exact test is used for the sparse \(2\times2\) case.
- [ ] Part 5 contains AI-use and conclusion.
- [ ] All code is executed and output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

Be prepared to use examples from this assignment to explain categorical counts, goodness-of-fit tests, contingency tables, independence versus homogeneity, expected counts, Pearson's \(\chi^2\), degrees of freedom, approximation conditions, category contributions, Pearson and adjusted residuals, Cramér's \(V\), permutation or Monte Carlo checks, sparse tables, pooling, Fisher's exact test, and responsible conclusions from categorical studies.

You need not memorise code, but you must understand each table, expected count, test, diagnostic, and conclusion. AI use does not change this requirement.
