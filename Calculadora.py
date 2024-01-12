from tkinter import *

raiz  = Tk()
raiz.title("Calculadora")
raiz.resizable(0,0)

miFrame = Frame()
miFrame.pack()
miFrame.config(bg = "azure")

# -------------- VARIABLES GLOBALES ----------- #

operacion = ""
resultado = 0
comas = FALSE
final_operacion = ""

# ------------------ PANTALLA --------------------------- #

numeroPantalla = StringVar()


pantalla = Entry(miFrame, width = 20, font=('Arial 24'), textvariable=numeroPantalla)
pantalla.grid(row = 0, column = 1, padx = 20, pady = 20, columnspan= 4, rowspan= 1)
pantalla.config(background="black", fg = "green1", justify="right")
    
# Necesitamos que la pantalla se expanda a las 4 columnas, para que no nos descuadre

# ------------------- Pulsaciones teclado ------------------------ #

def numeroPulsado(num):
    
    global operacion
    global comas
    
    if operacion !="":  #Para resetear la pantalla por si hemos pulsado un parametro de operacion
        numeroPantalla.set(num)
        operacion = ""
    else:
        if num == "." and comas == FALSE:
            numeroPantalla.set(numeroPantalla.get() + num)
            comas = TRUE
        elif num == "." and comas == TRUE:
            numeroPantalla.set(numeroPantalla.get())
        else:
            numeroPantalla.set(numeroPantalla.get() + num)
            
    # Esto lo que quiere decir es que primero con el get comprueba lo que hay en pantalla y luego le añade un num
    # y lo saca por pantalla
    # El num pulsado sería el que pulsemos con el botón
    # Date cuenta que estamos concatenando un string!!! Por eso se pueden utilizar los métodos set y get

# ------------------- BORRAR PANTALLA O SÓLO NUMEROS ------------- # 

def borrado_total():
    
    global operacion 
    global resultado
    global comas
    global final_operacion
    
    operacion = ""
    resultado = 0
    comas = FALSE
    final_operacion = ""
    numeroPantalla.set("")
    
    
def borrado_individual():
    
    numeroPantalla.set(numeroPantalla.get()[:-1]) #Para eliminar un sólo caracter
    
     
def borrado_parcial():

    global comas

#   numeroPantalla.set(numeroPantalla.get()[:-len(numeroPantalla.get())])
    numeroPantalla.set("")

    comas = FALSE



# ----------------- OPERACIONES --------------------- #

def suma(num):
    
    #Variables globales que sirven para todos los niveles del programa
    global operacion 
    global resultado
    global comas
    global final_operacion
    
    if resultado == 0:  # Tenemos que hacer esto si no queremos que el primer número que tengamos salga negativo
        resultado = float(num)
    else:
        resultado += float(num) #Aqui almacenamos el resultado de la cadena de numeros   
        
        
    comas = FALSE
    
    operacion = "suma" #PAra resetear en los numeros pulsados y empezar un numero nuevo
    
    final_operacion = "suma"
    
    numeroPantalla.set(str(resultado))


def resta(num):
    
    #Variables globales que sirven para todos los niveles del programa
    global operacion 
    global resultado
    global comas
    global final_operacion
    
    if resultado == 0:  # Tenemos que hacer esto si no queremos que el primer número que tengamos salga negativo
        resultado = float(num)
    else:
        resultado -= float(num) #Aqui almacenamos el resultado de la cadena de numeros
    
    comas = FALSE
    
    operacion = "resta" #PAra resetear en los numeros pulsados y empezar un numero nuevo
    
    final_operacion = "resta"   
    
    numeroPantalla.set(str(resultado))
    
    
    
def multiplicacion(num):
    
    #Variables globales que sirven para todos los niveles del programa
    global operacion 
    global resultado
    global comas
    global final_operacion
    
    if resultado == 0:  # Tenemos que hacer esto si no queremos que el primer número que tengamos salga negativo
        resultado = float(num)
    else:
        resultado *= float(num) #Aqui almacenamos el resultado de la cadena de numeros
    
    comas = FALSE
    
    operacion = "multiplicacion" #PAra resetear en los numeros pulsados y empezar un numero nuevo
    
    final_operacion = "multiplicacion"   
    
    numeroPantalla.set(str(resultado))
   

def division(num):
    
    #Variables globales que sirven para todos los niveles del programa
    global operacion 
    global resultado
    global comas
    global final_operacion
    
    
    try: 
        if resultado == 0:  # Tenemos que hacer esto si no queremos que el primer número que tengamos salga negativo
            resultado = float(num)
        
        else:
            resultado /= float(num) #Aqui almacenamos el resultado de la cadena de numeros
            
       
        comas = FALSE    
        operacion = "division"             
        final_operacion = "division"               
        numeroPantalla.set(str(resultado))
            
    except ZeroDivisionError:
            
        numeroPantalla.set("No se puede dividir entre 0")
        operacion = ""
        resultado = 0
        comas = FALSE
        final_operacion = ""
    

   
def result():
    
    global operacion
    global resultado
    global comas
    global final_operacion

    reseteo = FALSE
    
    if final_operacion == "suma":
        numeroPantalla.set(str(resultado+float(numeroPantalla.get()))) #Asi sumamos lo que hay en la pantalla más lo almacenado hasta el momento
    elif final_operacion == "resta":
        numeroPantalla.set(str(resultado-float(numeroPantalla.get())))
    elif final_operacion == "multiplicacion":
        numeroPantalla.set(str(resultado*float(numeroPantalla.get())))
    elif final_operacion == "division":
        try:
            numero = round(resultado/float(numeroPantalla.get()),9)
            numeroPantalla.set(str(numero)) #Aqui almacenamos el resultado de la cadena de numeros
        except ZeroDivisionError:
            numeroPantalla.set("No se puede dividir entre 0")
            final_operacion = "reseteo"
    elif final_operacion == "reseteo":
        borrado_total()
    



# --------------------- BOTONES DE BORRADO ------------------------------ -#


botonBorradoParcial = Button(miFrame, text = "CE", width = 3, bg = "azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:borrado_parcial())
botonBorradoParcial.grid(row=1, column = 2, pady = 10)

botonBorradoTotal = Button(miFrame, text = "C", width = 3, bg = "azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:borrado_total())
botonBorradoTotal.grid(row=1, column = 3, pady = 10)

botonBorradoIndividual = Button(miFrame, text = "<x", width = 3, bg = "azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:borrado_individual())
botonBorradoIndividual.grid(row = 1, column = 4, pady = 10)


    

# -------------------- PRIMERA FILA DE BOTONES: 7, 8, 9, / --------------- #

boton7 = Button(miFrame, text = "7", width = 3, bg="azure3" , padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("7"))
boton7.grid(row=2, column = 1, pady = 10)

boton8 = Button(miFrame, text = "8", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("8"))
boton8.grid(row=2, column = 2, pady = 10)

boton9 = Button(miFrame, text = "9", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("9"))
boton9.grid(row=2, column = 3, pady = 10)

botonDiv = Button(miFrame, text = "/", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2, column = 4, pady = 10)


# -------------------- SEGUNDA FILA DE BOTONES: 4, 5, 6, * --------------- #

boton4 = Button(miFrame, text = "4", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("4")) # el lambda sirve para que no se ejecute al inicio
boton4.grid(row=3, column = 1, pady = 10)

boton5 = Button(miFrame, text = "5", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("5"))
boton5.grid(row=3, column = 2, pady = 10)

boton6 = Button(miFrame, text = "6", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("6"))
boton6.grid(row=3, column = 3, pady = 10)

botonMult = Button(miFrame, text = "*", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column = 4, pady = 10)



# -------------------- TERCERA FILA DE BOTONES: 1, 2, 3, - --------------- #

boton1 = Button(miFrame, text = "1", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("1"))
boton1.grid(row=4, column = 1, pady = 10)

boton2 = Button(miFrame, text = "2", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("2"))
boton2.grid(row=4, column = 2, pady = 10)

boton3 = Button(miFrame, text = "3", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("3"))
boton3.grid(row=4, column = 3, pady = 10)

botonRest = Button(miFrame, text = "-", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column = 4, pady = 10)


# -------------------- CUARTA FILA DE BOTONES: 0, , , =, + --------------- #

boton0 = Button(miFrame, text = "0", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("0"))
boton0.grid(row=5, column = 1, pady = 10)

botonComa = Button(miFrame, text = ",", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:numeroPulsado("."))
botonComa.grid(row=5, column = 2, pady = 10)

botonIgual = Button(miFrame, text = "=", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:result())
botonIgual.grid(row=5, column = 3, pady = 10)

botonSuma = Button(miFrame, text = "+", width = 3, bg="azure3", padx = 10, pady = 10, font=('Arial 12'), command = lambda:suma(numeroPantalla.get())) 
#No hay que olvidarse del get porque es donde se ha almacenado toda la cadena de caracteres
botonSuma.grid(row=5, column = 4, pady = 10)



raiz.mainloop()

