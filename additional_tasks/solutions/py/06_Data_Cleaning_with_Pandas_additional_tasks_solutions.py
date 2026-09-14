# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 06 Data Cleaning with Pandas
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom.
# ======================================================================

import pandas as pd

# ----------------------------------------------------------------
# Additional Task 6.1: Clean the mortgage book (Stretch)
# ----------------------------------------------------------------
m = pd.read_csv('data/mortgage_applicants.csv').drop(columns='Unnamed: 0')
assert len(m) == 856

missing_before = m['Score'].isna().sum()
print("missing scores before fill:", missing_before)
assert missing_before == 20

group_means = m.groupby('Term')['Score'].transform('mean')
m['Score'] = m['Score'].fillna(group_means)  # reassignment, not chained assignment -
# m['Score'][...] = x does not write in pandas 3

missing_after = m['Score'].isna().sum()
print("missing scores after fill:", missing_after)
assert missing_after == 0

means_by_term = m.groupby('Term')['Score'].mean()
print("mean score by term:\n", means_by_term)
assert round(means_by_term['10 Years']) == 414
assert round(means_by_term['20 Years']) == 543
# Filling by group beats one overall mean: the two Term groups have very
# different average scores (~414 vs ~543), so a single overall mean would
# have dragged both groups towards the middle and distorted the fill.

# ----------------------------------------------------------------
# Additional Task 6.2: Text to number with regex (Challenge)
# ----------------------------------------------------------------
m['TermYears'] = m['Term'].str.extract(r'(\d+)').astype(int)
assert set(m['TermYears'].unique()) == {10, 20}
assert m['TermYears'].dtype.kind == 'i'

m['band'] = pd.cut(
    m['Income'],
    bins=[0, 20000, 40000, m['Income'].max()],
    labels=['low', 'mid', 'high'],
)
assert m['band'].isna().sum() == 0  # every row lands in a bin

band_counts = m.groupby('TermYears', observed=True)['band'].value_counts()
print("Income band counts per term length:\n", band_counts)

# ----------------------------------------------------------------
# Additional Task 6.3: Forensics on the raw renfe file (Challenge)
# ----------------------------------------------------------------
r = pd.read_csv('data/renfe_trains.csv')
raw_rows = len(r)
print("raw rows:", raw_rows)
assert raw_rows == 85948

embedded_headers = int((r['origin'] == 'origin').sum())
print("embedded header rows:", embedded_headers)
assert embedded_headers == 3875

r = r[r['origin'] != 'origin']
r['price'] = pd.to_numeric(r['price'], errors='coerce')

# Once the header rows are gone, every remaining NaN in price is a genuine
# missing value (there is nothing else left that could have manufactured it).
genuine_missing = int(r['price'].isna().sum())
print("genuine missing prices (headers already removed):", genuine_missing)
assert genuine_missing == 13179

# For comparison: coercing price on the UNFILTERED raw file (headers still
# present) shows where that 13,179 comes from and how much the headers add.
r_with_headers = pd.read_csv('data/renfe_trains.csv')
r_with_headers['price'] = pd.to_numeric(r_with_headers['price'], errors='coerce')
missing_prices_incl_headers = int(r_with_headers['price'].isna().sum())
nan_from_headers = int(r_with_headers.loc[r_with_headers['origin'] == 'origin', 'price'].isna().sum())
nan_non_headers = int(r_with_headers.loc[r_with_headers['origin'] != 'origin', 'price'].isna().sum())
print("total NaN prices on the unfiltered file:", missing_prices_incl_headers)
print("  - of which caused by embedded header rows:", nan_from_headers)
print("  - of which genuine (non-header) missing prices:", nan_non_headers)
assert missing_prices_incl_headers == 17054
assert nan_from_headers == embedded_headers == 3875
assert nan_non_headers == genuine_missing == 13179
assert missing_prices_incl_headers == nan_from_headers + nan_non_headers

# --- MISMATCH FLAG (STRETCH_GOALS.md, Module 6, task 6.3) ---------------
# Note: STRETCH_GOALS.md is not included in this course package - this
# flag documents a discrepancy noticed against an external answer-key
# document at authoring time; it is preserved here as a correctness note,
# not a claim that the file ships alongside these solutions.
# STRETCH_GOALS.md's checkable line reads: "13,179 total missing prices
# after coercion, of which 3,875 are the headers, so 9,304 are genuine".
# Running the actual data shows this arithmetic does not hold:
#   - 13,179 is the GENUINE missing-price count (rows left once the 3,875
#     header rows are removed) - not a "total" that the header count is
#     subtracted from.
#   - Coercing price WITHOUT removing header rows first gives 17,054 NaNs
#     in total (13,179 genuine + 3,875 header-caused) - this is the true
#     "total missing prices after coercion" figure, and STRETCH_GOALS.md
#     never states it.
#   - So the correct genuine-missing figure is 13,179, not 9,304. This
#     verification run flags the discrepancy rather than silently
#     adjusting the source document's figure.
# --------------------------------------------------------------------------

# Dedupe, following the task's own order (headers already removed above).
before_dedupe = len(r)
r = r.drop_duplicates()
after_dedupe = len(r)
duplicates_removed = before_dedupe - after_dedupe
print("duplicates removed (after header rows were already stripped):", duplicates_removed)
print("final row count:", after_dedupe)
assert duplicates_removed == 48678
assert after_dedupe == 33395

# --- MISMATCH FLAG (STRETCH_GOALS.md, Module 6, task 6.3) ---------------
# Note: STRETCH_GOALS.md is not included in this course package - see the
# note on the first mismatch flag above.
# STRETCH_GOALS.md's checkable line also states "52,552 duplicated rows
# disappear on dedupe". That figure only reproduces if drop_duplicates()
# is run on the RAW file while the 3,875 embedded header rows are still
# present (they collapse into a single row as duplicates of each other,
# inflating the count). Following the task's own instructions in order -
# remove the header rows, coerce price, THEN dedupe - actually removes
# 48,678 duplicate rows, leaving 33,395 rows, not 33,396. Both figures are
# shown below for the record; this run flags the mismatch rather than
# silently rewriting STRETCH_GOALS.md's number.
raw_incl_headers = pd.read_csv('data/renfe_trains.csv')
dedup_incl_headers = raw_incl_headers.drop_duplicates()
duplicates_removed_incl_headers = len(raw_incl_headers) - len(dedup_incl_headers)
print("[for comparison only] duplicates removed if deduped BEFORE header "
      "removal:", duplicates_removed_incl_headers, "-> matches STRETCH_GOALS.md's 52,552")
assert duplicates_removed_incl_headers == 52552
# --------------------------------------------------------------------------

print("All Module 6 additional task checks passed (with 2 flagged mismatches"
      " against STRETCH_GOALS.md's task 6.3 checkable figures - see comments above).")
