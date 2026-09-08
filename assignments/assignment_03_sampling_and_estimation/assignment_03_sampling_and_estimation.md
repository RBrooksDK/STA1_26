# Assignment 3 — Sampling Distributions and Estimation

In this mini-project, you will connect repeated sampling with statistical estimation. You will first investigate how sample means vary and become approximately normal, then estimate an unknown population mean and proportion with confidence intervals.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Sessions 5–6 and Brooks, Chapters 5–6
    - **Required method:** Python throughout

## Preparation, resources and AI

Before beginning, review:

- [Session 5 — Sampling Distributions and the Central Limit Theorem](../05_Sampling_Distributions_and_the_CLT/README.md);
- [Tutorial 5](../05_Sampling_Distributions_and_the_CLT/Tutorial_05_notebook.ipynb);
- [Session 6 — Estimation and Confidence Intervals](../06_Estimation_and_Confidence_Intervals/README.md);
- [Tutorial 6](../06_Estimation_and_Confidence_Intervals/Tutorial_06_notebook.ipynb); and
- [Brooks: Chapters 5–6](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use:

1. [assignment03_sensor_calibration.csv](../data/assignment03_sensor_calibration.csv); and
2. [assignment03_access_control.csv](../data/assignment03_access_control.csv).

Begin with the assignment title, group members, a table of contents, imports, and both files loaded from a local data folder.

### How to present your work

Use executed code for every simulation, estimate, interval, table, and plot. Use Markdown for model statements, formulas, assumptions, coverage interpretations, and conclusions. Show requested interval components before verifying with a library function.

### Working with AI

AI may help write simulation code, translate interval formulas, check SciPy or statsmodels calls, debug plots, and challenge interpretations. You remain responsible for all assumptions and results. Part 4 documents your AI use.

## Part 1 — Sampling distributions and the CLT

Restoration time in a service system is modelled as exponential with population mean and standard deviation \(\mu=\sigma=60\) minutes. Use this known population model and NumPy's random generator with seed 2026 and at least 20,000 repetitions per sample size.

Complete the following tasks:

1. Simulate samples for \(n=1,5,20,80\) and store their means. Create a table with \(n\), theoretical mean, simulated mean of means, theoretical standard error \(\sigma/\sqrt n\), and empirical standard deviation of the simulated means.
2. Create one figure showing the four sampling distributions with density histograms and overlay \(N(\mu,\sigma^2/n)\). Explain how centre, spread, and shape change and why the normal curve is an approximation for this non-normal population.
3. For \(n=20\) and \(n=80\), estimate \(P(\bar X>75)\) by simulation and calculate the CLT approximation. Compare the values.
4. Find the smallest integer \(n\) for which \(\operatorname{SE}(\bar X)\le6\) minutes and verify it by simulation.
5. Generate one sequence of 5,000 observations and plot its running mean. Explain the law of large numbers and how this plot differs from a sampling distribution.

State explicitly that the CLT concerns sample means. It neither makes individual restoration times normal nor repairs dependence, drift, or unrepresentative sampling.

## Part 2 — Estimating mean sensor error

The file [assignment03_sensor_calibration.csv](../data/assignment03_sensor_calibration.csv) contains calibration errors from 64 independently selected temperature sensors. Error is `sensor reading − reference temperature`. Let \(\mu\) be the population mean calibration error.

Complete the following tasks:

1. Report \(n\), \(\bar x\), \(s\), and the estimated standard error. Explain standard deviation versus standard error.
2. Create a histogram and normal QQ-plot. Discuss whether a one-sample \(t\) interval appears reasonable and why plots cannot establish independence.
3. Construct a 95% \(t\) interval by calculating the degrees of freedom, critical value, standard error, and margin of error. Verify it with SciPy and interpret both the interval and the 95% confidence level correctly.
4. Create a table of 90%, 95%, and 99% \(t\) intervals and widths. Explain the confidence–precision trade-off.
5. Using \(s\) as a planning value and the normal critical value, find the smallest approximate sample size for a 95% margin of error no larger than \(0.10\ ^\circ\mathrm C\).
6. With seed 2026 and at least 10,000 resamples, construct a percentile bootstrap interval. Compare it with the \(t\) interval and state what the comparison cannot validate.

## Part 3 — Estimating a false-rejection proportion

The file [assignment03_access_control.csv](../data/assignment03_access_control.csv) contains 240 independently staged legitimate login attempts. `false_reject` equals 1 when a legitimate attempt was rejected and 0 otherwise. Let \(p\) be the population false-rejection probability under the test conditions.

Complete the following tasks:

1. Report \(n\), the number of false rejections \(x\), and \(\hat p\). Explain why \(\hat p\) is also the sample mean of a binary variable.
2. Construct and interpret a 95% Wilson interval for \(p\) with statsmodels. State the population and parameter clearly.
3. Calculate the 95% Wald interval from its formula. Compare it with Wilson and explain why Wilson is the preferred default.
4. Create a table of 90%, 95%, and 99% Wilson intervals and widths.
5. Estimate the sample size for a 95% margin of error no larger than 0.02 using first \(p=0.5\) and then the observed \(\hat p\). Round up and explain the difference.

## Part 4 — AI-use and conclusion

### AI-use

State which AI tools you used, what they contributed, what you changed or rejected, and how you verified the work. A short paragraph or table is sufficient. If AI produced most of the code or text, state this honestly.

### Overall conclusion

Write approximately 150–250 words explaining how sample size and sampling variability affect sample means, standard errors, and confidence-interval precision. Report the two parameter estimates with uncertainty and state one design limitation for each study.

Only use Sessions 5–6. Do not perform hypothesis tests or use methods from later sessions.

## Submission checklist

- [ ] Sampling distributions are distinguished from populations and observed samples.
- [ ] Standard error is distinguished from standard deviation.
- [ ] Exact normal sampling and the CLT approximation are distinguished.
- [ ] The \(t\) interval is used because population \(\sigma\) is unknown.
- [ ] Wilson is the primary proportion interval.
- [ ] Confidence levels use repeated-sampling interpretation.
- [ ] Bootstrap and planning calculations are reproducible.
- [ ] Part 4 contains AI-use and conclusion.
- [ ] All code is executed and output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

Be prepared to use examples from this assignment to explain random samples, statistics as random variables, sampling distributions, \(E[\bar X]\), \(\operatorname{SE}(\bar X)\), the law of large numbers, the central limit theorem, estimator versus estimate, bias and precision, confidence intervals and coverage, \(z\) versus \(t\), degrees of freedom, Wilson versus Wald, interval width and sample-size planning, and percentile bootstrap intervals.

You need not memorise Python syntax, but you must understand what is simulated or estimated, which interval is constructed, what assumptions it uses, and how its output is interpreted. AI use does not change this requirement.
