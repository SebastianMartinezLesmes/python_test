presupuesto=int(input('ingrese su presupuesto: '))
valGasto=0
nC=3
totPagar=0
print('Su presupuesto es: ',presupuesto,'\nHa gastado: ',valGasto,'\nLe quedan ',nC,' cambios disponibles')
preg=input('¿Desea hacer un gasto? ')
while preg=='s' or preg=='S' or preg=='si' or preg=='Si':
    if nC>=1: 
        if presupuesto>0:
            valGasto=int(input('Ingrese el valor del gasto que desea realizar: '))
            totPagar=(presupuesto-valGasto)
            presupuesto=totPagar
            nC-=1
            print('Su presupuesto es: 0 esta debiendo:',presupuesto,'\nHa gastado todo su presupuesto \nLe quedan ',nC,' cambios disponibles')
            preg=input('¿Desea hacer otro gasto? ')

    if nC<=0 or presupuesto<=0:
        print('Lo lamento, pero se han acabado los cambios')
        preg=='n'
        break
print('Ha gastado todo su presupuesto \no/y tiene',nC,' cambios disponibles')