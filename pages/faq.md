<h1 align="center">FAQ</h1>

### General information

??? question "How does STA1 relate to SMP1?"

    STA1 is the practical statistics course. SMP1 is the more mathematical course on probability models and stochastic processes. About 25–30% of the language overlaps (events, random variables, standard distributions). The purpose differs: STA1 analyses observed data; SMP1 models dependence and processes. Time series belong to SMP1.

??? question "Do I need MSE1 before STA1?"

    The [official course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0) lists MSE1 as a prerequisite. This edition of STA1 nevertheless teaches descriptive statistics and the probability needed for inference from the beginning. If you have had MSE1, treat Sessions 01–02 as a fast recap.

??? question "How many contact hours are there?"

    Twelve sessions of \(2 \times 45\) minutes, so 18 hours in class. The remaining workload is tutorials, six assignments, the project, and exam preparation. See the workload table on the home page.

??? question "Are there mandatory exercises besides the assignments?"

    The six assignments and the group project are the course assessment activities. The assessment link on each session page is reserved for the relevant brief and supporting material; tutorials provide the regular practice.

??? question "Which programming language do we use?"

    Python. The core libraries are NumPy, Pandas, SciPy, and Matplotlib. Statsmodels is used for inference. Scikit-learn appears in Session 10 for fitting a simple prediction model, not as a replacement for statistical tests.

??? question "Where are the data files?"

    In the `data/` folder of the repository. They are catalogued on the [Datasets](datasets.md) page. From a session notebook, load them with a path such as `Path("../data/sensor_thickness.csv")`.

---

### Who to contact?

??? question "Who is the course responsible?"

    Richard Brooks, [rib@via.dk](mailto:rib@via.dk).

??? question "Where do I find slides and extra files?"

    Session pages link to notes when they exist. Additional course materials are published on itslearning when needed.

---

### Exam and assessment

??? question "What is the exam format?"

    A 20-minute oral exam based on one of the six assignments, plus a discussion of the group project. See the [Exam](exam.md) page.

??? question "Are the assignments graded separately?"

    The final grade is an overall assessment of the assignment work and the oral examination, as stated in the [course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0).

??? question "May I use AI tools?"

    During the oral exam, no tools are allowed. For coursework, follow the programme rules announced on itslearning. You must be able to explain every figure and number in your assignment.

---

## Resources

??? question "Which book should I buy?"

    Ross, *Introduction to Probability and Statistics for Engineers and Scientists*, 6th edition, is the main book from Session 03. Sessions 01–02 use Brooks, *Mathematics for Software Engineering*. Details are on the [Literature](literature.md) page.

??? question "Why do tutorials sometimes disagree with SciPy's default arguments?"

    SciPy's normal distribution uses `scale=sigma` (standard deviation), the exponential uses `scale=1/rate`, and NumPy's `var` divides by \(n\) unless `ddof=1`. The course conventions are collected on the [Conventions](conventions.md) page.
