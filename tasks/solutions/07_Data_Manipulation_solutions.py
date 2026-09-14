# ======================================================================
# SOLUTIONS - 07 Data Manipulation
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Part 1 - Pivot tables
# ----------------------------------------------------------------
import pandas as pd

# Load in the dataset
df = pd.read_csv('data/renfe_trains_cleaned.csv')

# Pivot tables
df.pivot_table(values=['price'],
               index='fare',
               columns='destination',
               aggfunc='mean').round()

# ----------------------------------------------------------------
# 2.1. Convert departure & arrival to a more appropriate datatype.
# ----------------------------------------------------------------
# Working with time series
df['departure'] = pd.to_datetime(df['departure'])
df['arrival'] = pd.to_datetime(df['arrival'])

# ----------------------------------------------------------------
# 2.2 Calculate the duration of each train journey and add it as a column
# ----------------------------------------------------------------
df['duration'] = df['arrival'] - df['departure']

# ----------------------------------------------------------------
# 2.4. Attempt to chain a `sort_index()` low to high (earlier to later). This will make slicing
# ----------------------------------------------------------------
df = df.set_index('departure').sort_index()  # assignment added so the date slicing below works (the notebook did not save it)

# ----------------------------------------------------------------
# 2.5. Select all journeys which departed on 07/05/19.
# ----------------------------------------------------------------
df.loc['2019-05-07']

# ----------------------------------------------------------------
# 2.6. Select all journeys which departed on 07/05/19 to 11/05/19.
# ----------------------------------------------------------------
df.loc['2019-05-07':'2019-05-11']

# ----------------------------------------------------------------
# 2.7. Add one year to each date in the index of the DataFrame (but do not
# ----------------------------------------------------------------
# Add one year to index dates (without saving)
df.index + pd.DateOffset(years=1)

# ----------------------------------------------------------------
# 2.8. Create a subset of the DataFrame called madrid_to_barca which
# ----------------------------------------------------------------
madrid_to_barca = df[(df['origin'] == 'MADRID') & (df['destination'] == 'BARCELONA')]

# ----------------------------------------------------------------
# 2.9. Advanced: Select only those tickets in madrid_to_barca which are in the Promo
# ----------------------------------------------------------------
madrid_to_barca = madrid_to_barca[(madrid_to_barca['fare'] == 'Promo') & (madrid_to_barca['vehicle_class'] == 'Turista')]

# ----------------------------------------------------------------
# 2.10. Advanced: Compute a seven day rolling average for price for the madrid_to_barca. Use `rolli...
# ----------------------------------------------------------------
madrid_to_barca['7D_rolling_mean'] = madrid_to_barca['price'].rolling(window='7D').mean()

# ----------------------------------------------------------------
# 2.11. Stretch & Challenge (optional): Plot the rolling average vs. the actual values of price.
# ----------------------------------------------------------------
# Compute rolling average
madrid_to_barca['price'].plot(style='.')
madrid_to_barca['7D_rolling_mean'].plot(kind='line')  # column name fixed (the notebook referenced a non-existent 'rolling' column)

# ----------------------------------------------------------------
# 3.1. Read in the fare_conditions.csv file. It contains the conditions for
# ----------------------------------------------------------------
# Read fare conditions and merge
fare_conditions = pd.read_csv('data/fare_conditions.csv')
df.merge(fare_conditions, on='fare')
