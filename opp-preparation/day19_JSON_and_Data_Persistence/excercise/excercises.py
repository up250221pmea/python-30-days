import json

# * Excercise 1

perfil = {
    'name':'Alex',
    'career':'IT Engineering ',
    'favorite_language':'Java'
}

with open('perfil.json', 'w') as file:
    json.dump(perfil, file, indent=4)

# * Excercise 2

with open('perfil.json', 'r') as data:
    content = json.load(data)

print(content['name'])
print(content['career'])
print(content['favorite_language'])

# * Excercise 3

languages = ['Ruby', 'Go', 'C#']

with open('perfil.json', 'w') as file:
    json.dump(languages, file, indent=4)

with open('perfil.json', 'r') as datos:
    ver = json.load(datos)

for i in ver:
    print(i)

# * Excercise 4

materia = {
    'curso':'Calculo Integral',
    'ejercicios_completados':10
}

with open('materia.json', 'r') as dato:
    check = json.load(dato)

check['ejercicios_completados'] += 1

with open('materia.json', 'w') as file:
    json.dump(materia, file, indent=4)

print(check)