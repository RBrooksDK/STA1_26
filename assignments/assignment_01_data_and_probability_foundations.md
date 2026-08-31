# Assignment 1 — Data and Probability Foundations

In this mini-project, you will describe two engineering datasets and analyse one probability model. The assignment moves from observations and visualisation to events, conditional probability, and Bayes' theorem. The questions and required outputs are fixed, but you decide how to organise the notebook and present the results.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Sessions 1–2 and Brooks, Chapters 1–2

## Preparation, resources and AI

Before beginning, review:

- [Session 1 — Data and Descriptive Statistics](../01_Data_and_Descriptive_Statistics/README.md);
- [Tutorial 1](../01_Data_and_Descriptive_Statistics/Tutorial_01_notebook.ipynb);
- [Session 2 — Probability for Data Analysis](../02_Probability_for_Data_Analysis/README.md);
- [Tutorial 2](../02_Probability_for_Data_Analysis/Tutorial_02_notebook.ipynb); and
- [Brooks: Chapters 1–2](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use the following supplied files:

1. [assignment01_digital_services.csv](../data/assignment01_digital_services.csv); and
2. [assignment01_smart_building.csv](../data/assignment01_smart_building.csv).

Begin the notebook with the assignment title, the names of all group members, and a short table of contents. Import the required libraries and read both files from a local data folder.

### How to present your work

Parts 1–2 are Python-based. Use executed code cells for summaries, tables, and plots and Markdown cells for interpretations. Part 3 should show the probability reasoning manually in Markdown with equations, a probability tree, a table, or clear embedded handwritten work. Python may check the arithmetic but must not replace the displayed reasoning.

### Working with AI

You are encouraged to use AI throughout the mini-project. AI may help you write or debug code, choose visualisations, check calculations, challenge an interpretation, or improve your writing. You remain responsible for checking the results. Every group member must understand the notebook and be able to explain it. In Part 4 you will state how you used AI.

## Part 1 — Digital services

The file [assignment01_digital_services.csv](../data/assignment01_digital_services.csv) contains latency measurements and security-alert categories for three digital services.

Complete the following tasks:

1. Identify the observational unit, the relevant population, and each variable as categorical or quantitative. Create a frequency table for `alert_type` containing counts and percentages.
2. For `latency_ms`, report the sample size, mean, median, sample standard deviation, minimum, \(Q_1\), \(Q_3\), maximum, and IQR:
    - for all observations combined; and
    - separately for each `service`.
3. Create a histogram of all latency measurements and side-by-side boxplots for the three services. Explain the histogram's axes, bins, and displayed shape and the boxplot's median, box, whiskers, and plotted potential outliers.
4. Apply the \(1.5\times\operatorname{IQR}\) rule within each service. Report the IDs and values of potential outliers, retain them in the analysis, and explain why a plotted outlier is not automatically a data error.
5. Write a short descriptive comparison of the services. Comment on typical latency, spread, skewness, the relationship between mean and median, and what cannot be generalised from these descriptive differences alone.

## Part 2 — Smart-building measurements

The file [assignment01_smart_building.csv](../data/assignment01_smart_building.csv) contains two days of hourly measurements from the north and south zones of a smart building.

Complete the following tasks:

1. Identify the observational unit and variables. For `indoor_temp_c` and `energy_kwh`, report \(n\), mean, median, and sample standard deviation separately for each zone.
2. Plot indoor temperature against `hour`, using a separate line for each zone. Describe the time pattern and explain what each axis and line represent.
3. Create a scatterplot of `outdoor_temp_c` against `energy_kwh`, using colour or separate panels for the zones. Describe the direction, form, strength, and unusual points visible in the association.
4. Write a short conclusion about temperature stability, differences between zones, and the visible energy–temperature relationship. Do not calculate correlation, fit a regression model, or make causal claims at this stage.

## Part 3 — Cybersecurity alert system

A security system monitors authentication attempts. Let \(M\) denote a malicious attempt and \(A\) denote an alert. Historical validation gives

\[
P(M)=0.006,\qquad P(A\mid M)=0.97,\qquad P(A\mid M^c)=0.015.
\]

Treat these values as model probabilities. For a natural-frequency interpretation, consider 100,000 authentication attempts, for which the expected counts can be treated as whole numbers.

Complete the following tasks:

1. Define the four elementary outcomes formed from \(M\), \(M^c\), \(A\), and \(A^c\). Explain why they are mutually exclusive and exhaustive.
2. Construct a labelled \(2\times2\) table of expected counts for 100,000 attempts, including row and column totals.
3. Use the probability model and verify the results from the table:
    - \(P(M\cap A)\);
    - \(P(A)\) using the law of total probability;
    - \(P(M\cup A)\);
    - \(P(M\mid A)\); and
    - \(P(M^c\mid A)\).
4. Explain the difference between \(P(A\mid M)\) and \(P(M\mid A)\). Determine whether \(M\) and \(A\) are independent and whether they are mutually exclusive, justifying both answers numerically.
5. Suppose an improved system reduces \(P(A\mid M^c)\) to 0.005 while leaving the other inputs unchanged. Recalculate \(P(M\mid A)\), compare it with the original value, and explain why both the false-positive rate and the base rate matter.

## Part 4 — AI-use and conclusion

### AI-use

Briefly state:

1. which AI tool or tools you used;
2. what you used them for;
3. what you changed or rejected; and
4. how you checked that the final work was correct.

A short paragraph or table is sufficient. If AI produced most of the code or text, say so honestly. Complete chat transcripts are not required. If you did not use AI, state that explicitly.

### Overall conclusion

Write a conclusion of approximately 150–250 words. Summarise the principal finding from each engineering case and explain the difference between describing observed data and reasoning from an assumed probability model. State one limitation of each analysis.

Only use methods introduced in Sessions 1–2. Do not use probability distributions, confidence intervals, hypothesis tests, correlations, regression, or other methods from later sessions.

## Submission checklist

- [ ] Both datasets have been imported and analysed.
- [ ] Every requested table and plot is followed by an interpretation.
- [ ] Sample standard deviations use \(n-1\).
- [ ] Potential outliers are identified but not automatically removed.
- [ ] The probability solution shows events, rules, substitutions, and calculations.
- [ ] Independence and mutual exclusivity are distinguished.
- [ ] Part 4 includes the AI-use statement and conclusion.
- [ ] All code cells have been executed in order and their output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

At the exam, be prepared to use examples from this assignment to explain:

- observations, variables, samples, populations, statistics, and parameters;
- categorical, discrete quantitative, and continuous quantitative variables;
- frequency tables, histograms, run plots, scatterplots, and boxplots;
- mean, median, mode, variance, sample standard deviation, range, quartiles, percentiles, IQR, and the five-number summary;
- symmetric and skewed distributions and how shape and outliers affect summaries;
- the \(1.5\times\operatorname{IQR}\) rule and why potential outliers require investigation;
- sample spaces, events, complements, unions, and intersections;
- conditional probability, independence, and mutually exclusive events;
- the addition and multiplication rules, total probability, and Bayes' theorem; and
- why association and descriptive group differences do not by themselves establish causation or population effects.

You are **not** expected to reproduce Python syntax from memory. You are expected to understand what the code calculates and displays, how each probability follows from the model, and how the results answer the engineering questions. Using AI to write code does not change this requirement.
