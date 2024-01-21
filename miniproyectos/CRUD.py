from tkinter import *
from tkinter import messagebox 
import sqlite3


##################### FUNCIONES DE LA INTERFAZ ############################

def conexionBBDD():
    
    try:
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        miCursor.execute('''
                    CREATE TABLE DATOSUSUARIOS(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE_USUARIO VARCHAR(50),
                     APELLIDO VARCHAR(10),
                     DIRECCION VARCHAR(50),
                     PASSWORD VARCHAR(50),
                     COMENTARIOS VARCHAR(100))
                     ''')
        
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def salirAplicacion():

    valor = messagebox.askquestion("Salir", "¿Quieres salir de la aplicación?")

    if valor == "yes":
        root.destroy()


def limpiarCampos():

    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    cuadroComentario.delete(1.0, END)

def Crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    listaUsuarios = (miNombre.get(), miApellido.get(), miDireccion.get(), miPass.get(), cuadroComentario.get(1.0, END))
    # Al texto hay que decirle de donde quiere coger los caracteres
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", listaUsuarios)

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")


def LeerRegistro():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = " + miID.get())
    miConexion.commit()

    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miDireccion.set(usuario[3])
        miPass.set(usuario[4])
        cuadroComentario.insert(1.0, END)

   
def Actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    listaUsuarios = (miNombre.get(), miApellido.get(), miDireccion.get(), miPass.get(), cuadroComentario.get(1.0, END))
    # Al texto hay que decirle de donde quiere coger los caracteres
    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + 
                    "', APELLIDO = '" + miApellido.get() +
                    "', DIRECCION = '" + miDireccion.get() +
                    "', PASSWORD = '" + miPass.get() +
                    "', COMENTARIOS = '" + cuadroComentario.get("1.0", END) +
                    "' WHERE ID =" + miID.get())"""

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO= ?, APELLIDO = ?, DIRECCION = ?, PASSWORD = ?, COMENTARIOS = ?" +
                    "WHERE ID=" + miID.get(), (listaUsuarios))
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def Borrar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "El registro se ha eliminado con éxito")




########################## INTERFAZ GRÁFICA ############################

root  = Tk()
root.title("CRUD")
root.resizable(0,0)
root.config(bg = "white")

##################### Barra de menu de la aplicacion #######################

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 3000, height = 100)

bbddMenu = Menu(barraMenu, tearoff = 0)
bbddMenu.add_command(label = "Conectar", command = conexionBBDD)
bbddMenu.add_command(label = "Salir", command = salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff = 0)
borrarMenu.add_command(label = "Borrar campos", command = limpiarCampos)

CRUDMenu = Menu(barraMenu, tearoff = 0)
CRUDMenu.add_command(label = "Crear", command = Crear)
CRUDMenu.add_command(label = "Leer", command = LeerRegistro)
CRUDMenu.add_command(label = "Actualizar", command = Actualizar)
CRUDMenu.add_command(label = "Borrar", command = Borrar)

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "Licencia")
ayudaMenu.add_command(label = "Acerca de ...")

barraMenu.add_cascade(label = "Base de Datos", menu=bbddMenu)
barraMenu.add_cascade(label = "Borrar", menu=borrarMenu)
barraMenu.add_cascade(label = "CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)


######################## Frame para la Base de datos ##########################


miFrame = Frame(root)
miFrame.pack()
miFrame.config(bg = "lightblue")

## inditificacion de cada variable

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

## cajas de entrada de datos

cuadroID = Entry(miFrame, textvariable = miID)
cuadroID.grid(row = 0, column = 1, padx = 10, pady = 10)

cuadroNombre = Entry(miFrame, textvariable = miNombre)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)
cuadroNombre.config(fg = "red", justify = "right")

cuadroApellido = Entry(miFrame, textvariable = miApellido)
cuadroApellido.grid(row = 2, column = 1, padx = 10, pady = 10)

cuadroPass = Entry(miFrame, textvariable = miPass)
cuadroPass.grid(row = 4, column = 1, padx = 10, pady = 10)
cuadroPass.config(show= "*")

cuadroDireccion = Entry(miFrame, textvariable = miDireccion)
cuadroDireccion.grid(row = 3, column = 1, padx = 10, pady = 10)

cuadroComentario = Text(miFrame, width = 16, height = 5)
cuadroComentario.grid(row = 5, column = 1, padx=10, pady = 10)
scrollvert = Scrollbar(miFrame, command = cuadroComentario.yview)
scrollvert.grid(row = 5, column = 2, sticky = "nsew") 

cuadroComentario.config(yscrollcommand = scrollvert.set)

### Labels para los cuadros de comentarios

idLabel = Label(miFrame, text ="ID: ")
idLabel.config(bg = "lightblue")
idLabel.grid(row= 0, column=0, sticky = "e", padx=10, pady = 10)

nombreLabel = Label(miFrame, text ="Nombre: ")
nombreLabel.config(bg = "lightblue")
nombreLabel.grid(row= 1, column=0, sticky = "e", padx=10, pady = 10)

apellidoLabel = Label(miFrame, text ="Apellido: ")
apellidoLabel.config(bg = "lightblue")
apellidoLabel.grid(row= 2, column=0, sticky = "e", padx=10, pady = 10)

direccionLabel = Label(miFrame, text ="Dirección: ")
direccionLabel.config(bg = "lightblue")
direccionLabel.grid(row= 3, column=0, sticky = "e", padx=10, pady = 10)

passLabel = Label(miFrame, text ="Contraseña: ")
passLabel.config(bg = "lightblue")
passLabel.grid(row= 4, column=0, sticky = "e", padx=10, pady = 10)


ComentarioLabel = Label(miFrame, text ="Comentarios: ")
ComentarioLabel.config(bg = "lightblue")
ComentarioLabel.grid(row= 5, column=0, sticky = "ne", padx=10, pady = 10)


############################ Segundo Frame: Botones CRUD ##############################

miFrame2 = Frame(root)
miFrame2.pack()
miFrame2.config(bg = "white")

botonCrear = Button(miFrame2, text  ="Create", command = Crear)
botonCrear.grid(row= 1, column=0, sticky = "e", padx=10, pady = 10)

botonLeer = Button(miFrame2, text  ="Read", command = LeerRegistro)
botonLeer.grid(row= 1, column=1, sticky = "e", padx=10, pady = 10)

botonActualizar = Button(miFrame2, text  ="Update", command = Actualizar)
botonActualizar.grid(row= 1, column=2, sticky = "e", padx=10, pady = 10)

botonBorrar = Button(miFrame2, text  ="Delete", command = Borrar)
botonBorrar.grid(row= 1, column=3, sticky = "e", padx=10, pady = 10)



########################## Fin de la interface #####################################

root.mainloop()