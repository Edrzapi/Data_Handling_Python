# =====================================================================
# GETTING DATA INTO PANDAS - CSV, EXCEL AND SQL
# =====================================================================
# Worked reference for the three readers you will use most: read_csv,
# read_excel and read_sql. Every file used here is already in the data
# folder of this repo, so you can run this top to bottom as it stands.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import sqlite3

import pandas as pd

# ---------------------------------------------------------------------
# 1. CSV - the one you will use most
# ---------------------------------------------------------------------
# pd.read_csv(path) - reads a comma-separated text file into a DataFrame
loans = pd.read_csv("data/loan_data.csv")

print(loans.head())      # first 5 rows; head(10) for more
print(loans.shape)       # (rows, columns)
print(loans.dtypes)      # what pandas decided each column is


# ---------------------------------------------------------------------
# 2. That leading 0, 1, 2 column - the index
# ---------------------------------------------------------------------
# Every DataFrame has an index. If you do not give it one, pandas
# numbers the rows 0, 1, 2... That is the unlabelled column on the left.
# You cannot delete it, but you have three options.

# (a) hide it when printing - the index still exists, you just do not show it
print(loans.head(3).to_string(index=False))

# (b) replace it with a column that actually identifies the row
by_id = loans.set_index("ID")
print(by_id.head(3))
print(by_id.index.name)        # 'ID' - it became the index
print(list(by_id.columns))     # ...and left the column list

# (c) do the same at load time
by_id_direct = pd.read_csv("data/loan_data.csv", index_col="ID")

# set_index is reversible - reset_index() turns it back into a column
print(list(by_id.reset_index().columns))


# ---------------------------------------------------------------------
# 3. Unnamed: 0 - what happens when someone forgets
# ---------------------------------------------------------------------
# Saving with to_csv() writes the index out as an extra unnamed column
# unless you pass index=False. Read that file back and the stray column
# turns up as "Unnamed: 0". Two files in this repo have exactly that:
cdc = pd.read_csv("data/cdc.csv")
print(cdc.columns[:3])      # note 'Unnamed: 0' sitting at the front

# Fix on read: tell pandas that column IS the index
cdc_fixed = pd.read_csv("data/cdc.csv", index_col=0)
print(cdc_fixed.columns[:3])

# Fix on write, so it never happens to the next person:
# cdc_fixed.to_csv("out.csv", index=False)


# ---------------------------------------------------------------------
# 4. EXCEL - same idea, but workbooks have sheets
# ---------------------------------------------------------------------
# pd.read_excel(path, sheet_name=...) - reads one sheet of a workbook.
# Needs the openpyxl package installed for .xlsx files.

# Without sheet_name you get the FIRST sheet, whatever it happens to be
march = pd.read_excel("data/loan_data.xlsx")
print(march.head(3))

# Do not assume a sheet is called "Sheet1". Ask:
# pd.ExcelFile(path) - opens the workbook so you can inspect it
workbook = pd.ExcelFile("data/loan_data.xlsx")
print(workbook.sheet_names)      # ['March'] - named after the month

# Then read the one you want by name
march = pd.read_excel("data/loan_data.xlsx", sheet_name="March")

# Useful variations:
#   sheet_name=0            by position instead of name
#   sheet_name=None         ALL sheets, returned as a dict of DataFrames
#   skiprows=2              skip title rows above the real header
#   usecols="A:D"           only some columns


# ---------------------------------------------------------------------
# 5. SQL - reading straight from a database
# ---------------------------------------------------------------------
# pd.read_sql(query, connection) - runs the query and hands back a
# DataFrame. You supply the connection; pandas does not open one for you.

# sqlite3 is in the standard library, so this needs no install
conn = sqlite3.connect("data/movies_db.sqlite")

# What is in this database? sqlite keeps its catalogue in sqlite_master
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(tables)

movies = pd.read_sql("SELECT * FROM movies", conn)
print(movies.head(3))

# WATCH OUT: plenty of tutorials show pd.read_sql("movies", conn), passing
# a bare table name. That only works on a SQLAlchemy connection. With a
# plain sqlite3 connection like this one it raises:
#     DatabaseError: Execution failed on sql 'movies': near "movies": syntax error
# Write real SQL and it always works.

# Let the DATABASE do the filtering when the table is large - it is far
# faster than loading everything and throwing most of it away.
# The ? is a placeholder; params supplies the value safely. Never build
# a query by gluing strings together with user input - that is how SQL
# injection happens.
best = pd.read_sql(
    "SELECT name, year, rating FROM movies WHERE rating >= ? ORDER BY rating DESC",
    conn,
    params=(9,),
)
print(best)

conn.close()      # always close when you are done

# This movies table only has a handful of rows, so filtering in SQL
# versus in pandas makes no practical difference here. Try the same
# thing against data/iris.db (150 rows) to see it matter. Note its
# column names contain spaces, so SQL needs them in double quotes:
#     conn = sqlite3.connect("data/iris.db")
#     pd.read_sql('SELECT * FROM iris WHERE "sepal length (cm)" > 6', conn)


# ---------------------------------------------------------------------
# 6. THE POINT
# ---------------------------------------------------------------------
# Three different sources, one destination. Once the data is a DataFrame
# it makes no difference where it came from: the same filtering,
# grouping and plotting works on all of it. Getting it loaded is the
# only part that changes.
