# STA1: Course, Website, and Textbook Project Plan

## Purpose and decision record

This is the internal implementation plan for **Statistics and Data Analysis
for Engineers (STA1)**.  STA1 is a practical, Python-oriented statistics
course.  It is distinct from SMP1: STA1 uses probability as a tool for
analysing observed data and supporting engineering decisions, whereas SMP1
carries the deeper probability theory, joint distributions, stochastic
processes, and simulation modelling.

The project will produce one coherent set of materials:

- the STA1 course website;
- a course-specific textbook, *Statistics and Data Analysis for Engineers*;
- twelve Python tutorials and their notebooks;
- six group assignments and one integrated group project; and
- stable links between all of the above.

The approved delivery principle is:

> Freeze the course structure first; then develop textbook chapters and the
> corresponding student-facing session material together.

The primary coordination document is `source_map.md`.  This plan and the
chapter/session contract define the decisions which the source map must
support.  Neither Ross nor any other external source is copied into the new
book; they provide mathematical checking, topic selection, and bibliographic
reference only.

The course begins on **1 September 2026**.  Student-facing structural work,
session links, and the first teaching wave therefore take priority over
nice-to-have refinement.  The site must remain usable throughout production;
unpublished work should stay in internal planning files or clearly non-public
book branches/directories until it is reviewed.

## Fixed course contract

The following are fixed unless the course responsible explicitly changes them.

- 12 taught sessions of 90 minutes, preceded by optional Session 00 for Python
  and data setup.
- 5 ECTS / approximately 135 student working hours.
- One textbook chapter for every taught session (Chapters 1--12).
- Session 00 maps to a Python appendix, not a numbered statistics chapter.
- The course uses Python throughout: NumPy, Pandas, Matplotlib, SciPy,
  statsmodels, and selectively scikit-learn.
- Six practice-oriented group assignments are released after Sessions 1, 3,
  5, 7, 9, and 11.  A small integrated group project follows Session 12.
- The twelve current `Exercises.md` pages are intentional placeholders for the
  six assignments and project workflow.  They are not missing conventional
  exercise sets and must not be filled with generic practice merely to make a
  page look complete.
- The oral exam is based on one assignment and the group project, in accordance
  with the official course description.
- `planning/STYLE_AND_NOTATION.md` is the canonical internal convention;
  `pages/conventions.md` is its student-facing counterpart.  The textbook and
  public page must remain aligned with the internal convention.

## Scope boundaries

Core STA1 topics are descriptive statistics; practical probability; selected
discrete and continuous distributions; sampling distributions; confidence
intervals; one- and two-sample inference; one-way ANOVA; simple linear
regression; and chi-square methods.

The following remain outside core STA1 unless explicitly introduced as a
short, labelled extension: general combinatorics, manual integration and
derivation of densities, multivariate/joint distributions, covariance theory
beyond what correlation needs, maximum likelihood, Bayesian inference,
multiple/polynomial/logistic regression, two-way ANOVA, time series, Markov
chains, and Monte Carlo modelling.  These boundaries prevent duplication with
SMP1 and keep the workload realistic.

## Implementation rules

- Planning files are internal.  Do not expose planning language, implementation
  placeholders, or AI/meta commentary on public student pages.
- A chapter and its session page are developed as a pair, but the textbook is
  the canonical explanation of theory.  The website should orient students,
  link material, and host concise teaching support rather than duplicate an
  entire chapter.
- Every mathematical claim, formula, notation choice, and code result is
  checked before publication.
- Use original prose, original examples, and appropriately licensed/open data.
  Record borrowed factual sources and data provenance.
- Do not change official assessment conditions, learning objectives, or course
  description wording without the course responsible's approval.
- Commit only cohesive, verified milestones.  Do not mix unrelated site,
  textbook, or generated-file changes in the same commit.

## Model-routing policy

Use the least expensive capable model and escalate when an error would
propagate into course content.  This policy applies to delegated work; the
main reviewer retains responsibility for every student-facing change.

| Work type | Preferred model / effort | Escalation rule |
| --- | --- | --- |
| Deterministic inventories, link checks, file/format scans, repetitive notebook regeneration, build/deployment monitoring | Luna, low or medium reasoning | Escalate to Terra if results require interpretation or a repair. |
| MkDocs/Markdown/Python implementation, ordinary textbook drafting, copy-editing, and structured consistency work | Terra, medium or high reasoning | Escalate to Sol if statistical judgement, architecture, or uncertain source reconciliation is required. |
| Curriculum architecture, statistical/mathematical correctness, notation decisions, licensing-sensitive judgement, and final chapter/cross-material review | Sol, high to xhigh reasoning | Sol review is required before material is treated as final. |

No parallel agents edit the same file.  In particular, generated files,
notebooks, book source, and public pages receive separate clean commit
checkpoints after their relevant build/verification steps.

## Six-phase delivery plan

| Phase | Objective | Dependencies | Concrete deliverables | Exit / acceptance criteria |
| --- | --- | --- | --- | --- |
| 1. Planning and contracts | Establish a single, approved curriculum contract. | Existing STA1 scaffold, MSE book, source material inventory. | Restored `source_map.md`; this plan; `CHAPTER_SESSION_CONTRACT.md`; notation and Python decisions; a source/provenance register. | All 12 topics, reading sources, assignment links, scope boundaries, and chapter/session titles are agreed; no unresolved contradiction with the official course description or SMP1 boundary. |
| 2. Website foundation | Make the existing site a clear, trustworthy course home before content expansion. | Phase 1 contract. | Revised front page, navigation, session-page template, literature/conventions/assessment pages, link and responsive-layout fixes. | No internal/meta language remains; public claims are accurate; navigation works on desktop and mobile; build is strict and links resolve.  Assignment/project pages remain frameworks until briefs are approved. |
| 3. Textbook foundation | Create a reproducible new-book project based on the approved MSE template. | Phase 1; completed MSE book revision. | New repository or clearly named book directory; copied/adapted template and licence decisions; master file; bibliography; chapter stubs; PDF build workflow; visual QA checklist. | A clean checkout builds a PDF; all chapter stubs compile; definitions, results, examples, remarks, Python sections, references, and cross-references render in the established house style. |
| 4. Content production in waves | Produce aligned, reviewed teaching content without drift. | Phases 1--3; chapter-specific source map entries. | Four waves: A (1--3), B (4--6), C (7--9), D (10--12).  For each chapter: book chapter, Python section, tutorial/notebook, web session update, and source record. | Each completed chapter meets the chapter contract; its notebook executes from a clean environment; corresponding web page has correct reading, links, data, and assignment/project connection. |
| 5. Assessment design | Turn deliberate placeholders into six authentic assignments and an integrated project. | Relevant content waves; confirmed exam framework. | Six briefs, datasets, marking/feedback guidance, group-work rules, project brief, submission schedule, and exam preparation alignment. | Every task has a realistic workload, an unambiguous deliverable, suitable data, method prerequisites already taught, and a clear connection to the oral exam.  No task accidentally becomes an unannounced extra project. |
| 6. Quality assurance and publication | Release a consistent, correct, usable course package. | All prior phases. | Mathematical/statistical audit, notebook execution report, PDF visual review, website/link/responsive audit, cross-material matrix, release notes. | Book PDF builds and is visually checked; MkDocs strict build passes; every public link works; all 12 session/chapter mappings, notation, datasets, assignments, and exam statements agree.  Changes are committed, pushed, and deployed. |

## Detailed sequence and gates

### Gate A — curriculum freeze

1. Restore and complete `source_map.md` from the existing material inventory.
2. Verify the twelve chapter/session titles against the live STA1 scaffold.
3. Reconcile common notation with the corrected MSE book and all existing
  tutorials.
4. Confirm each assignment pair and the project timing.
5. Approve the contract before substantive public rewriting or book creation.

**Gate A acceptance:** every chapter has a defined purpose, scope, exclusions,
source basis, Python outcome, dataset candidate, and assessment connection.

### Gate B — website freeze

1. Simplify visual and navigation issues without changing the curriculum.
2. Remove internal wording and stale warnings from public pages.
3. Make session page sections consistent: preparation, focus/outcomes,
material/tutorial, scope boundary where useful, and assessment link.
4. Check all published notebook and material links.

**Gate B acceptance:** the site can be used by students throughout the
semester even while assignments and the textbook are still being completed.

### Gate C — textbook foundation

1. Reuse the MSE book template and its proven build process, not its prose.
2. Create a chapter skeleton that implements the fields in the contract.
3. Establish citation, dataset, code, figure, and generated-PDF rules.
4. Build a minimal PDF and render representative pages for visual inspection.

**Gate C acceptance:** a contributor can draft one chapter without guessing
the structure, notation, or build commands.

### Gates D1--D4 — content waves

The four waves are sequenced because later inference depends on earlier
probability and sampling language:

| Gate | Chapters / sessions | Must be complete before advancing |
| --- | --- | --- |
| D1 | 1--3: descriptive data, probability, discrete distributions | Assignment 1 and 2 prerequisites, foundational notation, basic Python data workflow. |
| D2 | 4--6: continuous models, CLT, confidence intervals | Correct distinction between data distribution and sampling distribution; interval language and code. |
| D3 | 7--9: one-sample tests, two-group tests, ANOVA | Coherent inferential vocabulary, assumptions, effect-size/reporting guidance, Assignment 4 and 5 prerequisites. |
| D4 | 10--12: regression, categorical data, integrated analysis | Assignment 6, project support, method-choice guidance, and oral-exam synthesis. |

For each gate, first draft the chapters, then run technical review, then update
the paired website sessions/tutorials and test the notebooks.  Do not publish a
partial tutorial whose method disagrees with the book.

### Gate E — assessment release

Assignments may be prepared during their content wave, but are released only
after their methods and student-facing guidance have passed review.  The group
project is finalised after its data and expected use of methods are tested
against the completed course.

### Gate F — release

Run the complete QA checklist, then commit, push, and verify deployed GitHub
Pages and the published `main.pdf` (or equivalent textbook PDF) before calling
the package complete.

## Chapter-level workflow

For every numbered chapter, use this sequence:

1. Confirm the contract entry and source-map rows.
2. Select one central engineering question and data example.
3. Draft conceptual explanation, definitions/results where helpful, worked
   examples, and a concise Python section.
4. Perform a statistical/mathematical review and a notation review.
5. Build the chapter PDF and visually inspect formulas, code, figures,
   cross-references, and page breaks.
6. Update the corresponding website session: preparation, direct links,
   tutorial, data, and assignment/project connection.
7. Execute the tutorial notebook in a clean environment; verify that output,
   filenames, seed behaviour, and conclusions agree with the chapter.
8. Record completion and any remaining limitations in the source map.

## Definition of done

A topic is complete only when all applicable conditions below are true:

- The book chapter, session page, tutorial, and notebook use the same
  terminology and notation.
- Learning outcomes are observable and within the stated 90-minute session
  plus independent work.
- One original engineering context ties together concept, data, code, and
  interpretation.
- Assumptions and limitations are stated honestly; statistical significance is
  never presented as automatic practical importance.
- Code uses the course conventions, executes without hidden local paths, and
  has readable plots with labelled units.
- References, datasets, and figures have recorded provenance.
- Student-facing prose is concise, welcoming, and free from internal planning
  or generated-content language.
- Builds, links, and visual checks have passed at the relevant release gate.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| The book duplicates the website and later diverges. | Treat the book as canonical explanation and use the chapter/session contract at every review. |
| The practical course becomes too theoretical. | Enforce chapter scope/exclusions and the 90-minute session budget; move deeper probability to SMP1. |
| Tutorials become black-box library demonstrations. | Require method choice, assumptions, diagnostic plots, and plain-language conclusions in every notebook. |
| Assessment workload exceeds 5 ECTS. | Test each assignment/project against the 135-hour workload table before release. |
| Borrowed material creates licensing or originality problems. | Use sources for checking and citation; write original exposition, examples, figures, and tasks. |
| Unreviewed notebook or PDF changes break published material. | Require clean execution and strict builds before each cohesive commit. |
