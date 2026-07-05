# concatenar cadenas de texto
first_name = "eliut"
last_name = "piña"
space = " "
full_name = first_name + space + last_name
print(full_name)
# uso de variables dentro de strings
presentation = """hola mi nombre es piña
y tengo 19 años"""
print(presentation)
# uso de funciones con strings 
name = "eliut"
last_name = "  piña"
full_name = name + space + last_name
print(len(name))
print(len(last_name))
print(len(name) > len(last_name))
print(len(full_name))

# uso de secuencias de escape
print('Espero que todos estén disfrutando el Desafío de Python.\n¿Y tú?') # salto de línea
print('Días\tTemas\tEjercicios') # añadir tabulación o 4 espacios
print('Día 1\t5\t5')
print('Día 2\t6\t20')
print('Día 3\t5\t23')
print('Día 4\t1\t35')
print('Este es el símbolo de barra invertida (\\)') # Para escribir una barra invertida
print('En todos los lenguajes de programación comienza con \"Hola, Mundo!\"') # para escribir una comilla doble dentro de una comilla simple

# solo cadenas
first_name = 'Alexander'
last_name = 'Marin'
language = 'Python'
formated_string = 'Soy %s %s. Enseño %s' %(first_name, last_name, language)
print(formated_string)

# Cadenas y números
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El área de un círculo con radio %d es %.2f.' %(radius, area) # 2 se refiere a los 2 dígitos después del punto

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'Las siguientes son librerías de Python: %s' % (python_libraries)
print(formated_string) # "Las siguientes son librerías de Python:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']" 

# Formato de cadenas estilo Nuevo (str.format)
# Este formato se introdujo en Python 3.
first_name = 'Asabeneh'  # asigna el nombre de pila
last_name = 'Yetayeh'  # asigna el apellido
language = 'Python'  # asigna el lenguaje
formated_string = 'Soy {} {}. Enseño {}'.format(first_name, last_name, language)  # crea una cadena formateada con las variables
print(formated_string)  # muestra la cadena formateada en pantalla
a = 8  # define el valor de a (intercambiado)
b = 7  # define el valor de b (intercambiado)

print('{} + {} = {}'.format(a, b, a + b))  # muestra la suma de a y b
print('{} - {} = {}'.format(a, b, a - b))  # muestra la resta de a y b
print('{} * {} = {}'.format(a, b, a * b))  # muestra la multiplicación de a y b
print('{} / {} = {:.2f}'.format(a, b, a / b))  # muestra la división de a entre b con dos decimales
print('{} % {} = {}'.format(a, b, a % b))  # muestra el resto de la división de a entre b
print('{} // {} = {}'.format(a, b, a // b))  # muestra la división entera de a entre b
print('{} ** {} = {}'.format(a, b, a ** b))  # muestra a elevado a la potencia b

# Formato de cadenas estilo F-strings (Literal String Interpolation)
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# ejercicios de practica
# concatena las cadenas 'Thirty', 'Days', 'Of', 'Python' en una sola cadena 'Thirty Days Of Python'.
ca1 = "thirty "
ca2 = "days "
ca3 = "of "
ca4 = "python"
text = ca1 + ca2 + ca3 + ca4
print(text)
# concatena las cadenas 'Coding', 'For', 'All' en una sola cadena 'Coding For All'.
codigo = "coding "
para = "for "
toda = "all"
print(f'{codigo}+{para}+{toda}')
# declara una variable llamada company y asígnale el valor inicial "Coding For All".
company = "coding for all"
# imprime la variable company usando print().
print(company)
# imprime la longitud de la cadena company usando len() y print().
print(len(company))
# cambia todos los caracteres a mayúsculas usando upper().
print(company.upper())
# cambia todos los caracteres a minúsculas usando lower().
print(company.lower())
# usa los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# corta (slice) la primera palabra de la cadena Coding For All.
print(company[0:6])
# comprueba si la cadena Coding For All contiene la palabra Coding usando index, find u otros métodos.
print(company.index('coding')) 
print(company.find('coding'))
# reemplaza la palabra coding en la cadena 'Coding For All' por Python.
print(company.replace('coding', 'python'))
# cambia "Python for Everyone" a "Python for All" usando replace u otros métodos.
print(company.replace('python for everyone', 'python for all'))
# Otra forma: usar replace sobre la cadena original literal
print('Python for Everyone'.replace('Python for Everyone', 'Python for All'))
# Otra alternativa: usar split y join
words = 'Python for Everyone'.split()
words[-1] = 'All'
print(' '.join(words))
# divide la cadena 'Coding For All' usando el espacio como separador (split()).
words = 'coding for all'.split()
# divide la cadena "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" en las comas.
social_media = "facebook, google, microsoft, apple, IBM, oracle, amazon".split(",")
# ¿Cuál es el carácter en el índice 0 de la cadena Coding For All?
print(company[0])
# ¿Cuál es el último índice de la cadena Coding For All?
print(company[-1])
# ¿Qué carácter está en el índice 10 de la cadena "Coding For All"?
print(company[10])
# crea un acrónimo o abreviatura para el nombre 'Python For Everyone'.
acronimo = 'PFE'
# crea un acrónimo o abreviatura para el nombre 'Coding For All'.
acronimo_2 = 'CFA'
# usa index para determinar la posición de la primera aparición de C en Coding For All.
print(company.index("c"))
# usa index para determinar la posición de la primera aparición de F en Coding For All.
print(company.index("f"))
# usa rfind para determinar la posición de la última aparición de l en Coding For All People.
company_2 = 'coding for all people'
print(company_2.rfind('l'))
# usa index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
frase = 'you cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))
print(frase.find('because'))
# usa rindex para encontrar la posición de la última aparición de la palabra because en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
print(frase.rindex('because'))
# extrae la frase 'because because because' de la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
print(frase[31:54])
# encuentra la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))
# extrae la frase 'because because because' de la siguiente oración: 'You cannot end a sentence with because because because is a conjunction'
print(frase[31:54])
# ¿Comienza 'Coding For All' con la subcadena Coding?
print(company.startswith('Coding'))
# ¿Termina 'Coding For All' con la subcadena coding?
print(company.endswith('coding'))
# '   Coding For All      ', elimina los espacios a la izquierda y a la derecha de la cadena dada.
print(company.strip())
# ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
identificador1 = '30DaysOfPython'
identificador2 = 'thirty_days_of_python'
print(identificador1.isidentifier())
print(identificador2.isidentifier())
# La siguiente lista contiene los nombres de algunas librerías de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únelas usando un hash con espacio.
librerias = ['django', 'flask', 'bottle', 'pyramid', 'falcon']
print('# '.join(librerias))
# Usa la secuencia de escape de nueva línea para separar las siguientes oraciones.
fr1 = "Estoy disfrutando este desafío"
fr2 =  "Solo me pregunto qué sigue."
print(fr1 + "\n" + fr2)
# Usa la secuencia de escape de tabulación para escribir las siguientes líneas.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name \tAge \tCountry \tCity')
print('Eliut \t19 \tMexico \tAguascalientes')
# Usa el método de formateo de cadenas para mostrar lo siguiente:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))
# Haz lo siguiente usando métodos de formateo de cadenas:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')