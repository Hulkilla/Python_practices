# Librerias para inferfaces gráficas:
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
    # 1,1: Se pueden redimensionar ambos par�metros


#icono en la barra del t�tulo --> Necesario en formato ".ico"

raiz.iconbitmap("590780.ico")

# Tama�o por defecto

raiz.geometry("650x350") # Ancho x largo

# Cambiar el color del fondo

raiz.config(bg="lightgoldenrodyellow")



# La siguiente funci�n debe estar siempre al final:

raiz.mainloop() # Esta instruccion es necesaria para que la ventana est� siempre ejecutada

# Referencia: https://docs.python.org/es/3/library/tk.html





