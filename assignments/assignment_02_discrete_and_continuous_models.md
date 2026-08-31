# Assignment 2 — Discrete and Continuous Probability Models

In this mini-project, you will use Python to analyse discrete random variables and continuous probability models. The cases are fixed and cover finite probability tables, binomial and Poisson counts, and uniform, normal, and exponential models.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Submission:** one executed Jupyter notebook in English
    - **Expected workload:** approximately 5–8 hours in total
    - **Statistical scope:** Sessions 3–4 and Brooks, Chapters 3–4
    - **Required method:** Python, supported by formulas and interpretation in Markdown

## Preparation, resources and AI

Before beginning, review:

- [Session 3 — Random Variables and Discrete Distributions](../03_Random_Variables_and_Discrete_Distributions/README.md);
- [Tutorial 3](../03_Random_Variables_and_Discrete_Distributions/Tutorial_03_notebook.ipynb);
- [Session 4 — Continuous Distributions in Practice](../04_Continuous_Distributions_in_Practice/README.md);
- [Tutorial 4](../04_Continuous_Distributions_in_Practice/Tutorial_04_notebook.ipynb); and
- [Brooks: Chapters 3–4](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).

Use:

1. [assignment02_concrete_strength.csv](../data/assignment02_concrete_strength.csv); and
2. [assignment02_service_repairs.csv](../data/assignment02_service_repairs.csv).

Begin with the assignment title, group members, a table of contents, imports, and both data files loaded from a local data folder.

### How to present your work

Use executed Python cells for model calculations, tables, fitted parameters, and plots. Use Markdown cells to define random variables and events, show requested formulas, justify model assumptions, and interpret results. Selected formulas may be written manually and embedded clearly, but any task requesting SciPy or a plot must include executable code.

### Working with AI

AI use is encouraged for translating probability statements into SciPy functions, checking parameterisations, debugging plots, challenging assumptions, and improving explanations. You remain responsible for every result. In Part 5, state how AI was used and how its output was checked.

## Part 1 — Cooling-unit failures: a finite random variable

Let \(X\) be the number of cooling units that fail during a weekly maintenance window. The engineering model is

| \(x\) | 0 | 1 | 2 | 3 | 4 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(P(X=x)\) | 0.58 | 0.26 | 0.10 | 0.04 | 0.02 |

Complete the following tasks:

1. Verify that the table is a valid PMF, state the support, and distinguish the random variable \(X\) from an observed value \(x\).
2. Construct a table containing \(x\), \(p_X(x)\), and \(F_X(x)\). Use it to calculate \(P(X=2)\), \(P(X\le1)\), \(P(X\ge2)\), and \(P(1<X\le3)\).
3. Plot the PMF as a bar chart and the CDF as a step plot. Explain the meaning of the height at each value in both plots.
4. Calculate and interpret \(E[X]\), \(\operatorname{Var}(X)\), and \(\operatorname{SD}(X)\).

## Part 2 — Repeated-event count models

### Late supplier deliveries: binomial

A project expects 30 deliveries. Each is modelled as late with probability 0.12 independently of the others. Let \(B\) be the number of late deliveries.

1. Justify \(B\sim\operatorname{Bin}(30,0.12)\). Identify the Bernoulli trial and discuss fixed \(n\), constant \(p\), independence, and one realistic violation.
2. Use SciPy to calculate \(P(B=3)\), \(P(B\le4)\), and \(P(B\ge5)\). For \(P(B=3)\), also show the binomial formula and explain \(\binom{n}{k}\). For the upper tail, explain the correct survival-function argument.
3. Calculate and interpret the mean and standard deviation.

### Production stoppages: Poisson

Short stoppages are modelled as a Poisson process with mean 1.6 per 8-hour shift. Let \(Y\) be the count during one shift.

1. State the model, parameter, support, mean, and variance. Calculate \(P(Y=0)\) and \(P(Y\ge3)\) for one shift.
2. Scale the expected count and calculate the probability of at least three stoppages in 24 hours. Discuss the stable-rate and independent-event assumptions.

## Part 3 — Uniform and normal models

### Sensor polling delay: uniform

A monitoring device polls a sensor once every 12 seconds. An event is assumed to occur at a random point in the cycle, so the delay \(D\) until the next poll is modelled as \(D\sim\operatorname{Uniform}(0,12)\).

1. Create the SciPy model using the correct location and scale. Plot its PDF and CDF and explain the support, constant density, and why \(P(D=d)=0\).
2. Calculate \(P(D\le3)\), \(P(4<D<9)\), \(P(D>10)\), the mean, standard deviation, and 95th percentile.

### Concrete strength: normal working model

The file [assignment02_concrete_strength.csv](../data/assignment02_concrete_strength.csv) contains 160 compressive-strength measurements. Treat the generating parameters as unknown.

1. Report \(n\), mean, median, and sample standard deviation. Fit \(N(\hat\mu,\hat\sigma^2)\) and explain why SciPy receives \(\hat\sigma\), not \(\hat\sigma^2\), as `scale`.
2. Plot a density histogram with the fitted PDF and create a normal QQ-plot. Discuss symmetry, tails, unusual observations, and model adequacy.
3. From the fitted model, calculate \(P(X<35)\), \(P(38<X<46)\), the 95th percentile, and the \(z\)-score of 35 MPa. Compare the first two model probabilities with empirical proportions.

## Part 4 — Service restoration: an exponential working model

The file [assignment02_service_repairs.csv](../data/assignment02_service_repairs.csv) contains 180 restoration times from independent service incidents. Treat the rate as unknown.

1. Report \(n\), mean, median, sample standard deviation, minimum, and maximum. Plot a density histogram and describe the shape.
2. Fit an exponential model using \(\hat\lambda=1/\bar x\). State its fitted rate, mean, variance, and SciPy scale and add the fitted PDF to the histogram.
3. Compare empirical and fitted distributions using an empirical CDF with fitted CDF or an exponential QQ-plot. Discuss model strengths and limitations.
4. Calculate and interpret \(P(T\le30)\), \(P(T>120)\), the median, and the 90th percentile. Compare the two model probabilities with empirical proportions.
5. Calculate \(P(T>150\mid T>60)\) as both a ratio of survival probabilities and the probability of waiting an additional 90 minutes. Explain the memoryless and constant-rate assumptions.

## Part 5 — AI-use and conclusion

### AI-use

State which AI tools you used, what they contributed, what you changed or rejected, and how you verified the result. A short paragraph or table is sufficient. If AI produced most of the code or text, state this honestly.

### Overall conclusion

Write approximately 150–250 words comparing the probability models used in the assignment. Explain how support, mechanism, parameterisation, and graphical model assessment determine whether a calculated probability is useful.

Only use Sessions 3–4. Do not use sampling distributions, confidence intervals, hypothesis tests, bootstrap procedures, or later methods.

## Submission checklist

- [ ] Every random variable, event, support, and parameter is defined.
- [ ] PMF, PDF, CDF, SF, and PPF are used appropriately.
- [ ] Binomial and Poisson assumptions are discussed.
- [ ] SciPy scale parameters are correct.
- [ ] Fitted normal and exponential models are assessed graphically.
- [ ] Model probabilities and empirical proportions are distinguished.
- [ ] Part 5 contains the AI-use statement and conclusion.
- [ ] All code is executed and output is visible.

## Theory and code at the oral exam

The concepts below are the theory connected to this assignment. The oral examination will sample from this material; it is not expected to cover every item.

Be prepared to use examples from this assignment to explain random variables and observed values; PMFs, PDFs, CDFs, SFs, and quantiles; expectation and variance; Bernoulli, binomial, and Poisson models; uniform, normal, standard normal, and exponential models; \(z\)-scores; memorylessness; parameter estimation for a working model; graphical model assessment; and the assumptions and limitations of every model used.

You need not memorise Python syntax, but you must understand the model, parameters, function, plot, and engineering interpretation behind every code cell. AI use does not change this requirement.
