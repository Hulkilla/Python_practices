
class Empleado:
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self):
        return "{} que trabaja como {} tiene un salario mensual de {} €". format(self.nombre, self.cargo, self.salario)


ListaEmpleados = [
    
Empleado("Juan", "Director", 6700),
Empleado("María", "Presidente", 7500),
Empleado("Ana", "Administrativo", 2100),
Empleado("Antonio", "Secretaria", 2150),
Empleado("Mario", "Botones", 1800)
    
    ]

def calculo_comision(empleado):
    
    if empleado.salario <= 3000:
        empleado.salario = empleado.salario*1.03
    
    return empleado


ListaEmpleadosComision = map(calculo_comision, ListaEmpleados)

for comision in ListaEmpleadosComision:
    print(comision)
    

