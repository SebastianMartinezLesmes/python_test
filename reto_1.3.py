import random
d1=random.randint(1,6)
d2=random.randint(1,6)
sumaD=d1+d2
print("\n Vamos a jugar Craps \n")
print("Para ganar necesitas: \n1. que los 2 dados saquen 1 o 6 \n2. que la suma de los dos dados de 3, 7 o 11 \n")
if sumaD==2 or sumaD==12 or sumaD==3 or sumaD==7 or sumaD==11:
    print("El dado 1 saco: ",d1)
    print("El dado 2 saco: ",d2)
    print("La suma de los dados da: ",sumaD)
    print("\nHas ganado esta ronda, felicidades")
else:
    print("El dado 1 saco: ",d1)
    print("El dado 2 saco: ",d2)
    print("La suma de los dados da: ",sumaD)
    print("\nHas perdido esta ronda, buena suerte para la proxima\n")