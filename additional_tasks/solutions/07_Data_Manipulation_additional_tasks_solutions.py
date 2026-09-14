# ======================================================================
# SOLUTIONS - ADDITIONAL TASKS - 07 Data Manipulation with Pandas
#
# Data files are loaded from a 'data' folder next to this file: run with
# the working directory set to a folder containing that 'data' folder.
# Run top to bottom.
# ======================================================================

import pandas as pd

# ----------------------------------------------------------------
# Additional Task 7.1: Day-on-day price moves (Stretch)
# ----------------------------------------------------------------
r = pd.read_csv('data/renfe_trains_cleaned.csv')
r['departure'] = pd.to_datetime(r['departure'])
daily = r.set_index('departure')['price'].resample('D').mean()
print("daily series length:", len(daily))
assert len(daily) == 603

smooth = daily.rolling(7).mean()
print("rolling mean, first non-NaN values:\n", smooth.dropna().head(2))
first_two_rolling = smooth.dropna().head(2)
assert round(first_two_rolling.iloc[0], 1) == 81.7
assert str(first_two_rolling.index[0].date()) == '2019-04-18'
assert round(first_two_rolling.iloc[1], 1) == 80.8
assert str(first_two_rolling.index[1].date()) == '2019-04-19'
assert smooth.iloc[:6].isna().all()  # 6 leading NaNs before the first full 7-day window

change = daily - daily.shift(1)
biggest_jump_day = change.idxmax()
print("largest overnight jump:", biggest_jump_day.date(), round(change.max(), 2))

# ----------------------------------------------------------------
# Additional Task 7.2: The three-table loan book (Challenge)
# ----------------------------------------------------------------
loans = pd.read_csv('data/loan_data.csv')
business = pd.read_csv('data/business_account.csv').drop(columns='Unnamed: 0')
locations = pd.read_csv('data/locations.csv').drop(columns='Unnamed: 0')

step1 = loans.merge(business, on='ID')  # inner join - both sides carry every ID once
print("rows after first merge:", len(step1))
assert len(step1) == 856

full = step1.merge(locations, on='ID')
print("rows after second merge:", len(full))
assert len(full) == 856
# Inner join used both times; ID is a one-to-one key in every table, so an
# inner join loses no rows - the count stays at 856 throughout.

balance_pivot = full.pivot_table(values='Balance', index='nation', columns='Term')
print("mean Balance by nation and Term:\n", balance_pivot)

default_rate = full.groupby('nation')['Default'].mean()  # True counts as 1
print("default rate by nation:\n", default_rate)
assert round(default_rate['England'], 3) == 0.113
assert round(default_rate['N Ireland'], 3) == 0.171
assert round(default_rate['Scotland'], 3) == 0.066
assert round(default_rate['Wales'], 3) == 0.126

# ----------------------------------------------------------------
# Additional Task 7.3: Mean price without loading the file (Challenge)
# ----------------------------------------------------------------
totals, counts = {}, {}
for chunk in pd.read_csv('data/renfe_trains.csv', chunksize=10000):
    chunk['price'] = pd.to_numeric(chunk['price'], errors='coerce')
    g = chunk.groupby('vehicle_class')['price']
    for k, v in g.sum().items():
        totals[k] = totals.get(k, 0) + v
    for k, v in g.count().items():
        counts[k] = counts.get(k, 0) + v

streaming_means = {k: totals[k] / counts[k] for k in totals if counts[k]}
print("streaming means:", streaming_means)

full_file = pd.read_csv('data/renfe_trains.csv')
full_file['price'] = pd.to_numeric(full_file['price'], errors='coerce')
direct_means = full_file.groupby('vehicle_class')['price'].mean()
print("direct groupby means:\n", direct_means)

for vehicle_class, streamed_mean in streaming_means.items():
    assert abs(streamed_mean - direct_means[vehicle_class]) < 1e-9, (
        f"streaming and direct means disagree for {vehicle_class}"
    )

assert round(streaming_means['Turista'], 2) == round(direct_means['Turista'], 2) == 70.41
assert round(streaming_means['Preferente'], 2) == round(direct_means['Preferente'], 2) == 82.57

print("All Module 7 additional task checks passed.")
