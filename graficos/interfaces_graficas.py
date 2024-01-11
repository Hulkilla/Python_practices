# Librerias para inferfaces grÃ¡ficas:
    # Tkinter
    # WxPython
    # PyQT
    # PyGTK

# Referencia: https://docs.python.org/es/3/library/tk.html

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

raiz.geometry("700x400") # Ancho x largo 
#La raiz se adpata al tampo del frame que tenga incorpotado por lo que no hace falta indicarlo

# Cambiar el color del fondo

raiz.config(bg="lightgoldenrodyellow")



# Creacion del primer Frame

miFrame = Frame()

#Con Esto metemos el frame dentro de mi ventana
miFrame.pack(side = "left", anchor= "n") 
    #side: primera posición
    #anchor = segunda, posición

# rellenar el espacio en horizontal:
# miFrame.pack(side = "bottom", fill="x") 

#En vertical:
# miFrame.pack(fill="y", expand=TRUE) 

#En ambas:
#miFrame.pack(fill="both", expand=TRUE) 


miFrame.config(bg = "lightblue")

miFrame.config(width = "650", height="350")
#└Este tamaño no se adapta como la raiz. Este tamaño es fijo

# Contorno del frame:
    
miFrame.config(bd = 35)

miFrame.config(relief="groove")


#cambiar el cursor dentro de la mano

miFrame.config(cursor="pirate")



# La siguiente función debe estar siempre al final:

raiz.mainloop() # Esta instruccion es necesaria para que la ventana esté siempre ejecutada







