# ======================================================================
# TASKS - 04 Maths Ops with Numpy Arrays
#
# Converted from the delegate notebook '04_Maths_Ops_with_Numpy_Arrays.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/04_Maths_Ops_with_Numpy_Arrays_solutions.py
# ======================================================================

# # Python NumPy Numerical Arrays Exercises
#
# This notebook provides exercises on creating and manipulating NumPy arrays, formatted for easy use in environments like Google Colab. It covers nd-array attributes, `arange`, `dtype` conversion, broadcasting, slicing, filtering, and mathematical methods.
#
# ## NumPy Arrays Reference Table
#
# | Concept | Purpose | Syntax/Keywords | Common Use Case |
# |:----------:|:---------:|:--------:|:-------------------:|
# | **`ndarray` Creation** | Create N-dimensional arrays. | `np.array()`, `np.arange()` | Storing and manipulating homogeneous numerical data. |
# | **Array Attributes** | Inspect array properties. | `.shape`, `.dtype`, `.ndim` | Understanding the structure and type of your data. |
# | **Broadcasting** | Perform operations between arrays of different shapes. | `+`, `-`, `*`, `/` | Applying an operation with a scalar to an entire array. |
# | **Slicing & Filtering**| Select subsets of array data. | `[start:stop]`, `[boolean_mask]` | Data extraction and selection based on conditions. |
# | **Math Methods**| Perform mathematical and statistical computations. | `.sum()`, `.mean()`, `.max()`, `.min()` | Aggregating data and performing statistical analysis. |
#
# ## Part 1: nd-arrays and their attributes
#
# The core of NumPy is the `ndarray` object, a powerful N-dimensional array. You can inspect its properties like shape, dimensions, and data type.
#
# ### Exercise 1.1: Creating and Inspecting an Array
#
# 1. Import the `numpy` library and alias it as `np`.
# 2. Create a Python list of lists: `[[10, 20, 30], [40, 50, 60]]`.
# 3. Convert this list into a NumPy array named `my_matrix`.
# 4. Print the array itself.
# 5. Print the array's shape (`.shape`), number of dimensions (`.ndim`), and data type (`.dtype`).

# >>> Your code here

# ## Part 2: `arange` and Changing `dtype`
#
# NumPy provides convenient functions like `np.arange()` to create arrays with sequences of numbers. You can also explicitly control the data type (`dtype`) of an array.
#
# ### Exercise 2.1: Creating an Array with `arange` and Changing its `dtype`
#
# 1. Use `np.arange()` to create an array named `int_array` containing integers from 5 to 15 (inclusive).
# 2. Print the `int_array` and its `dtype`.
# 3. Create a new array named `float_array` by converting `int_array` to the `float64` data type using the `.astype()` method.
# 4. Print the `float_array` and its `dtype`.

# >>> Your code here

# ## Part 3: Broadcasting and Element-wise Operations
#
# Broadcasting allows NumPy to perform operations on arrays of different shapes. The most common case is operating between an array and a scalar (a single number).
#
# ### Exercise 3.1: Broadcasting and Element-wise Operations
#
# 1. Create an array `arr1` with the values `[5, 10, 15]`.
# 2. Create a second array `arr2` with the values `[1, 2, 3]`.
# 3. **Broadcasting**: Add `100` to every element in `arr1` and print the result.
# 4. **Element-wise Operation**: Multiply `arr1` by `arr2` and print the result.

# >>> Your code here

# ## Part 4: Slicing and Filtering
#
# You can select subsets of data from an array using slicing or filter data based on conditions (boolean masking).
#
# ### Exercise 4.1: Slicing and Boolean Filtering
#
# 1. Create a 1D NumPy array named `data` with integers from 0 to 10.
# 2. **Slicing**: Use slicing to select and print the elements from index 3 up to (but not including) index 8.
# 3. **Filtering**: Create a boolean mask to find all elements in `data` that are greater than 5.
# 4. Use the boolean mask to select and print only those elements.

# Remember to add coding cells

# ## Part 5: Maths and Statistical Methods
#
# NumPy arrays have a wide range of built-in mathematical and statistical methods for performing aggregate calculations.
#
# ### Exercise 5.1: Basic Statistical Methods
#
# 1. Create a 2D array (3x4 matrix) with the numbers from 1 to 12. Use `array.reshape(rows, columns)`
# 2. Calculate and print the sum of all elements in the array using the `.sum()` method.
# 3. Calculate and print the mean (average) of all elements using the `.mean()` method.
# 4. Find and print the maximum value in the array using the `.max()` method.

# >>> Your code here

# ### **Advanced**:
# ## Part 6: Maths and Statistical Methods
#
# NumPy arrays have a wide range of built-in mathematical and statistical methods for performing aggregate calculations.
#
# ### Exercise 6.1: Basic Statistical Methods from loading data
#
# 1. Generate a normally distributed dataset of the heights of women in the UK, we only know the following descriptive statistics to have a `mean` of 165cm with an `standard deviation` of 7.5cm
# 2. Use `np.random.randn` to generate a sample of 200 from a standard normal distribution.
# 3. **Advanced** - place this normal distribution generator in a **user-defined function** based on `np.random.randn`

# >>> Your code here

# Calculate the min, max and interquartile range of the data to answer the question:
#
# *"Is this the best way to generate synthetic data for expectedly normal distributions? What possible improvements could be made when generating the data?"*

# >>> Your code here
