
# * Excercise 1

with open('message.txt', 'r') as file:
    content = file.read()
print(content)

# * Excercise 2

with open('profile.txt', 'w') as dato:
    dato.write('Software Development')

# Comprobation 

with open('profile.txt', 'r') as dato:
    content = dato.read()

print(content) 

# * Excercise 3

with open('profile.txt', 'a') as data:
    data.write('\nLearning: OOP')

# * Excercise 4

with open('profile.txt', 'r') as dat:
    ver = dat.read()

print(ver)

# * Excercise 5

programming = str(input('ingresa tu lenguaje aprendido: '))

with open('languages.txt', 'a') as file:
    file.write(programming + '\n')

with open('languages.txt', 'r') as file:
    content = file.read()

print(content)

# * Excercise 6

try:
    with open('numbers.txt', 'r') as file:
        check = file.read()
    print(check)
except FileNotFoundError:
    print('No existe el archivo')

# * Excercise 7

# excercise/
#       NoteManager/
#               notemanager.py

