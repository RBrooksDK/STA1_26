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
* **Sessions:** 12 lectures of \(2 \times 45\) minutes, plus independent work on tutorials, assignments, and the project
* **Level:** Bachelor — practical statistics for software and engineering students
* **Assessment:** 20-minute oral exam based on one of the six assignments and a discussion of the group project
* **Recommended prerequisites:** Mathematics at the programme admission level. The course itself introduces descriptive statistics and the probability needed for inference.

## <i class="fas fa-vector-square" style="color:#6CA2C6"></i> Lectures and Course Organization

STA1 is a **practical data-analysis course**. The work is organised in three layers:

1. **The textbook** delivers the theory: definitions, assumptions, notation, and the statistical arguments.
2. **The tutorials** translate that theory into practice in Python: computation, visualisation, and interpretation of a worked engineering example.
3. **The assignments** are where you use the methods independently. They replace in-class exercises, and they are the exam assignments.

**Lectures** present theory, examples, and discussion. There are no separate exercise sheets in class. After the lecture you work independently on the current assignment and, later, the group project.

Each session has a matching textbook chapter and a Python tutorial. Read the chapter, work through the tutorial, then apply the same ideas in the assignment.

## <i class="fas fa-clipboard-list" style="color:#6CA2C6"></i> Assignments and Project

The course contains **six practice-oriented group assignments** and one **small group project**. These are the official learning activities from the [course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0). They are also the basis of the exam.

| Activity | After session | Focus |
| ---: | ---: | --- |
| [Assignment 1](assignments/assignment_01_data_and_probability_foundations.md) | 02 | Data, descriptive analysis, and probability foundations |
| [Assignment 2](assignments/assignment_02_discrete_and_continuous_models.md) | 04 | Discrete and continuous probability models |
| [Assignment 3](assignments/assignment_03_sampling_and_estimation.md) | 06 | Sampling distributions and estimation |
| [Assignment 4](assignments/assignment_04_one_and_two_sample_tests.md) | 08 | One- and two-sample hypothesis testing |
| [Assignment 5](assignments/assignment_05_anova_and_regression.md) | 10 | ANOVA and simple linear regression |
| [Assignment 6](assignments/assignment_06_categorical_data.md) | 11 | Categorical data and chi-square analysis |
| [Project](pages/project.md) | 12 | A complete analysis of an engineering data set |

See the [Assignments](pages/assignments.md) overview and the dedicated [Group Project brief](pages/project.md).

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

Python is used throughout with Pandas, NumPy, SciPy, Matplotlib, and statsmodels.

## <i class="fas fa-robot" style="color:#6CA2C6"></i> Using AI in this course {: #using-ai-in-this-course }

> *The better we are without AI, the stronger we become with it.*

AI is not something you need to hide in this course. Quite the opposite: you are strongly encouraged to use it. Tools such as ChatGPT, Copilot, Claude, and Gemini are becoming part of how engineers work.

But there is a difference between **using AI to learn** and **using AI instead of learning**.

Use AI when you are stuck. Ask it to explain a concept differently. Let it give you another example. Ask why your solution does not work. Discuss different approaches with it. Use it to check an answer you have already worked out, validate an assignment, or challenge your reasoning.

In other words: make AI your tutor, sparring partner and rubber duck — not your substitute.

You are also welcome to use AI to help write all the Python code in the course. In practice, this is increasingly how software is developed. The important part is that you understand exactly what the code does — in detail. You should be able to explain the individual steps, the functions being used, the inputs and outputs, and why the code produces the result it does. AI may write the code; you are still responsible for understanding it.

A useful rule of thumb is: Think first. Ask AI second. Think again afterwards.

The stronger your own understanding becomes, the better you become at asking questions, evaluating answers, spotting mistakes and using AI intelligently.

The better we are without AI, the stronger we become with it.

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

The course uses the purpose-built textbook
[*Statistics and Data Analysis for Engineers*](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf).
Its twelve chapters follow the twelve course sessions in the same order.

The textbook is a work in progress and may be updated throughout the course as explanations and worked examples are refined. Please use the online version whenever possible. A downloaded copy will not update automatically; if you keep one locally, remember to replace it regularly with the newest version.

Each session page states the matching textbook chapter. Data files live in `data/` and are catalogued under [Datasets](pages/datasets.md).

Install Python from python.org, then Visual Studio Code, then the Jupyter extension. The step-by-step guide — Windows and macOS — is [Session 00](00_Getting_Started_with_Python_and_Data/README.md).
