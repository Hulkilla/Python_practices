from tkinter import *
from PIL import Image, ImageTk

root  = Tk()


root.title("Imagenes y texto")

root.resizable(1,1)

miFrame = Frame(root, width = 500, height = 500)

miFrame.pack()


# MiImagen = PhotoImage(file = "giphy.gif") --> Aqui la cargamos tal cual
# PhotoImage es para imagenes en formatos PGM, PPM, GIF y PNG

# Con el siguiente subcódigo podemos redimensionar la imagen
img = Image.open("590780.png")

img = img.resize((45, 45), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)

Label(miFrame, image = img).place(x = 250, y = 50)


miLabel = Label(miFrame, 
                text="Hola, Harry Potter. Soy Tom Riddle, ¿Quieres saber quien soy?", 
                fg="red", 
                font = ("Comic Sans MS", 9))
#Respecto al tipo de letra, debe estar bien escrito. Se puede checkear en el word para saber cuales tenemos instaladas

miLabel.place(x = 100, y = 100) #Nos permite ubicar el texto en función de las coordenadas x,y que pongamos
# Las coordenadas se miden el pixeles y la x es de izq a der y la y de arr a abajo



# Otra opción: 
# miLabel = Label(miFrame, text="Hola, Harry Potter. Soy Tom Riddle, ¿Quieres saber quien soy?").place(x = 100, y = 200)
# Esto se hace si no vas a usar la Label más que una vez






root.mainloop()