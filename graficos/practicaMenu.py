from tkinter import *
from tkinter import messagebox #Hay que importarlo
from tkinter import filedialog

root = Tk()
root.resizable(1,1)
root.geometry("300x100") 

def infoAdicional():
    messagebox.showinfo("Procesador de Marina", "Programa de hacer cosas version 2023") # Nombre de la ventana emergente y el texto
                  
def LicenciaEstado():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def QuieresSalir():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    # askquestion devuelve yes o no  
    
    if valor == "yes":
        root.destroy()
    
    # valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    # y el valor devuelve TRUE o FALSE
    
def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

    if valor == False:
        root.destroy()


def abreFichero():
    fichero = filedialog.askopenfile(title = "Abrir", initialdir = "C:/", filetypes = (("Ficheros de Excel", ".xlsx"),("Ficheros de texto", ".txt"), ("Todos los ficheros", "*.*")))
    # filetypes necesita una tupla y se consigue con 2 parentesis, uno de los cuales va a llevar el texto del tipo de archivo y y su extensión. Como mínimo se necesitan 2 parámetros
    
    print(fichero)
    
Button(root, text = "Abrir fichero", command = abreFichero).pack()


barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height=300) #Hay que especificar que se cree el na raiz el menú


archivoMenu = Menu(barraMenu, tearoff=0) #Tearoff es para quitar un separador que sale y que queda raro
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir Archivo", command = abreFichero)
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label = "Salir", command = QuieresSalir)

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label = "Copiar")
edicionMenu.add_command(label = "Cortar")
edicionMenu.add_command(label = "Pegar")


herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label = "Licencia", command = LicenciaEstado)
ayudaMenu.add_command(label = "Acerca de...", command = infoAdicional)


#Forma de colocar el menú
barraMenu.add_cascade(label = "Archivo", menu=archivoMenu)
barraMenu.add_cascade(label = "Edición", menu=edicionMenu)
barraMenu.add_cascade(label = "Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)

root.mainloop()

