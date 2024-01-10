# La serialización sirve par ael manejo de archivos pero codificado en binario
# Porque asi la distribución es muhco más cómoda

# Biblioteca a usar: Pickle: https://docs.python.org/es/3/library/pickle.html
    # Metodo dump(): volcar los datos al fichero binario
    # Método load(): cargar los datos de lfichero binario 


import pickle
from io import open


lista_nombres = ["Pedro", "Ana", "María", "Isabel"]


#Crear un fichero que va a guardar la información en formato binario

fichero_binario = open("lista_nombres", mode="wb") #wb: write binary

pickle.dump(lista_nombres, fichero_binario) #Este fichero no se puede abrir de forma externa

fichero_binario.close()

del(fichero_binario)



#Abrir el fichero binario


fichero = open("lista_nombres", "rb") #rb: read binary

pickle.load(fichero)
