---
tags:
    - Estimation
    - Confidence Intervals
    - t-interval
    - Bootstrap
---

<h1 align="center">Estimation and Confidence Intervals</h1>

An estimate is a number; an interval says how precise that number is. After the CLT we can attach a margin of error to a mean or a proportion and talk about coverage rather than a single lucky sample.

We distinguish an estimator from an estimate, construct a \(t\)-interval for a mean when \(\sigma\) is unknown, mention a \(z\)-interval only when population \(\sigma\) is known, and use a **Wilson** interval as the practical default for a proportion. The Wald interval is shown only to explain why it can fail. A bootstrap interval is a computational check. A 95% interval is a statement about the procedure, not a claim that “the parameter now lies in this interval with probability 0.95”. Width depends on \(n\) and on the confidence level.

#### Key Concepts

- Estimator versus estimate, and bias at an intuitive level
- \(z\)-interval (known \(\sigma\)) and \(t\)-interval (unknown \(\sigma\)) for a mean
- Wilson interval for a proportion (practical default; Wald as a contrast)
- Coverage and correct interpretation
- How width depends on \(n\) and confidence level

!!! tip "Learning Objectives"

    - Distinguish an estimator from an estimate, and discuss bias at an intuitive level.
    - Construct a \(t\)-interval for a mean, and a \(z\)-interval only when \(\sigma\) is known.
    - Construct a Wilson interval for a proportion.
    - Interpret a 95% interval without claiming that the parameter lies in this interval with probability 0.95 after the data are seen.
    - See how interval width depends on \(n\) and on the confidence level.

<hr/>

### Session Preparation:

Brooks: [Chapter 6](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/RBrooksDK/STA_book_v1/main/main.pdf)

### Resources

[Session material](https://github.com/RBrooksDK/STA1_26/tree/main/06_Estimation_and_Confidence_Intervals/session_material)

[Tutorial 6: How precise is this measurement?](Tutorial_06_notebook.ipynb)
