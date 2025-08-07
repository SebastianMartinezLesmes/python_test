from vpython import *
import math

# Configuración de la escena
scene.title = "Estructura cúbica flotante"
scene.background = vector(0.1, 0.1, 0.1)
scene.width = 900
scene.height = 600

# Parámetros
cubo_size = 1
espaciado = cubo_size * 1.5
cubos = []
direcciones = []

# Función para crear un cubo
def crear_cubo(pos):
    cubo = box(
        pos=pos,
        size=vector(cubo_size, cubo_size, cubo_size),
        color=vector(0.2, 0.7, 1),
        opacity=0.4
    )
    cubos.append(cubo)
    direcciones.append(1)

# Función para colapsar los cubos
def colapsar():
    for c in cubos:
        c.color = color.red
        c.opacity = 0.4

# Función para reorganizar los cubos en forma cúbica
def reorganizar_cubos():
    total = len(cubos)
    
    # Calcular la raíz cúbica aproximada
    side = math.ceil(total ** (1/3))  # Número de cubos por eje

    index = 0
    offset = (side - 1) * espaciado / 2  # Centrado

    for z in range(side):
        for y in range(side):
            for x in range(side):
                if index >= total:
                    return
                cubos[index].pos = vector(
                    x * espaciado - offset,
                    y * espaciado - offset,
                    z * espaciado - offset
                )
                index += 1

# Función para agregar un nuevo cubo
def agregar_cubo():
    crear_cubo(vector(0, 0, 0))  # Posición inicial temporal
    reorganizar_cubos()

# Crear el primer cubo
crear_cubo(vector(0, 0, 0))

# Botones
button(text="Colapsar", bind=colapsar)
button(text="+ cube", bind=agregar_cubo)

# Animación flotante
while True:
    rate(60)
    for i, cubo in enumerate(cubos):
        cubo.pos.y += 0.002 * direcciones[i]
        if cubo.pos.y > cubo.pos.y + 0.5 or cubo.pos.y < cubo.pos.y - 0.5:
            direcciones[i] *= -1
