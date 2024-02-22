nN=int(input('ingrese el numero de notas que desea colocar: '))
cal=0
for i in range(nN):
    nota=int(input('Ingrese la nota en un rango del 1 al 5: '))
    cal=cal+nota
prom = cal/nN
print(prom)

if 0.0<=prom<=2.9:
    print('El aprendiz perdio')
elif 3.0<=prom<=4.0:
    print('El aprendiz paso')
elif prom>4.0:
    print('El aprendiz es ¡Sobresaliente!')
