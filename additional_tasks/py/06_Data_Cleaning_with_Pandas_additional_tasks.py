# ======================================================================
# ADDITIONAL TASKS - 06 Data Cleaning with Pandas
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in '06_Data_Cleaning_with_Pandas_tasks.py' are
# complete.
#
# The standard exercise cleans renfe_trains.csv. These tasks apply the
# same toolkit to a different loan-book file, plus a forensic look back
# at the renfe file.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/06_Data_Cleaning_with_Pandas_additional_tasks_solutions.py
# ======================================================================

import pandas as pd

# ## Additional Task 6.1: Clean the mortgage book (Stretch)
#
# Extends Module 6 exercises - fillna with groupby transform.
#
# File: data/mortgage_applicants.csv
#
# 1. Load data/mortgage_applicants.csv. Drop the 'Unnamed: 0' column.
# 2. The Score column has missing values: count them, then fill each
#    with the mean score of that applicant's Term group (transform, as
#    in the renfe exercise).
# 3. Verify no nulls remain.
# 4. Note in a comment why filling by group beats one overall mean here.

# >>> Your code here

# ## Additional Task 6.2: Text to number with regex (Challenge)
#
# Extends Module 6 exercises - str.extract and pd.cut.
#
# File: data/mortgage_applicants.csv
#
# 1. The Term column holds the strings "10 Years" and "20 Years" -
#    present, unique enough, but invalid as numbers. Create an integer
#    column TermYears by extracting the digits with
#    .str.extract(r'(\d+)') and converting with astype(int).
# 2. Bin Income into three labelled bands of your choosing with pd.cut.
# 3. Produce a value_counts() of the bands per term length.

# >>> Your code here

# ## Additional Task 6.3: Forensics on the raw renfe file (Challenge)
#
# Extends Module 6 exercises - coercion, dedupe, and investigating why
# values are missing before deleting them.
#
# File: data/renfe_trains.csv
#
# 1. The raw renfe file is dirtier than the standard exercise lets on:
#    the file was stitched together from several exports, so the header
#    row is repeated inside the data. Prove it: count rows where
#    origin == 'origin'.
# 2. Remove those rows, coerce price to numeric.
# 3. Report how many missing prices are genuinely missing versus how
#    many were manufactured by the embedded headers.
# 4. Finish with a full dedupe and a final row count.

# >>> Your code here
