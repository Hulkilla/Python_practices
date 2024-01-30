def compruebaMail(mailUsuario):

    """
    La función compruebaMail evalua un mail recibido 
    en busca de la @. si tiene una @ es correcto, pero si tiene
    más de una @ es incorrecto, y si la @ está al final también es incorrecto
    
    >>> compruebaMail('marina@estudiante.es')
    True

    >>> compruebaMail('marinaestudiante.es@')
    False

    >>> compruebaMail('marinaestudiante.es')
    False

    >>> compruebaMail('marina@estudiante.es@')
    False

    """

    arroba = mailUsuario.count('@')

    if (arroba !=1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0):
        return False
    else: 
        return True

import doctest
doctest.testmod()