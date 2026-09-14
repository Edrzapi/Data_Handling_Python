# ======================================================================
# TASKS - 05 Introduction to Pandas
#
# Converted from the delegate notebook '05_Introduction_to_Pandas.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/05_Introduction_to_Pandas_solutions.py
# ======================================================================

# ## Introduction to Pandas Exercises
#
# This notebook provides exercises on data manipulation and analysis using the `pandas` library, formatted for easy use in environments like Google Colab. It covers Series, DataFrames, loading files (CSV/JSON), indexing, filtering, type conversion, date parsing, and aggregation.
#
# **Note**: These exercises will use the `loan_data.csv` and `cdc.csv` files
#
# ## Pandas Reference Table
#
# | Concept | Purpose | Syntax/Keywords | Common Use Case |
# |:----------:|:---------:|:--------:|:-------------------:|
# | **Data Structures** | 1D (Series) or 2D (DataFrame) labeled data. | `pd.Series()`, `pd.DataFrame()` | Storing and manipulating tabular data. |
# | **I/O** | Reading and writing data from/to files. | `pd.read_csv()`, `pd.read_json()` | Loading data from external sources. |
# | **Indexing (Selection)** | Selecting subsets of data by label or position. | `.loc[]`, `.iloc[]`, `[]` | Retrieving specific rows and columns. |
# | **Filtering** | Using boolean masks to select data. | `df[df['col'] > 5]` | Finding data that meets specific criteria. |
# | **Type Conversion** | Changing the data type of a column. | `.astype()`, `pd.to_datetime()` | Cleaning data and preparing for analysis. |
# | **Aggregation** | Summarizing data using groups. | `.groupby()`, `.mean()`, `.agg()` | Calculating statistics for different categories. |
#
# ## Part 1: Querying Series using `loc` and `iloc`
#
# A `Series` is a one-dimensional labeled array. You can select data from it by its integer-based position (`iloc`) or its label (`loc`).
#
# ### Exercise 1.1: Creating and Querying a Series
#
# 1.  Import the `pandas` library and alias it as `pd` and create a `pd.Series` named `data_series` with the data `[10, 20, 30, 40]` and a custom index of `['a', 'b', 'c', 'd']`.
# 2.  Use **`.iloc`** to select and print the element at integer position `2`.
# 3.  Use **`.loc`** to select and print the element with the index label `'b'`.

#1

# 2

# 3

# ## Part 2: DataFrames, Loading and Setting the Index
#
# A `DataFrame` is a 2D labeled data structure. You can load data directly from files and set one of the columns as the index for easier lookups.
#
# ### Exercise 2.1: Loading `cdc.csv` and Setting an Index
#
# 1.  Load the `cdc.csv` file into a pandas DataFrame named `cdc_df`.
# 2.  Display the first 5 rows of the DataFrame using the `.head()` method.
#
# 3. Drop `Unnamed` Column, use `drop(column, axis= )`
# 4. Calculate ratio for height and weight columns, store as new column `cdc_df['height_weight_ratio']`

# >>> Your code here

# ###2.2 Filtering for categorical values
#
# 1. Filter for rows with `very good` in `genhlth` column save as `vgood_df`
# 2. Filter for rows with `poor` in `genhlth` column save as `poor_df`

# >>> Your code here

# ###2.3 Creating new calculated columns
#
# 1. Calculate the mean of `['height_weight_ratio']` for both `very good` and `poor` Genhelth outcomes, use the two saved dataframes above

# >>> Your code here

# ## Part 3: Flagging Accounts in Loans Dataset
#
# ### Exercise 3.1:
# 1. Load in Loans dataset
#
# 2. View 10 rows from dataframe

# >>> Your code here

# ### Exercise 3.2: Setting Index and Ordering
#
# - Set ID as Index with `.set_index()` and chain with `.sort_index()`
#
# - `df.method().method()`
# - Check and save the new dataframe as `indexed_df`

# >>> Your code here

# ### Exercise 3.3: Filtering using a Single Column
#
# - Now filter out any Debt that is 0 and save as `filtered_df`.
#
# - Use `df['Column'] != 0`
#
# - Check to see how many rows are you left with.

# >>> Your code here

# ### Exercise 3.4: Filtering using Multiple Columns, to create a flagged dataframe
#
# 1. Filter dataframe of people who have:
# 2. `Default = 1` , remember to use `==` as an evaluater
# 3. `Income` less than 25000
# 4. Name this df `flagged_df`

# >>> Your code here

# ## Part 4: Changing Column Datatypes
#
# Data often loads with incorrect types (e.g., numbers as strings). The `.astype()` method is essential for cleaning data.

# ### Exercise 4.1: Summary Stats and Datatypes of flagged dataframe
#
# 1. Derive the Descriptive statistics `df.describe()`
# 2. Find the Datatypes with `df.info()`, try and identify which requires casting as a different datatype

# >>> Your code here

# ### Exercise 4.2: Correcting Data Types
#
# 1.  Using `flagged_df`. Make sure the `Default` column is saved as a `bool` (boolean) data type.

# >>> Your code here

# ## **Advanced**:
#
# 1. Compare the Means of `Balance`, `Score` and `Debt` of both the Flagged Dataframe and the Original Loan Dataframe
#
# 2. Visualise the difference in distribution of Score in both dataframes

# >>> Your code here
