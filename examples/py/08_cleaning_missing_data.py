# =====================================================================
# CLEANING: MISSING VALUES, JUNK AND DUPLICATES
# =====================================================================
# Real data arrives broken. This file works through the four problems
# you will hit on almost every dataset: values that are missing, values
# that are text where a number should be, rows that are repeated, and
# columns you do not want.
#
# The dataset is data/renfe_trains.csv - Spanish rail ticket prices,
# scraped rather than exported, so it is messy in all the usual ways.
# It is a big file, so we read only the first few thousand rows with
# nrows=. Everything shown here works exactly the same on the full file.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import pandas as pd

# ---------------------------------------------------------------------
# 1. LOOK BEFORE YOU CLEAN
# ---------------------------------------------------------------------
# nrows=3000 - read only the first 3000 data rows. On a file this size
# that is the difference between an example that runs instantly and one
# you sit and wait for.
trains = pd.read_csv("data/renfe_trains.csv", nrows=3000)

print(trains.head())
print(trains.shape)          # (3000, 8)
print(trains.dtypes)

# Look at that dtype list: price is str, not a number. That is the
# first warning sign. pandas gives a column a numeric dtype only if
# EVERY value in it parses as a number, so a single piece of junk
# anywhere in the column drags the whole thing back to text.


# ---------------------------------------------------------------------
# 2. FINDING MISSING VALUES
# ---------------------------------------------------------------------
# A missing value in pandas is NaN ("not a number"). An empty cell in
# the CSV becomes NaN on read.

# .isna() - a DataFrame of True/False, True where the value is missing.
# .isnull() is the same method under a second name; use whichever you
# find readable, they are not different functions.
print(trains.isna().head())

# True counts as 1 when you add it up, so .sum() on that gives you a
# count of missing values per column. This is the one line to run first
# on any new dataset.
print(trains.isna().sum())
#   vehicle_class       4
#   price            1333
#   fare                4
# Nearly half the prices are missing. That is a fact about the data you
# need to know before you decide what to do about it.

# The proportion is often more useful than the count
print(trains.isna().mean().round(3))

# Which ROWS have a problem? .any(axis=1) asks "is anything True across
# this row?" - axis=1 means work along the row rather than down the column.
rows_with_gaps = trains[trains.isna().any(axis=1)]
print(len(rows_with_gaps))          # 1333

# The opposite: only complete rows. .notna() is the inverse of .isna().
complete = trains[trains.notna().all(axis=1)]
print(len(complete))                # 1667

# To inspect just one column's gaps, filter on that column
print(trains[trains["price"].isna()].head(3))


# ---------------------------------------------------------------------
# 3. JUNK HIDING IN A NUMERIC COLUMN
# ---------------------------------------------------------------------
# Before touching the missing prices, find out why price is text.
# Whoever built this file appended several scrapes together and left
# the header line in each time, so the word "price" appears as a data
# value partway down the column.
print(trains[trains["company"] == "company"].head(3))
print((trains["company"] == "company").sum())    # 53 stray header rows

# pd.to_numeric(series) - converts text to numbers. By default it
# refuses to guess and raises on anything it cannot parse:
try:
    pd.to_numeric(trains["price"])
except ValueError as err:
    print(f"{type(err).__name__}: {err}")
# ValueError: Unable to parse string "price" at position 69
# That message is a gift. It names the offending value and the row.

# errors="coerce" - turn anything unparseable into NaN instead of
# raising. You now have one uniform problem (missing values) rather than
# two (missing values AND junk), and section 4 deals with it.
trains["price"] = pd.to_numeric(trains["price"], errors="coerce")
print(trains["price"].dtype)         # float64 - now genuinely numeric
print(trains["price"].isna().sum())  # 1386 = the original 1333 + 53 junk

# WATCH OUT: older tutorials show errors="ignore" to leave bad values
# alone. That option was removed in pandas 3 and now raises:
try:
    pd.to_numeric(trains["price"], errors="ignore")
except ValueError as err:
    print(f"{type(err).__name__}: {err}")
# ValueError: invalid error value specified

# Those stray header rows are not real journeys, so drop them outright.
# Keep the rows where company is NOT the word "company":
trains = trains[trains["company"] != "company"]
print(trains.shape)                  # (2947, 8)


# ---------------------------------------------------------------------
# 4. THE THREE STRATEGIES
# ---------------------------------------------------------------------
# For every column with gaps you choose one of three things:
#
#   REMOVE  - drop the rows (or the whole column). Honest, but you lose
#             every other value on those rows too.
#   IMPUTE  - fill the gap with a stand-in, usually the average or the
#             most common value. Keeps your row count up, but you are
#             inventing data, so the spread of the column shrinks.
#   LEAVE   - do nothing. pandas skips NaN in mean(), sum() and groupby
#             anyway, and a chart will simply not plot the point.
#
# There is no default right answer. Half the prices here are missing,
# so filling them all with one average would say more about your fill
# than about Spanish rail fares. Removing them is defensible; leaving
# them and being clear about the sample size is often better.


# ---------------------------------------------------------------------
# 5. REMOVE - dropna()
# ---------------------------------------------------------------------
# .dropna() - returns a copy with rows containing missing values removed.
print(trains.dropna().shape)              # (1614, 8) - any gap, row goes

# how= controls how strict "has a gap" is.
#   how="any" (the default) - drop the row if ANY value is missing
#   how="all"               - drop it only if EVERY value is missing
print(trains.dropna(how="all").shape)     # (2947, 8) - no fully blank rows

# thresh=N - keep the row if it has at least N non-missing values.
# This is the middle ground: tolerate one gap, reject a row that is
# mostly holes. There are 8 columns, so thresh=7 allows a single gap.
print(trains.dropna(thresh=7).shape)      # (2943, 8)

# subset=[...] - only look at these columns when deciding. Usually what
# you actually want: the row is useless without a price, but a missing
# fare type does not spoil it.
print(trains.dropna(subset=["price"]).shape)   # (1614, 8)

# axis=1 drops COLUMNS that have gaps rather than rows. Reach for it
# only when a column is so empty it is not worth keeping.
print(trains.dropna(axis=1).shape)        # (2947, 5) - price is gone

# All of those printed a shape but changed nothing. See section 8.


# ---------------------------------------------------------------------
# 6. IMPUTE - fillna(), ffill(), bfill()
# ---------------------------------------------------------------------
# .fillna(value) - returns a copy with every NaN replaced by value.

# (a) a constant. Fine when the gap has a meaning you can name.
fares = trains["fare"].fillna("Unknown")
print(fares.value_counts().head())

# Never fill a numeric gap with 0 out of habit. 0 is a real price and it
# will drag your mean down; NaN is honestly absent and mean() skips it.
print(trains["price"].mean().round(2))                # 75.95 over real prices
print(trains["price"].fillna(0).mean().round(2))      # 41.59 - meaningless

# (b) a computed average. .mean() ignores NaN, so this is the average of
# the prices you DO have, used to stand in for the ones you do not.
avg_price = trains["price"].mean()
filled = trains["price"].fillna(avg_price)
print(filled.isna().sum())            # 0
print(filled.std().round(2), "vs", trains["price"].std().round(2))
# 16.95 vs 22.9 - the spread shrank, because every filled row now sits
# exactly on the mean. That is the cost of imputing, and it is why you
# say in your write-up how many values you filled.

# .median() is the safer average when a column has extreme values, since
# one 500 euro ticket cannot drag it the way it drags a mean.
print(trains["price"].median())             # 76.3

# (c) the most common value, for text columns where a mean makes no sense.
# .mode() returns a SERIES, not a single value, because a column can be
# tied for most common. [0] takes the first row of that result - it is
# selecting the first mode, not an index label or a column position.
print(trains["vehicle_class"].mode())       # 0    Turista
top_class = trains["vehicle_class"].mode()[0]
print(top_class)                            # Turista
classes = trains["vehicle_class"].fillna(top_class)
print(classes.isna().sum())                 # 0

# (d) carry a neighbouring value across the gap. This only makes sense
# when the rows are in a meaningful ORDER, normally time, because it
# assumes the row above is a fair guess for the row below.
by_time = trains.sort_values("departure")
prices = by_time["price"]

# .ffill() - "forward fill", copy the last known value downwards
# .bfill() - "backward fill", copy the next known value upwards
print(prices.head(8).tolist())
print(prices.ffill().head(8).tolist())
print(prices.bfill().head(8).tolist())
# ffill cannot fill a gap at the very top of the column (nothing above
# it to copy), and bfill cannot fill one at the very bottom. Chain them
# if you need every gap gone: prices.ffill().bfill()

# WATCH OUT: fillna(method="ffill") was the old spelling. It was removed
# in pandas 3 and now raises:
try:
    prices.fillna(method="ffill")
except TypeError as err:
    print(f"{type(err).__name__}: {err}")
# TypeError: NDFrame.fillna() got an unexpected keyword argument 'method'
# Call .ffill() and .bfill() as methods in their own right.


# ---------------------------------------------------------------------
# 7. DUPLICATES
# ---------------------------------------------------------------------
# .duplicated() - True for a row that has already appeared above it.
# The FIRST occurrence is False, because it is not yet a repeat.
print(trains.duplicated().sum())               # 742

# keep= chooses which copy is treated as the original:
#   keep="first" (default) - mark every copy after the first
#   keep="last"            - mark every copy before the last
#   keep=False             - mark ALL copies, originals included.
#                            Use this to LOOK at duplicates, because it
#                            shows you both sides of each pair.
print(trains.duplicated(keep=False).sum())     # 1339

repeats = trains[trains.duplicated(keep=False)].sort_values("departure")
print(repeats.head(4))

# .drop_duplicates() - returns a copy with the repeats removed. It takes
# the same keep= argument.
print(trains.drop_duplicates().shape)          # (2205, 8)

# subset= checks only those columns. Here it answers a different
# question: how many distinct routes are there, ignoring price and time?
routes = trains.drop_duplicates(subset=["origin", "destination"])
print(routes[["origin", "destination"]])

# Think before you drop. Two identical rows can be a scraping glitch, or
# two people who genuinely bought the same ticket for the same train.
# Only the first is a duplicate in the sense you care about.


# ---------------------------------------------------------------------
# 8. THEY ALL RETURN A NEW DATAFRAME
# ---------------------------------------------------------------------
# dropna, fillna, drop_duplicates, drop, ffill, bfill: every one of them
# hands you a NEW DataFrame and leaves the original untouched.
trains.dropna(subset=["price"])       # result thrown away
print(trains.shape)                   # (2947, 8) - unchanged

# So you must reassign. This is the single most common beginner bug in
# pandas, and it is silent: nothing errors, your cleaning just does not
# happen.
clean = trains.dropna(subset=["price"])
print(clean.shape)                    # (1614, 8)

# Reassigning to the same name is fine and is what you will usually write:
#     df = df.dropna()
#     df = df.drop_duplicates()

# Most of these methods also take inplace=True, which modifies the
# original and returns None. Prefer reassignment: inplace= saves no
# memory under pandas 3's Copy-on-Write, it cannot be chained, and if
# you forget it returns None you end up with df set to None.

# It matters even more on a COLUMN. Under Copy-on-Write, df["col"] hands
# you a view, so an inplace method on it updates a temporary object that
# is discarded immediately. pandas 3 warns rather than letting it pass:
#     trains["price"].fillna(0, inplace=True)
# ChainedAssignmentError: A value is being set on a copy of a DataFrame
# or Series through chained assignment using an inplace method. Such
# inplace method never works to update the original DataFrame or Series...
# The prices stay exactly as they were. Assign the column instead:
trains["price"] = trains["price"].fillna(trains["price"].median())
print(trains["price"].isna().sum())   # 0


# ---------------------------------------------------------------------
# 9. DROPPING WHAT YOU DO NOT NEED
# ---------------------------------------------------------------------
# .drop() removes labels. axis= says which kind of label you mean:
#   axis=0 (the default) - row labels, ie index values
#   axis=1               - column labels
print(trains.drop("fare", axis=1).columns.tolist())
print(trains.drop(["fare", "vehicle_class"], axis=1).shape)   # (2947, 6)

# columns= does the same thing and reads better, so most code uses it.
# There is a rows= spelling too but index= is the usual one.
print(trains.drop(columns=["fare"]).shape)                    # (2947, 7)
print(trains.drop(index=trains.index[:5]).shape)              # (2942, 8)

# Every train here is operated by renfe, so that column tells you nothing
tidy = trains.drop(columns=["company"])
print(tidy.columns.tolist())


# ---------------------------------------------------------------------
# 10. THE WHOLE THING, START TO FINISH
# ---------------------------------------------------------------------
# The same pipeline as above, written the way you would actually write
# it: read, remove the junk rows, fix the type, drop the unusable rows,
# de-duplicate, drop the dead column. Reassigning at every step.
df = pd.read_csv("data/renfe_trains.csv", nrows=3000)
df = df[df["company"] != "company"]
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["price"])
df = df.drop_duplicates()
df = df.drop(columns=["company"])

print(df.shape)                  # (1184, 7)
print(df.isna().sum().sum())     # 0
print(df.head())

# Say what you did. "1816 of 3000 rows removed, 1333 of them for a
# missing price" is part of the result, not an aside - anyone reading
# your numbers needs to know which rows they are based on.


# ---------------------------------------------------------------------
# 11. A SECOND DATASET, A DIFFERENT CALL
# ---------------------------------------------------------------------
# data/mortgage_applicants.csv has 856 rows and 20 missing credit
# scores. Dropping 2% of your rows to lose one column's worth of gaps is a poor
# trade, so this is a good candidate for imputing.
apps = pd.read_csv("data/mortgage_applicants.csv", index_col=0)
print(apps.isna().sum())

apps["Score"] = apps["Score"].fillna(apps["Score"].median())
print(apps.isna().sum().sum())   # 0
print(len(apps))                 # 856 - all rows kept

# Same tools, opposite decision, because the proportion missing was
# different. That judgement is the part you cannot look up.
