# Loops o ciclos 
# * Ejercicios: Nivel 1
# Implementa iteraciones de 0 a 10 usando while y for.
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
for numer in numeros:
    print(numer) # ---> es una forma de hacerlo usando listas, la salida es la misma
for valor in range(11):
    print(valor) # ---> esta es usando rangos

count = 0
while count < 11:
    print(count)
    count = count + 1
# Implementa iteraciones de 10 a 0 usando while y for.
cont = 10
while cont >= 0:
    print(cont)
    cont = cont - 1
for i in range(10, -1, -1):
    print(i)
# Escribe un bucle que llame a print() 7 veces para producir este triángulo:
#
##
###
####
#####
######
#######
for i in range(1, 8):
    print("#" * i)
# Usa bucles anidados para producir la siguiente salida:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for table in range(8):
    for col in range(8):
        print("#", end=" ")  
    print()
# Usando un bucle, produce la siguiente salida:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for j in range(11):
    print(f'{j} x {j} = {j * j}')
# Recorre con for la lista ['Python', 'Numpy','Pandas','Django', 'Flask'] e imprime cada elemento.
skills = ['Python', 'Numpy','Pandas', 'Django', 'Flask']
for h in skills:
    print(h)
# Recorre con for de 0 a 100 e imprime todos los números pares.
for k in range(0, 101, 2):
    print(k)
# Recorre con for de 0 a 100 e imprime todos los números impares.
for e in range(0 ,101, 3):
    if e % 2 == 0:
        continue
    else:
        print(e)
# *Ejercicios: Nivel 2
# Usa un for para sumar los números de 0 a 100.
# The sum of all numbers is 5050.
total = 0
for suma in range(101):
    total = total + suma

print(f'la suma es {total}')
# Usa un for para sumar por separado los impares y los pares de 0 a 100.
# The sum of all odd numbers is 2500. And the sum of all even numbers is 2550.
pares = 0
impares = 0
for q in range(101):
    if q % 2 == 0:
        pares = pares + q
    else:
        impares = impares + q

print(f'la suma de los pares es {pares}')
print(f'la suma de los impares es {impares}')

# *Ejercicios: Nivel 3
# Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
paises = []
for pais in countries:
    if 'land' in pais:
        paises.append(pais)

print(paises)
# Dada la lista fruits = ['banana', 'orange', 'mango', 'lemon'], invierte los elementos usando un bucle.
fruits = ['banana', 'orange', 'mango', 'lemon']
for frutas in fruits:
    frutas_2 = fruits[::-1]

print(frutas_2)