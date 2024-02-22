valorGlobalJugador=0
valorGlobalCasa=0
nRepeticiones=int(input("¿Cuantas veces quiere jugar? "))
rGanadas=0
rPerdidas=0

print('\nVamos a jugar cara o sello \n Escoje una opcion \n cara=1 y sello=2 \n')
for i in range(nRepeticiones):
    valApuesta=int(input("ingrese la cantidad que desea apostar: "))

    respuesta=int(input('escoje tu lado: '))

    import random
    ran=random.randint(1,2)

    if  respuesta==1:
            if ran== respuesta:
                print("\nEl lado ganador es: Cara\n")
                print('Ganaste, tienes buena suerte \n')
                rGanadas=rGanadas+1
                valorGlobalJugador=valorGlobalJugador+(valApuesta*2)
            else:
                print('perdiste, el lado ganador es sello mejor suerte para la proxima \n')
                rPerdidas=rPerdidas+1
                valorGlobalCasa=valorGlobalCasa+valApuesta
    if  respuesta==2:
            if ran== respuesta:
                print("\nEl lado ganador es: Sello\n")
                print('Ganaste, tienes buena suerte \n')
                rGanadas=rGanadas+1
                valorGlobalJugador=valorGlobalJugador+(valApuesta*2)
            else:
                print('perdiste, el lado ganador es cara mejor suerte para la proxima \n')
                rPerdidas=rPerdidas+1
                valorGlobalCasa=valorGlobalCasa+valApuesta

print("Rondas Ganadas: ",rGanadas,"\nRondas Perdidas:",rPerdidas,"\nDinero Ganado:",valorGlobalJugador,"\nDinero Perdido: ",valorGlobalCasa)
if nRepeticiones>10:
     print("\nNecesitas ayuda, ya eres un apostador compulsivo, cuidado con eso carnal")
else:
     print("\nNo te vallas a viciar con esto!, cuidado")