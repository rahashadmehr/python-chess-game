# MSR 2027 Mining Challenge

**A Research Challenge on AI Agent Skills and Specification-Driven Software Development**

## 1. What Is the MSR Mining Challenge?

MSR stands for **Mining Software Repositories**. It is a research area that studies software development using data from repositories, such as GitHub projects, source code, commit histories, and documentation.

The MSR 2027 Mining Challenge invites researchers to investigate two emerging areas of software engineering:

* **GitSkills:** Understanding how AI agent skills are created, reused, maintained, and distributed.
* **SpecMine:** Understanding how software specifications are written, maintained, and connected to software implementation.

Researchers can focus on either dataset or combine both in a single study.

Official website: https://2027.msrconf.org/track/msr-2027-mining-challenge

## 2. Dataset One: GitSkills

GitSkills focuses on `SKILL.md` files used to provide AI agents with instructions for performing specific tasks. A skill may also include scripts, reference documents, and other supporting resources.

According to the challenge description, the dataset contains:

| Metric                          |     Count |
| ------------------------------- | --------: |
| Observed `SKILL.md` occurrences | 3,797,117 |
| Distinct skill contents         | 1,877,981 |
| GitHub repositories             |   282,200 |
| Repository owners               |   195,841 |
| Supporting files                | 7,264,865 |
| Sampled commit histories        |   458,548 |

The data was collected in July 2026.

### Potential Research Questions

* How do AI agent skills spread across GitHub repositories?
* Which skills are copied or reused most frequently?
* How do skills evolve over time?
* What factors are associated with skill quality and maintainability?
* Can duplicated or modified skills introduce security risks?

## 3. Dataset Two: SpecMine

SpecMine focuses on **Specification-Driven Development (SDD)**, an approach in which software development is guided by written requirements and specifications.

For example, before developing a chess application, a developer might document its features, rules, expected behavior, and requirements. An AI agent can then use these specifications to help implement the software.

According to the challenge description, SpecMine includes:

| Metric                                                   |     Count |
| -------------------------------------------------------- | --------: |
| `spec.md` and `specs.md` files                           |   470,795 |
| Related repositories                                     |    73,030 |
| Named SDD tools in the main dataset                      |        17 |
| SDD tool families examined                               |        18 |
| Additional Kiro requirements, design, and task documents |    98,574 |
| Complete commit histories                                |   780,335 |
| Extracted specification features                         |        39 |
| Selected pull requests                                   |     5,992 |
| Typed specification-to-code references                   | 2,421,323 |

These figures describe different components of the dataset and should not be treated as mutually exclusive groups.

### Potential Research Questions

* How is Specification-Driven Development adopted across GitHub projects?
* What characteristics distinguish clear, complete specifications from ambiguous ones?
* How closely do software implementations follow their specifications?
* How do specifications and source code evolve together?
* Can specification quality be associated with implementation effort or subsequent changes?

## 4. How to Participate

A typical research workflow involves six steps:

1. **Choose a dataset:** Select GitSkills, SpecMine, or both.
2. **Explore the data:** Read the documentation and inspect sample files.
3. **Define a research question:** Identify a specific, answerable question.
4. **Analyze the data:** Use programming and data-analysis tools to investigate it.
5. **Interpret the findings:** Explain the results, their significance, and their limitations.
6. **Write and submit a research paper:** Present your methods and findings according to the official requirements.

You do not need to analyze the entire dataset. A focused research question and a well-designed analysis can be more valuable than an overly broad project.

## 5. Tools and Resources

The challenge description provides links to datasets, research papers, and repositories.

* **GitHub:** Version control, collaboration, and project hosting.
* **Python:** Data cleaning, processing, and analysis.
* **SQL:** Querying structured datasets.
* **Jupyter Notebook:** Running and documenting analyses.
* **Markdown:** Writing project documentation and `README.md` files.
* **LaTeX:** Preparing a research paper using the IEEE conference template.

The complete GitSkills SQLite database is approximately 44 GB, so beginners should start with sample data rather than downloading the entire dataset.

## 6. Paper Requirements

Submissions must follow the official IEEE conference format.

Key requirements include:

* Maximum length: **4 pages of main text plus 1 page of references**.
* Anonymous submission for double-blind review.
* A clear research question, dataset description, methodology, results, implications, and conclusion.
* A separate section discussing ethical considerations.
* Documentation of the exact dataset version used.

The challenge also encourages open and reproducible research. Publishing analysis code and supporting data makes it easier for other researchers to verify and reproduce the findings.

## 7. Important Dates

According to the official challenge page:

| Milestone                  | Deadline          |
| -------------------------- | ----------------- |
| Abstract submission        | December 18, 2026 |
| Paper submission           | December 23, 2026 |
| Notification of acceptance | January 19, 2027  |
| Camera-ready paper         | January 26, 2027  |
| MSR 2027 conference        | April 26–27, 2027 |

All deadlines use the **Anywhere on Earth (AoE)** time zone.

Submissions are handled through the conference's official submission system.

## 8. Awards and Opportunities

The challenge offers:

* A **Best Mining Challenge Paper Award**.
* A **Best Student Presentation Award**, intended to recognize an effective and engaging student presentation.

Participation can help you develop experience in empirical software engineering, data analysis, research methodology, and scientific writing. However, acceptance or publication is not guaranteed.

## 9. Recommended Starting Point

If you are new to research, start small:

1. Learn the basics of Git and GitHub.
2. Understand Markdown and project documentation.
3. Select a small sample from GitSkills.
4. Use Python to explore and analyze the data.
5. Formulate a specific research question.
6. Document your methods and findings.
7. Learn how to structure a scientific paper.

**My recommendation:** Start with GitSkills and a small, manageable research question. Your first goal should be to complete a simple analysis from beginning to end. Once you understand the dataset and can produce meaningful results, you can develop the analysis into a research paper.

**The most important principle is to begin with a clear question, not with the goal of writing a paper immediately.**
