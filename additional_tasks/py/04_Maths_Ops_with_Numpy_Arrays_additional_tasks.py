# ======================================================================
# ADDITIONAL TASKS - 04 Maths Ops with Numpy Arrays
#
# For students who are progressing well / have finished the standard
# exercises early. These go beyond the core material - attempt after the
# standard exercises in '04_Maths_Ops_with_Numpy_Arrays_tasks.py' are
# complete.
#
# NumPy only for these tasks - no pandas yet. np.genfromtxt() with
# usecols pulls single columns out of a CSV, matching how the standard
# exercises load data.
#
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is
# alongside this script before running it.
#
# Solutions: solutions/04_Maths_Ops_with_Numpy_Arrays_additional_tasks_solutions.py
# ======================================================================

import numpy as np

# ## Additional Task 4.1: Outliers by z-score (Stretch)
#
# Extends Module 4 exercises - broadcasting and boolean masks.
#
# File: data/cdc.csv
#
# 1. Load the weight column (column position 6) from data/cdc.csv with
#    np.genfromtxt(..., delimiter=',', skip_header=1, usecols=6).
# 2. Compute each value's z-score: (value - mean) / std.
# 3. Use a boolean mask to count how many respondents are more than 2
#    standard deviations from the mean weight.
# 4. Show the five heaviest respondents with fancy indexing or masking.
#
# Do this with broadcasting only - no loops anywhere.

# >>> Your code here

# ## Additional Task 4.2: Height and weight, related? (Stretch)
#
# Extends Module 4 exercises - descriptive statistics and np.corrcoef.
#
# File: data/cdc.csv
#
# 1. Load height (usecols=5) and weight (usecols=6) as two arrays.
# 2. Report mean, median and std of each.
# 3. Compute np.corrcoef() between them.
# 4. Answer in a comment: which statistic differs most between mean and
#    median for weight, and what does that say about the distribution's
#    shape?

# >>> Your code here

# ## Additional Task 4.3: Missing scores without pandas (Challenge)
#
# Extends Module 4 exercises - np.isnan and masked arithmetic.
#
# File: data/loan_data.csv
#
# 1. Load the Score column (usecols=5) from data/loan_data.csv with
#    np.genfromtxt. Missing values arrive as nan.
# 2. Count them with np.isnan().
# 3. Compute the mean score of the valid values only, using a mask
#    (remember nan == nan is False, which is exactly why isnan exists).
# 4. Produce a "repaired" copy of the array with each nan replaced by
#    that mean.

# >>> Your code here
