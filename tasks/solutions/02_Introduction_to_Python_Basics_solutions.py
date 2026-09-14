# ======================================================================
# SOLUTIONS - 02 Introduction to Python Basics
#
# The delegate notebook does not include solutions, so these were written
# to match the style of the other modules. The notebook uses input() to
# ask for a name and an age; fixed example values are used here so the
# code runs without waiting for keyboard input.
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Task: Modify the values
# ----------------------------------------------------------------
# Assign your own values to the variables and print them.
name = "Sam"      # a string, so it needs quotes
age = 42          # an integer, no quotes needed

print(name)
print(age)

# ----------------------------------------------------------------
# Task: Multiply age by 12 to get months (variables are case-sensitive)
# ----------------------------------------------------------------
# 'age' holds an integer, so we can do maths with it directly.
age_in_months = age * 12
print(f"{age} years is {age_in_months} months")

# ----------------------------------------------------------------
# Task: Multiply user_age by 365 to get age in days
# ----------------------------------------------------------------
# In the notebook these values come from input():
#   user_name = input("What is your name? ")
#   user_age = input("How old are you? ")
user_name = "Sam"
user_age = "42"

print(f"Hello, {user_name}! It's nice to meet you.")
print(f"You are {user_age} years old.")

# What happened?
# input() ALWAYS returns a string, so multiplying user_age by 365 does not
# do arithmetic - it repeats the string 365 times!
# Uncomment the line below to see the (very long) result:
# print(user_age * 365)

# To get the age in days we must first convert the string to an integer
# (type casting), then multiply.
age_in_days = int(user_age) * 365
print(f"You are roughly {age_in_days} days old.")

# ----------------------------------------------------------------
# Task: Is the number 679 a PRIME NUMBER?
# ----------------------------------------------------------------
# A prime number is only divisible by 1 and itself. The modulo operator (%)
# gives the remainder of a division, so if number % divisor == 0 the divisor
# divides the number exactly.
number_to_check = 679

is_prime = True
for divisor in range(2, number_to_check):
    if number_to_check % divisor == 0:
        # We found an exact divisor, so the number is not prime.
        print(f"{number_to_check} is divisible by {divisor} ({divisor} x {number_to_check // divisor})")
        is_prime = False
        break

if is_prime:
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is NOT a prime number.")

# 679 = 7 x 97, so it is not prime.
