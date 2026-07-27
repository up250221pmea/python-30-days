# Ejemplos claros para no confundir antes de los ejercicios 
# 1. Declarar y llamar una función
def saludar():   # ---->     # declarar
    print("Hola!")

saludar()    #  ----->    # llamar/invocar
# 2. return vs print
# !Esta es una de las confusiones más comunes.
def con_print():
    print("Hola")   # ---->   # muestra en pantalla, pero no devuelve nada útil

def con_return():
    return "Hola"  # ----->    # devuelve el valor para que lo uses

# La diferencia importa aquí:
resultado = con_return()
print(resultado.upper())   # funciona: "HOLA"

resultado2 = con_print()   # imprime "Hola"...
# ! print(resultado2.upper())  # ERROR: resultado2 es None
# 3. Parámetros y argumentos
# ? Parámetro = la variable que defines en la función.
# * Argumento = el valor que le pasas al llamarla. <----- lo que esta dentro del parentesis
def elevar(base, exponente):   # base y exponente son parámetros
    return base ** exponente

print(elevar(2, 3))   # ----> 2 y 3 son argumentos → resultado: 8
print(elevar(5, 2))   # → resultado: 25

# 4. Keyword arguments (argumentos con nombre)
# Normalmente el orden importa. Con keyword arguments, no.
def describir(nombre, edad, ciudad):
    return f"{nombre} tiene {edad} años y vive en {ciudad}"

# Orden normal
descripcion = describir("Ana", 25, "CDMX")
print(descripcion)
# Con keyword — el orden no importa
describir(edad=25, ciudad="CDMX", nombre="Ana")   # mismo resultado

# 5. Parámetros por defecto
# Puedes darle un valor predeterminado a un parámetro. Si no se lo pasas, usa ese valor.
def potencia(base, exponente=2):   # exponente por defecto es 2
    return base ** exponente

print(potencia(5))      # usa exponente=2 → 25
print(potencia(5, 3))   # sobreescribe el default → 125

# 6. *args — número arbitrario de argumentos
# Cuando no sabes cuántos valores te van a pasar.
def mostrar_compras(*productos):
    for p in productos:
        print("-", p)

mostrar_compras("leche", "pan")
mostrar_compras("leche", "pan", "huevos", "arroz")
# ? El * hace que Python agrupe todo en una tupla dentro de la función. El nombre args es convención, podría llamarse *cosas, *items, etc.

# 7. **kwargs — número arbitrario de argumentos nombrados
# Igual que *args pero recibe pares clave=valor. Python los agrupa en un diccionario.
def perfil(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

perfil(nombre="Luis", edad=22, carrera="ISC")
# ? SALIDA:
# nombre: Luis
# edad: 22
# carrera: ISC

# 8. Dictionary unpacking con **
# Si ya tienes un diccionario y quieres pasarlo como argumentos a una función, usas **.
def presentar(nombre, ciudad):
    print(f"Soy {nombre} de {ciudad}")

info = {"nombre": "María", "ciudad": "Guadalajara"}

presentar(**info)   # equivale a presentar(nombre="María", ciudad="Guadalajara")

# 9. Función como parámetro de otra función
# En Python, las funciones son objetos que puedes pasar igual que un número o string.
def doble(n):
    return n * 2

def triple(n):
    return n * 3

def aplicar(funcion, valor):   # recibe una función
    return funcion(valor)

print(aplicar(doble, 5))    # → 10
print(aplicar(triple, 5))   # → 15
# Nota que pasas doble sin paréntesis — no la estás llamando, la estás pasando para que aplicar la use.
# 10. En el contexto de funciones, devolver significa que la función te regresa un valor como resultado de su trabajo.
# Cuando una función "devuelve" algo, ese valor queda disponible para usarlo en el resto del programa.
def sumar(a, b):
    return a + b   # -------> la función DEVUELVE el resultado

resultado = sumar(3, 5)
print(resultado)  # 8

# 11. La diferencia clave: devolver vs solo hacer algo
# ! Esta función HACE algo pero no devuelve nada
def saludar(nombre):
    print(f"Hola {nombre}")   # solo muestra, no devuelve

# Esta función DEVUELVE un valor
def crear_saludo(nombre):
    return f"Hola {nombre}"   # devuelve el texto

# La diferencia al usarlas:
saludar("Ana")                    # imprime directo, no puedes guardar nada útil
mensaje = crear_saludo("Ana")     # guardas lo que devolvió
print(mensaje)                    # ahora sí lo usas cuando quieras
# En Python la palabra clave para devolver es return. En cuanto el código llega a return, la función termina y ese valor "sale" hacia donde fue llamada.
# ? Ejemplo claro:
# Declara un funcion para calcular el area de un circulo con un parametro
def area_circulo(r): # -----> tu funcion se llama area_circulo y tu argumento es r
    return 3.14 * r ** 2

area1 = area_circulo(5) #-----> llamas a la funcion con el parametro 5 
area2 = area_circulo(10)
print(area1, area2)  # -----> imprimes lo que quieres

# //*Ejercicios: Nivel 1
# Declara un funcion para calcular el area de un circulo con un parametro
def area_circulo(r):
    return 3.14 * r ** 2

area1 = area_circulo(5)
area2 = area_circulo(10)
print(area1, area2)

# Declara una función add_two_numbers. Debe aceptar dos parámetros y devolver su suma.

def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(4, 6))

# Escribe una función llamada add_all_nums que acepte un número arbitrario de argumentos y sume todos. Verifica que todos los elementos sean de tipo numérico. Si no, devuelve un mensaje apropiado.
def add_all_nums(*numeros):
    total = 0
    for i in numeros:
        if not isinstance(i, (int, float)):
            return'ingresa un valor numerico'
        total = total + i
    return total

print(add_all_nums(10, 7, 9, 10))
print(add_all_nums('hola', 'hello'))
# La temperatura en Celsius (°C) se puede convertir a Fahrenheit (°F) con: °F = (°C x 9/5) + 32. Escribe una función convert_celsius_to_fahrenheit.
def ConvertCelsiusToFahrenheit(grados):
    far = (grados * (9/5)) + 32
    return far
con = ConvertCelsiusToFahrenheit(35)
print(con)

# Escribe una función llamada check_season que acepte un mes y devuelva la estación: otoño, invierno, primavera o verano.
def check_season(mes):
    estaciones = {
        'primavera':['marzo', 'abril','mayo'],
        'verano':['junio', 'julio','agosto'],
        'otoño':['septiembre', 'octubre', ],
        'invierno':['diciembre', 'enero', 'febrero']
    }
    for estacion, meses in estaciones.items():
        if mes in meses:
            return f'tu estacion es {estacion}'

print(check_season('enero'))
# Escribe una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal.
def calculate_slope(y2, y1, x2, x1):
    pediente = (y2 - y1) / (x2 - x1)
    return pediente

m = calculate_slope(3, 7, 6, 10)
m2 = calculate_slope(8, 6, 8, 3)
print(f'la pendiente es {m2}')
print(f'la pendiente es {m}')
# La ecuación cuadrática se calcula como: ax² + bx + c = 0. Escribe una función solve_quadratic_eqn que calcule las soluciones.
def slove_quadratic_eqn(a , b, c):
    exp = -1*b
    dis1 = b**2
    dis2 = -1*(4+(a*c))
    deno = 2*a
    discriminante = dis1 * 1 *(dis2)
    if discriminante == 0:
        ecuacion_general = exp / deno
    else:
        ecuacion_general = (exp * (discriminante ** 0.5)) / deno 
    return ecuacion_general
print(slove_quadratic_eqn(3, 6, 8))
# Declara una función llamada print_list que acepte una lista y imprima cada elemento.
frutas = list(input('ingresa datos: ').split(","))
def print_list(frutas):
    for i in frutas:
        print(i)

print(print_list(frutas))

# Declara una función llamada reverse_list que acepte un arreglo y devuelva su reverso (usa un bucle).
# print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

numeros = [1, 3, 5, 7, 9]
def reverse_list(numeros):
    num = []
    for i in range(4, -1, -1):
        numeros[i]
        num.append(numeros[i])
    return num
print(reverse_list(numeros))

# Declara una función capitalize_list_items que acepte una lista y devuelva una lista con los elementos en mayúscula.
ciudades = ['ciudad de mexico', 'aguascalientes', 'morelia','puebla']
def capitalizate_list_items(ciudades):
    citys = []
    for j in range(4):
        ciudades[j]
        may = ciudades[j].upper()
        citys.append(may)
    return citys
print(capitalizate_list_items(ciudades))
# Declara una función add_item que acepte una lista y un ítem. Debe devolver la lista con el ítem agregado al final.
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def food_items(receta, item):
    receta.append(item)
    return receta
print(food_items(numbers, 5))
# Declara una función remove_item que acepte una lista y un ítem. Debe devolver la lista con el ítem eliminado.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(receta, item):  
    receta.remove(item)
    return receta
print(remove_item(food_staff, 'Potato'))
# Declara una función sum_of_numbers que acepte un número y sume todos los números en ese rango.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers(numero):
    suma = 0
    for k in range(1, numero + 1):
        print(f'suma={k} + {suma}')
        suma = k + suma
    return suma 
print(sum_of_numbers(3))
print(sum_of_numbers(5))
# Declara una función sum_of_odds que acepte un número y sume todos los impares en ese rango.
def sum_of_odds(numero):
    num = 0
    for r in range(1, numero + 1):
        if r % 2 == 1: 
            print(f'sum= {r} + {num}')
            num = num + r
    return num
print(sum_of_odds(7))
# Declara una función sum_of_even que acepte un número y sume todos los pares en ese rango.
def sum_of_even(numero):
    mun = 0
    for w in range(1 , numero + 1):
        if w % 2 == 0:
            print(f'suma = {w} + {mun}') #? <---- esta parte del codigo es para debuggear y verificar que todo este bien 
            mun = w + mun
    return mun
print(sum_of_even(8))
# //*Ejercicios: Nivel 2
# Declara una función evens_and_odds que acepte un entero positivo y calcule la cantidad de pares e impares en ese número.
# print(evens_and_odds(100))
# La cantidad de números pares es 50.
# La cantidad de números impares es 50.
def evens_and_odds(numero):
    int(numero)
    pares = []
    impares = []
    for j in range(1, numero + 1):
        if j % 2 == 0:
            pares.append(j)
        else:
            impares.append(j)
    im = print(f'la cantidad de impares es: {len(impares)}')
    pa = print(f'la cantidad de pares es: {len(pares)}')
print(evens_and_odds(10))
# Llama a tu función factorial que acepte un entero y devuelva su factorial.
def factorial(fact):
    acu = 1
    for y in range(1, fact + 1):
        acu = y * acu
        print(f'factorial {y} * {fact}')  #? <---- esta parte del codigo es para debuggear y verificar que todo este bien 
    fact = fact - 1
    return acu
print(factorial(5))
# Llama a tu función is_empty que acepte un argumento y verifique si está vacío.
def is_empty(argumento):
    if len(argumento) == 0:
        print('la casilla esta vacia')
        return True
    return False
print(is_empty([]))
# Escribe distintas funciones que acepten listas y calculen: media, mediana, moda, rango, varianza y desviación estándar.
data = [4, 4, 6, 9, 10, 24, 25]
def media(data):
    dat = sum(data)
    med = dat / len(data)
    return med
print(media(data))
def mediana(data):
    medio = len(data) // 2
    if medio % 2 == 0:
        md = sum(data) / len(data)
    else:
        md = sum(data) // len(data)
    return md 
print(mediana(data))
# //*Ejercicios: Nivel 3
# Escribe una función is_prime que verifique si un número es primo.
def is_prime(valor):
    if valor / valor and valor /  1:
        print('el numero es primo')
    else:
        print('el numero no es primo')
print(is_prime(5))
# Escribe una función que verifique si todos los ítems en una lista son únicos.
mis_items = [2, 6, 6, 7, 8, 9]
print(f' Tu lista es: {mis_items}')
def unicos(mis_items):
    comparar = len(mis_items)
    mis_itemes_2 = len(set(mis_items))
    if comparar == mis_itemes_2:
        return True
    else:
        return False
unicos(mis_items)
# Escribe una función que verifique si todos los ítems en una lista son del mismo tipo de dato.
mi_persona = [19, 'Eliut', False, 1.76]
print(f'tus datos son {mi_persona}')
def datos(mi_persona):
    first = mi_persona[0]
    gen = type(first)
    for u in mi_persona:
        ver = type(u)
        if ver == gen:
            print(True)
        else:
            print(False)
            return False
    return False
datos(mi_persona)
# Escribe una función que verifique si una variable proporcionada es un nombre de variable válido en Python.
palabras_reservadas = (
    'False', 'None', 'True', 'and', 'as', 'assert',
    'async', 'await', 'break', 'class', 'continue', 'def',
    'del', 'elif', 'else', 'except', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
)
def verf_var(palabra):
    if palabra in palabras_reservadas:
        print('este nombre no es valido para tu variable')
    else:
        print('correcto, puedes asignar ese nombre')
    return 'Puedes usar esa variable'
verf_var('False')
"""
Despues de todos estos ejercicios debes saber la importancia de las funciones, y su importancia a la hora 
de aprender Programacion Orientada a Objetos
"""
# ? FUNCIONES EN PYTHON
# * Una función es un bloque de código reutilizable que solo se ejecuta cuando se llama.
# * Nos permiten organizar, reutilizar y simplificar el código.

# ! SINTAXIS BÁSICA:
# * def nombre_funcion(parametros):
# *     cuerpo de la función
# *     return resultado

# ? ¿PARA QUÉ SIRVE return?
# * return → entrega un valor al lugar donde se llamó la función (se puede guardar o usar).
# * print  → solo muestra algo en pantalla, no entrega ningún valor utilizable.

# ! EJEMPLO:
# * def doble(n):
# *     return n * 2        ← devuelve el valor
# *
# * resultado = doble(5)    ← puedes guardarlo
# * print(resultado)        ← imprime 10

# ? PARÁMETROS vs ARGUMENTOS
# * Parámetro → variable en la definición:   def suma(a, b)
# * Argumento → valor real al llamarla:      suma(3, 5)

# ! IMPORTANTE
# todo El código después de un return NO se ejecuta.
# todo Una función sin return devuelve None automáticamente.
# todo Puedes tener múltiples return, pero solo se ejecuta el primero que se alcance.