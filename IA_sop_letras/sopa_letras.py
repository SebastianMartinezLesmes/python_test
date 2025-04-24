import random
import string

# Diccionario con temas y palabras
temas_palabras = {
    "astronomía": ["planeta", "galaxia", "estrella", "cometa", "nebulosa", "luz", "saturno"],
    "música": ["melodía", "nota", "guitarra", "piano", "ritmo", "voz", "bajo"],
    "gastronomía": ["receta", "sabor", "ingrediente", "chef", "cocina", "plato", "horno"],
    "videojuegos": ["consola", "pantalla", "nivel", "juego", "control", "avatar", "enemigo"],
    "escritores": ["novela", "autor", "cuento", "poesía", "libro", "letras", "ensayo"],
    "emociones": ["alegría", "miedo", "enojo", "tristeza", "amor", "sorpresa", "ansiedad"]
}

def crear_sopa(tamano):
    return [[' ' for _ in range(tamano)] for _ in range(tamano)]

def colocar_palabra(sopa, palabra):
    tamano = len(sopa)
    palabra_len = len(palabra)
    direccion = random.choice(['horizontal', 'vertical'])
    colocada = False

    while not colocada:
        if direccion == 'horizontal':
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - palabra_len)
            if all(sopa[fila][columna + i] == ' ' for i in range(palabra_len)):
                for i in range(palabra_len):
                    sopa[fila][columna + i] = palabra[i]
                colocada = True
        else:
            fila = random.randint(0, tamano - palabra_len)
            columna = random.randint(0, tamano - 1)
            if all(sopa[fila + i][columna] == ' ' for i in range(palabra_len)):
                for i in range(palabra_len):
                    sopa[fila + i][columna] = palabra[i]
                colocada = True

def rellenar_sopa(sopa):
    for i in range(len(sopa)):
        for j in range(len(sopa[i])):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(string.ascii_uppercase)

def imprimir_y_guardar_sopa(sopa, tema, palabras, archivo_nombre):
    with open(archivo_nombre, 'w', encoding='utf-8') as f:
        f.write(f"Tema: {tema.capitalize()}\n")
        f.write("Palabras ocultas: " + ', '.join(palabras) + "\n\n")
        print(f"Tema: {tema.capitalize()}")
        print("Palabras ocultas:", ', '.join(palabras), "\n")

        for fila in sopa:
            linea = ' '.join(fila)
            print(linea)
            f.write(linea + '\n')

def generar_sopa_con_tema(tamano, archivo_salida="sopa_de_letras.txt"):
    tema = random.choice(list(temas_palabras.keys()))
    palabras = random.sample(temas_palabras[tema], 5)
    palabras_mayus = [p.upper() for p in palabras]

    sopa = crear_sopa(tamano)
    for palabra in palabras_mayus:
        colocar_palabra(sopa, palabra)
    rellenar_sopa(sopa)

    imprimir_y_guardar_sopa(sopa, tema, palabras, archivo_salida)

# Ejecutar
generar_sopa_con_tema(12)
