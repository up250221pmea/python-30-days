# ========================================== #
#                Notes Manager
# ========================================== #

try:
    print('1. Add note \n2. View notes ')
    usuario = int(input('Que accion quieres hacer: '))

    if usuario == 1:
        nota = input('¿Que idea tienes hoy? ')
        with open('Notes.txt', 'a') as file:
            file.write(nota + '\n')

    if usuario == 2:
        with open('Notes.txt', 'r') as file:
            view = file.read()
        print(view)
except ValueError:
    print('Ingresa una opcion valida')

except FileNotFoundError:
    print('No existe tus archivo de notas')