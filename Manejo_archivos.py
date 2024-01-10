 # Trabajar con archivos externos

# Se trata de que los datos no se pierdan y hay y alternativas: archivos externos y BBDD

# Fases necesarias para la manipulación de archivos: Creación, apertura, manipulación y cierre

# Documentación: https://docs.python.org/es/3/library/io.html

from io import open

#creación y apertura

archivo_texto = open("archivo.txt", mode = "w") #w: write


#Manipulación

frase = "Estupendo día para estudiar Python \n el miércoles"

archivo_texto.write(frase)


#Cierre

archivo_texto.close()



# Abrir en modo lectura

archivo_texto = open("archivo.txt", mode = "r") # r:read 

texto = archivo_texto.read()

archivo_texto.close()

print(texto)



# Leer por lineas

archivo_texto = open("archivo.txt", mode = "r") #w: write, r:read 

texto_lista = archivo_texto.readlines()

archivo_texto.close()

print(texto_lista)
print(texto_lista[1])


# Lo devuelve entre corchetes --> Es una tupla



# Introducir nuevo texto

archivo_texto = open("archivo.txt", mode = "a") #a: append

archivo_texto.write("\n siempre es una buena ocasión para estudiar Python jeje")

archivo_texto.close()



# Uso de la posición del puntero en el archivo de texto

# Por defecto está en posición 0

archivo_texto = open("archivo.txt", mode = "r")

archivo_texto.read()

# cuando la función termina de leer, el puntero se queda en la posición final del texto

#Como luego ya no hay nada, si intentamos volver a leer o a hacer otra función, no hace nada porque ya es un texto vacío



# ¿cómo se situa el puntero?

archivo_texto.seek(11) # Con esto los primeros 11 caracteres no se tienen en cuenta

archivo_texto.read()

archivo_texto.seek(0)

archivo_texto.read(11) # Aquí por ejemplo, solo imprime los primeros 11 caracteres




# Colocar el puntero en la mitad de todos los caracteres que hay en el texto
archivo_texto.seek(0)

archivo_texto.seek(len(archivo_texto.read())/2)

# y una vez colocado el puntero, el texto lee la mitad final del archivo
archivo_texto.read()




# Colocarlo al final de la primera línea

archivo_texto.seek(0)

archivo_texto.seek(len(archivo_texto.readline()))

# y una vez colocado el puntero, el texto lee las otras dos lineas
archivo_texto.read()

archivo_texto.close()


# Método de escrituta y lectura


archivo_texto = open("archivo.txt", mode = "r+") #r+: read and write

# El texto que ahora está esrito va a ser sustituido porque no hemos colocado el puntero al final
archivo_texto.write("Comienzo del texto")

archivo_texto.seek(0)
archivo_texto.read()

# ¿como eliminar el comando de saltos de líneas "\n"?


archivo_texto.seek(0)

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta línea ha sido incluido desde el exterior \n"


archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()













