
# Las siguientes funciones van a estar dentro de mi modulo de funciones llamado "calculos"
# Para que python entienda que tenemos un pauqete de funciones tenemos que generar un archivo 
# cuyo título sea __init__.py


def sumar(op1,op2):
    print("El resultado de la suma: ", op1+op2)
    
    
def restar(op1,op2):
    print("El resultado de la resta: ", op1-op2)


def multiplicar(op1,op2):
    print("El resultado de la multiplicación: ", op1*op2)


def dividir(dividendo,divisor):
    print("El resultado de la división: ", dividendo/divisor)


def potencia(base,exponente):
    print("El resultado de la potencia: ", base**exponente)
    

def redondear(numero):
    print("El resultado del redondeo: ", round(numero))