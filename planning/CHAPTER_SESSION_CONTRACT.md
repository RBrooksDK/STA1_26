# STA1 Chapter--Session Contract

## Purpose

This contract maintains a **one-to-one alignment** between the twelve taught
STA1 sessions, the twelve numbered chapters of *Statistics and Data Analysis
for Engineers*, and the corresponding Python tutorials.  Session 00 is an
orientation session and maps to Appendix A rather than a numbered chapter.

The contract is a planning and review document.  It does not itself change the
published course content.  When the book, website, tutorial, assignment, or
dataset changes, update the relevant row and the corresponding `source_map.md`
entry before publication.

## Shared chapter template

Every numbered chapter must contain the following, scaled to the topic:

1. **Engineering question and motivation** — one question that a practitioner
   could recognise.
2. **Learning outcomes** — phrased as observable abilities and matched to the
   session.
3. **Core concepts** — definitions, notation, and only the results needed for
   correct application.
4. **Worked engineering example** — calculations plus interpretation.
5. **Assumptions, diagnostics, and limitations** — including what a conclusion
   does *not* establish.
6. **Python in practice** — reproducible code, an appropriate plot/table, and
   a plain-language conclusion.
7. **Common pitfalls** — especially notation, interpretation, or library
   parameter traps.
8. **Short practice / bridge** — enough to prepare the tutorial and the
   relevant assignment; this is not a seventh assignment.
9. **References and data provenance** — source-checking reference, data origin,
   and licences where applicable.

Definitions, propositions/theorems, examples, remarks, and exercises should
use the same visual language as the MSE book template, but their amount must be
appropriate to a practical 5-ECTS statistics course.  Proof-heavy exposition
is not a goal unless it is necessary to avoid a misconception.

## Shared review fields

Each chapter/session has to answer these fields before it is marked complete:

| Field | Required decision or evidence |
| --- | --- |
| Canonical title | Exact same number and title in book, session page, tutorial, and plan. |
| Prerequisites | Earlier chapters and specific notation/code skills assumed. |
| Student outcome | What students can do after the session and independent practice. |
| In scope | Concepts, procedures, models, and interpretation rules taught. |
| Out of scope | Nearby material deliberately left to SMP1 or a later course. |
| Sources | MSE sections, Ross sections, old STA/SMP notes, existing STA1 material, and any new source. |
| Engineering context / data | One main scenario and named dataset(s), including provenance. |
| Python outcome | Libraries, functions, visualisations, reproducibility requirements, and expected interpretation. |
| Assessment bridge | Assignment/project/exam connection and student deliverable expectations. |
| Acceptance evidence | Mathematical review, notebook execution, PDF visual check, MkDocs strict build, and link check. |

## Common notation and Python contract

The canonical internal convention is `planning/STYLE_AND_NOTATION.md`.
`pages/conventions.md` is its student-facing counterpart.  The textbook and
public page must adopt the internal convention, or all three must be changed
together as one reviewed decision.

- Population parameters: \(\mu, \sigma^2, \sigma\); observed sample summaries:
  \(\bar{x}, s^2, s\); random statistics: \(\bar{X}, S^2\).
- Normal distributions use \(N(\mu,\sigma^2)\), while SciPy's `scale` is
  explicitly identified as the standard deviation \(\sigma\).
- Exponential distributions use rate \(\lambda\) in mathematics and `rate` in
  Python; code never uses the reserved name `lambda`.
- Sample variance is the \(n-1\) version.  NumPy examples must set `ddof=1`
  when a sample variance/standard deviation is intended.
- Tutorials set an explicit random seed when simulation is used, label plot
  axes with units, and finish with a context-specific conclusion.

## Alignment map

| Ch. / session | Canonical title | Main dependency | Assessment bridge |
| --- | --- | --- | --- |
| A / 00 | Getting Started with Python and Data | None | Enables all tutorials and assignments |
| 1 / 01 | Data and Descriptive Statistics | Appendix A | Assignment 1 |
| 2 / 02 | Probability for Data Analysis | Chapter 1 | Assignment 2 |
| 3 / 03 | Random Variables and Discrete Distributions | Chapter 2 | Assignment 2 |
| 4 / 04 | Continuous Distributions in Practice | Chapters 2--3 | Assignment 3 |
| 5 / 05 | Sampling Distributions and the Central Limit Theorem | Chapters 1, 3--4 | Assignment 3 |
| 6 / 06 | Estimation and Confidence Intervals | Chapter 5 | Assignment 4 |
| 7 / 07 | Hypothesis Testing I: Principles and One-Sample Tests | Chapter 6 | Assignment 4 |
| 8 / 08 | Hypothesis Testing II: Comparing Two Groups | Chapters 6--7 | Assignment 5 |
| 9 / 09 | Analysis of Variance | Chapter 8 | Assignment 5 |
| 10 / 10 | Simple Linear Regression | Chapters 1, 6--7 | Assignment 6 and project introduction |
| 11 / 11 | Categorical Data and Chi-Square Tests | Chapters 2--3, 7 | Assignment 6 |
| 12 / 12 | Integrated Statistical Analysis and Exam Preparation | Chapters 1--11 | Group project and oral exam |

## Per-chapter contracts

### Appendix A / Session 00 — Getting Started with Python and Data

- **Purpose:** establish a reproducible Python/Jupyter environment, file-path
  conventions, data import, and the distinction between a notebook and a
  report.
- **In scope:** Python installation route, Jupyter/VS Code workflow, imports,
  relative paths, DataFrame inspection, simple plot, seed use, and the course
  data catalogue.
- **Out of scope:** Python programming instruction beyond what is needed to
  begin statistical work.
- **Main sources:** existing STA1 Session 00 material and the course Python
  conventions.
- **Acceptance:** a new student can open and run the starter notebook from a
  clean checkout and locate a course dataset without editing hidden paths.

### Chapter 1 / Session 01 — Data and Descriptive Statistics

- **Purpose and outcome:** students describe a sample responsibly with tables,
  numerical summaries, histograms, boxplots, and scatterplots; distinguish
  sample/statistic from population/parameter.
- **In scope:** variable and data types, mean/median/mode, quartiles/IQR,
  sample variance and standard deviation, distribution shape, 1.5-IQR outlier
  flagging, and graphical summaries.
- **Out of scope:** inferential conclusions from plots, formal estimation
  theory, time-series decomposition.
- **Sources:** MSE Chapter 6; old STA descriptive-statistics material; existing
  STA1 Session 01 and `sensor_thickness.csv`; Ross 1.2--1.4 and 2.1--2.3 as
  checking/optional reading.
- **Python outcome:** import/clean a measurement file; compute `describe()`
  plus explicit summaries; make histogram, boxplot, and scatterplot with
  units; state a data-quality caveat.
- **Assessment bridge:** Assignment 1—small end-to-end descriptive analysis.
- **Acceptance:** book and notebook both explain why sample variance uses
  `ddof=1`; all displayed plots and conclusions are reproducible.

### Chapter 2 / Session 02 — Probability for Data Analysis

- **Purpose and outcome:** students translate a practical uncertainty question
  into events, tables/trees, conditional probabilities, independence, total
  probability, and Bayes' theorem.
- **In scope:** sample spaces, events, complement/union/intersection,
  conditional probability, independence, contingency tables, probability
  trees, total probability, and Bayes.
- **Out of scope:** standalone combinatorics catalogue, axiomatic proof
  development, and joint distributions.
- **Sources:** MSE Chapters 4--5 (selectively); old STA probability note and
  SMP Session 01 as explanation checks; existing STA1 Session 02; Ross
  3.1--3.4 and 3.6--3.8.
- **Python outcome:** calculate and visualise false-positive/false-negative
  scenarios from a contingency table; distinguish base rate from predictive
  value.
- **Assessment bridge:** Assignment 2 begins—probability modelling for an
  engineering process.
- **Acceptance:** every independence claim is distinguished from mutual
  exclusivity, and Bayes is interpreted in the data context.

### Chapter 3 / Session 03 — Random Variables and Discrete Distributions

- **Purpose and outcome:** students model engineering counts with random
  variables, PMFs/CDFs, expectation, variance, Bernoulli, binomial, and
  Poisson distributions.
- **In scope:** random variable versus observation, PMF/CDF, expectation and
  variance as summaries, Bernoulli/binomial/Poisson selection, and the
  binomial coefficient only in its binomial-model role.
- **Out of scope:** geometric/negative-binomial as core material, joint random
  variables, covariance of sums, and moment-generating functions.
- **Sources:** Ross 4.1--4.2, 4.4, 4.6, 5.1--5.2; old STA discrete-distribution
  notes; SMP Session 02; existing STA1 Session 03 and `packet_loss.csv`.
- **Python outcome:** use `scipy.stats.binom` and `poisson` for probabilities,
  compare observed counts with a plausible model, and report modelling limits.
- **Assessment bridge:** Assignment 2 completes.
- **Acceptance:** binomial assumptions are stated explicitly; Poisson parameter
  meaning and units are correct.

### Chapter 4 / Session 04 — Continuous Distributions in Practice

- **Purpose and outcome:** students use uniform, normal, and exponential
  distributions to analyse continuous measurements and waiting times.
- **In scope:** PDF/CDF/survival/quantile concepts, the zero probability of an
  exact continuous value, z-scores, model choice, normal diagnostics, and the
  practical Poisson-count/exponential-wait link.
- **Out of scope:** manual integration/CDF derivation, integral derivations of
  moments, Gamma/Weibull/logistic as core models, and Poisson-process theory.
- **Sources:** Ross 5.4--5.6; old STA continuous-distribution notes; SMP
  Session 03; existing STA1 Session 04, `response_times.csv`, and
  `component_lifetimes.csv`.
- **Python outcome:** use SciPy CDF/SF/PPF correctly, create a QQ plot, and
  explain why a diagnostic does not prove normality.
- **Assessment bridge:** Assignment 3 begins.
- **Acceptance:** normal is always parameterised by variance in prose/math and
  SciPy `scale` is described as standard deviation.

### Chapter 5 / Session 05 — Sampling Distributions and the CLT

- **Purpose and outcome:** students explain why sample means vary, calculate a
  standard error, and use simulation to understand the central limit theorem.
- **In scope:** statistic as random variable, sampling distribution of the
  mean, standard error, normal-population result, CLT conditions/limitations,
  repeated-sampling simulation.
- **Out of scope:** finite-population correction, CLT proof, and confusing the
  raw-data distribution with the distribution of a mean.
- **Sources:** Ross 6.1--6.5 (selectively); old STA sampling-distributions
  note; existing STA1 Session 05.
- **Python outcome:** simulate repeated samples with a fixed seed, plot sample
  means, compare empirical and theoretical standard errors, and identify a
  case where the CLT is not a remedy.
- **Assessment bridge:** Assignment 3 completes.
- **Acceptance:** the distribution is written \(N(\mu,\sigma^2/n)\), never
  with \(\sigma/\sqrt{n}\) in the variance position.

### Chapter 6 / Session 06 — Estimation and Confidence Intervals

- **Purpose and outcome:** students estimate means/proportions, construct and
  correctly interpret confidence intervals, and understand interval width.
- **In scope:** estimator versus estimate, intuitive bias, z- and t-intervals
  for a mean, approximate proportion interval, confidence-level interpretation,
  width versus sample size, and bootstrap as a computational check.
- **Out of scope:** maximum likelihood, Bayesian estimation, and full bootstrap
  theory; prediction intervals wait for Chapter 10.
- **Sources:** Ross 7.1, 7.3, 7.5; old STA interval-estimation note; SMP
  Session 06; existing STA1 Session 06 and `batteries.xlsx`.
- **Python outcome:** calculate intervals with transparent inputs, bootstrap a
  mean with a seed, and compare interval widths.
- **Assessment bridge:** Assignment 4 begins.
- **Acceptance:** no material says that a fixed parameter has a 95% probability
  of lying in the realised frequentist interval.

### Chapter 7 / Session 07 — Hypothesis Testing I: Principles and One-Sample Tests

- **Purpose and outcome:** students formulate one-sample questions, run and
  interpret one-sample mean/proportion tests, and connect p-values to intervals
  and practical decisions.
- **In scope:** \(H_0\), \(H_1\), one/two-sided choices, test statistic,
  p-value, significance level, type I/II errors, intuitive power, one-sample
  t-test, one-sample proportion test, and CI/test duality.
- **Out of scope:** two-sample/paired design and full power-curve calculation.
- **Sources:** Ross 8.1--8.3 and one-sample 8.6; old STA hypotheses note; SMP
  Session 07; existing STA1 Session 07 and a specification-focused dataset.
- **Python outcome:** perform both tests with assumptions and contextual
  conclusion; show why p-value is not \(P(H_0\mid\text{data})\).
- **Assessment bridge:** Assignment 4 completes.
- **Acceptance:** examples distinguish statistical from practical significance
  and include a suitable effect/context measure where possible.

### Chapter 8 / Session 08 — Hypothesis Testing II: Comparing Two Groups

- **Purpose and outcome:** students choose between independent and paired
  designs, compare two groups, and report uncertainty and practical effect.
- **In scope:** independent versus paired data, pooled versus Welch framing,
  two-sample t-test, paired t-test, interval for a difference, effect size, and
  practical versus statistical significance.
- **Out of scope:** two-variance tests as a standalone topic, indiscriminate
  repeated pairwise tests, and treating paired data as independent.
- **Sources:** Ross 7.4, 8.4, and two-sample 8.6; old STA testing material;
  existing STA1 Session 08 and `cpu_order_lines.xlsx`.
- **Python outcome:** inspect paired structure, use `ttest_ind`/`ttest_rel`
  appropriately, report a difference interval and visual comparison.
- **Assessment bridge:** Assignment 5 begins.
- **Acceptance:** every worked example states its design and avoids assuming
  equal variances without justification.

### Chapter 9 / Session 09 — Analysis of Variance

- **Purpose and outcome:** students compare three or more group means with
  one-way ANOVA, check practical assumptions, and use Tukey HSD responsibly.
- **In scope:** motivation versus many t-tests, between/within variation, ANOVA
  table, F test, independence/normality/similar-variance assumptions, one-way
  ANOVA, and Tukey HSD.
- **Out of scope:** two-way ANOVA, interaction effects, and identifying pairs
  from a significant omnibus F-test alone.
- **Sources:** Ross 10.1--10.3; STA_26 ANOVA session/site material; existing
  STA1 Session 09 and `resin_impurities.xlsx`.
- **Python outcome:** make group boxplots, run one-way ANOVA and Tukey HSD in
  statsmodels, diagnose assumptions at an introductory level, and communicate
  which comparisons differ.
- **Assessment bridge:** Assignment 5 completes.
- **Acceptance:** use a newly reviewed original ANOVA exposition and example;
  do not claim the old STA course has a separate note PDF if it does not.

### Chapter 10 / Session 10 — Simple Linear Regression

- **Purpose and outcome:** students fit, interpret, diagnose, and communicate
  a simple linear regression model, including the difference between mean
  response and new-observation prediction.
- **In scope:** response/predictor roles, least squares, intercept/slope with
  units, correlation and \(R^2\), slope inference, residual diagnostics,
  confidence interval for mean response, prediction interval, and a limited
  train/test illustration.
- **Out of scope:** multiple, polynomial, and logistic regression; causal
  inference from observational data; treating machine-learning metrics as
  statistical inference.
- **Sources:** Ross 9.1--9.2, 9.4--9.6; old STA regression note; SMP Session
  08; existing STA1 Session 10, `energy_load.csv`, and `scope_filter_intensity.xlsx`.
- **Python outcome:** fit using statsmodels for inference and scikit-learn only
  for the stated predictive comparison; create scatter, residual, and QQ plots.
- **Assessment bridge:** Assignment 6 begins; group project introduced.
- **Acceptance:** intervals are not conflated with prediction intervals, and
  \(R^2\) is not presented as causal evidence.

### Chapter 11 / Session 11 — Categorical Data and Chi-Square Tests

- **Purpose and outcome:** students analyse categorical counts using
  goodness-of-fit and independence tests and interpret residual patterns.
- **In scope:** categorical variables, contingency tables, expected counts,
  goodness-of-fit, independence, chi-square statistic, expected-count
  guideline, standardised residuals, and contextual conclusions.
- **Out of scope:** Ross 11.5--11.6 and causal claims from association.
- **Sources:** Ross 11.1--11.4; STA_26 goodness-of-fit/contingency material;
  existing STA1 Session 11 and `defect_types.csv`.
- **Python outcome:** build `crosstab`, run `chi2_contingency` and a
  goodness-of-fit calculation, inspect expected counts/residuals, and explain
  limitations for sparse tables.
- **Assessment bridge:** Assignment 6 completes.
- **Acceptance:** degrees of freedom and expected-count assumptions are correct
  in text, code, and output interpretation.

### Chapter 12 / Session 12 — Integrated Statistical Analysis and Exam Preparation

- **Purpose and outcome:** students select a justified method, complete an
  analysis from raw data to recommendation, and explain an assignment/project
  in the oral-exam format.
- **In scope:** method choice, problem formulation, data preparation,
  visualisation, assumptions, method selection, uncertainty, written
  recommendation, and oral explanation.
- **Out of scope:** new model families or a mock written examination replacing
  the oral format.
- **Sources:** existing STA1 method map, tutorials 01--11, assignment/project
  framework, official course description, and selected examples from earlier
  Ross/MSE chapters.
- **Python outcome:** a reproducible integrated notebook using a real or
  carefully designed engineering dataset, with an explicit decision trail.
- **Assessment bridge:** group project completion and oral-exam preparation.
- **Acceptance:** the method map, project brief, exam page, final tutorial, and
  textbook chapter all agree about what students must be able to defend.

## Completion checklist for a chapter/session pair

- [ ] Exact canonical title matches the alignment map.
- [ ] Session preparation points to the finished chapter/sections and valid
      supporting material.
- [ ] The chapter has all shared template sections appropriate to the topic.
- [ ] Website theory is concise and does not duplicate the full chapter.
- [ ] A dataset and engineering question are named and provenance is recorded.
- [ ] Tutorial notebook runs in a clean environment and its download link works.
- [ ] Formulae, notation, units, library parameters, and inferential claims have
      been reviewed.
- [ ] Assignment/project connection is accurate and does not promise an
      unapproved student task.
- [ ] PDF and MkDocs visual/build checks pass.
- [ ] `source_map.md` records the final sources, decisions, and any extension
      material.
