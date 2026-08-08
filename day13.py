# ERRORES COMUNES EN PYTHON
# Selecciona un error para provocarlo intencionalmente.

print("""
1. SyntaxError
2. NameError
3. IndexError
4. ModuleNotFoundError
5. AttributeError
6. KeyError
7. TypeError
8. ImportError
9. ValueError
10. ZeroDivisionError
""")

opcion = int(input("Selecciona un error del 1 al 10: "))


if opcion == 1:
    # exec() intenta ejecutar el código escrito dentro del string.
    # Falta colocar los dos puntos después del if.
    exec("""
if 10 > 5
    print("Diez es mayor")
""")


elif opcion == 2:
    # La variable nombre no está definida.
    print(nombre)


elif opcion == 3:
    # La lista solo tiene los índices 0, 1 y 2.
    numeros = [10, 20, 30]
    print(numeros[5])


elif opcion == 4:
    # El módulo no existe.
    import modulo_inexistente


elif opcion == 5:
    # Los strings no tienen el método append().
    nombre = "Eliut"
    nombre.append(" Piña")


elif opcion == 6:
    # La clave "correo" no existe.
    usuario = {
        "nombre": "Eliut",
        "edad": 18
    }

    print(usuario["correo"])


elif opcion == 7:
    # No se puede sumar directamente un string y un entero.
    edad = 18
    print("Edad: " + edad)


elif opcion == 8:
    # El módulo math existe, pero no contiene sumar.
    from math import sumar


elif opcion == 9:
    # El string "hola" no puede convertirse a entero.
    numero = int("hola")
    print(numero)


elif opcion == 10:
    # No se puede dividir entre cero.
    resultado = 10 / 0
    print(resultado)


else:
    print("La opción debe estar entre 1 y 10.")