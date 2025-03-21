import turtle
import colorsys

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Círculo de colores en movimiento")

# Configuración del objeto turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Número de colores y pasos
n = 36
h = 0

# Dibujar el círculo de colores en movimiento
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    h += 1/n
    t.color(c)
    t.forward(i)
    t.right(59)
    t.forward(i)
    t.right(59)

# Finalizar el dibujo
turtle.done()
