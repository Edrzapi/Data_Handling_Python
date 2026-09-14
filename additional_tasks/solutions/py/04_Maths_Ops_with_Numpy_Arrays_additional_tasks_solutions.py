# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 04 Maths Ops with Numpy Arrays
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom.
# ======================================================================

import numpy as np

# ----------------------------------------------------------------
# Additional Task 4.1: Outliers by z-score (Stretch)
# ----------------------------------------------------------------
weights = np.genfromtxt('data/cdc.csv', delimiter=',', skip_header=1, usecols=6)
print("weights loaded:", weights.shape[0])
assert weights.shape[0] == 20000

z = (weights - weights.mean()) / weights.std()
outliers = np.abs(z) > 2  # boolean mask
outlier_count = int(outliers.sum())
print("outliers beyond 2 std:", outlier_count)
assert outlier_count == 874

heaviest_five = np.sort(weights)[-5:][::-1]
print("five heaviest:", heaviest_five)

# ----------------------------------------------------------------
# Additional Task 4.2: Height and weight, related? (Stretch)
# ----------------------------------------------------------------
h = np.genfromtxt('data/cdc.csv', delimiter=',', skip_header=1, usecols=5)
w = np.genfromtxt('data/cdc.csv', delimiter=',', skip_header=1, usecols=6)

print("height: mean=%.2f median=%.2f std=%.2f" % (h.mean(), np.median(h), h.std()))
print("weight: mean=%.2f median=%.2f std=%.2f" % (w.mean(), np.median(w), w.std()))

corr = np.corrcoef(h, w)
print("correlation matrix:\n", corr)
off_diagonal = corr[0, 1]
print("height/weight correlation:", round(off_diagonal, 3))
assert round(off_diagonal, 2) == 0.56

# Weight's mean exceeds its median (mean pulled up by heavier outliers),
# indicating a right-skewed distribution - Module 8's histogram shows this.
assert w.mean() > np.median(w)

# ----------------------------------------------------------------
# Additional Task 4.3: Missing scores without pandas (Challenge)
# ----------------------------------------------------------------
scores = np.genfromtxt('data/loan_data.csv', delimiter=',', skip_header=1, usecols=5)
print("scores loaded:", scores.shape[0])
assert scores.shape[0] == 856

mask = np.isnan(scores)
nan_count = int(mask.sum())
print("missing scores:", nan_count)
assert nan_count == 20

valid_mean = scores[~mask].mean()
print("valid mean score:", round(valid_mean, 2))
assert round(valid_mean, 1) == 450.9

repaired = scores.copy()
repaired[mask] = valid_mean  # write through the mask
assert int(np.isnan(repaired).sum()) == 0
assert round(repaired.mean(), 2) == round(valid_mean, 2)  # unchanged mean, as expected when
# replacing nans with the mean of the remaining values

print("All Module 4 additional task checks passed.")
