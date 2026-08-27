<h1 align="center">FAQ</h1>

### General information

??? question "How does STA1 relate to SMP1?"

    STA1 is the practical statistics course. SMP1 is the more mathematical course on probability models and stochastic processes. About 25–30% of the language overlaps (events, random variables, standard distributions). The purpose differs: STA1 analyses observed data; SMP1 models dependence and processes. Time series belong to SMP1.

??? question "Do I need MSE1 before STA1?"

    The [official course description](https://my.via.dk/media/mitvia/semesteroverblik/kursusbeskrivelser/software-engineering/6.-og-7.-semester/it-sta1-1-0) lists MSE1 as a prerequisite. This edition of STA1 nevertheless teaches descriptive statistics and the probability needed for inference from the beginning. If you have had MSE1, treat Sessions 01–02 as a fast recap.

??? question "How many contact hours are there?"

    Twelve sessions of \(2 \times 45\) minutes, so 18 hours in class. The remaining workload is tutorials, six assignments, the project, and exam preparation. See the workload table on the home page.

??? question "Are there mandatory exercises besides the assignments?"

    The six assignments and the group project are the course assessment activities. Tutorials provide the regular practice. Exercises will be added to the session pages later.

??? question "Which programming language do we use?"

    Python. The core libraries are NumPy, Pandas, SciPy, and Matplotlib. Statsmodels is used for inference. Scikit-learn appears in Session 10 for fitting a simple prediction model, not as a replacement for statistical tests.

??? question "How do I install Python and Jupyter?"

    Follow [Session 00](../00_Getting_Started_with_Python_and_Data/README.md): install Python from [python.org](https://www.python.org/downloads/), then Visual Studio Code, then the Python and Jupyter extensions. There are separate steps for Windows and macOS.

??? question "Where are the data files?"

    Download the [data folder](https://download-directory.github.io/?url=https://github.com/RBrooksDK/STA1_26/tree/main/data) (no Git required) and follow [Session 00](../00_Getting_Started_with_Python_and_Data/README.md). The files are catalogued on the [Datasets](datasets.md) page. The folder is updated during the semester; if a file is missing, download it again. From a notebook next to `data/`, use `Path("data/sensor_thickness.csv")`.

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

    No purchase is required. The course textbook, Brooks, [*Statistics and Data Analysis for Engineers*](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf), is provided online and follows the twelve sessions chapter by chapter. Because it is updated throughout the course, use the online version whenever possible. Each session page links to the matching chapter.

??? question "Why do tutorials sometimes disagree with SciPy's default arguments?"

    SciPy's normal distribution uses `scale=sigma` (standard deviation), the exponential uses `scale=1/rate`, and NumPy's `var` divides by \(n\) unless `ddof=1`. Session 00 summarises the Python hygiene used throughout the course.
