def areaTriangulo(base, altura):
    
    """
    Esta función calcula el area del triángulo a partir de su base y su altura
    
    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'
    >>> areaTriangulo(4,5)
    'El área del triángulo es: 11.0'
    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13.5'

    """ 
    # >>> la función con lso argumentos que va a testear
    # Resultado lógico en función de lo que debe devolver.

    return "El área del triángulo es: " + str((base*altura)/2)


import doctest
doctest.testmod()


# Como ver la documentación de una función: 
# print(areaTriangulo.__doc__)
# help(areaTriangulo)

# print(areaTriangulo(2,4))