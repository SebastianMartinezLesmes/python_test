from POO.reto_salud import persona

class empleado(persona):
    # atributos
    def __init__(self,cargo,valorHora,horasTrabajadas,departamento):
        self.cargo=cargo
        self.valorHora=valorHora
        self.horasTrabajadas=horasTrabajadas
        self.departamento=departamento
        self.pagoEmpleado=self.calcularHorarios()

    def __init__(self):
        self.empleado1 = empleado("", "", "", "", 0, 0, 0, "","",0,0,"",0)

    # metodos
    def pedirDatos(self):
        self.tipoDocumento=input('ingrese el tipo de documento del empleado: ')
        self.numeroDocumento=input('ingrese el numero: ')
        self.nombre=input('ingrese el nombre: ')
        self.apellido=input('ingrese el apellido: ')
        self.peso=float(input('ingrese su peso en kg: '))
        self.estatura=float(input('ingrese su altura en mts: '))
        self.edad=int(input('ingrese su edad: '))
        self.sexo=input('indique su sexo: ')
        self.cargo=input('indique el cargo del empleado: ')
        self.valorHora=float(input('ingrese cuanto va a pagarle al empleado por hora: '))
        self.horasTrabajadas=float(input('ingrese las horas que trabajo el empleado: '))
        self.departamento=input('indique el departamento del empleado: ')

    def calcularHorarios(self):
        valorTotal = self.valorHora * self.horasTrabajadas
        reteica = valorTotal * 0.00966
        honorarios = valorTotal - reteica
        return honorarios
    
    def mostrarEmpleado(self):
        print(f'\n {self.tipoDocumento} \n{self.nombre} \n{self.apellido} \n{self.cargo} \n{self.horasTrabajadas} \n{self.valorHora} \n{self.pagoEmpleado}')

