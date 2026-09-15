# ======================================================================
# TASKS - 03.2 Python Flow Control, Functions and File Handling
#
# Converted from the delegate notebook '03.2_Python_Flow_Control,_Functions_and_File_Handling.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/03.2_Python_Flow_Control,_Functions_and_File_Handling_solutions.py
# ======================================================================

# ## Python Flow Control, Functions, and File Handling Exercises
#
# Here is a Python notebook, formatted for easy export and use in environments like Google Colab, covering exercises on flow control, user-defined functions, and file handling.
#
# ## Python Control Flow & Functions Reference Table
#
# | Concept | Purpose | Syntax/Keywords | Common Use Case |
# |:----------:|:---------:|:--------:|:-------------------:|
# | **Conditionals** | Execute code blocks based on conditions. | `if`, `else`, `elif`, `in` | Decision-making logic (e.g., checking user age). |
# | **Loops** | Repeat a block of code multiple times. | `for`, `while`, `break` | Iterating over collections or repeating a task until a condition is met. |
# | **Functions**| Group reusable code blocks. | `def`, `return` | Organizing code and preventing redundancy (DRY principle). |
#
# ## Part 1: Conditional Logic (`if`/`else`/`elif`/`in`)
#
# Conditional statements allow your program to make decisions. The `in` keyword is useful for checking membership in a collection (like a list or string).
#
# ### Exercise 1.1: Basic Conditional Statement
#
# 1.  Create a list named `permissions` containing the strings: `['read', 'write', 'execute']`.
# 2.  Create a string variable `user_action` and set it to `'write'`.
# 3.  Write an `if` statement using the `in` keyword to check if `user_action` is in the `permissions` list.
# 4.  If it is, use: `print(f"Permission granted for {user_action}!)"`
# 5.  If it is not, print: `"Permission denied."`

# >>> Your code here

# ### Exercise 1.2: Advanced Conditional (`elif`)
#
# 1.  Create an integer variable `score` and set it to `85`.
# 2.  Write a conditional structure that checks the score and prints the corresponding grade:
#       * If `score >= 90`, print: `"Grade: A"`
#       * Else if `score >= 80`, print: `"Grade: B"`
#       * Else if `score >= 70`, print: `"Grade: C"`
#       * Else, print: `"Grade: F"`

# >>> Your code here

# ## Part 2: `while` Loop
# ### 2.1 - Loops using Counter to break
# 1.  Save a variable `counter` to `5`.
# 2.  Use a **`while`** loop that continues as long as `counter` is greater than `0`.
# 3.  Inside the loop, print the current value of `counter`.
# 4.  Lower the `counter` by `1` in each iteration.
# 5.  After the loop finishes, print: `"Countdown finished!"`

# >>> Your code here

# ## ADVANCED
# ### 2.2: Loops using (`while`/`break`)
#
# Loops are used to iterate over collections or repeat a block of code multiple times.
#
# ### Exercise 2.1: `for` Loop and Iteration
#
# 1.  Create a list named `items_to_process` with elements: `['data1', 'data2', 'error', 'data3']`.
# 2.  Use a `for` loop to iterate through the `items_to_process` list.
# 3.  Inside the loop, print the message: `"Processing [item]..."` for each item.
# 4.  If the item is `'error'`, use the **`break`** keyword to immediately stop the loop and print: `"Critical error found. Stopping process."`

# >>> Your code here

# ## Part 3: User-Defined Functions
#
# Functions are defined blocks of reusable code. The `def` keyword is used to create a function, and `return` is used to output a value.
#
# ### Exercise 3.1: Simple Function with a `return` Value
#
# 1.  Define a function named `tax_calculator` that takes two parameters: `bill` and `tax_rate`.
# 2.  Inside the function, calculate the total amount owed (`bill * tax_rate`).
# 3.  The function should **`return`** the calculated total.
# 4.  Call the function with `bill=1786` and `tax_rate=1.2` and print the result.

# >>> Your code here

# ### Exercise 3.2: Function with Conversion
#
# 1. Define a function named `fahrenheit_to_celsius` that takes one parameter: `fahrenheit`.
# 2. Inside the function, calculate the Celsius equivalent using the formula: `(fahrenheit - 32) * 5/9`.
# 3. The function should **`return`** the calculated Celsius temperature.
# 4. Call the function with a Fahrenheit temperature (e.g., `32`) and print the result, rounded to one decimal place.

# >>> Your code here

# ### Exercise 3.3: Handling Errors with `try`/`except`
#
# So far, a bad input has crashed the program. `try`/`except` lets you catch a
# specific error and carry on instead. (Other languages call this `try`/`catch`;
# Python's keyword is `except`.)
#
# ```
# try:
#     risky_thing()
# except SomeErrorType:
#     handle_it_instead()
# ```
#
# **Part 1: a calculator that survives division by zero**
#
# 1.  Define a function named `divide` that takes two parameters: `a` and `b`.
# 2.  Inside the function, `return a / b` - but wrap it in a `try`/`except` that
#     catches `ZeroDivisionError`.
# 3.  When `b` is `0`, return the string `"Cannot divide by zero"` instead of
#     letting the program crash.
# 4.  Test it with `divide(10, 2)` and `divide(10, 0)`.
#
# **Part 2: opening a file that might not be there**
#
# 5.  Define a function named `read_file_safely` that takes one parameter:
#     `filename`.
# 6.  Inside the function, `open()` the file and `read()` it - wrapped in a
#     `try`/`except` that catches `FileNotFoundError`.
# 7.  On success, return the file's contents. On failure, return the string
#     `"File not found."` instead of the raw traceback.
# 8.  Test it with `'data/data.txt'` (which exists) and
#     `'data/no_such_file.txt'` (which does not), changing nothing but the
#     filename.

# >>> Your code here

# ### **Advanced**: Function with Conditional Logic
#
# 1.  Define a function named `get_status` that takes one parameter: `data` (which is expected to be a dictionary with a `'status'` key).
# 2.  Inside the function, use conditional logic (`if`/`else`) to check the value of `data['status']`.
# 3.  If the status is `'complete'`, the function should return the string `"Task is finished."`.
# 4.  Otherwise, it should return the string `"Task is pending."`.
# 5.  Test the function with a dictionary: `task1 = {'name': 'report', 'status': 'complete'}`.

# ## Part 4: File Handling (`open`/`read`/`write`)
#
# File handling allows programs to interact with external files. The `with open(...)` construct is best practice as it automatically closes the file.
#
# ### Exercise 4.1: Writing to a File
#
# 1.  Define a string variable `file_content` with the text: `"Hello Python World!\nThis is line two."`.
# 2.  Use the `open()` function to open a file named `output.txt` in **write mode (`'w'`)**.
# 3.  Use the file object's `write()` method to write the `file_content` to the file.

# >>> Your code here

# ### Exercise 4.2: Reading from a File
#
# 1.  Use the `with open()` statement to open the file named `output.txt` (created in the previous exercise) in **read mode (`'r'`)**.
# 2.  Use the file object's **`read()`** method to read the entire contents into a variable named `read_data`.
# 3.  Print the `read_data` variable.

# >>> Your code here

# ### Last note on file handling:
# Python allows use to automate file handling (using os.list)and processing with multiple data that are viewable in their raw unprocessed form.

import os

os.listdir('data')

for file in os.listdir('data'):
  if file.endswith('.json'):
    print(file)
    # Can then open file and process for .json format
