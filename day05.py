# Declara una lista vacía
lst = list()
lista = []
# Declara una lista con más de 5 elementos
autos = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']
#Encuentra la longitud de la lista
print(len(autos))
#Obtén el primer, medio y último elemento de la lista
print(autos[0])
print(autos[2])
print(autos[-1])
#Declara una lista llamada mixed_data_types que contenga tu nombre, edad, altura, estado civil y dirección
mixed_data_types = ['Eliut', 19, 1.76, 'soltero', 'la barranca']
#Declara una lista it_companies e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies = ['facebook', 'google', 'microsoft', 'apple', 'IBM', 'oracle', 'amazon']
#Imprime la lista usando print()
print(it_companies)
#Imprime el número de empresas en la lista
print(len(it_companies))
#Imprime la primera, la del medio y la última empresa
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
#Cambia el nombre de una de las empresas y vuelve a imprimir la lista
it_companies[3] = 'samsung'
print(it_companies)
#Agrega una empresa IT a it_companies
it_companies.append('intel')
#Inserta una empresa IT en la mitad de la lista
it_companies.insert(4, 'hp')
#Cambia el nombre de una empresa en it_companies a mayúsculas (¡excepto IBM!)
it_companies[0] = it_companies[0].upper()
#Une it_companies en una cadena usando la cadena '#;  '
it_companies_str = '#;  '.join(it_companies)
print(it_companies_str)
#Verifica si una empresa existe en it_companies
existe = 'samsung' in it_companies
print(existe)
existe = 'mercado libre' in it_companies
print(existe)
#Ordena la lista usando el método sort()
it_companies.sort()
print(it_companies)
#Invierte la lista en orden descendente usando reverse()
it_companies.reverse()
print(it_companies)
#Corta (slice) las primeras 3 empresas de la lista
it_companies[0:3]
#Corta (slice) las últimas 3 empresas de la lista
it_companies[-1:-3]
#Corta la(s) empresa(s) del medio de la lista
it_companies[3:6]
#Elimina la primera empresa IT de la lista
it_companies.remove(it_companies[0])
#Elimina la(s) empresa(s) del medio de la lista
it_companies.remove(it_companies[3])
#Elimina la última empresa IT de la lista
it_companies.remove(it_companies[-1])
#Elimina todas las empresas IT de la lista
it_companies.clear()
#Destruye la lista it_companies
del it_companies
#Concatena las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#Inserta 'Python' y 'SQL' después de full_stack en la lista concatenada.
full_stack.insert(0, 'python')
full_stack.insert(1, 'SQL')
print(full_stack)
# ! Ejercicios: Nivel 2
#A continuación, una lista con las edades de 10 estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Ordena la lista y encuentra la edad máxima y mínima
ages.sort()
min_age = ages[0]
max_age = ages[-1]
#Agrega la edad mínima y máxima nuevamente a la lista
ages.insert(0, min_age)
ages.insert(-1, max_age)
print(ages) # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
#Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios) # sin usar condicionales
mediana = (ages[4] + ages[5]) / 2
print(mediana) # 24.0
#Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
promedio = sum(ages) / len(ages)
print(promedio) # 23.0
#Encuentra el rango de edades (máximo - mínimo)
range = max_age - min_age
print(range) # 7
#Compara |min - promedio| y |max - promedio| usando la función abs()
print(abs(min_age - promedio)) # 4.0
print(abs(max_age - promedio)) # 3.0
#Encuentra el país del medio en la lista de países
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mediana_pais = paises[len(paises) // 2] # Finland
#Para la lista paises separa los tres primeros países de los países nórdicos restantes.
paises_potencia = paises[0:3]
print(paises_potencia)
#Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
primer_mitad = paises[0:4]
segunda_mitad = paises[4:7]
print(primer_mitad)
print(segunda_mitad)