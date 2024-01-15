from tkinter import *

root = Tk()
root.geometry("200x100")
root.resizable(0,0)

#Los Radiobuttons sirven para hacer apartados de selecciones Ej.

varOpcion = IntVar() #Una variable entera que irá cambiando a lo largo de todo el programa


def imprimir():
    
    # print(varOpcion.get())
    #No hay que olvidarse del get porque sino no puede leerse el IntVar
    #El IntVar es una variable entera de la librería tkinter y está asociada con cada radiobutton
    #cuando pulsamos un radiobutton, la variable varOption coje el valor asociado de dicho radiobutton
    #Con la función podemos mandar el valor a que lo saque por pantalla
    
    if varOpcion.get() == 1:
        etiqueta.config(text ="Has elegido masculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text ="Has elegido femenino")
    else:
        etiqueta.config(text = "Has elegido helicóptero apache")


Label(root, text ="Género: ", justify=LEFT)

Radiobutton(root, text="Masculino", variable = varOpcion, value = 1, command = imprimir, justify=LEFT).grid(row=1, sticky="W")
#El value nos va a dar un valor en cada botón, cada radiobutton tiene su propio valor y están referenciados al intvar


Radiobutton(root, text="Femenino", variable = varOpcion, value = 2, command = imprimir, justify= LEFT).grid(row=2, sticky="W")



Radiobutton(root, text="Helicóptero Apache", variable = varOpcion, value = 3, command = imprimir, justify= LEFT).grid(row=3, sticky="W")



etiqueta = Label(root)
etiqueta.grid(row=4, sticky="W")




root.mainloop()