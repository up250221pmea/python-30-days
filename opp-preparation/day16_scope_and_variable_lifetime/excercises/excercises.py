
# * Ejercicio 1

# Identificar la salida de este codigo sin ejecutarlo

nombre = "Python"

def mostrar():
    nombre = "Java"

    print(nombre)

mostrar()

print(nombre)

# La primera salida imprime "Java"
# La segunda salida imprime "Python"
# La variable local es la que esta dentro de la funcion mostrar() -- nombre = "Java"
# La varible global es la que esta fuera de la funcion la que dice nombre = "Python"

# * Ejercicio 2 

# Encuentra el error en este codigo

def calcular_precio():
    precio = 250
    descuento = 50

    total = precio - descuento


calcular_precio()

# print(total)  <------ el error esta aqui porque quiere imprimir la variable local fuera de la funcion que la usa tiene que usar return para devolver el total

# * Ejercicio 3

# Antes de ejecutar puedes predecir que imprime este codigo:

lenguaje = "Python" # Global 


def desarrollo():
    lenguaje = "Java" # Enclosing 

    def backend():
        print(lenguaje)

    backend()


desarrollo()

# El codigo imprime la variable lenguaje = "Java" pero porque la imprime la funcion backend()
# Busca en que parte esta la variable local 

# * Ejercicio 4

def calcular_total(precio, cantidad):
    subtotal = precio * cantidad 
    print(subtotal)
    return subtotal

calcular_total(150, 3)

# * Ejercicio 5

TAX = 0.16

def calculate_order_total(price, quantity):
    subtotal = price * quantity
    impuesto = TAX * subtotal
    total = subtotal + impuesto
    print(total)
    return total 

calculate_order_total(90, 4)