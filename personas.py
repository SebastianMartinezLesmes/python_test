grupo=int(input('Ingrese el numero de integrantes del grupo: '))
nH=0
nM=0

for i in range(grupo):
    res=input('¿Eres hombre?')
    if res =='si':
        nH=nH+1
    else:
        nM=nM+1
print('El grupo tiene ',nH,' hombres y ',nM,' mujeres y son un total de ',grupo)