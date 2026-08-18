
# 1. Predice la salida
# Antes de ejecutar el código, escribe qué crees que va a imprimir.

a = [1, 2, 3]
b = a

b.append(4)

print(a)       # [1, 2, 3, 4]
print(b)       # [1, 2, 3, 4]

"""Sale lo mismo ya que ambos estan escogiendo el mismo objeto o hacen referencia"""


# 2. ¿Mismo valor o mismo objeto?
# Predice el resultado de cada comparación.

x = [10, 20]
y = [10, 20]
z = x

print(x == y)   # True, ya que valen lo mismo
print(x is y)   # False, ya que no son el mismo objeto

print(x == z)   # True, tienen el mismo valor 
print(x is z)   # True, son el mismo objeto

# == --> comparan el contenido/valo
# is --> comparan la identidad del objeto

# 3. Asignación vs modificación
# Predice cuál será el valor final de a y b.

a = [1, 2, 3]
b = a

b = [4, 5, 6]

print(a)    # la salida es [1, 2, 3]
print(b)    # la salida es [4, 5, 6]

"""Lo que pasa es que si aputan al mismo onjeto solo que al reasignar ya toma otro valor diferente"""

# 4. Crea una copia independiente
# Modifica list_b sin cambiar list_a.

list_a = ["Python", "Java"]

# Escribe tu código aquí

list_b = list_a.copy()
list_b.append("C++")

print(list_a)   # ["Python", "Java"]
print(list_b)   # ["Python", "Java", "C++"]

# La idea es:
# list_a debe quedarse igual
# list_b debe tener un lenguaje extra


# 5. Encuentra el problema
# ¿Por qué cambia original?

original = [1, 2, 3]
# copy_list = original

# copy_list.append(100) # ! Quita el simbolo de comentario para que veas la salida

print(original) # <---- Salida es [1, 2, 3, 100]
# print(copy_list) <---- Salida es [1, 2, 3, 100]

"""Porque copy_list = original no crea una copia.
Ambas variables hacen referencia al mismo objeto."""

# Corrige el código para que original no cambie.

copy_list_2 = original.copy()
copy_list_2.append(100)

print(original)     # <--- [1, 2, 3]
print(copy_list_2)  # <--- [1, 2, 3, 100]

# 6. Objetos mutables en funciones
# Predice el resultado antes de ejecutarlo.

def add_item(items):
    items.append("C#")


languages = ["Python", "Java"]

add_item(languages)

print(languages)    # ["Python", "Java", "C#"]
""" La salida es esa porque esta modificando la lista
languages = ["Python", "Java"], cuando llama a la funcion"""

# 7. Objetos inmutables en funciones
# Compara este ejercicio con el anterior.

def increase(number):
    number += 10


value = 5

increase(value)

print(value)  # 5 
"""En este caso no cambia el valor porque los valores
entero son INMUTABLES no pueden cambiar"""