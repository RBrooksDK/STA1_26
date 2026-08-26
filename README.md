<p align="center">
    <h1 align="center">Statistics and Data Analysis for Engineers - 2026</h1>
    <p align="center">Course page for <a href="https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0">STA1</a> at VIA University College</p>
</p>

<p align="center">
  <a href="https://rbrooksdk.github.io/STA1_26">
    <video class="video-light custom-video" width="700" autoplay loop muted src="figures/sta_intro_light.mp4?v=2"></video>
    <video class="video-dark custom-video" width="700" autoplay loop muted src="figures/sta_intro_dark.mp4?v=2"></video>
  </a>
</p>

## <i class="fas fa-circle-info" style="color:#6CA2C6"></i> Course Information

* **Course Responsible:** [Richard Brooks](https://rbrooksdk.github.io), <rib@via.dk>
* **Credits:** 5 ECTS (European Credit Transfer System), equivalent to about 135 working hours
* **Sessions:** 12 sessions of \(2 \times 45\) minutes, plus independent work on tutorials, assignments, and the project
* **Level:** Bachelor — practical statistics for software and engineering students
* **Assessment:** 20-minute oral exam based on one of the six assignments and a discussion of the group project
* **Recommended prerequisites:** Mathematics at the programme admission level. The course itself introduces descriptive statistics and the probability needed for inference.

## <i class="fas fa-vector-square" style="color:#6CA2C6"></i> Lectures and Course Organization

STA1 is a **practical data-analysis course**. Each session focuses on one statistical idea, one worked engineering example, and a short Python demonstration. Tutorials, assignments, and the group project provide the main opportunity to practise.

A typical 90-minute session looks like this:

1. A short recap of the previous session.
2. The statistical problem of the day, with one carefully chosen engineering example.
3. A live Python demonstration that connects the formula to software.
4. Time to start the tutorial or the current assignment.

After class, complete the session tutorial and work on the current assignment when it is released.

STA1 is the sister course of [Stochastic Modelling and Processes (SMP1)](https://rbrooksdk.github.io/SMP1_26/). The overlap is intentional and limited:

- **STA1** asks: *What can we conclude from observed data?*
- **SMP1** asks: *How do we model and simulate systems that evolve under uncertainty?*

## <i class="fas fa-clipboard-list" style="color:#6CA2C6"></i> Assignments and Project

The course contains **six practice-oriented group assignments** and one **small group project**. These are the official learning activities from the [course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0). They are also the basis of the exam.

| Activity | After session | Focus |
| ---: | ---: | --- |
| Assignment 1 | 01 | Data, preprocessing, and descriptive analysis |
| Assignment 2 | 03 | Probability and discrete models |
| Assignment 3 | 05 | Continuous models, sampling, and the CLT |
| Assignment 4 | 07 | Confidence intervals and one-sample tests |
| Assignment 5 | 09 | Comparing two and several groups |
| Assignment 6 | 11 | Regression and categorical data |
| Project | 12 | A complete analysis of an engineering data set |

See [Assignments](pages/assignments.md) and [Project](pages/project.md) for the assessment overview. The detailed briefs will be published during the semester through the relevant session assessment pages.

## <i class="fas fa-wave-square" style="color:#6CA2C6"></i> Course Content and Learning Objectives

The course moves from describing data, through modelling uncertainty, to drawing conclusions and communicating them for engineering decisions.

**Learning Objectives**

- **Descriptive statistics**: summarise and visualise measurements with histograms, boxplots, scatterplots, and numerical summaries.
- **Probability foundations**: use random variables, mean, and variance as the language of uncertainty.
- **Distributions**: apply binomial, Poisson, normal, and exponential models to engineering problems.
- **Sampling and estimation**: explain sampling distributions and the central limit theorem, and construct confidence intervals.
- **Hypothesis testing**: formulate, perform, and interpret \(t\)-tests, including type I and type II errors and \(p\)-values.
- **Comparing groups**: analyse several groups with one-way ANOVA and post-hoc comparisons.
- **Modelling relationships**: fit and interpret simple linear regression, including residual analysis.
- **Categorical data**: use contingency tables and chi-square tests.
- **Engineering communication**: select methods, state assumptions, and present results so that a technical or non-technical stakeholder can act on them.

Python is used throughout with Pandas, NumPy, SciPy, Matplotlib, and, where it is statistically appropriate, scikit-learn.

## <i class="fas fa-clock" style="color:#6CA2C6"></i> Expected Workload

| Activity | Hours |
| --- | ---: |
| 12 sessions \(\times\) 1.5 hours | 18 |
| Tutorials and independent practice | 36 |
| Six assignments | 48 |
| Group project | 25 |
| Exam preparation | 8 |
| **Total** | **135** |

## <i class="fas fa-book-open" style="color:#6CA2C6"></i> Resources

The current course readings use two books, with one primary text per session:

- Richard Brooks, *Mathematics for Software Engineering*, Chapters 4–6, for Sessions 1–2.
- Sheldon M. Ross, *Introduction to Probability and Statistics for Engineers and Scientists*, 6th edition, for Sessions 3–12.

The mapping from sessions to sections is on the [Literature](pages/literature.md) page. Notation and Python conventions are collected in [Conventions](pages/conventions.md). Data files live in `data/` and are catalogued under [Datasets](pages/datasets.md).

Install a working Python 3.10+ environment with Jupyter. The easiest route is [Anaconda](https://www.anaconda.com/products/distribution) or VS Code with the Jupyter extension. Session 00 walks through the setup.
