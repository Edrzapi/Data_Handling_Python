# ======================================================================
# TASKS - 07 Data Manipulation
#
# Converted from the delegate notebook '07_Data_Manipulation.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/07_Data_Manipulation_solutions.py
# ======================================================================

# # 07 Data Manipulation with Pandas
# - Pivot Tables
# - Datetime formatting
# - Merging Tables on Columns (aka JOINs)

# ## Part 1 - Pivot tables
#
# 1. Load in the dataset renfe_trains_cleaned.csv.
#
# 2. Use a pivot table to explore how price differs with respect to the type of
# fare for each destination.

# >>> Your code here

# ## Part 2 - Working with Time series
# 2.1. Convert departure & arrival to a more appropriate datatype.

# >>> Your code here

# 2.2 Calculate the duration of each train journey and add it as a column
# called duration.

# >>> Your code here

# 2.3 Make departure the index of the DataFrame
#
# 2.4. Attempt to chain a `sort_index()` low to high (earlier to later). This will make slicing
# possible later.

# >>> Your code here

# 2.5. Select all journeys which departed on 07/05/19.

# >>> Your code here

# 2.6. Select all journeys which departed on 07/05/19 to 11/05/19.

# >>> Your code here

# 2.7. Add one year to each date in the index of the DataFrame (but do not
# save it!).

# >>> Your code here

# 2.8. Create a subset of the DataFrame called madrid_to_barca which
# contains only journeys with origin as MADRID and destination as
# BARCELONA.

# >>> Your code here

# ## Advanced Challenges

# 2.9. **Advanced**: Select only those tickets in madrid_to_barca which are in the Promo
# category for fare and Turista for vehicle_class. Update
# madrid_to_barca to only contain these.

# >>> Your code here

# 2.10. **Advanced:** Compute a seven day rolling average for price for the madrid_to_barca. Use `rolling()` method and chain with `mean()`
# DataFrame.
# Add it as a column called `7D_rolling_mean`.

# >>> Your code here

# 2.11. **Stretch & Challenge (optional):** Plot the rolling average vs. the actual values of price.
#
# > Plotting is not covered until the Data Visualisation module, so treat this as a preview - have a go using the solution as a guide, or come back to it after the next module.

# >>> Your code here

# ## Part 3 Combining tables
# 3.1. Read in the fare_conditions.csv file. It contains the conditions for
# the type of ticket that has been purchased.

# >>> Your code here
