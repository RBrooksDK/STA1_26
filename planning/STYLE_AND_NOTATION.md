# Style, notation, and computational conventions

## Status and scope

This internal guide is the shared contract for the STA1 website, tutorials, notebooks, assignments, project and planned textbook. Public-facing material may explain a convention more gently, but it must not contradict this guide.

## Pedagogical voice

- Write for bachelor-level software and engineering students taking a practical statistics course.
- Begin with an engineering question, measurement or decision rather than a formula catalogue.
- Explain the statistical idea before naming the Python function.
- Use plain English, short paragraphs and concrete units.
- End every worked analysis with an interpretation in the problem context.
- Distinguish statistical significance from practical importance.
- State assumptions and limitations without turning every section into a warning list.
- Do not expose editorial instructions, AI prompts, unresolved drafting language or internal source disputes to students.
- Avoid claiming causation from observational data.

## Division of responsibility

| Artifact | Primary responsibility |
| --- | --- |
| Textbook | standalone theory, definitions, results, explanations at STA1 level, and worked examples using formulas |
| Session page | preparation, session focus, links, learning outcomes, material and assessment connection |
| Tutorial/notebook | guided practical analysis and executable Python |
| Assignment | a bounded analysis that students can defend orally |
| Group project | integrated method selection and complete engineering analysis |
| Course-site reference page | logistics, conventions, literature, datasets and exam information |

The website should not duplicate whole textbook sections. The textbook should not contain executable Python, exercises, semester dates, release schedules, course logistics, or platform instructions. It may mention that statistical software evaluates a quantity, but the concrete Python workflow belongs in the tutorials.

## Textbook environments

Reuse the visual system and LaTeX template from `MSE_book_v2`.

- **Definition:** terminology that must be used precisely.
- **Result/Theorem:** an actual mathematical or statistical statement, with assumptions.
- **Example:** a worked application with context, calculation and interpretation.
- **Remark:** clarification, nuance or connection.
- **Warning/Common mistake:** a specific recurring misconception, used sparingly.
- **Closing synthesis:** a natural prose transition or recap where useful, not a mandatory repeated chapter template.

Do not label procedural advice as a theorem. Do not use formal proof language where the course only needs an intuitive or simulation-based justification.

## Mathematical notation

| Concept | Convention |
| --- | --- |
| Sample space | \(S\) |
| Events | \(A,B,\ldots\) |
| Probability | \(P(A)\) |
| Conditional probability | \(P(A\mid B)\) |
| Random variable / realised value | \(X\) / \(x\) |
| Observations | \(x_1,\ldots,x_n\) |
| Population mean / variance / SD | \(\mu\), \(\sigma^2\), \(\sigma\) |
| Observed sample mean / variance / SD | \(\bar{x}\), \(s^2\), \(s\) |
| Random sample statistics | \(\bar{X}\), \(S^2\) |
| Population proportion / sample proportion | \(p\), \(\hat p\) |
| PMF | \(p_X(k)=P(X=k)\) |
| PDF | \(f_X(x)\) |
| CDF | \(F_X(x)=P(X\le x)\) |
| Expected value / variance | \(E[X]\), \(\operatorname{Var}(X)\) |
| Covariance / correlation | \(\operatorname{Cov}(X,Y)\), \(\rho\) for population and \(r\) for sample |
| Standard error | \(\operatorname{SE}(\hat\theta)\) |
| Significance level | \(\alpha\) |
| p-value | italic lower-case \(p\), disambiguated from a population proportion in the same context |
| Confidence level | \(1-\alpha\) |

### Distribution parameterisation

- Normal: \(X\sim N(\mu,\sigma^2)\). The second parameter is variance.
- Sample mean: \(\bar X\sim N(\mu,\sigma^2/n)\) when the stated conditions hold.
- Bernoulli: \(X\sim\operatorname{Bernoulli}(p)\).
- Binomial: \(X\sim\operatorname{Bin}(n,p)\).
- Poisson: \(X\sim\operatorname{Pois}(\lambda)\), with \(\lambda\) defined for the stated interval.
- Exponential: \(T\sim\operatorname{Exp}(\lambda)\), where \(\lambda\) is a rate and \(E[T]=1/\lambda\).
- Student t: state the degrees of freedom.
- Chi-square and F: state all relevant degrees of freedom.

If a source or software library uses a different parameterisation, translate it explicitly.

### Samples and variance

The observed sample variance is

\[
s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar{x})^2.
\]

Use population variance only when the data genuinely constitute the full population being described. Never switch between divisors silently.

### Hypothesis-testing language

- State the parameter before stating hypotheses.
- Write \(H_0\) and \(H_1\) explicitly.
- A p-value is a tail probability calculated under \(H_0\); it is not \(P(H_0\mid\text{data})\).
- Use “reject \(H_0\)” or “fail to reject \(H_0\)”.
- Do not use “accept \(H_0\)” as the routine conclusion.
- Report an estimate and confidence interval alongside a test whenever useful.
- Report exact p-values when practical; use \(p<0.001\) rather than `p = 0.000`.

## Python conventions

### Standard setup

```python
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA = Path("../data")
rng = np.random.default_rng(2026)
```

- From the repository root, use `Path("data")`; explain the difference once.
- Use `np.random.default_rng(seed)` rather than global random state.
- All simulations must be reproducible unless randomness itself is the teaching point.
- Pandas is the default for tables and grouping.
- SciPy named distributions are the default for probabilities, quantiles and simulation.
- Statsmodels is the default for inference, ANOVA and regression summaries.
- Statsmodels is also used for the statistical regression workflow in Session 10; scikit-learn and train/test modelling are outside the course scope.

### Translation table

| Mathematical quantity | Python convention |
| --- | --- |
| Sample SD | `x.std(ddof=1)` or `np.std(x, ddof=1)` |
| Population SD | `np.std(x, ddof=0)` |
| Standard error | `scipy.stats.sem(x)` with assumptions stated |
| \(N(\mu,\sigma^2)\) | `norm(loc=mu, scale=sigma)` |
| \(\operatorname{Bin}(n,p)\) | `binom(n=n, p=p)` or frozen distribution equivalent |
| \(\operatorname{Pois}(\lambda)\) | `poisson(mu=rate)` |
| \(\operatorname{Exp}(\lambda)\) | `expon(scale=1 / rate)` |

Do not use the Python identifier `lambda`; use `rate` or a context-specific name.

### Code quality

- Prefer short, readable cells that follow the analysis stages.
- Label axes and include units.
- Use meaningful variable names.
- Do not hide statistical choices in helper functions before students understand them.
- Avoid long dumps of library output without interpretation.
- Check assumptions with appropriate plots and diagnostics; do not describe a diagnostic as proof.
- Make code in Markdown tutorials and notebooks equivalent. Generate one from the other where practical to prevent drift.

## Figures, tables, and data

- Every figure has labelled axes, units and a caption or nearby explanatory sentence.
- Tables state units and use consistent precision.
- Do not use excessive decimal places.
- Record dataset provenance, licence, generation method, variables and units in `pages/datasets.md`.
- Synthetic data must be clearly documented internally and must use reproducible generation.
- Do not expose hidden “true” synthetic parameters in student-facing analysis unless the exercise is about simulation validation.

## Terminology

- **Population / sample:** complete target set versus observed subset.
- **Sample space / sample:** possible random outcomes versus observed data; explicitly distinguish the two meanings.
- **Parameter / statistic:** population quantity versus function of sample data.
- **Estimator / estimate:** random procedure versus realised numerical value.
- **Standard deviation / standard error:** variability in observations versus variability in an estimator.
- **Confidence interval / prediction interval:** uncertainty about a parameter or mean response versus uncertainty about a new observation.
- **Independent / mutually exclusive:** never treat these as synonyms.
- **Association / causation:** observational association does not establish causation.

## Chapter and session quality gate

Before a chapter/session bundle is approved:

- notation agrees with this guide;
- formulas and parameterisations have been checked;
- Python code executes from a clean environment;
- the dataset path and units are correct;
- the book and site state the same scope;
- the tutorial supports the stated outcomes;
- internal drafting instructions have been removed;
- reused material has been rewritten as needed and checked for copyright;
- the final example ends with an engineering interpretation;
- website and PDF layouts have been inspected visually.
