# ======================================================================
# ADDITIONAL TASKS - Cross-Module Mini-Projects
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt only
# after ALL of Modules 5-8 are complete, since each mini-project draws
# on cleaning, manipulation and visualisation together.
#
# Each mini-project needs 30-45 minutes and combines skills from several
# modules. Suitable for end-of-course fast finishers or as take-home
# practice.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/Cross_Module_Mini_Projects_solutions.py
# ======================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ## Mini-Project 1: Loan book risk report
#
# Combines: Module 6 (cleaning - fillna by group), Module 7 (merging
# multiple tables, pivot tables), Module 8 (bar chart, box plot).
#
# Files: data/loan_data.csv, data/business_account.csv, data/locations.csv
#
# Build a short "risk report", narrated with comments throughout:
#
# 1. Clean: load loan_data.csv, count and fill the 20 missing Score
#    values with the mean score per Term group; justify the choice in a
#    comment.
# 2. Combine: merge in business_account.csv and locations.csv on ID
#    (856 rows must survive - assert it with a row-count check).
# 3. Derive: a debt_ratio column (Debt / Income), and a Score band via
#    pd.cut with labels of your choosing.
# 4. Aggregate: default rate by nation, and a pivot of mean debt_ratio
#    by nation and Term.
# 5. Visualise: a bar chart of default rate by nation, and a box plot of
#    Score split by Default. One comment under each: what does this
#    chart say to a lending manager?

# >>> Your code here

# ## Mini-Project 2: Renfe end to end, from raw to weekly trend
#
# Combines: Module 6 (forensic cleaning of the raw file), Module 7
# (datetime derivation, merge, resample/unstack), Module 8 (multi-series
# line chart, violin plot).
#
# Files: data/renfe_trains.csv, data/fare_conditions.csv
#
# Start from the RAW renfe_trains.csv (not the cleaned one) and finish
# with a presentable weekly price chart:
#
# 1. Clean: remove the embedded header rows (origin == 'origin'), coerce
#    price to numeric, drop rows with no price, drop the duplicate rows,
#    and reset_index(drop=True).
# 2. Enrich: parse departure and arrival to datetime and derive a
#    duration_mins column from their difference
#    (.dt.total_seconds() / 60); merge in fare_conditions.csv on fare
#    with a left join and explain in a comment why left, not inner.
# 3. Manipulate: set departure as the index; resample to weekly mean
#    price per vehicle_class (hint: groupby('vehicle_class')
#    .resample('W')['price'].mean(), then unstack the class level - or
#    pivot after resampling).
# 4. Visualise: one line per vehicle class on a single Axes, legend
#    outside or compact, plus a violin plot of price by vehicle_class on
#    the cleaned data.

# >>> Your code here

# ## Mini-Project 3: CDC health survey brief
#
# Combines: Module 6 (deriving columns, cleaning), Module 7 (pivot
# tables, groupby aggregation), Module 8 (heatmap, scatter with a
# reference line, proportional stacked bar).
#
# File: data/cdc.csv
#
# Produce a one-page analysis brief for a health authority:
#
# 1. Clean and derive: drop Unnamed: 0; build bmi as
#    703 * weight / height ** 2 (the survey uses pounds and inches);
#    build wt_gap as wtdesire - weight (negative means wants to lose).
# 2. Bin: age into brackets with pd.cut (for example 18-29, 30-44,
#    45-59, 60+), labelled.
# 3. Aggregate: a pivot of mean bmi by age bracket and gender; the share
#    of respondents wanting to lose weight (wt_gap < 0) per genhlth
#    category.
# 4. Visualise: a heatmap of the bmi pivot with annot=True; a scatter of
#    weight vs wtdesire with the diagonal y = x line drawn on for
#    reference; and a proportional stacked bar of smoking (smoke100) by
#    genhlth.
# 5. Conclude: three comment bullet points a non-technical reader could
#    act on.

# >>> Your code here
