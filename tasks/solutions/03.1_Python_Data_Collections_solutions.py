# ======================================================================
# SOLUTIONS - 03.1 Python Data Collections
#
# Data files are loaded from a 'data' folder next to the tasks file: run
# with the working directory set to a folder containing that 'data' folder.
# The solutions build on each other in order; run the file top to bottom.
# ======================================================================

# ----------------------------------------------------------------
# Solution is in cell below. Only open to check your work
# ----------------------------------------------------------------
# 1. Create the list 'inventory'
inventory = ["apple", 3, True, 45.99]

# 2. Print the entire list
print(f"Inventory list: {inventory}")

# 3. Access and print the third item (index 2)
print(f"Third item (index 2): {inventory[2]}")

# 4. Print the length
print(f"Length of inventory: {len(inventory)}")

# ----------------------------------------------------------------
# Exercise 1.2: Modifying a List
# ----------------------------------------------------------------
# The list from the previous exercise: inventory = ["apple", 3, True, 45.99]

# 1. Append "banana"
inventory.append("banana")

# 2. Change the first item (index 0)
inventory[0] = "orange"

# 3. Insert 100 at index 1
inventory.insert(1, 100)

# 4. Print the final list
print(f"Modified inventory list: {inventory}")

# ----------------------------------------------------------------
# Exercise 2.1: Tuple Construction and the tale of two cities
# ----------------------------------------------------------------
# 1. Create the tuple 'coordinates'
coordinates = ('41.89 N', '12.48 E')

#2. Save them as latitude and longitude
latitude, longitude = coordinates

# 2. Print the longitude
print(f"Longitude: {longitude}")

# ----------------------------------------------------------------
# 2.2 Data Collection Type Conversion
# ----------------------------------------------------------------
# 1. Attempt to modify (This should produce an error!)
# coordinates[0] = '-87.63 W'
# print(coordinates) # Do not run this line unless you want to see the error.
print("Attempt to modify the tuple was commented out because tuples are immutable.")
l_coords = list(coordinates)
l_coords[1] = '-87.63 W'
l_coords = tuple(l_coords)
print(type(l_coords))
print(f'{l_coords}')

# ----------------------------------------------------------------
# Exercise 3.1: Dictionary Construction and Access
# ----------------------------------------------------------------
# 1. Create the dictionary 'user_profile'
user_profile = {
    'name': 'Alice',
    'city': 'New York',
    'orderID': [100123, 100394]
}

# 2. Print the entire dictionary
print(f"User Profile: {user_profile}")

# 3. Access and print 'city'
print(f"Alice's city: {user_profile['city']}")

# Access and print 'Alice's 2nd orderID
print(f"Alice's 2nd orderID: {user_profile['orderID'][1]}")

# ----------------------------------------------------------------
# Exercise 3.2: Modifying a Dictionary
# ----------------------------------------------------------------
# The dictionary from the previous exercise: user_profile = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 1. Add a new key-value pair
user_profile['is_active'] = True

# 2. Change the value for 'Albany'
user_profile['city'] = 'Albany'

# 3. Print all keys
print(f"All keys: {user_profile.keys()}")

# 4. Print all values
print(f"All values: {user_profile.values()}")

# Print the final dictionary
print(f"Updated User Profile: {user_profile}")

# ----------------------------------------------------------------
# Advanced Challenge (Optional)
# ----------------------------------------------------------------
#1
import json
import numpy as np

with open('data/weather.json', 'r') as f:
    weather_data = json.load(f)
print(weather_data)

#2
print(weather_data['columns'])

#3 A more streamlined approach is possible
tmp=[]
for i in weather_data['data']:
  tmp.append(i[0])
np.mean(tmp)
