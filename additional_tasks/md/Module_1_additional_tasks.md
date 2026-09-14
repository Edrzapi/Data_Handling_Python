# ADDITIONAL TASKS - Module 1: Introduction to Programming for Data Handling

For students who are progressing well / have finished the standard exercises early. These go
beyond the core material - attempt after the standard Module 1 material is complete.

Module 1 has no coding exercises, so these are discussion and research extensions. They are
best done as a short written answer or a two-minute verbal summary, not code.

---

## 1.1 Classify your own data estate (Stretch)

*Extends Module 1 - data structure types and tool families.*

List five real data sources from your own organisation (or a previous role) and classify each
as structured, semi-structured, or unstructured, justifying each choice. Then, for each source,
name the most suitable tool family from the five on the tools slide (programming language,
database, command line, spreadsheet, BI tool) and give one sentence on why.

**Checkable:** five sources, a defensible classification for each, and a tool choice that
matches the classification (for example, unstructured sources should not be assigned to
spreadsheets).

**Guidance for self-marking:**

- Watch for correct edge-case reasoning: log files and emails are usually semi-structured, not
  unstructured.
- The tool mapping should show the "coexist, not compete" point: a realistic pipeline uses
  several tools together.
- A good answer mentions repetition, volume, or integration as the trigger for programming over
  a spreadsheet tool such as Excel.

## 1.2 One library beyond the course (Challenge)

*Extends Module 1 - the "after this course" slide.*

Pick one library from the "after this course" slide (statsmodels, scikit-learn, Plotly/Dash,
Bokeh), spend ten minutes on its official site, and prepare a two-minute verbal summary: what
problem it solves, one concrete example of its use, and how it builds on what this course
teaches (NumPy arrays or pandas DataFrames as input).

**Checkable:** the summary must name the data structure the library expects, which forces you
to connect it back to the course stack.

**Guidance for self-marking:**

- scikit-learn: takes NumPy arrays / DataFrames, `fit`/`predict` pattern, e.g. predicting loan
  default.
- Plotly/Dash: interactive charts from DataFrames, dashboards in the browser.
- The link-back is the marking point: all of these libraries consume exactly the structures
  Modules 4 and 5 teach (NumPy arrays and pandas DataFrames).
