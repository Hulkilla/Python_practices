
#Importar desde el paquete "calculos" el modulo calculos_generales:
    
from calculos.calculos_generales import dividir

dividir(3,2)


from calculos.calculos_generales import potencia

potencia(3,2)


# Y ahora una de las carpetas de las que hemos creado

# paquete -- subpaquete -- modulo de operacion
from calculos.basicos.operaciones_basicas import sumar

sumar(3,4)


from calculos.redondeo_potencia.redondeo_y_potencia import potencia

potencia(3,8)