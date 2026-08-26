<h1 align="center">Assignments</h1>

The [course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0) specifies **six practice-oriented group assignments** and a **small group project** distributed through the semester. They connect statistical theory with engineering applications and form the exam basis.

Detailed task briefs will be published during the semester.

## Purpose

Each assignment is a complete, small analysis that you should be able to defend in a 20-minute oral exam:

1. state an engineering question;
2. prepare or simulate relevant data;
3. choose and apply a statistical method;
4. interpret the result, including assumptions and uncertainty;
5. communicate a recommendation.

Tutorial examples prepare you for the assignments; they are not additional assessment tasks.

## Cadence

| Assignment | After session | Statistical focus |
| ---: | ---: | --- |
| 1 | [01 Descriptive statistics](../01_Data_and_Descriptive_Statistics/README.md) | Data collection or import, preprocessing, summaries, and visualisation |
| 2 | [03 Discrete distributions](../03_Random_Variables_and_Discrete_Distributions/README.md) | Probability, random variables, and discrete models |
| 3 | [05 Sampling and the CLT](../05_Sampling_Distributions_and_the_CLT/README.md) | Continuous models, sampling distributions, and the CLT |
| 4 | [07 Hypothesis testing I](../07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/README.md) | Confidence intervals and one-sample tests |
| 5 | [09 ANOVA](../09_Analysis_of_Variance/README.md) | Two-sample tests and comparison of several groups |
| 6 | [11 Categorical data](../11_Categorical_Data_and_Chi_Square_Tests/README.md) | Simple linear regression and categorical analysis |
| Project | [12 Integrated analysis](../12_Integrated_Analysis_and_Exam_Preparation/README.md) | A complete analysis of an engineering data set |

## Format

The detailed brief for each assignment will confirm the requirements. Unless a brief says otherwise, use these defaults:

- **Group size:** 2–4 students.
- **Product:** a short Jupyter notebook (or a short report plus notebook) with a clear question, analysis, figures, and a written conclusion in ordinary language.
- **Length:** enough to be discussed in 20 minutes — typically a few pages of narrative, not a dump of Python output.
- **Language:** English.
- **Tools:** Python with Pandas, NumPy, SciPy, Matplotlib, and, where relevant, statsmodels or scikit-learn.

## What is assessed

- Is the statistical method appropriate for the question?
- Are assumptions stated and, where possible, checked?
- Is Python used as a means of analysis, not as a black box?
- Does the conclusion answer the engineering question and mention uncertainty?

## Group project

At the end of the course you complete a **small group project**. You analyse a more comprehensive engineering data set, apply relevant statistical methods, and present the findings. The project is part of the oral exam together with one of the six assignments.

The project is the course's synthesis: a full data-analysis workflow from raw measurements to a decision. You should be able to formulate an engineering question, import and preprocess data, select methods from across the course, implement the analysis in Python, and communicate results, assumptions, limitations, and uncertainty.

The project is introduced in [Session 10](../10_Simple_Linear_Regression/README.md) and submitted after [Session 12](../12_Integrated_Analysis_and_Exam_Preparation/README.md). Session 12 is organised around a complete worked analysis in the same spirit as the project.

Unless the brief says otherwise:

- **Group size:** the same groups as for the assignments.
- **Product:** a short report supported by a Jupyter notebook, or a well-written notebook that can stand as the report.
- **Scope:** one coherent engineering data set, not six disconnected analyses.
- **Language:** English.

The six assignments train individual methods. The project asks you to choose among them and use them in one coherent analysis.
