# Ejercicios: Día 13
# Usa una comprensión de listas para filtrar los números negativos y ceros de la siguiente lista:
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numeros = [i for i in numbers
            if i > 0
]
print(numeros)
# Aplana la siguiente lista de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [first for second in list_of_lists for first in second for first in first]
print(new_list)
# Salida:
# <[1, 2, 3, 4, 5, 6, 7, 8, 9]>
# Crea la siguiente lista de tuplas usando una comprensión de listas
potencias = [tuple(n**i for i in range(11)) for n in range(7)]
for fila in potencias:
    print(fila)
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# Aplana la siguiente estructura en una nueva lista:
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
codes = {
    'Finlandia':'FIN',
    'Suecia':'SWE',
    'Noruega':'NOR'
}
new_coutries = [
    [name[0], codes[name[0]], name[1]]
    for j in countries 
    for name in j
    ]
print(new_coutries)
# Salida:
# [['Finlandia', 'FIN', 'Helsinki'], ['Suecia', 'SWE', 'Estocolmo'], ['Noruega', 'NOR', 'Oslo']]
# Convierte la siguiente lista en una lista de diccionarios:
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
nuevos_paises = [
    {
        'País': pais[0],
        'Ciudad': pais[1]
    }
    for lista in countries
    for pais in lista
]

print(nuevos_paises)
# Salida:
# [{'País': 'Finlandia', 'Ciudad': 'Helsinki'},
# {'País': 'Suecia', 'Ciudad': 'Estocolmo'},
# {'País': 'Noruega', 'Ciudad': 'Oslo'}]
# Convierte la siguiente lista en una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nuevos_nombres = [
    nombre[0] + ' ' + nombre[1]
    for lista in names
    for nombre in lista
]

print(nuevos_nombres)
# Salida:
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# Escribe una función lambda que calcule la pendiente o la ordenada al origen de una función lineal.
# * m = (y2 - y1) / 
m = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(f'tu pendiente es {m(3, 5, 6, 4)}')