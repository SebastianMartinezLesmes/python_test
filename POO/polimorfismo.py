from math import pi

class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

# Uso de las clases
figuras = [Cuadrado(4), Circulo(3)]

for figura in figuras:
    print(f"Área: {figura.area():.2f}")
