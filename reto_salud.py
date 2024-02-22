class persona:
    #atributos
    def __init__(self,tipoDocumento,numeroDocumento,nombre,apellido,peso,estatura,edad,sexo):
        self.tipoDocumento=tipoDocumento
        self.numeroDocumento=numeroDocumento
        self.nombre=nombre
        self.apellido=apellido
        self.peso=peso
        self.estatura=estatura
        self.edad=edad
        self.sexo=sexo

    #metodos
    def pedirDatos(self):
        self.tipoDocumento=input('ingrese el tipo de documento: ')
        self.numeroDocumento=input('ingrese el numero: ')
        self.nombre=input('ingrese el nombre: ')
        self.apellido=input('ingrese el apellido: ')
        self.peso=float(input('ingrese su peso en kg: '))
        self.estatura=float(input('ingrese su altura en mts: '))
        self.edad=int(input('ingrese su edad: '))
        self.sexo=input('indique su sexo: ')

    def mostrarDatos(self):
        print(f'Tipo de documento: {self.tipoDocumento} \nNumero de documento: {self.numeroDocumento} \nNombre: {self.nombre}\nApellido: {self.apellido}\nPeso: {self.peso}\nEstatura: {self.estatura}\nEdad: {self.edad}\nSexo: {self.sexo}')
  
    def calcularIMC(self):
        pesoActual=self.peso/(self.estatura**2)
        print(f'el ususario {self.nombre} {self.apellido} \nidentificado con el tipo de documento: {self.tipoDocumento} \n tiene un peso de {self.pesoActual}')
        return pesoActual

    def CalcularMayorEdad(self):
        if self.edad>=18:
            print('El usuario ya es mayor de edad')
        else:
            print('El usuario aun no es mayor de edad')

'''class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # atributo privado
        self._edad = edad  # atributo privado

    def get_nombre(self):
        
       
return self._nombre  # método público

    def set_nombre(self, nombre):
        
       
self._nombre = nombre  # método público

    def get_edad(self):
        return self._edad  # método público

    def set_edad(self, edad):
        self._edad = edad  # método público'''