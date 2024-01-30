import math

def raizCuadrada(listaNumeros):

    """
    Esta función devuelve una lista con la raiz cuadra de los elementos numéricos pasados por parámetros en otra lista
    
    >>> lista =[]
    >>> for i in [4,9,16]: 
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]


    >>> lista =[]
    >>> for i in [4,9,16,50,78,-90,125]: 
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    
    """
    # como la lista esta anidada en el bucle for, hay que poner los 3 puntos (...)
    # con la lista negativa nos tiene que devolver una primera y una ultima linea obligatorias, pero en el medio con los ... indicamos que nos da igual lo que haya dentro

    return [math.sqrt(n) for n in listaNumeros]


print(raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()