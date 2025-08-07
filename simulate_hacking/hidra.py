from vpython import *

# Configuración inicial de la escena
scene.title = "Cubo flotante 3D con botón"
scene.background = vector(0.1, 0.1, 0.1)
scene.width = 800
scene.height = 600

# Tamaño del cubo
size = 2

# Crear cubo semi-transparente
cubo = box(
    pos=vector(0, 0, 0),
    size=vector(size, size, size),
    color=vector(0.2, 0.7, 1),  # Azul claro
    opacity=0.4
)

# Función para cambiar el color del cubo
def colapsar():
    cubo.color = color.red
    cubo.opacity = 0.4  # Mantener transparencia

# Botón en la escena
button(text="Colapsar", bind=colapsar)

# Animación flotante y rotación
direction = 1

while True:
    rate(60)
    cubo.pos.y += 0.01 * direction
    if cubo.pos.y > 1 or cubo.pos.y < -1:
        direction *= -1
    cubo.rotate(angle=0.03, axis=vector(0, 1, 0))
