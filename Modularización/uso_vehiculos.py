from modulo_vehiculos import *

miCoche = Vehiculos("Mazda", "MX5")

miCoche.estado()


#¿Qué ocurre si el modulo_vehículos está en otra carpeta?
#El programa no funciona porque está buscando el modulo en el mismo directorio
#Si no está en el mismo directorio, lo busca en el syspath

#Para solucionar este problema hay que utilizar los paquetes que vienen en python