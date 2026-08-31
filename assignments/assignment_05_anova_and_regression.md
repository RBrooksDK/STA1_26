# Assignment 5 — ANOVA and Simple Linear Regression

In this mini-project, you will analyse quantitative responses with two different predictors. ANOVA compares mean strength across categorical curing methods; simple linear regression models mean energy use against a quantitative flow rate. Both analyses require study-design reasoning, residual diagnostics, effect estimates, and uncertainty.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Sessions 9–10 and Brooks, Chapters 9–10
    - **Required method:** Python with statsmodels and SciPy where appropriate

## Preparation, resources and AI

Review Sessions and Tutorials [9](../09_Analysis_of_Variance/README.md) and [10](../10_Simple_Linear_Regression/README.md), together with [Brooks: Chapters 9–10](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use:

1. [assignment05_composite_strength.csv](../data/assignment05_composite_strength.csv); and
2. [assignment05_pump_energy.csv](../data/assignment05_pump_energy.csv).

Begin with the title, group members, table of contents, imports, and both files loaded from a local data folder.

### How to present your work

Use the fitted models to answer the stated engineering questions rather than copying complete software summaries without explanation. Every conclusion must include the effect in engineering units, uncertainty, diagnostic evidence, and design limitations.

### Working with AI

AI may help formulate models, use statsmodels, construct diagnostics, interpret output, and critique conclusions. You remain responsible for checking whether the code matches the question and whether assumptions are credible. Part 5 documents your AI use.

## Part 1 — Composite strength across curing methods

The file [assignment05_composite_strength.csv](../data/assignment05_composite_strength.csv) contains independent composite specimens cured by four methods. The response is `strength_mpa`; the factor is `curing_method`.

Complete the following tasks:

1. Identify the population, observational unit, response, factor, and factor levels. Explain what additional design information would be needed for a causal claim about curing method.
2. Report group sample sizes, means, and sample standard deviations. Create side-by-side boxplots and describe between-group differences and within-group variation.
3. State the one-way ANOVA hypotheses. Explain why a collection of unadjusted pairwise \(t\)-tests is a poor default.
4. Fit the classical one-way model and produce an ANOVA table. Report sums of squares, degrees of freedom, mean squares, \(F\), and \(p\), and explain what the \(F\) ratio compares.

## Part 2 — Diagnostics, post-hoc comparisons, and magnitude

Continue with the composite-strength study.

1. Diagnose independence from the study description and inspect within-group errors using group spreads, residual-versus-fitted, and a QQ-plot of residuals. Explain why the pooled raw response is not the correct normality diagnostic.
2. Decide whether the classical common-variance model is credible. Also run Welch's one-way ANOVA as a sensitivity analysis and explain why it is not paired automatically with ordinary Tukey HSD.
3. Calculate \(\eta^2=SS_{\text{between}}/SS_{\text{total}}\) and interpret it as a descriptive fraction of observed squared variation, not causation.
4. If the classical omnibus test is relevant and significant, perform Tukey HSD. Report simultaneous pairwise intervals and adjusted \(p\)-values and identify which curing methods are distinguishable. Do not treat a non-significant pair as proof of equal means.
5. Write a recommendation in MPa that distinguishes the global question, specific pairwise differences, practical importance, and design limitations.

## Part 3 — Pump flow and energy use

The file [assignment05_pump_energy.csv](../data/assignment05_pump_energy.csv) contains independent benchmark runs over an observed flow-rate range. Let energy use be \(Y\) and flow rate be \(x\), with the statistical model

\[
Y=\beta_0+\beta_1x+\varepsilon.
\]

Complete the following tasks:

1. Identify the population, observational unit, response, predictor, and observed predictor range. Create a scatterplot and discuss whether a linear conditional-mean model is plausible before fitting it.
2. Fit an intercept model with statsmodels. Report and interpret \(\hat\beta_0\), \(\hat\beta_1\), residual standard deviation, Pearson correlation \(r\), and \(R^2\). Include units and discuss whether the intercept has a useful engineering interpretation.
3. Verify that \(R^2=r^2\) for this simple intercept model. Explain what correlation and \(R^2\) measure and what they do not establish.
4. Test \(H_0:\beta_1=0\) against a two-sided alternative and report the slope estimate, standard error, 95% interval, \(t\), degrees of freedom, and \(p\)-value. State the conclusion as an association, not automatically as causation.

## Part 4 — Regression diagnostics and prediction

Continue with the pump study.

1. Create residual-versus-fitted, residual-versus-run-order, and normal QQ-plots. Discuss linearity, constant spread, unusual observations, normal-error approximation, and what the plots cannot establish about independence or sampling.
2. Calculate leverage and Cook's distance. Identify the most influential run, investigate it rather than deleting it automatically, and explain what operational information you would seek.
3. At \(x_0=70\) L/min, report the fitted mean energy, a 95% confidence interval for mean energy, and a 95% prediction interval for one new run. Explain why the prediction interval is wider.
4. Explain why using this fitted line at 10 or 120 L/min would be extrapolation. State what evidence would be needed before extending the relationship outside the observed range.
5. Give a practical conclusion that includes slope in kWh per L/min, uncertainty, residual variation, \(R^2\), prediction uncertainty, and study-design limitations.

## Part 5 — AI-use and conclusion

### AI-use

State which AI tools you used, what they contributed, what you changed or rejected, and how you verified the work. A short paragraph or table is sufficient.

### Overall conclusion

Write approximately 150–250 words comparing ANOVA and regression as methods for a quantitative response. Explain how the type of predictor determines the question, how residuals are used in both analyses, and why statistical modelling does not by itself prove causation.

Only use Sessions 9–10. Do not use multiple regression or machine-learning workflows.

## Submission checklist

- [ ] The ANOVA factor, response, units, and hypotheses are clear.
- [ ] Classical versus Welch ANOVA is justified from diagnostics.
- [ ] Tukey is used only with a compatible significant classical analysis.
- [ ] \(\eta^2\) is not interpreted causally.
- [ ] Regression coefficients, \(r\), and \(R^2\) are interpreted correctly.
- [ ] Residual and influence diagnostics are included.
- [ ] Mean-response and prediction intervals are distinguished.
- [ ] Extrapolation and causal claims are limited.
- [ ] Part 5 contains AI-use and conclusion.
- [ ] All code is executed and output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

Be prepared to use examples from this assignment to explain one-way ANOVA, between- and within-group variation, the \(F\) statistic and ANOVA table, family-wise error, classical versus Welch ANOVA, Tukey HSD, \(\eta^2\), the simple linear regression model, least squares, fitted values and residuals, slope and intercept, correlation, \(R^2\), inference for the slope, diagnostics, leverage and influence, confidence versus prediction intervals, extrapolation, and the role of study design in causal interpretation.

You need not memorise code, but you must understand every fitted model, output quantity, diagnostic, and engineering conclusion. AI use does not change this requirement.
