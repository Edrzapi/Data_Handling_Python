# ======================================================================
# ADDITIONAL TASKS - 05 Introduction to Pandas
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in '05_Introduction_to_Pandas_tasks.py' are complete.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/05_Introduction_to_Pandas_additional_tasks_solutions.py
# ======================================================================

import pandas as pd

# ## Additional Task 5.1: Weather from JSON, sliced by date (Stretch)
#
# Extends Module 5 exercises - loading semi-structured JSON and .loc
# date slicing.
#
# File: data/weather.json
#
# 1. Load data/weather.json with pd.read_json(..., orient='split') - the
#    orient parameter is required or the load fails.
# 2. Convert the index to datetime with pd.to_datetime.
# 3. Use .loc with date-string labels to report the mean temperature
#    from 2023-07-17 to 2023-07-20 inclusive.
# 4. Find the day with the most sun hours using idxmax().

# >>> Your code here

# ## Additional Task 5.2: Beating your group average (Challenge)
#
# Extends Module 5 exercises - groupby and transform.
#
# File: data/cdc.csv
#
# 1. Load data/cdc.csv and drop the 'Unnamed: 0' column.
# 2. Add a column wt_vs_group holding each respondent's weight minus the
#    mean weight of their genhlth group, using
#    groupby(...)['weight'].transform('mean').
# 3. Report, per group, what fraction of respondents are above their own
#    group's average (hint: a boolean column and groupby(...).mean() -
#    True counts as 1).

# >>> Your code here

# ## Additional Task 5.3: pandas meets SQL (Stretch)
#
# Extends Module 5 exercises - reading from a database into a DataFrame.
#
# File: data/movies_db.sqlite
#
# 1. Using sqlite3.connect('data/movies_db.sqlite') and pd.read_sql,
#    pull everything from the 'movies' table into a DataFrame (it is
#    deliberately tiny - three rows).
# 2. Set 'name' as the index, and check the dtypes.
# 3. Add a decade column derived from year using integer arithmetic
#    (year // 10 * 10).

# >>> Your code here
