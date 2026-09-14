# ======================================================================
# ADDITIONAL TASKS - 07 Data Manipulation with Pandas
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in '07_Data_Manipulation_tasks.py' are complete.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/07_Data_Manipulation_additional_tasks_solutions.py
# ======================================================================

import pandas as pd

# ## Additional Task 7.1: Day-on-day price moves (Stretch)
#
# Extends Module 7 exercises - resample, rolling and shift.
#
# File: data/renfe_trains_cleaned.csv
#
# 1. Load data/renfe_trains_cleaned.csv, parse departure with
#    pd.to_datetime, set it as the index, and resample to a daily mean
#    price.
# 2. Add a 7-day rolling mean column.
# 3. Use shift(1) to compute the day-on-day change in mean price.
# 4. Report the single day with the largest overnight jump.

# >>> Your code here

# ## Additional Task 7.2: The three-table loan book (Challenge)
#
# Extends Module 7 exercises - chained merge and pivot_table.
#
# Files: data/loan_data.csv, data/business_account.csv, data/locations.csv
#
# 1. Merge loan_data.csv with business_account.csv and then
#    locations.csv, joining on ID each time (drop the 'Unnamed: 0'
#    columns first).
# 2. Check the row count after each merge - it should stay at 856 -
#    and state which join type you used and why the count did not
#    change.
# 3. Produce a pivot table of mean Balance with nation as the index and
#    Term as the columns, and a default rate per nation.

# >>> Your code here

# ## Additional Task 7.3: Mean price without loading the file (Challenge)
#
# Extends Module 7 exercises - chunked reading with chunksize.
#
# File: data/renfe_trains.csv
#
# 1. Pretend renfe_trains.csv is too big for memory. Using
#    pd.read_csv(..., chunksize=10000), compute the mean price per
#    vehicle_class across the whole file without ever holding it all at
#    once: keep running totals and counts in dictionaries, coercing
#    price inside each chunk, then divide at the end.
# 2. Compare your answer to the direct full-file groupby to prove the
#    streaming version is right.

# >>> Your code here
