import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de programación sencillo"

print(re.search("aprender", cadena)) #re.sreach devuelve un objeto

textoBuscar = "aprender"

textoEncontrado = re.search("aprender", cadena)

if textoEncontrado is not None:

    print("He encontrado el texto")

else:

    print("No he encontrado no")

print("El texto", textoBuscar, "empieza en el caracter nº", textoEncontrado.start(), "y termina en el caracter nº", textoEncontrado.end())

textoEncontrado.span() #Nos delvuelve una tupla con el principio y el fin de donde está el caracter

textoBuscado = "Python"

print(len(re.findall(textoBuscado, cadena)))


#Metacaracteres
lista_nombre = ['Ana Gómez',
                'María Martín',
                'Sandra López',
                'Santiago Martín',
                'Sandra Fernández']


for elemento in lista_nombre:
    if re.findall('^Sandra',elemento): # ^nos indica que el caracter debe empezar por lo que nos pongamos después
        print(elemento)


for elemento in lista_nombre:
    if re.findall('Martín$',elemento): # $nos indica que el caracter debe terminar por lo que nos pongamos antes
        print(elemento)


lista_dominios = ['http://pildorasinformaticas.es',
                'ftp://pildorasinformaticas.es',
                'http://pildorasinformaticas.com',
                'ftp://pildorasinformaticas.com',
                'http:informaticaenespaña.es']

for elemento in lista_dominios:
    if re.findall('es$',elemento): 
        print(elemento)

for elemento in lista_dominios:
    if re.findall('^ftp',elemento): 
        print(elemento)


for elemento in lista_dominios:
    if re.findall('[ñ]',elemento): # [] nos dice si hay elementos que contengan esa letra
        print(elemento)


lista_personas = ['hombres',
                  'mujeres',
                  'niños',
                  'niñas']

for elemento in lista_personas:
    if re.findall('niñ[oa]s',elemento): # [] 
        print(elemento)

lista = ['camión',
         'camion',
         'coche',
         'azucar']

for elemento in lista:
    if re.findall('cami[oó]n',elemento): # [] 
        print(elemento)


lista_nombres = ['Ana',
                 'Pedro',
                 'María',
                 'Rosa',
                 'Sandra',
                 'Celia']

for elemento in lista_nombres:
    if re.findall('^[O-T]',elemento): # [-]  Devuelve todos los nombres que tengan una letra comprendida entre la o y la t. Distingue entre la minus y la mayus

        print(elemento)

for elemento in lista_nombres:
    if re.findall('[o-t]$',elemento): # [-]  Devuelve todos los nombres que tengan una letra comprendida entre la o y la t. Distingue entre la minus y la mayus

        print(elemento)

lista_codigos = ['Ma1',
                 'Se1',
                 'Ma2',
                 'Ba1',
                 'Ma3',
                 'Va1',
                 'Ma4',
                 'Va2',
                 'MaA',
                 'Ma.5',
                 'MaB',
                 'Ma:C']


for elemento in lista_codigos:
    if re.findall('Ma[0-3]',elemento): # [-] También sirve con números

        print(elemento)


for elemento in lista_codigos:
    if re.findall('Ma[^0-3]',elemento): # [^ - ] Lo niega y debería devolver otro número

        print(elemento)

for elemento in lista_codigos:
    if re.findall('Ma[0-3A-B]',elemento): # [-] También sirve con números

        print(elemento)

for elemento in lista_codigos:
    if re.findall('Ma[.:]',elemento): # [-] También sirve con otros caracteres
        print(elemento)



    

nombre1 ="Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "Jara Fernández"
nombre5 = "Lara Fernández"

# Función Match: cruza las cadenas de caracteres para ver si EMPIEZAN igual

if re.match("Sandra", nombre4, re.IGNORECASE): #ignorecase ignora mayus y minus
    print("Hemos encontrado el nobmre")
else:
    print("No hemos encontrado nada")


if re.match(".ara", nombre5, re.IGNORECASE): # . Ignora la primera letra
    print("Hemos encontrado el nobmre")
else:
    print("No hemos encontrado nada")


cadena1 ="Jara López"
cadena2 = "3454564534"
cadena3 = "a645645645"

if re.match("\d", cadena2): # \ identifica si la cadena empieza por número
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado nada")


# Función Search: mira las cadenas de caracteres para ver si  coinciden en cualquier punto de la cadena

if re.search("López", nombre1, re.IGNORECASE): #ignorecase ignora mayus y minus
    print("Hemos encontrado el apellido")
else:
    print("No hemos encontrado nada")


código1 = "dfhytiwuntoefweltu71dflgihudflgjdrg"
código2 = "dsgldf71lsgjudñgodgjñsgjñdhdgdghldbjdg"
código3 = "fñgidglñdfgkjd vld"

if re.search("71", código1, re.IGNORECASE): #ignorecase ignora mayus y minus
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado nada")
