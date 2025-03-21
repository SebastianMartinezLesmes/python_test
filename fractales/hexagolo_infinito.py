import turtle
import colorsys

pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Círculo de colores en movimiento")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

n = 50
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    h += 1/n
    t.color(c)
    t.forward(i)
    t.right(59)
    t.forward(i)
    t.right(59)

turtle.done()
