# ======================================================================
# TASKS - 02 Introduction to Python Basics
#
# Converted from the delegate notebook '02_Introduction_to_Python_Basics.ipynb' for use in PyCharm.
# Data files are loaded from a 'data' folder next to this file: copy the
# 'data' folder that sits beside the delegate notebooks so it is alongside
# this script before running it.
# Solutions: solutions/02_Introduction_to_Python_Basics_solutions.py
# ======================================================================

# # Introduction to Python Basics Exercises
#
# In this quick tutorial, you'll learn the absolute basics:
#
#   * **Variables**: How to store information.
#   * **Data Types**: The different kinds of information.
#   * **Basic Maths Operations**: How to perform simple calculations.
#
# To run a code cell like the ones below, just press `Shift + Enter`.
#
# ## Part 1: Variables and Input
#
# Think of a **variable** as a labeled box where you can store information.
#
# We can store a name and an age like this.

# **Task: Modify the values**

# We use the '=' sign to assign a value to a variable.
# Text data (called a "string") needs to be in quotes.
name = "Alex"

# Number data (called an "integer") doesn't need quotes.
age = 35

# The print() function displays the value of the variable.
print(name)
print(age)

# ### Task: Multiply age by 12 to get months (variables are case-senstive)

# Code Here

# ### Getting User Input
#
# What if we want to ask the user for their name and age? We can use the `input()` function. It shows the user a message and waits for them to type something.

# Ask the user for their name and store it in a new variable.
user_name = input("What is your name? ")

# Ask for their age.
user_age = input("How old are you? ")

# Print a friendly message using the variables.
# The 'f' before the string lets us put variables directly inside {}
print(f"Hello, {user_name}! It's nice to meet you.")
print(f"You are {user_age} years old.")

# ### Task : Multiply user_age by 365 to get age in days

#Code here

# ## What happened?

# ## Part 2: Data Types
#
# In Python, every piece of data has a "type." The most common ones are:
#
#   * `str` (string): Plain text, like `"Hello"` or `"Alex"`.
#   * `int` (integer): A whole number, like `10` or `42`.
#   * `float` (float): A number with a decimal point, like `3.14`.
#
# **Important:** The `input()` function *always* gives us back a string (`str`), even if you type in a number\! We can check the type of a variable with the `type()` function.

# ### Changing a Data Type (Type Casting)
#
# If we want to do math with the user's age, we first need to change its type from a string to an integer. This is called **type casting**. We can change types using functions like `int()`, `str()`, and `float()`.
#
# Let's convert `user_age` to an integer.

# Take the string value in user_age and convert it to an integer.
# We store the result in a new variable.
age_as_number = int(user_age)

# Now let's check the type of our new variable.
# It should be <class 'int'>.
print(type(age_as_number))

# Now we can do math with it! Let's see how old the user will be in 5 years.
print(f"In 5 years, you will be {age_as_number + 5} years old!")

# ### A Special Operator: Modulo `%`
#
# The **modulo** operator (`%`) might be new to you. It doesn't give you the result of a division; instead, it gives you the **remainder**.
#
# For example, `15 / 4` is 3 with a remainder of 3. So, `15 % 4` is `3`.
#
# This is super useful for figuring out if a number is even or odd. If a number divided by 2 has a remainder of 0, it's even\!

# Let's find the remainder of 15 divided by 4.
remainder = 15 % 4
print(f"The remainder of 15 / 4 is: {remainder}")

# Now let's check if a number is even or odd.
number_to_check = 20
remainder_after_dividing_by_2 = number_to_check % 2
print(f"The remainder of {number_to_check} / 2 is: {remainder_after_dividing_by_2}")

# Let's try an odd number.
number_to_check = 21
remainder_after_dividing_by_2 = number_to_check % 2
print(f"The remainder of {number_to_check} / 2 is: {remainder_after_dividing_by_2}")

# ### Task: Is the number 679 a PRIME NUMBER?

#Code here

# This is the foundation for almost everything you'll do in Python.
# Keep experimenting! We have so far done:
#
#   * Create **variables** to store data.
#   * Use `input()` to get information from a user.
#   * Understand the difference between **data types** like `str` and `int`.
#   * Change a variable's data type.
#   * Perform **basic math**, including division (`/`) and finding the remainder (`%`).
