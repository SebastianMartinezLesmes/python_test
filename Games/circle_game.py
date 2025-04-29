import pygame
import random
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Multiplicación de esferas en rebotes")

def color_aleatorio():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Clase Esfera
class Esfera:
    def __init__(self, x, y, radio=30):
        self.x = x
        self.y = y
        self.radio = radio
        self.vel_x = random.choice([-4, -3, 3, 4])
        self.vel_y = random.choice([-4, -3, 3, 4])
        self.color = color_aleatorio()

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        reboto = False

        if self.x - self.radio <= 0 or self.x + self.radio >= ANCHO:
            self.vel_x *= -1
            self.color = color_aleatorio()
            reboto = True

        if self.y - self.radio <= 0 or self.y + self.radio >= ALTO:
            self.vel_y *= -1
            self.color = color_aleatorio()
            reboto = True

        return reboto

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), self.radio)

# Inicialización
esferas = [Esfera(ANCHO // 2, ALTO // 2)]
rebotes = 0
MAX_ESFERAS = 100

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((25, 25, 25))

    total_rebotes = 0
    for esfera in esferas:
        if esfera.mover():
            total_rebotes += 1
        esfera.dibujar(pantalla)

    # Si hubo al menos un rebote, actualizar rebotes global
    if total_rebotes > 0:
        rebotes += 1
        cantidad_deseada = min(2 ** rebotes, MAX_ESFERAS)
        nuevas = cantidad_deseada - len(esferas)
        for _ in range(nuevas):
            esferas.append(Esfera(random.randint(100, ANCHO - 100), random.randint(100, ALTO - 100)))

    pygame.display.flip()
    clock.tick(60)
