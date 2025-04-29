import time
import sys
import random

def prueba1():
    print("\n🔹 PRUEBA 1: Comparación de dos números")
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if num1 > num2:
            print(f"El número mayor es {num1}.")
        elif num2 > num1:
            print(f"El número mayor es {num2}.")
        else:
            print(f"Los números {num1} y {num2} son iguales.")
    except ValueError:
        print("⚠️ Error: Debe ingresar números enteros válidos.\n")

def prueba2():
    print("\n🔹 PRUEBA 2: Precio de ingreso según edad")
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("⚠️ La edad no puede ser negativa. Inténtelo nuevamente.")
        elif edad <= 4:
            print("El cliente ingresa GRATIS. 👶")
        elif edad <= 17:
            print("El cliente debe pagar $20,000 para su ingreso. 🧒")
        elif edad <= 60:
            print("El cliente debe pagar $15,000 para su ingreso. 🧑")
        else:
            print("El cliente debe pagar $3,000 para su ingreso. 👴")
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido para la edad.")

def prueba3():
    print("\n🔹 PRUEBA 3: ¿Trajo los ingredientes del desayuno?")

    def verificar_respuesta(respuesta):
        return respuesta.lower() in ["s", "si"]

    leche = input("¿Trajo la leche? (s/si o n/no): ").strip().lower()
    pan = input("¿Trajo el pan? (s/si o n/no): ").strip().lower()
    huevos = input("¿Trajo los huevos? (s/si o n/no): ").strip().lower()

    if all(verificar_respuesta(item) for item in [leche, pan, huevos]):
        print("✅ ¡Se ganó el desayuno!")
    else:
        print("⚠️ Prueba de resistencia y dolor.")

    if any(verificar_respuesta(item) for item in [leche, pan, huevos]):
        print("✅ ¡Venga a desayunar, amor!")
    else:
        print("❌ Deje así, que yo miro qué hago.")

def prueba4():
    print("\n🔹 PRUEBA 4: Adivinación de número pensado")
    print("Piense un número, súmele 5, multiplíquelo por 3 y réstele 15.")
    try:
        resultado = int(input("Ingrese el resultado obtenido: "))
        numero_pensado = resultado / 3
        print(f"El número que pensaste es: {numero_pensado:.0f}")

        respuesta = input("¿El número es correcto? (sí/no): ").strip().lower()
        if respuesta in ["sí", "si"]:
            print("¡Soy todo un genio! 😎")
        else:
            print("Rectifica tus cuentas y verás que no me equivoco. 😉")
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido.")

def juego_piedra_papel_tijeras():
    consolD = random.randint(1, 3)
    peopleD = int(input('tijeras es 1 \npapel es 2 \npiedra es 3 \n¿Cual elijes? '))

    if peopleD == consolD:
        print("Empate.")
    elif (peopleD == 1 and consolD == 2) or (peopleD == 2 and consolD == 3) or (peopleD == 3 and consolD == 1):
        print("Ganaste.")
    else:
        print("Perdiste.")

def juego_descuento_aleatorio():
    valorCompra = int(input("Ingrese el valor de la compra: "))

    if valorCompra >= 50000:
        print("\nSacarás una bola de la caja:")
        print("Roja: 10% de descuento\nAzul: 30% de descuento\nAmarilla: 50% de descuento\nBlanca: 100% de descuento")

        bola = random.randint(1, 4)
        descuentos = {1: 0.1, 2: 0.3, 3: 0.5, 4: 1.0}
        colores = {1: 'Roja', 2: 'Azul', 3: 'Amarilla', 4: 'Blanca'}

        descuento = valorCompra * descuentos[bola]
        totPago = valorCompra - descuento if bola != 4 else 0

        print(f"Valor de compra: {valorCompra}\nColor de la bola: {colores[bola]}\nDescuento aplicado: {int(descuentos[bola]*100)}%\nTotal a pagar: {totPago}")

def tabla_multiplicar():
    print("\n🔹 PRUEBA 8: Tabla de Multiplicar")
    try:
        selecN = int(input('Ingrese el número de la tabla que desea ver: '))
        limite = int(input('Ingrese el límite de la tabla: '))

        for i in range(limite + 1):
            resultado = selecN * i
            print(f"{selecN} x {i} = {resultado}")
    except ValueError:
        print("⚠️ Error: Debes ingresar números enteros válidos.")

def animacion_terminar():
    print("\nTerminando", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print()  # Salto de línea al finalizar la animación

def menu():
    while True:
        print("\n=== MENÚ DE PRUEBAS Y JUEGOS ===")
        print("1. Comparación de números")
        print("2. Precio según edad")
        print("3. Ingredientes del desayuno")
        print("4. Adivinación de número pensado")
        print("5. Piedra, papel o tijeras")
        print("6. Descuento aleatorio en compras")
        print("7. Tabla de multiplicar")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            prueba1()
        elif opcion == "2":
            prueba2()
        elif opcion == "3":
            prueba3()
        elif opcion == "4":
            prueba4()
        elif opcion == "5":
            juego_piedra_papel_tijeras()
        elif opcion == "6":
            juego_descuento_aleatorio()
        elif opcion == "7":
            tabla_multiplicar()
        elif opcion == "8":
            animacion_terminar()
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

menu()