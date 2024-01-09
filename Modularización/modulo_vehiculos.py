#Superclase
class Vehiculos():

  def __init__(self, marca, modelo):

    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):

    self.enmarcha = True

  def acelerar(self):
    self.acelera = True

  def frenar(self):
    self.frena = True

  def estado(self):
    print(""" Marca:""", self.marca, """
 Modelo:""", self.modelo, """
 En marcha:""", self.enmarcha, """
 Acelerando:""", self.acelera, """
 Frenando:""", self.frena)
 

#Subclase de Vehículos: Furgoneta

class Furgoneta(Vehiculos):

  def carga(self, cargar):
    self.cargado = cargar
    if(self.cargado): #Recuerda, si no pone nada es igual a True
      return " La furgoneta está cargada"
    else:
      return " La furgoneta no está cargada"




# Subclase de Vehículos: Moto

class Moto(Vehiculos):
  def __init__(self, marca, modelo, cilindrada):
    super().__init__(marca, modelo) #Esto viene de la superclase anterior. Por eso se pone el super().__init__
    self.cilindrada = cilindrada #Y esto es propio de la moto, por lo que va unicamente con el self.

  Hcaballito=""
  def caballito(self):
    self.Hcaballito="Haciendo el caballito"

  def estado(self): #Como tenemos nuevas cosas en el estado, este se sobreescribe al método general de la superclase Vehíchulos

    super().estado()
    print(""" Cilindrada:""", self.cilindrada, """
 """,self.Hcaballito)
 
 

 # Clase nueva: Vehículos eléctricos

class VElectricos(Vehiculos):
  def __int__(self, marca,modelo):

    super().__init__(marca,modelo)

    self.autonomia = 100

  def cargarEnergia(self):
    self.cargando = True
    


# Subclase de vehículos y vehículos electricos: Bicicleta eléctrica
# Herencia multiple

class BicicletaElectrica(VElectricos, Vehiculos):
  pass
 