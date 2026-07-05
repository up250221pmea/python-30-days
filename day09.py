# Ejercicios - Día 9
# Ejercicios: Nivel 1
# Usa input para obtener la edad del usuario (por ejemplo: "Introduce tu edad:"). Si el usuario tiene 18 años o más, muestra: 'Ya tienes la edad suficiente para aprender a conducir.' Si es menor, muestra cuántos años le faltan. Ejemplo de salida:
# Introduce tu edad: 30
# Ya tienes la edad suficiente para aprender a conducir.
# Salida:
# Introduce tu edad: 15
# Aún necesitas esperar 3 años para aprender a conducir.
edad = int(input("ingresa tu edad y ver si eres apto para conducir: "))
if edad >= 18:
    print("puedes conducir")
else:
    rango = 18 - edad
    print(f'te faltan {rango} años para conducir')
# Usa if…else para comparar my_age y your_age. ¿Quién es mayor (yo o tú)? Usa input("Introduce tu edad:") para obtener la edad. Puedes usar condicionales anidados para imprimir 'año' cuando la diferencia sea 1, 'años' para diferencias mayores, y un mensaje personalizado si my_age = your_age. Salida de ejemplo:
# Introduce tu edad: 30
# Tienes 5 años más que yo.
my_age = 19
your_age = int(input("Introduce tu edad: "))
diferencia = your_age - my_age
if diferencia == 0:
    print('tienes la misma edad que yo')
    if diferencia == 1:
        print(f'tienes {diferencia} año mas que yo')
    else:
        print(f'tienes {diferencia} años mas que yo')
else:
    if diferencia < 0:
        diferencia = abs(diferencia)
    if diferencia == 1:
        print(f'tengo {diferencia} año mas que tu')
    else:
        print(f'tengo {diferencia} años mas que tu')
# Pide al usuario dos números con input. Si a > b, imprime 'a es mayor que b'; si a < b, imprime 'a es menor que b'; si son iguales, imprime 'a es igual a b'.
# Introduce el primer número: 4
# Introduce el segundo número: 3
# 4 es mayor que 3
a = float(input('ingresa un numero: '))
b = float(input('ingresa otro numero: '))
if a > b:
    print(f'{a} es mayor que {b}')
elif a < b:
    print(f'{b} es mayor que {a}')
else:
    print(f'los numeros son iguales')
# * Ejercicios: Nivel 2
# Escribe un código que asigne una calificación según la nota del estudiante:
# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F
calificacion = float(input('ingresa tu calificacion: '))
if calificacion >= 80 and calificacion <= 100:
    print('tu nota es A')
elif calificacion >= 70:
    print('tu nota es B')
elif calificacion >= 60:
    print('tu nota es C')
elif calificacion >= 50:
    print('tu nota es D')
else:
    print('tu nota es F')
# Comprueba si es otoño, invierno, primavera o verano. Si el usuario introduce: Septiembre, Octubre o Noviembre → otoño. Diciembre, Enero o Febrero → invierno. Marzo, Abril o Mayo → primavera. Junio, Julio u Agosto → verano.
mes = str(input('ingresa el mes y te digo que estacion es: '))
if mes in ['marzo', 'abirl', 'mayo']:
    print('Estas en primavera')
elif mes in ['junio', 'julio', 'agosto']:
    print('Estas en verano')
elif mes in ['septiembre', 'octubre', 'noviembre']:
    print('Estas en otoño')
else:
    print('Estas en invierno')

# La siguiente lista contiene algunas frutas:
fruits = ['banana', 'orange', 'mango', 'lemon']
# Si una fruta no está en la lista, añádela e imprime la lista modificada. Si ya existe, imprime 'La fruta ya está en la lista'.
new_fruit = str(input('ingresa una fruta: '))
if  new_fruit in fruits:
    print(fruits)
else:
    fruits.append('apple')
    print(fruits)

# * Ejercicios: Nivel 3
# Aquí hay un diccionario persona. ¡Siéntete libre de modificarlo!
person = {
    'first_name': 'Eliut',
    'last_name': 'Piña',
    'age': 19,
    'country': 'Mexico',
    'is_married': False,
    'skills': ['git', 'Python', 'SQL', 'NoSQL', 'Math'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}
# Comprueba si existe la clave skills en el diccionario; si existe, imprime la habilidad central de la lista skills.
if 'skills' in person:
    habilidades = person['skills']
    indice_central = len(habilidades) // 2
    print(habilidades[indice_central])
# Comprueba si existe la clave skills; si existe, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
if 'skills' in person:
    lenguaje = person['skills']
    py = 'Python' in lenguaje
    print(py)
# Comprueba si la persona está casada y vive en México.
# Si ambas condiciones se cumplen, imprime:
# 'Eliut Piña vive en México. Está casado.'
# (Ajusta el mensaje según el estado civil y país reales de la persona)
nombre_completo = person['first_name'] + ' ' + person['last_name']

if person['is_married'] and person['country'] == 'Mexico':
    print(f'{nombre_completo} vive en México. Está casado.')
else:
    print(f'{nombre_completo} no cumple ambas condiciones (casado y viviendo en México).')