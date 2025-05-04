import pygame
import random
import sys
import math

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esferas con gravedad, colisiones y contadores")

GRAVEDAD = 0.2
REBOTE_ELASTICO = 0.9
MAX_ESFERAS = 100
FUENTE = pygame.font.SysFont("Arial", 24)

def color_aleatorio():
    return (random.randint(50,255), random.randint(50,255), random.randint(50,255))

class Esfera:
    def __init__(self, x, y, radio=20):
        self.x = x
        self.y = y
        self.radio = radio
        self.vel_x = random.choice([-2, -1, 1, 2])
        self.vel_y = random.choice([-2, -1, 1, 2])
        self.color = color_aleatorio()

    def mover(self):
        self.vel_y += GRAVEDAD
        self.x += self.vel_x
        self.y += self.vel_y
        reboto = False

        if self.x - self.radio <= 0 or self.x + self.radio >= ANCHO:
            self.vel_x *= -REBOTE_ELASTICO
            self.x = max(self.radio, min(ANCHO - self.radio, self.x))
            reboto = True

        if self.y - self.radio <= 0 or self.y + self.radio >= ALTO:
            self.vel_y *= -REBOTE_ELASTICO
            self.y = max(self.radio, min(ALTO - self.radio, self.y))
            reboto = True

        return reboto

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), self.radio)

    def colisiona_con(self, otra):
        dx = self.x - otra.x
        dy = self.y - otra.y
        distancia = math.hypot(dx, dy)
        return distancia < self.radio + otra.radio

    def resolver_colision(self, otra):
        self.vel_x, otra.vel_x = otra.vel_x, self.vel_x
        self.vel_y, otra.vel_y = otra.vel_y, self.vel_y

        dx = self.x - otra.x
        dy = self.y - otra.y
        distancia = math.hypot(dx, dy)
        if distancia == 0:
            distancia = 0.1
        overlap = 0.5 * (self.radio + otra.radio - distancia + 1)
        nx = dx / distancia
        ny = dy / distancia
        self.x += nx * overlap
        self.y += ny * overlap
        otra.x -= nx * overlap
        otra.y -= ny * overlap

def dibujar_contadores(superficie, rebotes, total_esferas):
    texto = FUENTE.render(f"Rebotes: {rebotes}  |  Esferas: {total_esferas}", True, (255, 255, 255))
    superficie.blit(texto, (20, 20))

esferas = [Esfera(ANCHO // 2, ALTO // 2)]
rebotes = 0
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((25, 25, 25))

    total_rebotes_frame = 0

    for esfera in esferas:
        if esfera.mover():
            total_rebotes_frame += 1
        esfera.dibujar(pantalla)

    for i in range(len(esferas)):
        for j in range(i + 1, len(esferas)):
            if esferas[i].colisiona_con(esferas[j]):
                esferas[i].resolver_colision(esferas[j])

    if total_rebotes_frame > 0:
        rebotes += total_rebotes_frame
        cantidad_deseada = min(2 ** (rebotes), MAX_ESFERAS)
        nuevas = cantidad_deseada - len(esferas)
        for _ in range(nuevas):
            esferas.append(Esfera(random.randint(50, ANCHO - 50), random.randint(50, ALTO - 50)))

    dibujar_contadores(pantalla, rebotes, len(esferas))

    pygame.display.flip()
    clock.tick(60)
