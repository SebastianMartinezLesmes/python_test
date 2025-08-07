from vpython import *
import math
import time

# Configuración
scene.title = "Estructura cúbica flotante"
scene.background = vector(0.1, 0.1, 0.1)
scene.width = 900
scene.height = 600

# Texto contador
contador_texto = label(pos=vector(0, 3, 0), text="", height=30, box=False, color=color.white, opacity=0)

# Variables
cubo_size = 1
espaciado = cubo_size * 1.5
cubos = []
direcciones = []
contador = 0
colapsado = False
modo_rotacion = False
cubo_rotador = None

# Número base (tamaño cúbico)
cubes = 8  # Cambia este valor a 2, 3, 8, etc.

def formatear_numero(n):
    return f"{n:,}".replace(",", ".")

def crear_cubo(pos):
    cubo = box(
        pos=pos,
        size=vector(cubo_size, cubo_size, cubo_size),
        color=vector(0.2, 0.7, 1),
        opacity=0.4
    )
    cubos.append(cubo)
    direcciones.append(1)

def generar_estructura_cubica(n):
    offset = (n - 1) * espaciado / 2
    for z in range(n):
        for y in range(n):
            for x in range(n):
                pos = vector(
                    x * espaciado - offset,
                    y * espaciado - offset,
                    z * espaciado - offset
                )
                crear_cubo(pos)
                rate(20)

def colapsar():
    global cubos, direcciones, colapsado, modo_rotacion, cubo_rotador

    colapsado = True
    modo_rotacion = False
    contador_texto.opacity = 0

    for c in cubos:
        c.color = color.red
        c.opacity = 0.4
        rate(5)

    sleep(0.2)

    for c in cubos:
        for i in range(10):
            rate(20)
            c.opacity -= 0.04
            c.size *= 0.9
        c.visible = False

    cubos.clear()
    direcciones.clear()

def ejecutar():
    global cubos, direcciones, contador, modo_rotacion, cubo_rotador, colapsado

    colapsado = False  # Reset

    for c in cubos:
        c.color = color.green
        c.opacity = 0.4
        rate(5)

    centro = vector(0, 0, 0)
    pasos = 30
    for paso in range(pasos):
        rate(60)
        for c in cubos:
            c.pos += (centro - c.pos) / (pasos - paso)

    contador_texto.opacity = 1
    contador = 0

    if len(cubos) == 0:
        return
    cubo_rotador = cubos[0]
    for c in cubos[1:]:
        c.visible = False
    cubos = [cubo_rotador]
    direcciones = [1]

    modo_rotacion = True  # Activar rotación y contador

# Inicialización automática
generar_estructura_cubica(cubes)

# Botones
button(text="Colapsar", bind=colapsar)
button(text="Ejecutar", bind=ejecutar)

# Bucle principal
while True:
    rate(60)

    for i in range(min(len(cubos), len(direcciones))):
        cubo = cubos[i]
        cubo.pos.y += 0.002 * direcciones[i]
        if cubo.pos.y > 0.5 or cubo.pos.y < -0.5:
            direcciones[i] *= -1

    if modo_rotacion and not colapsado and cubos:
        cubo_rotador.rotate(angle=0.01, axis=vector(1, 0, 0), origin=cubo_rotador.pos)
        cubo_rotador.rotate(angle=0.01, axis=vector(0, 1, 0), origin=cubo_rotador.pos)
        contador += 1
        contador_texto.text = "$ " + formatear_numero(contador)
