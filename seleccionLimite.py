# para presentar la tabla del 1 al 10 que el usuario elija

selecN = int(input('ingrese el numero de la trabla que desee ver: '))
Limit = int(input('ingrese el numero hasta el cual quiere que la tabla llegüe: '))

for i in range(Limit+1):
    resultado= selecN * i
    print(selecN,' x ',i,' = ',resultado)
