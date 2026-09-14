# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 05 Introduction to Pandas
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom.
# ======================================================================

import pandas as pd

# The notebook solutions use IPython's display(); in a plain Python run
# there is no display(), so fall back to print().
try:
    display
except NameError:
    display = print

# ----------------------------------------------------------------
# Additional Task 5.1: Weather from JSON, sliced by date (Stretch)
# ----------------------------------------------------------------
w = pd.read_json('data/weather.json', orient='split')
w.index = pd.to_datetime(w.index)
four_day_mean = w.loc['2023-07-17':'2023-07-20', 'temp'].mean()  # .loc is end-inclusive: 4 rows
print("mean temp 17-20 Jul:", round(four_day_mean, 2))
assert round(four_day_mean, 2) == 18.55

sunniest_day = w['sun_hrs'].idxmax()
print("sunniest day:", sunniest_day.date())
assert str(sunniest_day.date()) == '2023-07-19'

# ----------------------------------------------------------------
# Additional Task 5.2: Beating your group average (Challenge)
# ----------------------------------------------------------------
cdc = pd.read_csv('data/cdc.csv').drop(columns='Unnamed: 0')
cdc['wt_vs_group'] = cdc['weight'] - cdc.groupby('genhlth')['weight'].transform('mean')
assert len(cdc['wt_vs_group']) == 20000

group_sums = cdc.groupby('genhlth')['wt_vs_group'].sum()
print("wt_vs_group sum per group (should be ~0):\n", group_sums)
assert (group_sums.abs() < 1e-6).all()

cdc['above'] = cdc['wt_vs_group'] > 0
above_fraction = cdc.groupby('genhlth')['above'].mean()
print("fraction above own group's average:\n", above_fraction)
assert (above_fraction < 0.5).all()  # right-skewed weights pull the mean above the median

# ----------------------------------------------------------------
# Additional Task 5.3: pandas meets SQL (Stretch)
# ----------------------------------------------------------------
import sqlite3

con = sqlite3.connect('data/movies_db.sqlite')
movies = pd.read_sql('SELECT * FROM movies', con)
assert len(movies) == 3
assert list(movies.columns) == ['id', 'name', 'year', 'rating']

movies = movies.set_index('name')
movies['decade'] = movies['year'] // 10 * 10
display(movies)
print(movies.dtypes)

assert (movies['decade'] == (movies['year'] // 10 * 10)).all()

print("All Module 5 additional task checks passed.")
