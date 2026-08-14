# Exercise 4 - Main program

# Import the calculator module
from calculator import add, subtract, multiply, divide

number1 = 10
number2 = 5

# Use the functions from calculator.py

addition = add(number1, number2)

subtraction = subtract(number1, number2)

multiplication = multiply(number1, number2)

division = divide(number1, number2)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")