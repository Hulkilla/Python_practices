# Importar la carpeta donde dondesta los modulos que necesito
import sys
sys.path.insert(0,  'G:\Mi unidad\Programación_Data_Science\Python_Pildoras_Informaticas\Modularización'   )


#Modularización
from modulo_vehiculos import Vehiculos

miCoche1 = Vehiculos("Mazda", "MX5")

miCoche2 = Vehiculos("Seat", "Leon")

miCoche3 = Vehiculos("Renault", "Megane")

coches = [miCoche1, miCoche2, miCoche3]



fichero = open("losCoches", "wb")

import pickle

pickle.dump(coches, fichero)

fichero.close()

del(fichero)


fichero = open("losCoches", "rb")

misCoches = pickle.load(fichero)

fichero.close()


for c in misCoches:
    print(c.estado())


