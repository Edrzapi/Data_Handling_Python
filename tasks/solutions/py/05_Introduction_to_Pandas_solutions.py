# ======================================================================
# SOLUTIONS - 05 Introduction to Pandas
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# The notebook solutions use IPython's display(); in a plain Python run
# there is no display(), so fall back to print().
try:
    display
except NameError:
    display = print

# ----------------------------------------------------------------
# Exercise 1.1: Creating and Querying a Series
# ----------------------------------------------------------------
# 1. Import pandas Create the Series
import pandas as pd

data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# 2. Select using iloc (position 2 is '30')
iloc_result = data_series.iloc[2]
print(f"iloc[2] result: {iloc_result}")

# 3. Select using loc (label 'b' is '20')
loc_result = data_series.loc['b']
print(f"loc['b'] result: {loc_result}")

# ----------------------------------------------------------------
# Exercise 2.1: Loading `cdc.csv` and Setting an Index
# ----------------------------------------------------------------
import pandas as pd

# Load the cdc.csv file
cdc_df = pd.read_csv('data/cdc.csv')  # path adjusted: the file lives in the data folder

#Drop Unamed Column
cdc_df.drop(columns=['Unnamed: 0'], inplace=True)

# Calculate a ratio for height and weight and store as new column
cdc_df['height_weight_ratio'] = cdc_df['height'] / cdc_df['weight']

# Display the first 5 rows
display(cdc_df.head())

# ----------------------------------------------------------------
# Exercise 2.2: Filtering for categorical values
# ----------------------------------------------------------------
#filter rows to only include very good
vgood_df = cdc_df[cdc_df['genhlth'] == 'very good']
poor_df = cdc_df[cdc_df['genhlth'] == 'poor']

# ----------------------------------------------------------------
# Exercise 2.3: Creating new calculated columns
# ----------------------------------------------------------------
#print the mean of height_weight_ratio
print(vgood_df['height_weight_ratio'].mean())
print(poor_df['height_weight_ratio'].mean())

# ----------------------------------------------------------------
# Exercise 3.1
# ----------------------------------------------------------------
import pandas as pd

# Load the loans.csv file
loans = pd.read_csv('data/loan_data.csv')  # path adjusted: the file lives in the data folder

display(loans.head(10))

# ----------------------------------------------------------------
# Exercise 3.2: Setting Index and Ordering
# ----------------------------------------------------------------
# Set ID as Index and sort
indexed_df = loans.set_index('ID').sort_index()
display(indexed_df)

# ----------------------------------------------------------------
# Exercise 3.3: Filtering using a Single Column
# ----------------------------------------------------------------
filtered_df = indexed_df[indexed_df['Debt']!=0]
display(filtered_df)

# ----------------------------------------------------------------
# Exercise 3.4: Filtering using Multiple Columns, to create a flagged dataframe
# ----------------------------------------------------------------
flagged_df = filtered_df[(filtered_df['Default'] == 1) & (filtered_df['Income'] < 25000)]
display(flagged_df)

# ----------------------------------------------------------------
# Exercise 4.1: Summary Stats and Datatypes of flagged dataframe
# ----------------------------------------------------------------
# Use df.describe() and df.info()
flagged_df.describe()
flagged_df.info()

# ----------------------------------------------------------------
# Exercise 4.2: Correcting Data Types
# ----------------------------------------------------------------
flagged_df['Default'] =  flagged_df['Default'].astype('bool')
flagged_df.info()

# ----------------------------------------------------------------
# Advanced
# ----------------------------------------------------------------
# Compare the means
print("Mean comparison:")
print(flagged_df[['Balance', 'Score', 'Debt']].mean())
print(loans[['Balance', 'Score', 'Debt']].mean())

# ----------------------------------------------------------------
# Advanced
# ----------------------------------------------------------------
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.boxplot([loans['Score'].dropna(), flagged_df['Score'].dropna()], tick_labels=['Original Loans', 'Flagged Loans'])  # 'labels=' renamed 'tick_labels=' in matplotlib 3.9+
plt.title('Box Plot of Score: Original vs Flagged Dataframes')
plt.ylabel('Score')
plt.show()
