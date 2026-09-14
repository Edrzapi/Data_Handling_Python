# ======================================================================
# TASKS - 03.1 Python Data Collections
#
# Converted from the delegate notebook '03.1_Python_Data_Collections.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/03.1_Python_Data_Collections_solutions.py
# ======================================================================

# ## Python Collections Reference Table
#
# | Collection | Data Type | Mutable? | Construction Syntax | Common Methods (Examples) |
# |:----------:|:---------:|:--------:|:-------------------:|:-------------------------:|
# | **List** | `list`    | Yes      | `[item1, item2, ...]` | `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `index()`, `len()` |
# | **Tuple** | `tuple`   | No       | `(item1, item2, ...)` | `count()`, `index()`, `len()` |
# | **Dictionary**| `dict` | Yes      | `{key: value, ...}` | `keys()`, `values()`, `items()`, `get()`, `pop()`, `update()`, `len()` |
#
# ## Part 1: Lists (The flexible Collection)
#
# Lists are ordered, mutable sequences that can contain items of different data types.
#
# ### Exercise 1.1: List Construction and Access
#
# 1.  Create a list named `inventory` containing the following items (in order): `apple`, `3`, `True`, `45.99`.
# 2.  Print the entire `inventory` list.
# 3.  Access and print the third item in the list (remember Python's zero-based indexing).
# 4.  Print the length of the list using the `len()` function.
# 5. **Advanced**: attempt to use notation: `print(f'This is the value: {variable}')`

# >>> Your code here

# The solution for this exercise is in the solutions file.

# ### Exercise 1.2: Modifying a List
#
# 1.  Use the `append()` method to add the string `"banana"` to the end of the `inventory` list.
# 2.  Change the first item in the list (`"apple"`) to `"orange"`.
# 3.  Use the `insert()` method to add the integer `100` at index 1.
# 4.  Print the final, modified `inventory` list.

# >>> Your code here

# ## Part 2: Tuples (The Immutable Collection)
#
# Tuples are ordered, **immutable** sequences. Once created, their contents cannot be changed. They are often used for data that shouldn't be altered.
#
# ### Exercise 2.1: Tuple Construction and the tale of two cities
#
# 1.  Create a tuple named `coordinates` with the values for latitude(1st) and longitude(2nd): `('41.89 N', '12.48 E')`.
# 2. Label them `latitude` and `longitude`
# 2. Print the value for `longitude`.

# >>> Your code here

# ### 2.2 Data Collection Type Conversion
#
# It's common to need to convert one collection type to another. The built-in functions `list()`, `tuple()`, and `dict()` handle these conversions.
#
# 1.  **Attempt** to change the Longitude to `-87.63 W`. Observe the error.
# 2. To do this successfully, convert tuple into another data collection and change first item. to `-87.63 W`

# >>> Your code here

# ## Part 3: Dictionaries (The Key-Value Collection)
#
# Dictionaries are unordered (as of Python 3.7+ they maintain insertion order), mutable collections of **key-value** pairs. Keys must be unique and immutable (like strings, numbers, or tuples).
#
# ### Exercise 3.1: Dictionary Construction and Access
#
# 1.  Create a dictionary named `user_profile` with the following key-value pairs:
#       * `'name'`: `'Alice'` (string)
#       * `'city'`: `'New York'` (string)
#       * `'orderID'`: `[100123, 100394]` (int)
#
# 2.  Print the entire `user_profile` dictionary.
# 3.  Access and print the value associated with the key `'age'`.
# 4. Access and print the 2nd value of the orderID `'orderID'`.

# >>> Your code here

# ### Exercise 3.2: Modifying a Dictionary
#
# 1.  Add a new key-value pair to `user_profile`: `'is_active'` with the boolean value `True`.
# 2.  Change the value of the key `'city'` to `Albany`.
# 3.  Use the `keys()` method to print a list of all keys in the dictionary.
# 4.  Use the `values()` method to print a list of all values in the dictionary.

# >>> Your code here

# ## **Advanced Challenge** (Optional)
#
# 1. Load in the JSON file `weather.json`. Feel free to the `json` package for loading data into dictionary.
#
# 2. What columns are represented here?
#
# 3. What's the average temperature in this dataset?

# >>> Your code here
