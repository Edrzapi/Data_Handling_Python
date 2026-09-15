# =====================================================================
# COMBINING DATA
# =====================================================================
# Real work almost never arrives in one table. Customer details sit in
# one file, where they live in another, their mortgage application in a
# third. This example covers the three ways of putting tables back
# together: concat for stacking, merge for matching on a key, and join
# for the common case where the key is already the index.
#
# The files used here all come from the data folder of this repo and all
# describe the same 856 loan customers, linked by an ID column.
#
# Run from the repo root so the relative data/ paths resolve.
# =====================================================================

import pandas as pd

loans = pd.read_csv("data/loan_data.csv")
print(loans.shape)
print(loans.head(3))


# ---------------------------------------------------------------------
# 1. concat, axis=0 - stacking tables on top of each other
# ---------------------------------------------------------------------
# pd.concat([df1, df2]) - glues DataFrames together. Use it when the
# tables are the SAME SHAPE OF THING, for example January's file and
# February's file, and you want one longer table.
first = loans.head(3)
last = loans.tail(3)

stacked = pd.concat([first, last])
print(stacked)
print(len(first), "+", len(last), "=", len(stacked))

# Notice the index: 0, 1, 2, 853, 854, 855. concat keeps the original
# row labels, so you end up with a gappy index and, if the two tables
# overlap, repeated labels. That breaks .loc lookups later.
# ignore_index=True renumbers from 0 and is usually what you want.
stacked = pd.concat([first, last], ignore_index=True)
print(stacked.index.tolist())

# If the columns do not match exactly, concat does not complain. It
# keeps every column it has seen and fills the gaps with NaN. Handy when
# a later file gained a column, dangerous when you have simply misspelt
# one, so check the column list afterwards.
odd = pd.DataFrame({"ID": [999], "Income": [30000], "Region": ["Wales"]})
print(pd.concat([first, odd], ignore_index=True))

# keys= labels each piece so you can still tell which file a row came
# from. That is worth doing when you are combining monthly extracts.
labelled = pd.concat([first, last], keys=["earliest", "latest"])
print(labelled.index[:2].tolist())


# ---------------------------------------------------------------------
# 2. concat, axis=1 - putting tables side by side
# ---------------------------------------------------------------------
# axis=1 sticks columns together instead of rows. It lines rows up BY
# INDEX POSITION LABEL, not by any ID column, so it is only safe when
# both tables describe the same rows in the same order.
scores = loans[["ID", "Score"]].head(4)
debts = loans[["Debt"]].head(4)
print(pd.concat([scores, debts], axis=1))

# Here is the trap. Give the second table a different index and the
# alignment falls apart, silently producing NaN:
shifted = loans[["Debt"]].iloc[2:6]          # index 2, 3, 4, 5
print(pd.concat([scores, shifted], axis=1))

# Six rows out of two four-row tables, and half the values missing. Only
# the two labels the tables share, 2 and 3, line up. If you have a
# proper key column such as ID, use merge instead. Reach for
# concat(axis=1) only when you genuinely know the rows line up.


# ---------------------------------------------------------------------
# 3. merge - matching on a key column
# ---------------------------------------------------------------------
# df.merge(other, on="ID") - matches rows by the value in a column, the
# way a SQL join does. This is the workhorse.
# To make the behaviour visible we use two small tables that only
# PARTLY overlap: customers holds the first six IDs, regions holds IDs
# four to nine.
locations = pd.read_csv("data/locations.csv", index_col=0)

customers = loans[["ID", "Income", "Score"]].iloc[0:6]
regions = locations[["ID", "nation"]].iloc[3:9]

print(customers["ID"].tolist())
print(regions["ID"].tolist())
# Three IDs appear in both, three are only in customers, three are only
# in regions. That is what makes the next section worth reading.


# ---------------------------------------------------------------------
# 4. how= - which rows survive
# ---------------------------------------------------------------------
# how= decides what happens to rows that have no match on the other
# side. Watch the row counts, they are the whole story.
inner = customers.merge(regions, on="ID", how="inner")   # the default
left = customers.merge(regions, on="ID", how="left")
right = customers.merge(regions, on="ID", how="right")
outer = customers.merge(regions, on="ID", how="outer")

print("inner", len(inner))    # 3 - only IDs found in BOTH tables
print("left ", len(left))     # 6 - every customer, matched or not
print("right", len(right))    # 6 - every region row, matched or not
print("outer", len(outer))    # 9 - everything from both sides

print(left)
# The three unmatched customers keep their income and score and get NaN
# for nation. That NaN is information: it tells you those customers have
# no location on file.

# Choosing:
#   inner   you only want rows where both sides have data
#   left    keep your main table intact and add what you can find.
#           This is the one you want most of the time, because it cannot
#           silently lose rows from the table you started with.
#   right   the same thing the other way round. Rare, because you can
#           just swap the tables over and use left.
#   outer   lose nothing, then investigate the NaNs. Good for checking
#           how well two sources actually line up.

# NaN counts tell you which side the gaps are on:
print(outer.isna().sum())


# ---------------------------------------------------------------------
# 5. Always check len() before and after
# ---------------------------------------------------------------------
# A merge can quietly drop rows (no match) or quietly add them
# (duplicate keys, see section 8). Neither raises an error. Get into the
# habit of checking, every single time:
before = len(customers)
after = len(customers.merge(regions, on="ID", how="left"))
print(f"rows before {before}, after {after}")

if after != before:
    print("row count changed - check for duplicate keys")

# A left merge should give you exactly the rows you started with. If it
# does not, the right-hand table has repeated keys and you need to know
# that before you report any totals.

# indicator=True adds a _merge column saying where each row came from.
# It is the quickest way to see what matched:
checked = customers.merge(regions, on="ID", how="outer", indicator=True)
print(checked["_merge"].value_counts())


# ---------------------------------------------------------------------
# 6. When the key columns have different names
# ---------------------------------------------------------------------
# on= only works when both tables spell the key the same way. They often
# do not: one system says ID, another says customer_id. left_on and
# right_on say which column to use on each side.
regions_renamed = regions.rename(columns={"ID": "customer_id"})
print(regions_renamed.columns.tolist())

by_name = customers.merge(regions_renamed, left_on="ID", right_on="customer_id", how="inner")
print(by_name)

# You now have BOTH key columns, holding identical values. Drop the
# spare so nobody has to wonder later which one is authoritative:
print(by_name.drop(columns="customer_id"))

# The keys must also be the same TYPE. An ID stored as the number 567 in
# one file and the text "567" in another will not match, and you get
# zero rows with no warning. If a merge returns nothing, check .dtypes
# on both key columns first.


# ---------------------------------------------------------------------
# 7. Column name clashes and the _x / _y suffixes
# ---------------------------------------------------------------------
# data/mortgage_applicants.csv describes the same customers with mostly
# the same column names. Merge the two and pandas has to keep both
# versions of Income, Balance and so on apart.
mortgages = pd.read_csv("data/mortgage_applicants.csv", index_col=0)
print(mortgages.columns.tolist())

clashed = loans.merge(mortgages, on="ID", how="inner")
print(clashed.columns.tolist())
# Income_x, Income_y, Balance_x, Balance_y ... _x is the left table, _y
# the right. It works, but in three months nobody will remember which
# was which, and a typo picks up the wrong column in silence.

# suffixes= replaces them with something you can read:
labelled = loans.merge(mortgages, on="ID", how="inner", suffixes=("_loan", "_mortgage"))
print([c for c in labelled.columns if c.endswith(("_loan", "_mortgage"))])

print(labelled[["ID", "Income_loan", "Income_mortgage"]].head(3))
# The two incomes disagree, which is exactly the sort of thing a merge
# is good at exposing. Better to carry both and look than to assume.

# Often you do not want the duplicates at all. Take only the columns you
# need from the right-hand table and the clash never happens:
tidy = loans.merge(mortgages[["ID", "Term"]], on="ID", how="left", suffixes=("", "_mortgage"))
print(tidy.columns.tolist())


# ---------------------------------------------------------------------
# 8. Duplicate keys make rows multiply
# ---------------------------------------------------------------------
# This is the one that catches people out. merge pairs up EVERY matching
# combination. If a key appears twice on the right, each left row that
# matches it comes back twice.
contacts = pd.DataFrame({
    "ID": [567, 567, 1259],          # 567 has two contact records
    "contact": ["email", "phone", "email"],
})

three_customers = customers.head(3)
print(len(three_customers), "customers,", len(contacts), "contact rows")

multiplied = three_customers.merge(contacts, on="ID", how="left")
print(multiplied)
print("result rows:", len(multiplied))     # 4, from 3 customers

# Customer 567 now appears twice. Nothing is wrong with the data and
# nothing is wrong with pandas: two contact records genuinely means two
# rows. The damage is done further downstream, when somebody sums Income
# on this table and double-counts that customer's salary.
print("income summed on the merged table:", multiplied["Income"].sum())
print("income summed on the original:   ", three_customers["Income"].sum())

# If both sides have the key twice you get four rows for it, and the
# growth gets out of hand quickly. Two habits protect you:
#   1. check len() before and after, as in section 5
#   2. check the right-hand table for repeats before merging
print(contacts["ID"].duplicated().sum(), "duplicate keys in contacts")

# validate= makes pandas enforce what you believe and raise if it is not
# true. Far better than finding out from a wrong total:
try:
    three_customers.merge(contacts, on="ID", validate="one_to_one")
except pd.errors.MergeError as err:
    print("validate=one_to_one ->", err)
# Use validate="one_to_many" when you expect the multiplying, and
# "one_to_one" when you do not.


# ---------------------------------------------------------------------
# 9. join - the shortcut when the key is the index
# ---------------------------------------------------------------------
# df.join(other) matches on the INDEX rather than on a column. It is
# merge with different defaults: less typing when your tables are
# already indexed by the key, and it defaults to how="left".
accounts = pd.read_csv("data/business_account.csv", index_col=0)

left_side = loans.set_index("ID")
right_side = accounts.set_index("ID")

joined = left_side.join(right_side)
print(joined.head(3))
print(len(left_side), "->", len(joined))     # left join, count unchanged

# The same result via merge, spelled out in full:
same = loans.merge(accounts, on="ID", how="left")
print(same.shape)

# Which to use: join when both tables are already indexed by the key and
# you want the brevity, merge everywhere else. merge is more explicit
# about what it is matching, and being explicit is worth a few extra
# characters when somebody else has to read your code.
# join also takes on= to match the left table's COLUMN against the right
# table's index, which covers the common half-way case:
print(loans.join(right_side, on="ID").shape)


# ---------------------------------------------------------------------
# 10. THE POINT
# ---------------------------------------------------------------------
# concat stacks tables that are already the same shape. merge matches
# them up on a key and how= decides who survives. join is merge for
# indexes. The tools are simple; the care goes into the checking. Look
# at the row count before and the row count after, every time, and you
# will catch the silent mistakes that make totals wrong.
