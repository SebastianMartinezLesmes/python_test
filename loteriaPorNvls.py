#prueba suerte
print('\n ')
print('Piensa en esto como una loteria, tienes que acertarle al numero \nDespues de cada acción precione la tecla "Enter" \n')

print(' para Facil coloque 1 \n para Normal coloque 2 \n para Dificil coloque 3 \n para Pesadilla coloque 4 \n')

respuesta=int(input('escoje una dicultad: '))

if respuesta == 1:
    numero=int(input('\nIngrese un numero del 1 al 3: '))
    import random
    ran=random.randint(1,3)
    print("\nel numero ganador es: ",ran,"\n")

    if ran== numero:
       print('ganaste, tienes buena suerte \n')
    else:
         print('perdiste, mejor suerte para la proxima \n')
         
         
elif respuesta== 2:
    numero=int(input('\nIngrese un numero del 1 al 5: '))
    import random
    ran=random.randint(1,5)
    print("\nel numero ganador es: ",ran,"\n")

    if ran== numero:
        print('ganaste, tienes buena suerte \n')
    else:
         print('perdiste, mejor suerte para la proxima \n')
         

elif respuesta== 3:
    numero=int(input('\nIngrese un numero del 1 al 10: '))
    import random
    ran=random.randint(1,10)
    print("\nel numero ganador es: ",ran,"\n")

    if ran== numero:
        print('ganaste, tienes buena suerte \n')
    else:
         print('perdiste, mejor suerte para la proxima \n')
         
         
elif respuesta== 4:
    numero=int(input('\nIngrese un numero del 1 al 15: '))
    import random
    ran=random.randint(1,15)
    print("\nel numero ganador es: ",ran,"\n")

    if ran== numero:
        print('ganaste, tienes buena suerte \n')
    else:
         print('perdiste, mejor suerte para la proxima \n')

#numero=int(input('ingrese un numero del 1 al 10: '))
#import random
#ran=random.randint(1,10)
#print(ran)

#if ran== numero:
 #   print('ganaste, tienes buena suerte')
#else:
 #   print('perdiste, mejor suerte para la proxima')
