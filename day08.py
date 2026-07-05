# Ejercios de diccionarios 
# Crea un diccionario vacío llamado dog
dog = {}
# Añade las claves name, color, breed, legs y age al diccionario dog
dog = {
    'name':'mike',
    'color':'brown',
    'breed':'doberman',
    'legs':True,
    'age':2,
}
# Crea un diccionario student con las claves first_name, last_name, gender, age, marital status, skills, country, city y address
student = {
    'first_name':'Eliut',
    'last_name':'Piña',
    'gender':'man',
    'age':19,
    'marital_status':'married',
    'skills': ['excel', 'comunication', 'mathematics', 'stress tolerant'],
    'country':'mexico',
    'city':'aguascalientes',
    'address': {
        'street':'independencia',
        'house number':'345',
    }
}
# Obtén la longitud del diccionario student
print(len(student))
# Obtén el valor de skills y comprueba su tipo; debe ser una lista
valor = type(student['skills'])
print(valor)
# Modifica skills añadiendo una o dos habilidades
student['skills'].extend(['time disponibility', 'hard working'])
print(student)
# Obtén la lista de claves del diccionario
claves = student.keys()
print(list(claves))
# Obtén la lista de valores del diccionario
valores = student.values()
print(list(valores))
# Usa el método items() para convertir el diccionario en una lista de tuplas
estudiante = student.items()
print(estudiante)
# Elimina un elemento del diccionario
student.pop('marital_status')
# Elimina uno de los diccionarios
del dog 