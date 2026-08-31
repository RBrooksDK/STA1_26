# Source map: *Statistics and Data Analysis for Engineers*

## Purpose

This is the editorial source map shared by the STA1 website and the planned textbook *Statistics and Data Analysis for Engineers*. It records what each chapter/session must cover, where the reusable material lives, and which sources are used only for verification or inspiration.

The book and course site must not drift apart. A scope change is first recorded here and in `planning/CHAPTER_SESSION_CONTRACT.md`, then applied to both artifacts.

## Authority and reuse

Use sources in this order:

1. The official STA1 course description and approved learning outcomes.
2. The frozen chapter/session contract in this repository.
3. Correct statistical theory, cross-checked against Ross and another authoritative source where necessary.
4. Brooks-authored material in `MSE_book_v2`, `STA_26`, `SMP1_25`, and `STA1_26`.
5. Newly written examples, explanations, Python tutorials, assignments, and project material.

Ross is a scope and verification source. Do not copy its prose, figures, examples, or exercises. Brooks-authored material may be revised and reused, but it must still be checked for correctness, notation, level, and fit with the new course.

Existing STA1 tutorials and notebooks are inputs, not curriculum authorities.
They may be reorganised, replaced, or rewritten when the MSE book, another
Brooks-authored example, or a newly designed example gives a clearer and more
correct learning progression. The final tutorial must follow the reviewed
textbook chapter and session contract, not constrain them.

## Structural correspondence

| Course item | Textbook item |
| --- | --- |
| Self-study 00 | Appendix A — Python and Data Setup |
| Session 01 | Chapter 1 — Descriptive Statistics |
| Session 02 | Chapter 2 — Probability for Data Analysis |
| Session 03 | Chapter 3 — Random Variables and Discrete Distributions |
| Session 04 | Chapter 4 — Continuous Distributions in Practice |
| Session 05 | Chapter 5 — Sampling Distributions and the Central Limit Theorem |
| Session 06 | Chapter 6 — Estimation and Confidence Intervals |
| Session 07 | Chapter 7 — Hypothesis Testing I: Principles and One-Sample Tests |
| Session 08 | Chapter 8 — Hypothesis Testing II: Comparing Two Groups |
| Session 09 | Chapter 9 — Analysis of Variance |
| Session 10 | Chapter 10 — Simple Linear Regression |
| Session 11 | Chapter 11 — Categorical Data and Chi-Square Tests |
| Session 12 | Chapter 12 — Planning and Reporting a Statistical Analysis |

## Chapter sources

### Appendix A — Python and Data Setup

- **STA1:** `00_Getting_Started_with_Python_and_Data/README.md`, `pages/conventions.md`, `pages/datasets.md`
- **Purpose:** environment setup, reproducibility, data paths, core packages, notebook and reporting workflow
- **Boundary:** installation and programming details belong here rather than in Chapter 1

### Chapter 1 — Data and Descriptive Statistics

- **STA1:** `01_Data_and_Descriptive_Statistics/README.md`, `Tutorial_01.md`, dataset `sensor_thickness.csv`
- **MSE:** `MSE_book_v2/chapter06.tex`
- **Old STA:** `01_Repetition_af_sandsynlighedsteori_og_stokastiske_variable/Tutorial_1.md`
- **Session notes:** [STA 01](https://drive.google.com/file/d/1D20cFjJA9CmBZQGu_rESr4u4jqoc_x7a/view?usp=sharing), used selectively
- **Ross check:** 1.2–1.4 and 2.1–2.3
- **Core:** populations and samples; data types; summaries; sample versus population variance; histograms, boxplots, scatterplots, shape and outliers
- **New work:** a coherent engineering dataset from import to interpretation; boxplots must appear here, not first in ANOVA

### Chapter 2 — Probability for Data Analysis

- **STA1:** `02_Probability_for_Data_Analysis/README.md`, `Tutorial_02.md`
- **MSE:** `MSE_book_v2/chapter04.tex` and `chapter05.tex`, selectively
- **Session notes:** [STA 01](https://drive.google.com/file/d/1D20cFjJA9CmBZQGu_rESr4u4jqoc_x7a/view?usp=sharing), [SMP 01](https://drive.google.com/file/d/1oqEy7sINksGCfdytv_O8qIZ0FoVEyWjz/view?usp=drive_link)
- **Ross check:** 3.1–3.4 and 3.6–3.8
- **Core:** events, rules, conditional probability, independence, total probability, Bayes, contingency tables and probability trees
- **Boundary:** no standalone combinatorics catalogue; joint-distribution theory remains in SMP1
- **Implemented draft:** the textbook and tutorial use one automated optical-inspection case throughout. The tutorial follows the reviewed chapter from event algebra and contingency tables through independence, Bayes, base-rate sensitivity, and simulation; it is a downstream practice layer rather than a source constraint.

### Chapter 3 — Random Variables and Discrete Distributions

- **STA1:** `03_Random_Variables_and_Discrete_Distributions/README.md`, `Tutorial_03.md`, dataset `packet_loss.csv`
- **Old STA:** sessions 02–03 and their tutorials
- **Session notes:** [STA 02](https://drive.google.com/file/d/1azFhbhkKSIiLboKuxTlyhh-41jYMtbRm/view?usp=sharing), [STA 03](https://drive.google.com/file/d/1laRKIxHLa2DBjmzVMQuKyc6vilaPrFNx/view?usp=sharing), [SMP 02](https://drive.google.com/file/d/1LJ8Nu0D1PLLB1FF1jTsLK50HGLhl1EtG/view?usp=sharing)
- **Ross check:** 4.1–4.2, 4.4, 4.6, 5.1–5.2; optional parts of 5.3
- **Core:** random variables, PMF, CDF, expectation, variance, Bernoulli, binomial and Poisson; SciPy and simulation
- **Boundary:** geometric, negative binomial and hypergeometric are enrichment; no MGFs or multivariate theory

### Chapter 4 — Continuous Distributions in Practice

- **STA1:** `04_Continuous_Distributions_in_Practice/README.md`, `Tutorial_04.md`, datasets `response_times.csv` and `component_lifetimes.csv`
- **Old STA:** sessions 04–05 and their tutorials
- **Session notes:** [STA 04](https://drive.google.com/file/d/1hfivT-AFbsnR9CxJeff-K2dTC7MC-HPZ/view?usp=sharing), [STA 05](https://drive.google.com/file/d/1qTGWWIihQLTLNe0e-0nUwGIbpkH7XWkS/view?usp=sharing), [SMP 03](https://drive.google.com/file/d/1-MKzwovM7uHrSUQ_XBe1NczVT2ssdbKd/view?usp=sharing)
- **Ross check:** 5.4–5.6
- **Core:** PDF, CDF, survival function, quantiles, uniform, normal and exponential models, standardisation and QQ-plots
- **Boundary:** probability is explained as area, but students do not integrate densities by hand; no calculus-based moment derivations

### Chapter 5 — Sampling Distributions and the Central Limit Theorem

- **STA1:** `05_Sampling_Distributions_and_the_CLT/README.md`, `Tutorial_05.md`
- **Old STA:** session 06 and its tutorial
- **Session notes:** [STA 06](https://drive.google.com/file/d/1YQHZe0Ukj0Jkhn3vTrjLkFKJfVwcWUOg/view?usp=sharing)
- **Ross check:** 6.1–6.3 and selected parts of 6.4–6.5
- **Core:** statistics as random variables, sampling distribution of the mean, standard error and simulation-based CLT
- **Critical check:** distinguish `N(mu, sigma^2/n)` in the book from SciPy's `scale=sigma/sqrt(n)`

### Chapter 6 — Estimation and Confidence Intervals

- **STA1:** `06_Estimation_and_Confidence_Intervals/README.md`, `Tutorial_06.md`
- **Old STA:** session 07 and its tutorial
- **Session notes:** [STA 07](https://drive.google.com/file/d/1HV1sbPdtBIYqaGUiHVdnnVXospCYBhAK/view?usp=sharing), [SMP 06](https://drive.google.com/file/d/1EFr1Pz5E2lyVtgxd2Lwj9O4SdvcyXw_x/view?usp=sharing)
- **Ross check:** 7.1, 7.3 and 7.5; defer 7.4 to Chapter 8
- **Core:** estimator versus estimate, bias and precision, standard error, z- and t-intervals for a mean, interval for a proportion and correct coverage interpretation
- **Enrichment:** one small bootstrap interval as a computational check

### Chapter 7 — Hypothesis Testing I

- **STA1:** `07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/README.md`, `Tutorial_07.md`
- **Old STA:** one-sample portions of session 08 and `Tutorial_8.md`
- **Session notes:** [STA 08](https://drive.google.com/file/d/1Ji4laf6gU06-unx-QhclQupT4u9OePUA/view?usp=sharing), [SMP 07](https://drive.google.com/file/d/1sIXa8DCVkjguV8dHwXPTtPZiQKLZsc-o/view?usp=sharing)
- **Ross check:** 8.1–8.3 and the one-sample part of 8.6
- **Core:** hypotheses, one- and two-sided alternatives, alpha, p-values, errors, intuitive power, one-sample t-test and proportion test
- **Critical language:** never define a p-value as `P(H0 | data)`; use “fail to reject,” not “accept”

### Chapter 8 — Hypothesis Testing II

- **STA1:** `08_Hypothesis_Testing_II_Comparing_Two_Groups/README.md`, `Tutorial_08.md`, dataset `response_times.csv`
- **Old STA:** two-sample and paired portions of session 08 and `Tutorial_8.md`
- **Session notes:** [STA 08](https://drive.google.com/file/d/1Ji4laf6gU06-unx-QhclQupT4u9OePUA/view?usp=sharing), [SMP 07](https://drive.google.com/file/d/1sIXa8DCVkjguV8dHwXPTtPZiQKLZsc-o/view?usp=sharing)
- **Ross check:** 7.4, 8.4 and the two-sample part of 8.6
- **Core:** independent versus paired designs, Welch t-test, paired t-test, two proportions, confidence intervals and effect sizes
- **Design rule:** determine the sampling design before selecting a Python function

### Chapter 9 — Analysis of Variance

- **STA1:** `09_Analysis_of_Variance/README.md`, `Tutorial_09.md`, datasets `resin_impurities.xlsx` and `scope_filter_intensity.xlsx`
- **Old STA:** `10_Variansanalyse_ANOVA/README.md` and tutorial/site exercises
- **Ross check:** 10.1–10.3
- **Core:** family-wise type I error, one-way ANOVA, between/within variation, F-statistic, assumptions, diagnostics and Tukey HSD
- **New work:** the old course has no separate session-notes PDF; this chapter requires substantial new prose, examples, and figures
- **Boundary:** no two-way ANOVA or interactions in core STA1

### Chapter 10 — Simple Linear Regression

- **STA1:** `10_Simple_Linear_Regression/README.md`, `Tutorial_10.md`, `Calculating_metrics.md`, dataset `energy_load.csv`
- **Old STA:** session 09 and `Tutorial_9.md`
- **Old SMP:** session 08 and `Calculating_metrics.md`
- **Session notes:** [STA 09](https://drive.google.com/file/d/155VOAnrutze7091LObcAhAcnau__uBl1/view?usp=sharing), [SMP 08](https://drive.google.com/file/d/1N_hUEd6Hwn93dVtaSWHsFqe9N47E2WRg/view?usp=sharing)
- **Ross check:** 9.1–9.2 and 9.4–9.6
- **Core:** least squares, coefficient interpretation, correlation, R-squared, slope inference, residual diagnostics, confidence and prediction intervals
- **Python:** statsmodels for coefficients, inference, diagnostics, confidence intervals, and prediction intervals; no machine-learning train/test workflow

### Chapter 11 — Categorical Data and Chi-Square Tests

- **STA1:** `11_Categorical_Data_and_Chi_Square_Tests/README.md`, `Tutorial_11.md`, dataset `defect_types.csv`
- **Old STA:** `10_Goodness_of_fit_og_analyse_af_kategoriske_data/README.md` and tutorial/site exercises
- **Ross check:** 11.1–11.4
- **Core:** counts and proportions, expected counts, goodness-of-fit, independence versus homogeneity, assumptions, Pearson and adjusted residuals, Cramér's V, simulation, and sparse-table alternatives
- **New work:** there is no separate old session-notes PDF; create a coherent textbook narrative and original engineering examples

### Chapter 12 — Planning and Reporting a Statistical Analysis

- **STA1:** `12_Integrated_Analysis_and_Exam_Preparation/README.md`, `Tutorial_12.md`, `pages/assignments.md`, `pages/project.md`
- **Inputs:** selected datasets and examples from Chapters 1–11
- **Core:** question, data audit, visualisation, method choice, assumptions, estimates, uncertainty, conclusion and recommendation
- **Boundary:** exam instructions stay on the course site; the book chapter teaches a reusable workflow

## SMP material outside STA1 core

- [SMP multivariate notes](https://drive.google.com/file/d/1oUHWdzQZa62bTqsmLe_eRts7OpOEhFgJ/view?usp=sharing) may support intuitive covariance/correlation explanations.
- Stochastic processes, Markov chains, joint densities, transformations and MGFs are not STA1 textbook chapters.
- Calculus-heavy derivations from SMP must not migrate into the practical STA1 treatment.

## Required per-chapter source package

Before drafting a chapter, record:

- official learning outcome and session outcome;
- primary Brooks-authored sources;
- Ross verification sections;
- dataset, units, provenance and licence;
- definitions and results to include;
- Python functions and conventions;
- worked engineering example;
- assignment/project connection;
- known gaps and disputed points;
- completed mathematical, computational and copyright checks.

## Known gaps

1. ANOVA and categorical analysis require the most new textbook writing.
2. Old hypothesis-testing material must be divided cleanly between Chapters 7 and 8.
3. MSE probability Chapters 4–5 must be condensed; general combinatorics is removed from the STA1 narrative.
4. Continuous-distribution explanations must be rewritten without manual integration.
5. The six assignment briefs remain placeholders. The fixed group-project requirements are already synchronised across the assessment page and Tutorial 12; the detailed project brief will be added separately.
6. Every reused example must be checked for units, assumptions, notation, licensing and alignment with the practical Python focus.
