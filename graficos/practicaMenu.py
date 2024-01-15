from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height=300) #Hay que especificar que se cree el na raiz el menú


archivoMenu = Menu(barraMenu, tearoff=0) #Tearoff es para quitar un separador que sale y que queda raro
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar")
archivoMenu.add_command(label = "Salir")

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label = "Copiar")
edicionMenu.add_command(label = "Cortar")
edicionMenu.add_command(label = "Pegar")


herramientasMenu = Menu(barraMenu, tearoff=0)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label = "Licencia")
ayudaMenu.add_command(label = "Acerca de")


#Forma de colocar el menú
barraMenu.add_cascade(label = "Archivo", menu=archivoMenu)
barraMenu.add_cascade(label = "Edición", menu=edicionMenu)
barraMenu.add_cascade(label = "Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)

root.mainloop()

