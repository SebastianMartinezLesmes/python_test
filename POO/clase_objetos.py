class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas  

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

# Uso de la clase
estudiante1 = Estudiante("Carlos", 20, [85, 90, 78])
print(f"Estudiante:{estudiante1.nombre} \nEdad:{estudiante1.edad} \nNotas:{estudiante1.notas}\n\n")
print(f"{estudiante1.nombre} tiene un promedio de {estudiante1.calcular_promedio():.2f}")
