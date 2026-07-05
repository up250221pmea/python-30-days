# Ejercios tuplas 
#Crea una tupla vacía
tuple()
tupla = ()
#Crea una tupla con los nombres de tus hermanos y hermanas (pueden ser ficticios)
Hermanos = ('Juan', 'Pedro', 'Leo')
Hermanas = ('Rubí', 'Ana')
#Concatena las tuplas de hermanos y asígnalas a siblings
Sibilings = Hermanos + Hermanas
#¿Cuántos hermanos tienes?
print(len(Sibilings))
#Modifica la tupla de siblings y añade los nombres de tus padres; asígnala a family_members
family_members = Sibilings + ('Maria', 'Ignacio')
print(family_members) 
# Ejercicios: Nivel 2
#Extrae los hermanos y los padres desde family_members
Hermans = family_members[0:5]
Father = family_members[5:]
#Crea las tuplas fruits, vegetables y animal_products. Concatena las tres tuplas y asígnalas a la variable food_stuff_tp
fruits = ('naranja', 'manzana', 'platano')
vegetables = ('zanahoria', 'cebolla', 'limon')
animal_products = ('crocetas', 'shampoo')
food_stuff_tp = fruits + vegetables + animal_products
#Convierte la tupla food_stuff_tp en la lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
#Extrae los elementos del medio desde la tupla food_stuff_tp o la lista food_stuff_lt
mitad = len(food_stuff_lt) // 2
medio = food_stuff_lt[mitad-2:mitad+2]
#Extrae las primeras tres y las últimas tres entradas de la lista food_stuff_lt
firts_three = food_stuff_lt[0:3]
second_three = food_stuff_lt[-3]
#Elimina completamente la tupla food_stuff_tp
del food_stuff_tp
#Comprueba si existen los elementos:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Verifica si 'Estonia' está en la tupla nordic_countries
print('Estonia' in nordic_countries) # False
#Verifica si 'Iceland' está en la tupla nordic_countries
print('Iceland' in nordic_countries)
