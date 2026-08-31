# Assignment 4 — One- and Two-Sample Tests

In this mini-project, you will move from one-sample claims to comparisons between two groups or conditions. The main task is to match the test to the study design and report an estimated effect with uncertainty rather than reducing the analysis to a \(p\)-value.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Sessions 7–8 and Brooks, Chapters 7–8
    - **Required method:** Python throughout

## Preparation, resources and AI

Review Sessions and Tutorials [7](../07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/README.md) and [8](../08_Hypothesis_Testing_II_Comparing_Two_Groups/README.md), together with [Brooks: Chapters 7–8](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use:

1. [assignment03_sensor_calibration.csv](../data/assignment03_sensor_calibration.csv);
2. [assignment03_access_control.csv](../data/assignment03_access_control.csv);
3. [assignment04_coating_durability.csv](../data/assignment04_coating_durability.csv); and
4. [assignment04_energy_retrofit.csv](../data/assignment04_energy_retrofit.csv).

Begin with the title, group members, table of contents, imports, and all files loaded from a local data folder.

### How to present your work

For each analysis, state the population, parameter, observational unit, design, comparison order, hypotheses, and significance level before reporting the software result. Use plots and numerical diagnostics for assumptions. Report estimates and confidence intervals in engineering units.

### Working with AI

AI may help identify the appropriate design, formulate hypotheses, write test and interval code, debug diagnostics, and challenge conclusions. You remain responsible for the method and interpretation. Part 5 documents your use.

!!! tip "Analysis order"
    1. Question, parameter, units, and comparison order.
    2. Study design and assumptions.
    3. Descriptive summaries and plots.
    4. Effect estimate and confidence interval.
    5. Hypotheses, statistic, \(p\)-value, and decision.
    6. Practical importance, limitations, and conclusion.

## Part 1 — One-sample decisions

### Mean sensor error

Use [assignment03_sensor_calibration.csv](../data/assignment03_sensor_calibration.csv). The engineering team asks whether population mean calibration error differs from zero; errors with absolute mean below \(0.50\ ^\circ\mathrm C\) are regarded as small in practice.

1. State \(H_0\), the two-sided \(H_1\), and \(\alpha=0.05\). Use a one-sample \(t\) procedure and report the sample mean, test statistic, degrees of freedom, and two-sided \(p\)-value.
2. Interpret the \(p\)-value as a tail probability conditional on \(H_0\) and the assumptions. State the decision and a contextual conclusion without treating the \(p\)-value as \(P(H_0\mid\text{data})\).
3. Reuse or reconstruct the 95% \(t\) interval and explain its duality with this two-sided test. Compare it with the practical limits and distinguish statistical significance from practical importance.

### False-rejection probability

Use [assignment03_access_control.csv](../data/assignment03_access_control.csv). The pre-specified question is whether the false-rejection probability exceeds the 5% target.

1. State the one-sided hypotheses. Perform an exact binomial test and report \(\hat p\), the \(p\)-value, decision, and conclusion.
2. Use the Wilson interval as an estimate of plausible values, while explaining why a two-sided Wilson interval is not the exact dual of a one-sided exact test.
3. Describe Type I and Type II errors in one of the two one-sample studies and state an operational consequence of each.

## Part 2 — Independent coating processes

The file [assignment04_coating_durability.csv](../data/assignment04_coating_durability.csv) contains independent specimens from a standard and modified coating process. Let

\[
\delta=\mu_{\text{modified}}-\mu_{\text{standard}},
\]

measured in durability hours. An increase of at least 8 hours is considered practically important.

Complete the following tasks:

1. Explain why the samples are independent rather than paired. Report group \(n\), mean, sample standard deviation, and boxplots.
2. State two-sided hypotheses about \(\delta\). Use Welch's two-sample \(t\) procedure and report the estimated difference, 95% confidence interval, statistic, approximate degrees of freedom, and \(p\)-value. Do not use a preliminary variance test to switch automatically between pooled and Welch procedures.
3. Assess independence from the design and distribution shape and unusual observations from group plots or residual diagnostics. State what the plots cannot establish.
4. Compare the interval with both zero and the 8-hour practical threshold. Give a recommendation that reflects statistical uncertainty and practical importance.

## Part 3 — Paired building-energy measurements

The file [assignment04_energy_retrofit.csv](../data/assignment04_energy_retrofit.csv) records energy use for the same 36 buildings before and after a control-system retrofit. Define the paired difference

\[
D=\text{before}-\text{after},
\]

so a positive value represents a reduction.

Complete the following tasks:

1. Explain the observational unit and why the rows form genuine pairs. Create the difference column and report its mean, standard deviation, and standard error.
2. Plot the paired values and the distribution or QQ-plot of differences. Diagnose the differences—not the two raw columns separately—for the paired \(t\) procedure.
3. Test \(H_0:\mu_D=0\) against a two-sided alternative and construct a 95% interval for \(\mu_D\), using `ttest_rel` or an equivalent one-sample procedure applied to the differences.
4. Explain why an independent-samples test would discard useful pairing. Interpret the estimated reduction and interval in kWh/day and state a practical recommendation.

## Part 4 — Comparing two independent proportions

Two independently assigned software configurations were evaluated using separate requests. Configuration A had 38 SLA failures among 300 requests; configuration B had 22 among 320. Define the risk difference as \(p_A-p_B\).

Complete the following tasks:

1. State the observational unit, binary outcome, populations, assumptions, comparison order, and two-sided hypotheses.
2. Calculate both sample proportions, their difference in percentage points, and a 95% confidence interval using separate estimated variances.
3. Test \(H_0:p_A=p_B\) with a two-proportion \(z\) procedure. Report \(z\), the two-sided \(p\)-value, decision, and contextual conclusion.
4. State what random sampling and random assignment would each support and why a significant difference alone is not enough for an unrestricted causal claim.

## Part 5 — AI-use and conclusion

### AI-use

State which AI tools you used, what they contributed, what you changed or rejected, and how you verified the final work. A short paragraph or table is sufficient.

### Overall conclusion

Write approximately 150–250 words comparing what the four designs allow you to conclude. Include effects and intervals, not only decisions, and distinguish statistical significance, practical importance, and causal interpretation.

Only use Sessions 7–8. Do not use ANOVA, regression, or chi-square methods.

## Submission checklist

- [ ] Every hypothesis concerns a clearly defined population parameter.
- [ ] Test direction and comparison order are fixed before results.
- [ ] \(p\)-values are interpreted conditionally on \(H_0\) and assumptions.
- [ ] “Fail to reject” is not described as proof of \(H_0\).
- [ ] Welch is the default for independent means and genuine pairs are analysed as differences.
- [ ] Proportion interval and test standard errors are not interchanged.
- [ ] Effects and confidence intervals are reported in engineering units.
- [ ] Part 5 contains AI-use and conclusion.
- [ ] All code is executed and output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

Be prepared to use examples from this assignment to explain hypotheses, one- and two-sided tests, test statistics, \(p\)-values, \(\alpha\), Type I and II errors, power, one-sample \(t\) and proportion tests, exact versus approximate procedures, test–interval duality, independent versus paired designs, Welch's test, paired tests as one-sample tests of differences, two-proportion comparisons, risk differences, effect uncertainty, practical importance, and the design requirements for generalisation and causation.

You need not memorise code, but you must understand which parameter each function tests, how the design determines the method, and how the output supports the conclusion. AI use does not change this requirement.
