# python generate_lab.py

import random

def generar_laberinto(filas, columnas):
    laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]
    inicio = (1, 1)
    fin = (filas - 2, columnas - 2)
    
    def hacer_camino(x, y):
        laberinto[x][y] = ' '
        direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(direcciones)
        
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 1 <= nx < filas-1 and 1 <= ny < columnas-1 and laberinto[nx][ny] == '#':
                laberinto[x + dx//2][y + dy//2] = ' '
                hacer_camino(nx, ny)
    
    hacer_camino(1, 1)
    
    laberinto[1][2] = ' '
    laberinto[2][2] = ' '
    
    laberinto[inicio[0]][inicio[1]] = 'A'
    laberinto[fin[0]][fin[1]] = 'B'
    
    return laberinto

def guardar_laberinto(laberinto, filename):
    with open(filename, 'w') as f:
        for fila in laberinto:
            f.write("".join(fila) + "\n")

laberinto = generar_laberinto(25, 25)
guardar_laberinto(laberinto, "myMaze.txt")
