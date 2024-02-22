import random
consolD=random.randint(1,3)
peopleD=int(input('tijeras es 1 \npapel es 2 \npiedra es 3 \n¿Cual elijes? '))

if peopleD== 1:
    if consolD==1:
        print('empate, la consola y tu sacaron tijeras')
    elif consolD==2:
        print('ganaste, la consola saco papel y tu tijeras')
    elif consolD==3:
        print('perdiste, la consola saco roca y tu tijeras')

if peopleD== 2:
    if consolD==2:
        print('empate, la consola y tu sacaron papel')
    elif consolD==3:
        print('ganaste, la consola saco piedra y tu papel')
    elif consolD==1:
        print('perdiste, la consola saco tijeras y tu papel')
    
if peopleD== 3:
    if consolD==3:
        print('empate, la consola y tu sacaron piedra')
    elif consolD==1:
        print('ganaste, la consola saco tijeras y tu piedra')
    elif consolD==2:
        print('perdiste, la consola saco papel y tu piedra')