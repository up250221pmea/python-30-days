# Day 16 - Scope and Variable Lifetime


# Local scope

def greet():
    message = "Hello"
    print(message)


greet()

# message only exists inside greet()
# print(message)  # NameError


# Local variables

def calculate_total():
    price = 500
    tax = 0.16
    total = price + (price * tax)

    return total


print(calculate_total())


# Example with function parameters

def calculate_final_price(price, discount):
    discounted_price = price - (price * discount)
    tax = discounted_price * 0.16
    total = discounted_price + tax

    return total


print(calculate_final_price(1000, 0.10))


# Global variable

tax_rate = 0.16


def calculate_price(price):
    return price + (price * tax_rate)


print(calculate_price(100))


# Global constants

APP_NAME = "StoreAPI"
VERSION = "1.0"
MAX_CONNECTIONS = 10
DEFAULT_TIMEOUT = 30


def show_info():
    print(APP_NAME)
    print(VERSION)


show_info()


# Local and global variables with the same name

name = "Eliut"


def change_name():
    name = "Carlos"
    print(name)


change_name()
print(name)

# Output:
# Carlos
# Eliut


# LEGB rule
#
# L - Local
# E - Enclosing
# G - Global
# B - Built-in


# Local scope

def local_example():
    number = 10
    print(number)


local_example()


# Enclosing scope

def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    inner()


outer()


# Global scope

language = "Python"


def show_language():
    print(language)


show_language()


# Built-in scope

numbers = [10, 20, 30]

print(len(numbers))


# LEGB example

message = "GLOBAL"


def outer_function():
    message = "ENCLOSING"

    def inner_function():
        message = "LOCAL"
        print(message)

    inner_function()


outer_function()

# Python finds the local variable first.


# Enclosing example

message = "GLOBAL"


def outer_function_2():
    message = "ENCLOSING"

    def inner_function_2():
        print(message)

    inner_function_2()


outer_function_2()


# Global example

message = "GLOBAL"


def outer_function_3():

    def inner_function_3():
        print(message)

    inner_function_3()


outer_function_3()


# Variable lifetime

def calculate():
    result = 10 + 20
    return result


print(calculate())

# result is created when the function runs.
# It is not available outside the function.


# Another lifetime example

def create_number():
    number = 100
    print(number)


create_number()

# print(number)  # NameError


# Each function call has its own local variables

def calculate_product_total(price):
    total = price * 1.16
    return total


print(calculate_product_total(100))
print(calculate_product_total(500))
print(calculate_product_total(1000))


# Using global

counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()

print(counter)


# global works, but using it too much can make code harder to maintain

balance = 1000


def buy():
    global balance
    balance -= 200


def refund():
    global balance
    balance += 200


buy()

print(balance)


# A cleaner way is usually passing values to functions

def make_purchase(current_balance, price):
    new_balance = current_balance - price
    return new_balance


user_balance = 1000

user_balance = make_purchase(user_balance, 200)

print(user_balance)


# nonlocal

def create_counter():
    number = 0

    def increment_counter():
        nonlocal number
        number += 1

    increment_counter()

    print(number)


create_counter()

# global -> global variable
# nonlocal -> variable from the outer function


# Simple login example

MAX_LOGIN_ATTEMPTS = 3


def login(username, password):
    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:

        if username == "admin" and password == "1234":
            return True

        attempts += 1

    return False


print(login("admin", "1234"))


# Avoid using Python built-in names as variables

# Bad:
# list = [1, 2, 3]
# str = "Hello"
# int = 10

# Better:

number_list = [1, 2, 3]
text = "Hello"
number = 10


# Quick notes:
#
# Local:
# Variables created inside a function.
#
# Global:
# Variables created outside functions.
#
# LEGB:
# Local -> Enclosing -> Global -> Built-in
#
# Variable lifetime:
# Local variables normally exist while the function is running.
#
# Good practice:
# Pass data using parameters and return the result.
# Avoid modifying global variables unless it is really necessary.