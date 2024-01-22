''' 
def area_triangulo(base,altura):
    
    return (base*altura)/2


Labmda: Función anónima
Este tipo de sintaxis sirven para funciones simples, porque así simplificamos la sinxtasis
Tambien se conocen como funciones on the go, on demand
'''

area_triangulo = lambda base,altura: (base*altura)/2

triangulo1 = area_triangulo(5, 7)
triangulo2 = area_triangulo(9, 6)

print(triangulo1)
print(triangulo2)


al_cubo = lambda numero: pow(numero,3) # = numero**3

print(al_cubo(133))


destacar_valor = lambda comision: "¡{}! €".format(comision)

comision_Ana = 15585

print(destacar_valor(comision_Ana))
