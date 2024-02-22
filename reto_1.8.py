numeroNotas=int(input('Solo factores nuemericos \n¿cuantas notas desea colocar? '))
sumaNotas=0
listaNotas=[]

for i in range(0,numeroNotas):
    notas=int(input('ingrese el valor de la nota: '))
    listaNotas.append(notas)
    sumaNotas=sumaNotas+notas
    promedio=sumaNotas/len(listaNotas)
print('el promedio que dio fue: ',promedio)

if promedio<3:
    print('Reprobado')
elif promedio>=3 and promedio<=4:
    print('Pasa raspando')
elif promedio>= 4:
    print('Pasa con buenos resultados')
