num=int(input('ingrese un numero:'))
cont=0
tot=0

for i in range (cont,6,1):
    price = int(input('ingrese el precio del producto: '))
    cant = int(input('ingrese la cantidad del producto: '))
    cont = cont+1 
    subTot = price*cant
    tot = tot+subTot
print('total: ',tot)

pag=int(input("Ingrese valor con el que paga \n"))
if tot >= pag:
    print("Debe ", tot-pag)
else:
    print("Su cambio es ", pag-tot)

linTel=input("¿Tiene linea telefonica? ")
if linTel=='si':
    print('Excelente,te daremos ', cant,' minutos'  )
else:
    print('pasate a nuestra linia movil')