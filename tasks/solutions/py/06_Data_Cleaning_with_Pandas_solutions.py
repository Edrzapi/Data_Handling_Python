# ======================================================================
# SOLUTIONS - 06 Data Cleaning with Pandas
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
# Part 1 - Data loading
# ----------------------------------------------------------------
import pandas as pd
import numpy as np

renfe_df = pd.read_csv('data/renfe_trains.csv')
display(renfe_df.head())

# ----------------------------------------------------------------
# 1.1 Inspect Data types and Value counts of Categorical Variables
# ----------------------------------------------------------------
display(renfe_df.info())

display(renfe_df['vehicle_class'].value_counts())
display(renfe_df['fare'].value_counts())

# ----------------------------------------------------------------
# 1.2 Inspect rows with 'price' value
# ----------------------------------------------------------------
renfe_df[renfe_df['price'] == 'price']

# ----------------------------------------------------------------
# 1.3 Drop erroneous rows
# ----------------------------------------------------------------
renfe_df = renfe_df[renfe_df['price'] != 'price']
display(renfe_df.head())

# ----------------------------------------------------------------
# 1.4 Convert 'price' to numeric
# ----------------------------------------------------------------
renfe_df['price'] = pd.to_numeric(renfe_df['price'], errors='coerce')
display(renfe_df.head())
renfe_df.info()

# ----------------------------------------------------------------
# Part 2: Completeness
# ----------------------------------------------------------------
renfe_df.isnull().sum()

# ----------------------------------------------------------------
# 2.3 Filter the DataFrame to display rows with any missing values to understand their structure. U...
# ----------------------------------------------------------------
display(renfe_df[renfe_df.isnull().any(axis=1)])

# ----------------------------------------------------------------
# 2.4 Drop rows where 'vehicle_class', 'price', and 'fare' are all missing and display the head of ...
# ----------------------------------------------------------------
renfe_df.dropna(subset=['vehicle_class', 'price', 'fare'], how='all', inplace=True)
display(renfe_df.head())

# ----------------------------------------------------------------
# 2.5 Calculate and display the mean price grouped by `vehicle_class` and `fare`. Group the datafra...
# ----------------------------------------------------------------
renfe_df.groupby(['vehicle_class', 'fare'])['price'].mean()

# ----------------------------------------------------------------
# Use `df.groupby(['col1','col2'])['col with nulls'].transform.mean()`
# ----------------------------------------------------------------
grouped_prices = renfe_df.groupby(['vehicle_class', 'fare'])['price'].transform('mean')
renfe_df['price'] = renfe_df['price'].fillna(grouped_prices)
display(renfe_df.head())

# ----------------------------------------------------------------
# 2.7: Verify that there are no remaining missing values in the DataFrame to ensure the completion
# ----------------------------------------------------------------
display(renfe_df.isnull().sum())

# ----------------------------------------------------------------
# 3.1 Use the `.duplicated()` method to check for duplicate rows in the DataFrame, and sum the numb...
# ----------------------------------------------------------------
display(renfe_df.duplicated().sum())

# ----------------------------------------------------------------
# 3.2 Drop duplicate rows from the DataFrame and display the head and the number of remaining dupli...
# ----------------------------------------------------------------
renfe_df.drop_duplicates(inplace=True)
print(renfe_df.duplicated().sum())

# ----------------------------------------------------------------
# 4.1 Define the bins and labels for the 'price' column and use `pd.cut()` to create the 'price_bin...
# ----------------------------------------------------------------
bins = [0, 100, 200, 300]
labels = ['(0, 100]', '(100, 200]', '(200, 300]']
renfe_df['price_bin'] = pd.cut(renfe_df['price'], bins=bins, labels=labels)
display(renfe_df.head())

# ----------------------------------------------------------------
# 4.2 Compute the tax amount for each price, assuming a 20% VAT rate was already included in price.
# ----------------------------------------------------------------
renfe_df['tax'] = renfe_df['price'] * 0.20  # line reassembled: the notebook solution was split by a stray code fence
display(renfe_df.head())

# ----------------------------------------------------------------
# 4.2 Compute the tax amount for each price, assuming a 20% VAT rate was already included in price....
# ----------------------------------------------------------------
renfe_df.loc[renfe_df['tax'] > 40, 'tax'] = 40
display(renfe_df['tax'].sort_values(ascending=False))

# ----------------------------------------------------------------
# 5.1 Replace the following with their direct English translation
# ----------------------------------------------------------------
renfe_df['vehicle_class'] = renfe_df['vehicle_class'].str.replace('Turista', 'Tourist', regex=True)
renfe_df['vehicle_class'] = renfe_df['vehicle_class'].str.replace('Preferente', 'Preferred', regex=True)
display(renfe_df.head())

# ----------------------------------------------------------------
# 5.2 Use Regex to replace all instances of Flexible in fare with 'Flexible+'
# ----------------------------------------------------------------
renfe_df['fare'] = renfe_df['fare'].str.replace('.*Flexible.*', 'Flexible+', regex=True)
display(renfe_df.head())
display(renfe_df['fare'].value_counts())
