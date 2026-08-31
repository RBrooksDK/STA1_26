<h1 align="center">Group Project — Integrated Statistical Analysis</h1>

The group project is a free, coherent investigation of an engineering question chosen by your group. You select the topic and dataset, formulate a decision or objective, and use statistical methods from the course to build one connected argument from data to recommendation.

The project is not three unrelated tests collected in one notebook. Every analysis must answer a stated subquestion and contribute to the same engineering objective.

!!! info "Practical information"
    - **Group size:** 2–4 students
    - **Workload:** approximately 25 hours per student
    - **Deadline:** 31 December 2026
    - **Submission:** one fully executed Jupyter notebook in English
    - **Statistical scope:** at least three methods from three different Sessions/Chapters 1–11
    - **Course guidance:** Brooks, Chapter 12 and Tutorial 12

## Purpose

The project demonstrates that you can independently:

1. translate an engineering objective into answerable statistical questions;
2. identify the target population, observational unit, variables, and study design;
3. audit and describe a dataset before applying inferential methods;
4. choose methods because they answer the questions—not because they produce desirable results;
5. implement and verify the analysis in Python;
6. interpret magnitude, uncertainty, assumptions, and practical importance; and
7. combine the results into a justified recommendation with specific limitations.

## Topic and dataset

Your group chooses its own engineering topic and dataset. The subject may come from software, cybersecurity, climate, supply chain, mechanical, production, building, or another relevant engineering field.

The data may be openly available, collected by your group, produced by an experiment or benchmark, or supplied by an organisation that has authorised its use. Do not submit confidential, personally identifiable, or otherwise restricted information.

Before analysing the data, state:

- the engineering objective and intended decision;
- the target population or operating conditions;
- the observational unit;
- how the observations were sampled, assigned, paired, grouped, or measured;
- the source and provenance of the dataset;
- the variables, units, coding, and relevant practical thresholds; and
- what the design can support: description, association, generalisation, or causation.

Choose a dataset with enough relevant observations and variables to support one coherent investigation and the required three methods. A large or complicated dataset is not automatically a better project; a well-scoped dataset that can be understood and defended is preferable.

## Statistical requirements

The project must include at least **three statistical methods from three different course sessions or textbook chapters**, excluding Session/Chapter 12. Each method must answer a stated question and add evidence to the same overall decision.

Examples of eligible method families include:

- probability or probability-distribution modelling;
- sampling distributions, confidence intervals, or bootstrap estimation;
- one-sample or two-sample tests for means or proportions;
- paired comparisons;
- one-way ANOVA and compatible post-hoc comparisons;
- simple linear regression; and
- goodness-of-fit or contingency-table analysis.

Descriptive summaries and plots are required in every project. Several summaries or plots of the same data do not automatically constitute several separate methods. Do not add a method merely to reach the minimum count; justify what question it answers.

The primary methods should come from Sessions 1–11. If your project appears to require a statistical method not covered by the course, discuss it with R. Brooks before Session 12 rather than introducing an unfamiliar method without guidance.

!!! tip "Plan before calculating"
    Before examining final inferential output, record:

    1. the primary engineering objective;
    2. the statistical subquestion answered by each method;
    3. the parameter, response, groups, or variables involved;
    4. the comparison direction and practical threshold, where relevant;
    5. the assumptions and diagnostics that will be examined; and
    6. which analyses are planned and which are later exploratory additions.

## Required workflow

The notebook must follow the integrated workflow in Brooks, Chapter 12 and [Tutorial 12](../12_Integrated_Analysis_and_Exam_Preparation/Tutorial_12_notebook.ipynb).

### 1. Engineering objective and questions

State one overall objective or decision and formulate the statistical subquestions. Explain how answering the subquestions contributes to the objective.

### 2. Data audit and preparation

Document the dataset's source, dimensions, identifiers, data types, units, category coding, missing values, duplicates, ranges, and unusual observations. Explain every exclusion, transformation, or derived variable. Do not delete an observation solely because it is inconvenient or changes a result.

### 3. Descriptive evidence

Use appropriate summaries and plots before inference. Tables and figures must have meaningful labels, units, and short interpretations. Describe what the sample shows without treating descriptive differences as established population effects.

### 4. Statistical analyses

For each of the three or more methods:

1. state the subquestion and population parameter or model quantity;
2. justify the method from the variables and study design;
3. state the hypotheses or model, where relevant;
4. examine assumptions and explain which cannot be checked from the data alone;
5. report the relevant estimate, uncertainty, statistic, degrees of freedom, \(p\)-value, effect magnitude, or prediction—not merely a software dump; and
6. write a contextual conclusion that distinguishes statistical evidence from practical importance.

### 5. Integrated conclusion and recommendation

Bring the analyses together. The final recommendation must use evidence from the complete project rather than list three disconnected conclusions. State conflicts or trade-offs honestly—for example, when one alternative performs better on one response but worse on another.

Explain what the evidence supports, what remains uncertain, and what should happen next. Keep generalisation and causal language within the limits of the study design.

### 6. Limitations

State specific limitations and their likely consequences. Examples include unrepresentative sampling, dependence, confounding, measurement limitations, missing operating conditions, small samples, sparse categories, model departures, or imprecise effects. “More data are needed” is not sufficient unless you explain what evidence is missing and why it matters.

## Notebook and reproducibility requirements

The notebook is the project report. No separate written report is required.

- Write objectives, reasoning, assumptions, interpretations, conclusions, AI use, and references in **Markdown cells**.
- Place Python only in **code cells**.
- Execute every code cell before submission so that all output, tables, and figures are visible.
- Arrange cells in a logical order and ensure the notebook runs from beginning to end without errors.
- Use relative paths or reproducible download code rather than paths tied to one group member's computer.
- Include the dataset with the submission when it cannot be retrieved reproducibly from a documented public source.
- Use fixed random seeds for simulations, resampling, or other random procedures.
- Cite the dataset and any external technical sources.
- Use sensible numerical precision and avoid unedited software output that does not contribute to the argument.

Begin the notebook with the project title and the names of all group members. Include a short table of contents and a concise description of each member's contribution.

## Use of AI

AI use is encouraged, but it must be transparent and critically evaluated. AI may help with topic development, code, debugging, method selection, interpretation, visualisation, or writing. It may contribute substantially, but every group member remains responsible for the submitted work.

Include an **AI-use** section stating:

1. which AI tool or tools were used;
2. what they were used for;
3. what AI suggestions were changed, rejected, or corrected; and
4. how the group checked the final code, calculations, and interpretations.

Complete chat transcripts are not required. If AI produced most of the code or text, say so honestly. If no AI was used, state that explicitly. Regardless of how the notebook was produced, every group member must understand the analysis and be able to defend it at the exam.

## Relation to the oral exam

The project is discussed during the oral examination together with one of the six assignments. It is **not graded separately**, but it contributes to the overall course grade through the examination. The same principle applies to the six assignments.

At the exam, you should be able to explain:

- why the topic and dataset are suitable;
- how the design affects the conclusions;
- why each statistical method was chosen;
- what the Python analysis does, without reproducing syntax from memory;
- how assumptions and diagnostics were handled;
- how estimates, intervals, tests, or predictions should be interpreted;
- how AI contributed and how its output was verified; and
- how the separate results support the final recommendation.

## Submission checklist

- [ ] The group contains 2–4 students, or a deviation was agreed before Session 12.
- [ ] The workload and scope are appropriate for approximately 25 hours per student.
- [ ] The notebook states one coherent engineering objective and related subquestions.
- [ ] The dataset's source, population, observational unit, variables, units, and design are documented.
- [ ] Data auditing and preprocessing decisions are reproducible.
- [ ] Descriptive summaries and plots precede inferential analysis.
- [ ] At least three justified statistical methods come from three different Sessions/Chapters 1–11.
- [ ] Each method includes assumptions, relevant diagnostics, results, and contextual interpretation.
- [ ] The conclusion integrates all analyses into a recommendation and states specific limitations.
- [ ] The AI-use section is complete and honest.
- [ ] External data and sources are cited.
- [ ] Every code cell has been executed and all output is visible.
- [ ] The notebook runs from beginning to end without errors.

The [project-planning table and worked example in Tutorial 12](../12_Integrated_Analysis_and_Exam_Preparation/Tutorial_12_notebook.ipynb) can be used to check readiness, but they do not dictate your topic or methods.
