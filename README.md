# Data Handling with Python

Course materials for QADHPYTHON. Everything here is yours to keep, run and
break. Nothing is marked, and you are meant to experiment with it.

**New here? Start with [SETUP.md](SETUP.md)** to get Python, the packages and
Jupyter running on your machine. Come back once `import pandas` works.

---

## What is in this repo

| Folder | What it is | When to use it |
| --- | --- | --- |
| **[examples/](examples/)** | Worked, runnable demonstrations of each topic | Read alongside the course, or when you are stuck on a task |
| **[tasks/](tasks/)** | The exercises you work through in class | During the course, one set per module |
| **[additional_tasks/](additional_tasks/)** | Harder, optional challenges | When you finish early, or afterwards to stretch yourself |
| **[data/](data/)** | Every dataset the code loads | You do not edit these, the code reads them |

Every folder that contains code is split by file type:

- **`py/`** plain Python scripts, for PyCharm, VS Code or the terminal
- **`ipynb/`** Jupyter notebooks, for Jupyter Lab or Notebook
- **`md/`** written questions with no code

The two formats contain the same material. Use whichever you prefer.

---

## Examples

Numbered in the order you meet them on the course. Each one runs top to bottom
on its own.

| # | Example | Covers |
| --- | --- | --- |
| 01 | Python basics | Variables, types, conversion, f-strings, division |
| 02 | Collections | Lists, tuples, dictionaries, sets, slicing, nesting |
| 03 | Flow control and functions | if/else, loops, `range`, `enumerate`, writing functions |
| 04 | Files | `open()` modes, `with`, reading and writing text files |
| 05 | NumPy arrays | Arrays vs lists, dtypes, broadcasting, masking, statistics |
| 06 | Loading data | `read_csv`, `read_excel`, `read_sql`, and the index |
| 07 | Selecting and filtering | `.loc`, `.iloc`, boolean masks, `.query`, sorting |
| 08 | Cleaning missing data | `isna`, `dropna`, `fillna`, duplicates, coercing junk |
| 09 | Text and regex | The `.str` accessor, pattern matching, binning with `cut` |
| 10 | Dates and time series | `to_datetime`, resampling, rolling windows, time zones |
| 11 | Combining data | `concat`, `merge` and its join types, checking row counts |
| 12 | Plotting | Matplotlib, chart types, labelling, seaborn |

---

## Running the code

**Always start from the repo root.** The code loads data using paths like
`data/loan_data.csv`, which only resolve from there.

### Notebooks

```bash
cd Data_Handling_Python
jupyter lab
```

Jupyter opens in your browser showing this folder. Click into `examples/ipynb/`
and open whichever notebook you want. Run a cell with **Shift + Enter**.

### Scripts

```bash
cd Data_Handling_Python
python examples/py/06_loading_data.py
```

In PyCharm, open the whole repo folder as the project (not a single file), so
that the working directory is the repo root and the data paths resolve.

---

## If something does not work

- **`FileNotFoundError` mentioning a data file** you are not running from the
  repo root. `cd` to the top of the repo and try again.
- **`ModuleNotFoundError: No module named 'pandas'`** your environment is not
  active, or the packages are not installed. See [SETUP.md](SETUP.md).
- **`ImportError` about openpyxl** when reading Excel, install it:
  `pip install openpyxl`.
- **Notebook runs but uses the wrong Python** the kernel does not match your
  environment. The troubleshooting section of [SETUP.md](SETUP.md) covers it.

### A note on pandas versions

These examples were checked against **pandas 3**. If you are on pandas 1 or 2,
a few things behave differently, and older tutorials you find online will
reflect the older behaviour:

- Text columns report their dtype as `str` on pandas 3, and `object` before it.
- Chained assignment (`df["col"][0] = x`) never updates the original on
  pandas 3. Use `df.loc[0, "col"] = x`.
- `fillna(method="ffill")`, `errors="ignore"` and `applymap` were removed in
  pandas 3. Use `.ffill()`, `errors="coerce"` and `.map()`.

Check your version with:

```python
import pandas as pd
print(pd.__version__)
```
