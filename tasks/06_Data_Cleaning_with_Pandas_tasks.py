# ======================================================================
# TASKS - 06 Data Cleaning with Pandas
#
# Converted from the delegate notebook '06_Data_Cleaning_with_Pandas.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/06_Data_Cleaning_with_Pandas_solutions.py
# ======================================================================

# ## Pandas Data Cleaning and Analysis Exercises
#
# ## Pandas DataFrame Reference Table
#
# | Concept | Purpose | Syntax/Keywords | Common Use Case |
# |:---:|:---:|:---:|:---:|
# | **Data Loading** | Import data from a file into a DataFrame. | `pd.read_csv()` | Reading a CSV file to begin analysis. |
# | **Data Inspection** | Understand DataFrame structure and data types. | `.info()`, `.dtypes`, `.shape` | Getting a quick overview of a dataset's size and content. |
# | **Filtering & Cleaning** | Select or remove data based on conditions. | `[boolean_mask]`, `pd.to_numeric()` | Removing invalid rows and ensuring columns have the correct data type. |
# | **Categorical Analysis** | Tally unique values in a Series. | `.value_counts()` | Analyzing the distribution and frequency of categorical features. |

# ## Part 1 - Data loading
# 1. Load in the packages numpy, pandas and save as aliases
# 2. Load in dataset `renfe_trains.csv`

# >>> Your code here

# ## 1.1 Inspect Data types and Value counts of Categorical Variables
#
# 1. Check the data types of each column in `renfe_df` and identify any inconsistencies.
# 2. Perform Value counts on Vehicle Class and Fare, use `.value_counts()` to find the occurrences of each unique value, then display the results.

# >>> Your code here

# ## 1.2 Inspect rows with 'price' value
#
# Display the rows where the 'price' column has the value 'price' to understand the nature of the error.

# **Reasoning**:
# Filter the DataFrame to show rows where the 'price' column is 'price' and display the result to examine the erroneous data.

# >>> Your code here

# ## 1.3 Drop erroneous rows
#
# Remove the rows where the column names have been incorrectly included in the data.
# Filter out rows where the `price` column is `price` and update the DataFrame.

# >>> Your code here

# ## 1.4 Convert 'price' to numeric
#
# 1. Convert the 'price' column to a numeric data type, handling any remaining non-numeric values if necessary.
#
# > **Tip:** `pd.to_numeric()` with `errors='coerce'` will turn anything that cannot be parsed into `NaN` instead of raising an error - useful when a column contains stray text.

# >>> Your code here

# ## **Data Processing** for Clean Data
# - Completeness
# - Uniqueness
# - Validity

# ## Part 2: Completeness
#
# 2.1: Check for missing values in the DataFrame.
# Use `df.isnull()` then chain `sum()` to it

# >>> Your code here

# ## Inspect rows with missing values
#
#  2.3 Filter the DataFrame to display rows with **any** missing values to understand their structure. Use `df.isnull()` chain to `.any(axis=)`
#
# > **Tip:** `axis=1` makes `.any()` look **across each row** (is there a missing value in any column of this row?), rather than down each column.

# >>> Your code here

# ## Drop rows with missing values
#
# ### 2.4 Drop rows where 'vehicle_class', 'price', and 'fare' are all missing and display the head of the updated dataframe to verify the removal.
#
# > **Tip:** `df.dropna()` accepts a `subset=` parameter - a list of columns to consider - and `how='all'` to drop only rows where **all** of those columns are missing.

# >>> Your code here

# ## Analyse ticket price by vehicle class and fare
#
# ### 2.5 Calculate and display the mean price grouped by `vehicle_class` and `fare`. Group the dataframe by 'vehicle_class' and 'fare' and calculate the mean of 'price'.

# >>> Your code here

# ## **Only continue here once you have covered aggregation**
#
# ## Imputation: Fill in remaining missing price values
#
# ### 2.6 Fill the remaining missing values in the 'price' column with the mean of all prices, grouped by `vehicle_class` and `fare`.
#
# #### Use `df.groupby(['col1','col2'])['col with nulls'].transform.mean()`

# >>> Your code here

# ### 2.7: Verify that there are no remaining missing values in the DataFrame to ensure the completion

# >>> Your code here

# # Part 3: Uniqueness
# # Perform data deduplication

# ## Identify duplicate rows
#
# ### 3.1 Use the `.duplicated()` method to check for duplicate rows in the DataFrame, and sum the number of total duplicated rows

# >>> Your code here

# ## Drop duplicate rows
#
# ### 3.2 Drop duplicate rows from the DataFrame and display the head and the number of remaining duplicate rows to verify the removal.

# >>> Your code here

# # Part 4: Validity
#
# ## Transformation
# ### 4.1 Define the bins and labels for the 'price' column and use `pd.cut()` to create the 'price_bin' column. Then display the head of the dataframe to verify the result. Use the slides as a guide

# >>> Your code here

# ### Create a new calculated column
# 4.2 Compute the tax amount for each price, assuming a 20% VAT rate was already included in price.
#
# e.g a £50 fare would have a tax of £10, save this column as `tax`

# >>> Your code here

# **Advanced**
# Filter all rows that have a Tax higher than £40 and reduce them all to a flat rate of £40. Check with `df['column'].sort_values(ascending=False)`

# >>> Your code here

# ## Part 5: Text Manipulation

# ### 5.1 Replace the following with their direct English translation
# Replace `Turista` with `Tourist`
#
# Replace `Preferente` with `Preferred`

# >>> Your code here

# ### 5.2 Use Regex to replace all instances of Flexible in fare with 'Flexible+'

#check the entries to change with renfe_df['fare'].value_counts()

# >>> Your code here
