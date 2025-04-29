# pip install pygame / pip install pygame --upgrade --force-reinstall
# para ejecutar: python best_hunter.py
import pygame
import random
import sys
import subprocess

try:
    import pygame
except ImportError:
    print("Instalando pygame... 🔧")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    except Exception as e:
        print(f"Error al intentar instalar pygame: {e}")
        sys.exit(1)  
    import pygame

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Caza al Monstruo")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)

clock = pygame.time.Clock()

fuente = pygame.font.Font(None, 36)

TIEMPO_LIMITE = 30  

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 10
        self.tamaño = 50

    def dibujar(self):
        pygame.draw.rect(pantalla, VERDE, (self.x, self.y, self.tamaño, self.tamaño))

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x - self.velocidad >= 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x + self.tamaño + self.velocidad <= ANCHO:
            self.x += self.velocidad
        if teclas[pygame.K_UP] and self.y - self.velocidad >= 0:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.y + self.tamaño + self.velocidad <= ALTO:
            self.y += self.velocidad

# 👾 Clase Monstruo
class Monstruo:
    def __init__(self):
        self.x = random.randint(0, ANCHO - 50)
        self.y = random.randint(0, ALTO - 50)
        self.tamaño = 50

    def dibujar(self):
        pygame.draw.rect(pantalla, ROJO, (self.x, self.y, self.tamaño, self.tamaño))

    def reposicionar(self):
        self.x = random.randint(0, ANCHO - 50)
        self.y = random.randint(0, ALTO - 50)

# 🎮 Clase Juego (Lógica del juego)
class Juego:
    def __init__(self):
        self.jugador = Personaje(ANCHO // 2, ALTO // 2)
        self.monstruo = Monstruo()
        self.puntaje = 0
        self.tiempo_restante = TIEMPO_LIMITE * 1000 
        self.tiempo_inicial = pygame.time.get_ticks()

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            pantalla.fill(BLANCO)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False

            teclas = pygame.key.get_pressed()
            self.jugador.mover(teclas)

            self.jugador.dibujar()
            self.monstruo.dibujar()

            self.mostrar_puntaje()
            self.mostrar_tiempo()

            if self.colision():
                self.puntaje += 1
                print(f"¡Capturado! Puntaje: {self.puntaje}")
                self.monstruo.reposicionar()

            if self.tiempo_restante <= 0:
                print("⏰ ¡Tiempo agotado! Juego terminado.")
                ejecutando = False

            pygame.display.update()
            clock.tick(30)

        pygame.quit()
        sys.exit()

    def colision(self):
        return (self.jugador.x < self.monstruo.x + self.monstruo.tamaño and
                self.jugador.x + self.jugador.tamaño > self.monstruo.x and
                self.jugador.y < self.monstruo.y + self.monstruo.tamaño and
                self.jugador.y + self.jugador.tamaño > self.monstruo.y)

    def mostrar_puntaje(self):
        texto = fuente.render(f"Puntaje: {self.puntaje}", True, NEGRO)
        pantalla.blit(texto, (10, 10))

    def mostrar_tiempo(self):
        tiempo_actual = pygame.time.get_ticks()
        self.tiempo_restante = max(0, self.tiempo_restante - (tiempo_actual - self.tiempo_inicial))
        self.tiempo_inicial = tiempo_actual
        segundos_restantes = self.tiempo_restante // 1000 
        texto = fuente.render(f"Tiempo: {segundos_restantes}s", True, NEGRO)
        pantalla.blit(texto, (ANCHO - 150, 10))

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
