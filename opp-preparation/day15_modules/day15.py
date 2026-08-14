# Modules

# Importing a module

import math

number = 25

print(math.sqrt(number))

# Importing specific functions from a module

from math import sqrt

number = 36

print(sqrt(number))

# Importing multiple functions

from math import sqrt, pow, pi

print(sqrt(49))
print(pow(2, 3))
print(pi)

# Importing a module with an alias

import math as m

number = 64

print(m.sqrt(number))

# Importing a function with an alias

from math import sqrt as square_root

print(square_root(81))

# Creating your own module 

# ? def add(a, b):
# *   return a + b


# ? def subtract(a, b):
# *    return a - b
# ? import operations

# ! print(operations.add(10, 5))
# ! print(operations.subtract(10, 5))
# *Organizing code into modules

"""project/
├── main.py
├── users.py
└── calculations.py"""

# * user.py
"""def create_user(name, age):
    return {
        "name": name,
        "age": age
    }"""

"""calculations.py
def calculate_average(numbers):
    return sum(numbers) / len(numbers)"""

"""main.py
from users import create_user
from calculations import calculate_average

user = create_user("John", 20)

grades = [90, 85, 95]

average = calculate_average(grades)

print(user)
print(f"Average: {average}")"""

# Exercise 1 - Math module

import math 

# 1. Calculate the square root of 81
# 2. Calculate 5 raised to the power of 3
# 3. Print the value of pi

square_root = sqrt(81)

power = pow(5, 3)

pi_value = pi

print(f"Square root: {square_root}")
print(f"Power: {power}")
print(f"Pi: {pi_value}")

# Exercise 2 - Random module

import random


# Generate a random number between 1 and 100

random_number = random.randint(1, 100)

print(f"Random number: {random_number}")

# Exercise 3 - Import a specific function

# Import only the sqrt function from the math module
from math import sqrt as square_root

number = 64

# Calculate the square root of number

result = square_root(number)

print(f"Square root of {number}: {result}")

# Excercise 4

# exercise_4/
# ├── main.py
# └── calculator.py

# Execercise 5 

# exercise_5/
# ├── main.py
# └── users.py

# Execercise 6

# student_manager/
# ├── main.py
# ├── students.py
# └── calculations.py
