# ======================================================================
# SOLUTIONS - 04 Maths Ops with Numpy Arrays
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Exercise 1.1: Creating and Inspecting an Array
# ----------------------------------------------------------------
# 1. Import numpy
import numpy as np

# 2. Create the list
data = [[10, 20, 30], [40, 50, 60]]

# 3. Convert to a NumPy array
my_matrix = np.array(data)

# 4. Print the array
print(f"The array is:\n{my_matrix}")

# 5. Print attributes
print(f"Shape: {my_matrix.shape}")
print(f"Dimensions: {my_matrix.ndim}")
print(f"Data Type: {my_matrix.dtype}")

# ----------------------------------------------------------------
# Exercise 2.1: Creating an Array with `arange` and Changing its `dtype`
# ----------------------------------------------------------------
import numpy as np

# 1. Create an integer array with arange
int_array = np.arange(5, 16)

# 2. Print the integer array and its type
print(f"Integer Array: {int_array}")
print(f"Integer Dtype: {int_array.dtype}")

# 3. Create a new float array using astype
float_array = int_array.astype(np.float64)

# 4. Print the float array and its type
print(f"Float Array: {float_array}")
print(f"Float Dtype: {float_array.dtype}")

# ----------------------------------------------------------------
# Exercise 3.1: Broadcasting and Element-wise Operations
# ----------------------------------------------------------------
import numpy as np

# 1. & 2. Create arrays
arr1 = np.array([5, 10, 15])
arr2 = np.array([1, 2, 3])

# 3. Add 100 to arr1 (broadcasting)
result_broadcast = arr1 + 100
print(f"Broadcasting result (arr1 + 100): {result_broadcast}")

# 4. Multiply arr1 and arr2 (element-wise)
result_elementwise = arr1 * arr2
print(f"Element-wise result (arr1 * arr2): {result_elementwise}")

# ----------------------------------------------------------------
# Exercise 4.1: Slicing and Boolean Filtering
# ----------------------------------------------------------------
import numpy as np

# 1. Create the array
data = np.arange(11)
print(f"Original array: {data}")

# 2. Slice the array
sliced_data = data[3:8]
print(f"Sliced data (index 3 to 8): {sliced_data}")

# 3. Create a boolean mask
mask = data > 5

# 4. Apply the mask to filter the data
filtered_data = data[mask]
print(f"Filtered data (> 5): {filtered_data}")

# ----------------------------------------------------------------
# Exercise 5.1: Basic Statistical Methods
# ----------------------------------------------------------------
import numpy as np

# 1. Create the 2D array
# np.arange(1, 13) creates numbers 1-12
# .reshape(3, 4) turns it into a 3x4 matrix
matrix = np.arange(1, 13).reshape(3, 4)
print(f"The matrix is:\n{matrix}")

# 2. Calculate the total sum
total_sum = matrix.sum()
print(f"Sum of all elements: {total_sum}")

# 3. Calculate the mean
total_mean = matrix.mean()
print(f"Mean of all elements: {total_mean}")

# 4. Find the maximum value
max_value = matrix.max()
print(f"Maximum value: {max_value}")

# ----------------------------------------------------------------
# Exercise 6.1: Basic Statistical Methods from loading data
# ----------------------------------------------------------------
def generate_random_data(mean, std_dev, num_samples=100):
  """
  Generates a dataset using np.random.randn with a specified mean and standard deviation.

  Args:
    mean: The desired mean of the dataset.
    std_dev: The desired standard deviation of the dataset.
    num_samples: The number of samples to generate (default is 100).

  Returns:
    A NumPy array containing the generated data.
  """
  data = np.random.randn(num_samples) * std_dev + mean
  return data

# Call the function. In the notebook this call sat inside the function body after
# 'return', so it never ran; it is moved out here and uses the values from the
# exercise brief (mean 165 cm, standard deviation 7.5 cm, 200 samples).
uk_w_heights = generate_random_data(mean=165, std_dev=7.5, num_samples=200)

# ----------------------------------------------------------------
# Exercise 6.1: Basic Statistical Methods from loading data
# ----------------------------------------------------------------
# Calculate the Variance and the interquartile range, ignoring NaN values
min_value = np.min(uk_w_heights)
max_value = np.max(uk_w_heights)
q75, q25 = np.percentile(uk_w_heights, [75 ,25])
iqr_data = q75 - q25

print(f"min value: {min_value}")
print(f"max value: {max_value}")
print(f"Interquartile range of the data: {iqr_data}")
