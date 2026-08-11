# EXERCISES - EXCEPTION HANDLING

# ! Exercise 1: Safe Division
# Ask the user for two numbers and divide them.
# Handle:
# - ValueError if the user enters something that is not a number.
# - ZeroDivisionError if the user tries to divide by zero.
try:
    a = int(input('ingresa un numero: '))
    b = int(input('ingresa otro numero: '))
    division = a / b
    print(division)
except ValueError:
    print('ingresa un valor numerico <ValueError>')
except ZeroDivisionError:
    print('no puedes dividir entre 0 <ZeroDivisorError>')

# ! Exercise 2: Convert Age
# Ask the user for their age using input().
# Convert the value to an integer.
# If the user enters something like "eighteen" instead of a number,
# handle the ValueError and display an appropriate message.
try:
    edad = int(input('ingresa tu edad: '))
    print(edad)
except ValueError:
    print('ingresa tu edad en numero no texto <ValueError>')

# ! Exercise 3: Access an Element from a List
# Use the following list:
# *languages = ['Python', 'Java', 'C#', 'JavaScript', 'Go']
# Ask the user for an index and display the corresponding language.
# Handle:
# - IndexError if the index does not exist.
# - ValueError if the user does not enter a number.
try:
    languages = ['Python', 'Java', 'C#', 'JavaScript', 'Go']
    indice =  int(input('ingresa el indice que quieres acceder: '))
    acceso = languages[indice]
    print(f'El lenguaje de programacion es {acceso}')
except IndexError:
    print('este indice esta fuera de la lista <IndexError>')
except ValueError:
    print('se deben usar numeros <ValueError>')

# ! Exercise 4: Search for a Key in a Dictionary
# Use the following dictionary:
#
# *student = {
# *    'name': 'Eliut',
# *    'career': 'Software Development',
# *    'semester': 3
# *}
#
# Ask the user for a key and display its value.
# If the key does not exist, handle the KeyError.
try:
    student = {
    'name': 'Eliut',
    'career': 'Software Development',
    'semester': 3
}
    valor = str(input('Ingresa que dato quieres saber: '))
    acc = student[valor]
    print(acc)
except KeyError:
    print('Ingresa un valor aceptable <KeyErorr>')

# ! Exercise 5: Calculator with Exceptions
# Create a function called:
#
# calculator(a, b, operation)
#
# The allowed operations are:
# +
# -
# *
# /
#
# Handle invalid values and division by zero.
def calculator(a, b, operation):
    try:
        if operation == '+':
            print(a + b)

        elif operation == '-':
            print(a - b)

        elif operation == '*':
            print(a * b)

        elif operation == '/':
            print(a / b)

        else:
            print('Operación no válida')
    except ZeroDivisionError:
        print('No puedes dividir entre cero')
calculator(10, 5, '+')
calculator(10, 5, '-')
calculator(10, 5, '*')
calculator(10, 5, '/')
# ! Exercise 6: Using else
# Ask the user for an integer.
#
# Use:
#
# try:
#     ...
# except:
#     ...
# else:
#     ...
#
# If no exception occurs, display:
#
# "The number entered correctly is: X"
#
# The goal is to understand that else runs only
# when no exception occurs.
try:
    num = int(input('ingresa un numero: '))
except ValueError:
    print('debe ser un numero entero')
else:
    print(f'el numero ingresado correctamente es: {num}')
# ! Exercise 7: Using finally
# Create a program that tries to divide two numbers.
#
# Regardless of whether an error occurs or not,
# the program must display:
#
# "Program finished."
#
# This message must be inside the finally block.
try:
    a = 5
    b = int(input('ingresa un numero: '))
    div = a / b
finally:
    print('programa finalizado')

# ! Exercise 8: Multiple Exceptions
# Use the following list:
#
# numbers = [10, 20, 30, 40, 50]
#
# Ask the user for:
# - An index
# - A divisor
#
# Get the number from the list using the index
# and divide it by the divisor.
#
# Handle:
# - ValueError
# - IndexError
# - ZeroDivisionError
try:
    numbers = [10, 20, 30, 40, 50]
    indice = int(input('ingresa el indice que quieres acceder: '))
    divisor = int(input('ingresa el numero por el cual quieres dividir: '))
    division = numbers[indice] / divisor
    print(f'el resultado es: {division}')
except ValueError:
    print('debes ingresar un valor entero <ValueError>')
except IndexError:
    print('el indice que ingresaste no es permitido <IndexError>')
except ZeroDivisionError:
    print('no se puede dividir entre 0 <ZeroDivisorError>')

# ! Exercise 9: Safe Function
# Create the following function:
#
# def safe_division(a, b):
#
# The function should try to calculate:
#
# a / b
#
# Handle possible errors inside the function
# so the program does not stop unexpectedly.
#
# Test the function with:
#
# safe_division(10, 2)
# safe_division(10, 0)
# safe_division(10, 'a')
def safe_division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('no se puede dividir en 0 <ZeroDivisorError>')
    except TypeError:
        print('el valor no es numerico <TypeError>')
    finally:
        print('la division a finalizado')
safe_division(10, 2)
safe_division(10, 0)
safe_division(10, 'a')
# ! Exercise 10: Student Grade System
# Create a program that asks for:
#
# Name
# Grade 1
# Grade 2
# Grade 3
#
# Convert the grades to numbers and calculate the average.
#
# Handle invalid inputs using exceptions.
#
# If everything is correct, display something like:
#
# Student: Eliut
# Average: 9.3
#
# If a grade is invalid, display:
#
# Error: grades must be numbers.
#
# Try to use:
# - try
# - except
# - else
# - finally
try:
    alumno = str(input('ingresa tu nombre: '))
    c1 =  float(input('ingresa tu primer calificacion: '))
    c2 =  float(input('ingresa tu segunda calificacion: '))
    c3 =  float(input('ingresa tu tercer calificacion: '))
    promedio = (c1 + c2 + c3) / 3
except ValueError:
    print('Error: las calificaciones deben ser numeros')
else:
    print(f'Alumno: {alumno} \n Promedio: {promedio}')
finally:
    print('El programa de calificaciones a terminado')