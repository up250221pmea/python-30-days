# 1. Declare your age as integer variable
age = 25
# 2. Declare your height as a float variable
height = 1.75
# 3. Declare a variable that stores a complex number
complex_number = 3 + 4j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height_triangle

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter_triangle = side_a + side_b + side_c

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * radius ** 2
circumference_circle = 2 * 3.14 * radius

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2

y_intercept = b
x_intercept = -b / m

print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
from math import sqrt

import math.sqrt
x1 = 2
y1 = 2

x2 = 6
y2 = 10

slope = (y2 - y1) / (x2 - x1)

distance = sqrt((x2-x1)**2 + (y2-y1)**2)

print("Slope:", slope)
print("Distance:", distance)
# Compare the slopes in tasks 8 and 9.
slope1 = 2
slope2 = 4/2

print(slope1 == slope2)
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3

y = x**2 + 6*x + 9

print(y)
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
python_word = "python"
dragon_word = "dragon"

print(len(python_word))
print(len(dragon_word))

print(len(python_word) == len(dragon_word))
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
# There is no 'on' in both dragon and python
print("on" in python_word and "on" in dragon_word)
# Find the length of the text python and convert the value to float and convert it to string
python_length = len(python_word)
python_length_float = float(python_length)
python_length_string = str(python_length_float)
print(python_length_string)
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
print(number % 2 == 0)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))
# Check if type of '10' is equal to type of 10
print(type('10') == type(10))
# Check if int('9.8') is equal to 10
print(int('9.8') == 10)
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
horas = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = horas * rate_per_hour
print("Pay:", pay)
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years: "))
seconds_in_year = 365 * 24 * 60 * 60
seconds_lived = years * seconds_in_year
print("Seconds lived:", seconds_lived)  

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("1 1 1 1 1")
print("2 1 2 4 8")  
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")  