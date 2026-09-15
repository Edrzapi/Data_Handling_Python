# =====================================================================
# SELECTING AND FILTERING IN PANDAS
# =====================================================================
# Worked reference for getting the rows and columns you actually want
# out of a DataFrame: [] versus .loc versus .iloc, boolean masks,
# .isin, .between, .query, sorting, and the chained indexing trap.
#
# The dataset is data/loan_data.csv - 856 loan applications with the
# columns ID, Income, Term, Balance, Debt, Score and Default.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import pandas as pd

loans = pd.read_csv("data/loan_data.csv")

print(loans.shape)        # (856, 7)
print(loans.dtypes)
# ID int64, Income int64, Term str, Balance int64, Debt int64,
# Score float64, Default bool
#
# Note "str" on Term. Older pandas reported text columns as "object",
# which really meant "a column of pointers to arbitrary Python objects".
# From pandas 3.0 text gets a proper string dtype and prints as str.
# Tutorials written against pandas 1.x or 2.x will still say object.
#
# Score is float64 rather than int64 for a reason: 20 of the 856 scores
# are missing, and a missing value can only live in a float column.
print(loans["Score"].isna().sum(), "missing scores")


# ---------------------------------------------------------------------
# 1. ONE COLUMN OR ONE-COLUMN TABLE: df[col] VERSUS df[[col]]
# ---------------------------------------------------------------------
# A single name in the brackets gives you a Series: one column of values
# with the index attached. Think of it as a labelled NumPy array.
income = loans["Income"]
print(type(income))       # <class 'pandas.Series'>
print(income.head(3))

# A LIST of names gives you a DataFrame, even when the list has one item
# in it. The extra brackets are a list, not special syntax.
income_df = loans[["Income"]]
print(type(income_df))    # <class 'pandas.DataFrame'>
print(income_df.head(3))
print(income_df.shape)    # (856, 1) - still two-dimensional

# Why it matters: the two have different methods. A Series has .str and
# .unique(); a DataFrame has .columns and .merge(). Pick the one that
# suits what you are about to do.
print(loans["Term"].unique())         # works - Series
print(loans[["Income", "Score"]].head(3))   # several columns, as a table

# Dot notation (loans.Income) also works and you will see it everywhere,
# but it breaks on any column name with a space in it, and it silently
# loses to real DataFrame attributes if a column is called "shape" or
# "count". Square brackets always work, so prefer them.


# ---------------------------------------------------------------------
# 2. .loc - SELECTING BY LABEL
# ---------------------------------------------------------------------
# .loc[rows, columns] works with LABELS: index labels and column names.
# This file has no meaningful index, so the labels are 0, 1, 2... Give
# it a real one and the difference becomes obvious.
print(loans.loc[0, "Income"])                # one value at row label 0
print(loans.loc[0:2, ["Income", "Score"]])   # rows 0 to 2, two columns
print(loans.loc[:, "Income"].head(3))        # : means all rows

# WATCH OUT: .loc slices are INCLUSIVE of the end label. Everywhere else
# in Python the end is excluded, so this one catches people out.
print(len(loans.loc[0:3]))     # 4 rows: labels 0, 1, 2 AND 3
print(len(loans.iloc[0:3]))    # 3 rows: the usual Python behaviour

# Set a real index and .loc reads much better:
by_id = loans.set_index("ID")
print(by_id.loc[567])                 # the application with ID 567
print(by_id.loc[[567, 523], "Score"]) # two specific applications


# ---------------------------------------------------------------------
# 3. .iloc - SELECTING BY POSITION
# ---------------------------------------------------------------------
# .iloc[rows, columns] ignores labels completely and counts from 0, the
# way a list does. Use it when you mean "the first row" or "the last
# three", regardless of what those rows are called.
print(by_id.iloc[0])          # the FIRST row, whatever its ID happens to be
print(by_id.iloc[-3:])        # the last three rows - negatives work

# The contrast is sharpest on the same number. 567 is both a label and a
# position here, and they point at completely different rows:
print(by_id.loc[567, "Income"])    # the row LABELLED 567
print(by_id.iloc[567]["Income"])   # the 568th row in the file

print(loans.iloc[0, 1])       # row 0, column 1 (Income)
print(loans.iloc[0:3, 0:3])   # end position excluded, as normal

# Mixing them up gives you a clear error, which is a mercy:
try:
    loans.iloc[0, "Term"]
except ValueError as err:
    print(f"ValueError: {err}")
# ValueError: Location based indexing can only have [integer, integer
# slice (START point is INCLUDED, END point is EXCLUDED), listlike of
# integers, boolean array] types
# iloc wanted a position and got a name.

try:
    loans.loc[0, 2]
except KeyError as err:
    print(f"KeyError: {err}")
# KeyError: 2
# loc went looking for a COLUMN NAMED 2 and there is not one.

# Rule of thumb: .loc when you know what the row is called, .iloc when
# you only know where it sits. If the index is the default 0, 1, 2 they
# look identical, which is exactly why the habit is worth forming early.


# ---------------------------------------------------------------------
# 4. .at AND .iat - ONE SINGLE VALUE
# ---------------------------------------------------------------------
# .at is .loc cut down to a single cell, .iat is .iloc cut down the same
# way. They skip all the machinery for handling slices and lists, so
# they are noticeably faster inside a loop.
print(loans.at[0, "Term"])    # 'Short Term' - by label
print(loans.iat[0, 2])        # 'Short Term' - by position, same cell

# They only do one cell. Ask for more and they refuse, which is the
# trade for the speed.
try:
    loans.at[0:2, "Term"]
except Exception as err:
    print(f"{type(err).__name__}: {err}")


# ---------------------------------------------------------------------
# 5. BOOLEAN MASKING - THE MAIN WAY YOU FILTER
# ---------------------------------------------------------------------
# Compare a column to a value and you get a Series of True/False, one
# per row. That is a mask.
high = loans["Income"] > 50000
print(high.head(3))
print(high.dtype)             # bool
print(high.sum())             # how many rows are True

# Put the mask in the brackets and you get back only the True rows. The
# index comes with them, so the row labels are no longer consecutive -
# that is a useful sign that you are looking at a filtered set.
rich = loans[high]
print(rich.shape)
print(rich.head(3))

# Usually written in one line:
print(loans[loans["Income"] > 50000].shape)

# .loc takes a mask too, and it lets you pick columns at the same time,
# which the plain bracket form cannot do:
print(loans.loc[loans["Income"] > 50000, ["ID", "Income", "Score"]].head(3))


# ---------------------------------------------------------------------
# 6. COMBINING CONDITIONS: & AND | AND THOSE BRACKETS
# ---------------------------------------------------------------------
# & means and, | means or, ~ means not. Each condition must be wrapped
# in its own round brackets.
risky = loans[(loans["Income"] < 25000) & (loans["Debt"] > 1000)]
print(risky.shape)

either = loans[(loans["Score"] > 900) | (loans["Income"] > 70000)]
print(either.shape)

not_short = loans[~(loans["Term"] == "Short Term")]
print(not_short.shape)

# WHY THE BRACKETS. & and | are arithmetic-level operators in Python and
# bind more tightly than the comparisons do. Without brackets,
#     loans["Income"] > 30000 & loans["Debt"] > 0
# is read as
#     loans["Income"] > (30000 & loans["Debt"]) > 0
# which is a different question entirely. Here it happens to blow up:
try:
    loans["Income"] > 30000 & loans["Debt"] > 0
except ValueError as err:
    print(f"ValueError: {err}")
# ValueError: The truth value of a Series is ambiguous. Use a.empty,
# a.bool(), a.item(), a.any() or a.all()
# It is not always so obliging. With the right mix of types it can
# quietly give a wrong answer, so always bracket.

# THE OTHER CLASSIC: using Python's `and` instead of `&`.
try:
    loans[(loans["Income"] > 30000) and (loans["Debt"] > 0)]
except ValueError as err:
    print(f"ValueError: {err}")
# ValueError: The truth value of a Series is ambiguous. Use a.empty,
# a.bool(), a.item(), a.any() or a.all()
#
# `and` needs to decide whether the thing on its left is true or false,
# as a single yes/no. The thing on its left is 856 separate yes/nos.
# pandas refuses to guess whether you meant "any of them" or "all of
# them", so it raises instead. & does not have that problem because it
# works element by element: row 1 against row 1, row 2 against row 2.
# Same story for `or` versus | and `not` versus ~.


# ---------------------------------------------------------------------
# 7. .isin AND .between - SHORTHAND FOR TWO COMMON FILTERS
# ---------------------------------------------------------------------
# .isin(list) - "is this value one of these?" It saves you chaining a
# pile of == conditions together with |.
short = loans[loans["Term"].isin(["Short Term"])]
print(short.shape)

# It is far more useful with several values, and with numbers too:
chosen = loans[loans["ID"].isin([567, 523, 544])]
print(chosen[["ID", "Income", "Term"]])

# ~ in front flips it to "is NOT one of these":
print(loans[~loans["Term"].isin(["Short Term"])].shape)

# .between(low, high) - a range test. Both ends are INCLUDED by default,
# unlike a Python slice. Pass inclusive="neither" to exclude both, or
# "left"/"right" for one of them.
mid = loans[loans["Score"].between(200, 400)]
print(mid.shape)
print(loans["Score"].between(200, 400).sum())
print(loans["Score"].between(200, 400, inclusive="neither").sum())

# The long way round, for comparison - .between says the same thing:
print(((loans["Score"] >= 200) & (loans["Score"] <= 400)).sum())

# Rows with a missing Score are False in both versions. nan is not
# known to be in the range, so it is left out rather than guessed at.


# ---------------------------------------------------------------------
# 8. .query - THE SAME FILTERS, WRITTEN AS A SENTENCE
# ---------------------------------------------------------------------
# .query("expression") takes the condition as a string and looks the
# column names up for you. No df[...] repeated on every line, and no
# bracket rules to remember.
print(loans.query("Income > 50000 and Debt > 1000").shape)

# Inside a query string, `and` / `or` / `not` are fine - pandas parses
# the string itself rather than letting Python evaluate it, so the
# problem from section 6 never arises. & and | work too.
print(loans.query("Term == 'Short Term' and Score > 800").shape)

# A bool column needs no comparison at all:
print(loans.query("Default").shape)
print(loans.query("Default and Income < 20000")[["ID", "Income", "Score"]].head())

# @name pulls in a Python variable:
threshold = 60000
print(loans.query("Income > @threshold").shape)

# Column names with spaces or dots go in backticks: `credit score`.
# Downsides: typos become runtime errors rather than anything your
# editor can catch, and it is slower on small frames. Use it when a
# filter has got long enough to be hard to read as brackets.


# ---------------------------------------------------------------------
# 9. SORTING
# ---------------------------------------------------------------------
# .sort_values(by=...) - returns a sorted COPY. The original is untouched
# unless you assign the result back.
print(loans.sort_values("Income").head(3)[["ID", "Income"]])
print(loans.sort_values("Income", ascending=False).head(3)[["ID", "Income"]])

# Several columns: sorted by the first, ties broken by the second.
# ascending takes a list so each column can go its own way.
ranked = loans.sort_values(["Term", "Score"], ascending=[True, False])
print(ranked[["Term", "Score"]].head(3))

# Missing values go LAST by default, whichever direction you sort in.
# na_position="first" moves them to the top, which is a quick way to see
# what is missing.
print(loans.sort_values("Score", na_position="first")[["ID", "Score"]].head(3))

# Sorting leaves the original index in place, so the labels come out
# shuffled. Use .reset_index(drop=True) if you want a clean 0, 1, 2
# afterwards; drop=True throws the old labels away instead of keeping
# them as a column.
print(loans.sort_values("Income").reset_index(drop=True).head(3)[["ID", "Income"]])

# .sort_index() puts a shuffled frame back in index order. And if all
# you want is the extremes, .nlargest / .nsmallest say it more directly
# than sorting the whole thing:
print(loans.nlargest(3, "Income")[["ID", "Income"]])


# ---------------------------------------------------------------------
# 10. CHAINED INDEXING - THE TRAP
# ---------------------------------------------------------------------
# Selecting twice in a row - loans["Balance"][0], or
# loans[loans["Income"] > 50000]["Score"] - is called chained indexing.
# For READING it is merely untidy. For WRITING it does not work.
#
# The first bracket produces an intermediate object. Under Copy-on-Write,
# which is how pandas 3 behaves, that intermediate is always a copy, so
# the second bracket writes into the copy and the copy is discarded.
before = loans.loc[0, "Balance"]
print(before)                      # 1460

loans["Balance"][0] = 999999       # emits a ChainedAssignmentError warning
print(loans.loc[0, "Balance"])     # 1460 - the write did NOT stick

# The warning printed above reads:
#   ChainedAssignmentError: A value is being set on a copy of a DataFrame
#   or Series through chained assignment. Such chained assignment never
#   works to update the original DataFrame or Series, because the
#   intermediate object on which we are setting values always behaves as
#   a copy (due to Copy-on-Write).
#   Try using '.loc[row_indexer, col_indexer] = value' instead, to
#   perform the assignment in a single step.
#
# Take the warning seriously. It is a warning rather than an error, so
# your script carries on with data that was never updated. In older
# pandas the equivalent message was SettingWithCopyWarning, and there the
# write sometimes DID land, which was worse: the same line of code could
# work or not work depending on how the frame was built.

# The fix is always the same: one set of brackets, one step.
loans.loc[0, "Balance"] = 999999
print(loans.loc[0, "Balance"])     # 999999 - it stuck
loans.loc[0, "Balance"] = before   # put it back

# Same rule for a filtered update. This does nothing useful:
#     loans[loans["Score"] < 100]["Default"] = True
# This does what you meant:
flagged = loans.copy()             # work on a copy so the demo is tidy
flagged.loc[flagged["Score"] < 100, "Default"] = True
print(flagged["Default"].sum(), "flagged vs", loans["Default"].sum(), "before")

# And if you are pulling a subset out to work on separately, take an
# explicit copy. It costs one method call and removes all doubt about
# whose data you are editing.
subset = loans[loans["Income"] > 70000].copy()
subset["Income"] = subset["Income"] / 1000
print(subset[["ID", "Income"]].head(3))
print(loans["Income"].max())       # original untouched


# ---------------------------------------------------------------------
# 11. THE POINT
# ---------------------------------------------------------------------
# Three tools cover nearly everything: [] for columns, .loc for labels,
# .iloc for positions. Filtering is just a boolean mask handed to one of
# them, and & / | / ~ join masks together as long as every condition has
# its own brackets.
#
# The one habit that saves the most time is writing every assignment as
# a single .loc step. Chained indexing does not raise an error, it just
# quietly fails to do anything, and that is a hard bug to spot later.
