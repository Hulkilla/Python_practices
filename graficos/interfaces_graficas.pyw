# Librerias para inferfaces grÃ¡ficas:
    # Tkinter
    # WxPython
    # PyQT
    # PyGTK

from tkinter import *

raiz  = Tk()

#Cambiar la pantalla que viene por defecto

raiz.title("Ventana de prueba")

raiz.resizable(1,1) #widht, #height: tipo booleano
    
    # 0,0: No se puede redimensionar ni el ancho ni el alto
    # 1,0
    # 0,1    
    # 1,1: Se pueden redimensionar ambos parámetros


#icono en la barra del título --> Necesario en formato ".ico"

raiz.iconbitmap("590780.ico")

# Tamaño por defecto

raiz.geometry("650x350") # Ancho x largo

# Cambiar el color del fondo

raiz.config(bg="lightgoldenrodyellow")



# La siguiente función debe estar siempre al final:

raiz.mainloop() # Esta instruccion es necesaria para que la ventana esté siempre ejecutada

# Referencia: https://docs.python.org/es/3/library/tk.html





