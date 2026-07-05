# Ejercicios sets
# Conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# ! Ejercicios: Nivel 1
# Encuentra la longitud del conjunto it_companies
print(len(it_companies))
# Agrega 'Twitter' a it_companies
it_companies.add('Twitter')
# Inserta varias empresas IT a it_companies de una sola vez
New_IT = ('Samnsung', 'Xiaomi', 'HP')
it_companies.update(New_IT)
# Elimina una empresa de it_companies
it_companies.pop()
# ¿Cuál es la diferencia entre remove() y discard()? 
# remove: elimina un elemento en especifico 
# discard: elimina un elemento en especifico pero no genera error si el elemento no existe
# Ejercicios: Nivel 2
# Concatena A y B
C = A | B
print(C)
# Encuentra la intersección entre A y B
A.intersection(B)
# ¿Es A un subconjunto de B?
A.issubset(B)
# ¿Son A y B conjuntos disjuntos?
A.isdisjoint(B)
# Combina A con B y viceversa
A.union(B)
B.union(A)
# ¿Cuál es la diferencia simétrica entre A y B?
A.symmetric_difference(B)
# Elimina un conjunto por completo
del A
# Ejercicios: Nivel 3
# Convierte la lista de edades a un conjunto y compara la longitud de la lista y la del conjunto: ¿cuál es mayor?
edades = [19, 23, 11, 21, 9, 10]
ages = set(edades)
print(len(edades) > len(ages))
# Explica la diferencia entre estos tipos de datos: cadena, lista, tupla y conjunto
# * Cadena = un cadena de texto es un tipo de dato que son textos puedes modificar, agregar y meter elementos dentro de textos y es entre comillas simples o dobles
# * Lista = es una lista donde puedes agregar diferentes tipos de datos, es muteable y puedes agregar, eliminr, cambiar datos en incluso los puedes cambiar a otro tipo de datos y se usan corchetes []
# * Tupla = es un tipo de dato que puedes ingresar cualquier tipo de datos solo que en cuanto haces una no puedes modificar estos datos, solo agregar algunos, te sirve por si solo quieres guardar cierto tipo de datos y no cambiarlos y se usan parentesis ()
# * Conjunto = es un tipo de dato donde puedes agregar cualquier tipo de dato solo que aqui no se repiten y puedes hacer otro tipo de operaciones estadisticas y probabilisticas como union, interseccion, diferencia smetrica, se usan llaves {}
# Para la frase "Soy profesor, me gusta motivar y enseñar a las personas." ¿cuántas palabras únicas tiene? Usa split() y conjuntos para obtener las palabras únicas.
frase = "Soy profesor, me gusta motivar y enseñar a las personas."
joined = frase.split()
unique_words = set(joined)
print(unique_words)