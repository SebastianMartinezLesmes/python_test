saldo=1000000

while True:
    quest=input('quiere hacer un retiro o una consignación? ')
    if quest=='retiro' or quest=='Retiro':
        retiro=int(input('¿Cuanto desea retirar?'))
        saldo=saldo-retiro
        print('Has retirado: ',retiro,'\nSaldo actual: ',saldo)
    elif quest=='consignar' or quest=='Consignar':
        consignar=int(input('¿Cuanto desea consignar?'))
        saldo=saldo+consignar
        print('Has consignado: ',consignar,'\nSaldo actual: ',saldo)
    else:
        print('Saldo actual: ',saldo)