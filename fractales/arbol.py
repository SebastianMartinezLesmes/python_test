import turtle

def dibujar_rama(longitud, nivel):
    if nivel > 0:
        turtle.forward(longitud)
        turtle.left(30)
        dibujar_rama(longitud * 0.7, nivel - 1)
        turtle.right(60)
        dibujar_rama(longitud * 0.7, nivel - 1)
        turtle.left(30)
        dibujar_rama(longitud * 0.7, nivel - 1)  # Rama adicional para más fractales
        turtle.right(30)
        dibujar_rama(longitud * 0.7, nivel - 1)  # Otra rama adicional
        turtle.left(30)
        turtle.backward(longitud)

turtle.speed('fastest')
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()

dibujar_rama(100, 6)  # Nivel incrementado para más detalles
turtle.done()
