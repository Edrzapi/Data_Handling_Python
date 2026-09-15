# ======================================================================
# SOLUTIONS - 03.2 Python Flow Control, Functions and File Handling
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Exercise 1.1: Basic Conditional Statement
# ----------------------------------------------------------------
# 1. Create the list
permissions = ['read', 'write', 'execute']

# 2. Set the action
user_action = 'write' # Try changing this to 'delete' later

# 3. and 4. Write the conditional
if user_action in permissions:
    print(f"Permission granted for {user_action}!")
else:
    print("Permission denied.")

# ----------------------------------------------------------------
# Exercise 1.2: Advanced Conditional (`elif`)
# ----------------------------------------------------------------
# 1. Set the score
score = 85

# 2. Write the conditional structure
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ----------------------------------------------------------------
# 2.1 - Loops using Counter to break
# ----------------------------------------------------------------
# 1. Initialize counter
counter = 5

# 2. and 3. Use a while loop and print
while counter > 0:
    print(f"Counting down: {counter}")
    # 4. Decrease the counter by 1 (below is shorthand for 'counter = counter - 1')
    counter -= 1

# 5. Final message
print("Countdown finished!")

# ----------------------------------------------------------------
# Exercise 2.1: `for` Loop and Iteration
# ----------------------------------------------------------------
# 1. Create the list
items_to_process = ['data1', 'data2', 'error', 'data3']

# 2. and 3. Use a for loop with break
for item in items_to_process:
    print(f"Processing {item}...")
    if item == 'error':
        print("Critical error found. Stopping process.")
        break

print("Loop finished.")

# ----------------------------------------------------------------
# Exercise 3.1: Simple Function with a `return` Value
# ----------------------------------------------------------------
# 1. Define the function
def bill_withtax(bill, tax_rate):
    """Calculates the total bill with tax."""
    # 2. Calculate the total
    total = bill * tax_rate
    # 3. Return the total
    return total

# 4. Call the function
total_bill = bill_withtax(1786, 1.2)
print(f"The total_bill is: {total_bill}")

# ----------------------------------------------------------------
# Exercise 3.2: Function with Conversion
# ----------------------------------------------------------------
# 1. Define the function
def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    # 2. Calculate Celsius
    celsius = (fahrenheit - 32) * 5/9
    # 3. Return Celsius
    return celsius

# 4. Call the function and print, rounded to one decimal place
fahrenheit_temp = 32
celsius_result = round(fahrenheit_to_celsius(fahrenheit_temp), 1)
print(f"{fahrenheit_temp}F is {celsius_result}C")

# ----------------------------------------------------------------
# Exercise 3.3: Handling Errors with `try`/`except`
# ----------------------------------------------------------------
# 1. and 2. Define divide() with try/except
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # 3. Return a message rather than crashing
        return "Cannot divide by zero"


# 4. Test both paths
print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Cannot divide by zero


# 5. and 6. Define read_file_safely() with try/except
def read_file_safely(filename):
    try:
        f = open(filename, 'r')
        contents = f.read()
        f.close()
        return contents
    except FileNotFoundError:
        # 7. Return a message rather than the raw traceback
        return "File not found."


# 8. Same function, two filenames - one exists, one does not
print(read_file_safely('data/data.txt'))
print(read_file_safely('data/no_such_file.txt'))

# ----------------------------------------------------------------
# Advanced: Function with Conditional Logic
# ----------------------------------------------------------------
# 1. Define the function
def get_status(data):
    """Checks the status field of a dictionary."""
    status_value = data.get('status', 'unknown') # Use .get() for safe access
    # 2., 3., and 4. Use conditional logic
    if status_value == 'complete':
        return "Task is finished."
    else:
        return "Task is pending."

# 5. Test the function
task1 = {'name': 'report', 'status': 'complete'}
task2 = {'name': 'review', 'status': 'in_progress'}

print(f"Task 1 status: {get_status(task1)}")
print(f"Task 2 status: {get_status(task2)}")

# ----------------------------------------------------------------
# Exercise 4.1: Writing to a File
# ----------------------------------------------------------------
# 1. Define the content
file_content = "Hello Python World!\nThis is line two."
print(file_content)
# 2. and 3. Open in write mode and write content
f = open('output.txt', 'w')
f.write(file_content)

# ----------------------------------------------------------------
# Exercise 4.2: Reading from a File
# ----------------------------------------------------------------
# 1. and 2. Open in read mode and read content
f = open('output.txt', 'r')  # stray colon removed (syntax error in the notebook solution)
read_data = f.read()

print(read_data)
