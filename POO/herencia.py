class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        return f"Gerente: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento}"

# Uso de las clases
empleado1 = Empleado("Ana", 3000)
gerente1 = Gerente("Luis", 5000, "Ventas")

print(empleado1.mostrar_info())
print(gerente1.mostrar_info())
