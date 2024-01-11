
from tkinter import *

raiz  = Tk()
raiz.title("Introducción de datos")
raiz.config(bg="lightgoldenrodyellow")
raiz.geometry("700x600")

miFrame=Frame(raiz, width=500, height=600)
miFrame.pack()
miFrame.config(bg = "lightblue")


cuadroTexto = Entry(miFrame)
# cuadroTexto.place(x = 100, y = 100) #Colocarlo asi es horrible
cuadroTexto.grid(row= 0, column=1, padx=10, pady = 10)
#grid(row, column) --> Empieza en el (0,0)


cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row= 0, column=1, padx=10, pady = 10)
cuadroNombre.config(fg = "red", justify = "center")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row= 1, column=1, padx=10, pady = 10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row= 2, column=1, padx=10, pady = 10)

cuadroContraseña = Entry(miFrame)
cuadroContraseña.grid(row= 3, column=1, padx=10, pady = 10)
cuadroContraseña.config(show="*") #De esta manera cuando vamos a escribir solo sale *

nombreLabel = Label(miFrame, text ="Nombre: ")
nombreLabel.config(bg = "lightblue")
#nombreLabel.place(x = 45, y = 100) #Hay que calcularlo para que quede bien al lado del cuadro de texto
nombreLabel.grid(row= 0, column=0, sticky = "e", padx=10, pady = 10)

#Lo más facil es hacerlo con la función grid() para colocar elementos
# Al gridear el frame, este ya no tiene en cuenta el tamaño que das, sino que se adapta

#La propiedad sticky nos deja alinear el texto, utilizando los puntos cardinales
# n, ne, e, se, s, sw, w, nw y si no dices nada, se te pone en el centro

#el pad (x o y) nos marca la distancia que tiene que haber entre lo de dentro del grid y el borde


ApellidoLabel = Label(miFrame, text ="Apellido: ")
ApellidoLabel.config(bg = "lightblue")
ApellidoLabel.grid(row= 1, column=0, sticky = "e", padx=10, pady = 10)

DireccionLabel = Label(miFrame, text ="Dirección de casa: ")
DireccionLabel.config(bg = "lightblue")
DireccionLabel.grid(row= 2, column=0, sticky = "e", padx=10, pady = 10)

ContraseñaLabel = Label(miFrame, text ="Contraseña: ")
ContraseñaLabel.config(bg = "lightblue")
ContraseñaLabel.grid(row= 3, column=0, sticky = "e", padx=10, pady = 10)
















raiz.mainloop()