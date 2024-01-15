
# Text: cuadro para escribir texto largos

# Buttom: Botones para interactuar con la interfaz

from tkinter import *

raiz  = Tk()
raiz.title("Introducción de botones")
raiz.config(bg="lightgoldenrodyellow")
raiz.geometry("300x300")



miFrame=Frame(raiz, width=200, height=500)
miFrame.pack()
miFrame.config(bg = "lightblue")


# Relación con el botón creado al final
minombre = StringVar()

# Cuadros de texto

cuadroNombre = Entry(miFrame, width = 21, textvariable=minombre) #con esto el cuadro está relacionado con la variable string "mi nombre"
cuadroNombre.grid(row= 0, column=1, padx=10, pady = 10)
cuadroNombre.config(fg = "red", justify = "center")

cuadroApellido = Entry(miFrame, width = 21)
cuadroApellido.grid(row= 1, column=1, padx=10, pady = 10)

cuadroDireccion = Entry(miFrame, width = 21)
cuadroDireccion.grid(row= 2, column=1, padx=10, pady = 10)

cuadroContraseña = Entry(miFrame, width = 21)
cuadroContraseña.grid(row= 3, column=1, padx=10, pady = 10)
cuadroContraseña.config(show="*") #De esta manera cuando vamos a escribir solo sale *

# Caja de texto grande

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 4, column = 1, padx=10, pady = 10)

# Necesitamos una scrollbar que nos ayude en la caja de texto grande

scrollvert = Scrollbar(miFrame, command = textoComentario.yview)
# Tenemos que decirle en que caja de comentario y si se va a mover en vertical u horizontal
scrollvert.grid(row = 4, column = 2, sticky = "nsew") 
#Ojo, como queremos que salga al lado derecho, lo podemos colocar en la siguiente columna del grid
# con el comando sitcky = "nsew" se adapta a la caja de comentarios

textoComentario.config(yscrollcommand = scrollvert.set)
#Con esta instrucción, la scrollbar se mueve con el texto y se queda fijado sin volver a la posición inicial



# Etiquetas de los cuadros de texto

nombreLabel = Label(miFrame, text ="Nombre: ")
nombreLabel.config(bg = "lightblue")
nombreLabel.grid(row= 0, column=0, sticky = "e", padx=10, pady = 10)

ApellidoLabel = Label(miFrame, text ="Apellido: ")
ApellidoLabel.config(bg = "lightblue")
ApellidoLabel.grid(row= 1, column=0, sticky = "e", padx=10, pady = 10)

DireccionLabel = Label(miFrame, text ="Dirección: ")
DireccionLabel.config(bg = "lightblue")
DireccionLabel.grid(row= 2, column=0, sticky = "e", padx=10, pady = 10)

ContraseñaLabel = Label(miFrame, text ="Contraseña: ")
ContraseñaLabel.config(bg = "lightblue")
ContraseñaLabel.grid(row= 3, column=0, sticky = "e", padx=10, pady = 10)


# Texto largo que puede introducir el usuario

ComentariosLabel = Label(miFrame, text ="Comentarios: ")
ComentariosLabel.config(bg = "coral1")
ComentariosLabel.grid(row= 4, column=0, sticky = "ne", padx=10, pady = 10)


# Mi primer botón


def codigoBoton():
    minombre.set("Marina")
    
# Al dar a enviar, sale el nombre anterior en el cuadro de "Nombre: "

botonEnvio = Button(raiz, text = "Enviar", border= 3, command= codigoBoton)
botonEnvio.pack() 




raiz.mainloop()