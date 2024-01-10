#Guardar informacion en ficheros de forma permanente

import pickle


class Persona():
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        
        print("Se ha creado una persona nueva con el nombre de",self.nombre)
        
    
    def __str__(self):
        
        return "{} {} {}".format(self.nombre, self.genero, self.edad) #Se devuelve en forma de lista
    


class ListaPersonas():
    
    personas=[]
    
    def __init__(self):
        
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se han cargado {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío") #Esto lo hacemos para cuando el fichero está vacío y no se ha cargado nada
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
      
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicherosExternos()
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicherosExternos(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def MostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)



miLista = ListaPersonas()

persona = Persona("Sandra", "Fememino", 29)
miLista.agregarPersonas(persona)
miLista = ListaPersonas()

p2 = Persona("Antonio", "Masculino", 38)
miLista.agregarPersonas(p2)
miLista = ListaPersonas()

p3 = Persona("Ana", "Fememino", 19)
miLista.agregarPersonas(p3)
miLista = ListaPersonas()


miLista.MostrarInfoFicheroExterno()

