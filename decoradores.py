def funcion_decoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs): 
        
        """ Para que reciba un número indeterminado de parámetros *args.
            kwargs nos sirve para cuando nosotros espeficamos que es algo tipo(base = ), argumentos con clave valor"""
            
        #Acciones adicionales que decoran
        print("Se va a realizar un cálculo: ")
        
        funcion_parametro(*args, **kwargs) #Aqui también hay que indicarlo
        
        #Acciones adicionales que decoran
        print("Se ha ejecutado correctamente el cálculo")

    return funcion_interior
#La función decoradora devuelve otra función


#@funcion_decoradora #Con esto yo le indico al programa de que me decore la función suma. 
def suma(num1, num2, num3):
    """ Calcula la suma de 3 números pasados por parámetros """
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora    
def potencia(base, exponente):
    print(pow(base, exponente))
    
suma(7,5,8)
resta(12,10)
potencia(base = 5, exponente = 4)

print(suma.__doc__)
help(suma)
help(funcion_decoradora)
