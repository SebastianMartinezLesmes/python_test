print('\nVamos a jugar cara o sello \n Escoje una opción \n cara = 1 y sello = 2 \n')

respuesta = int(input('escoje tu lado: '))

import random
ran=random.randint(1,2)

if  respuesta == 1:
        if ran == respuesta:
            print("\nEl lado ganador es: Cara\n")
            print('Ganaste, tienes buena suerte \n')
        else:
            print('perdiste, el lado ganador es sello mejor suerte para la proxima \n')
if  respuesta == 2:
        if ran == respuesta:
            print("\nEl lado ganador es: Sello\n")
            print('Ganaste, tienes buena suerte \n')
        else:
            print('perdiste, el lado ganador es cara mejor suerte para la proxima \n')
         