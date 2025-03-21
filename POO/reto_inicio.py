from POO.reto_salud import persona
class inicio:

    def __init__(self):
        self.persona1 = persona("", "", "", "", 0, 0, 0, "")
        self.persona2 = persona("", "", "", "", 0, 0, 0, "")

    def a(self):
        print('ingrese los datos del usuario 1')
        self.persona1.pedirDatos()

        print('Datos del usuario 1')
        self.persona1.mostrarDatos()

        if self.persona1.calcularIMC()<20 :
            print('El IMC del usuario 1 esta debajo del ideal')
        elif 20<= self.persona1.calcularIMC() <=25 :
            print('El IMC del usuario 1 es el ideal')
        else:
            print('El IMC del usuario 1 esta encima del ideal')
        self.persona1.calcularIMC()

        print(self.persona1.CalcularMayorEdad)

        print('ingrese los datos del usuario 2')
        self.persona2.pedirDatos()

        print('Datos del usuario 2')
        self.persona2.mostrarDatos()

        if self.persona2.calcularIMC()<20 :
            print('El IMC del usuario 2 esta debajo del ideal')
        elif 20<= self.persona2.calcularIMC() <=25 :
            print('El IMC del usuario 2 es el ideal')
        else:
            print('El IMC del usuario 2 esta encima del ideal')
        self.persona2.calcularIMC()

        print(self.persona2.CalcularMayorEdad)
inicio = inicio()
inicio.a()