nP=int(input("Ingrese la cantidad de productos que lleva: "))
valorCompra=0

for i in range(nP):
    cantidad=int(input("Ingrese la cantidad de producto: "))
    precio=int(input("Ingrese el valor del roducto: "))
    valorCompra=valorCompra+(precio*cantidad)

if valorCompra>=50000:
    print("\nAhora sacaras una bola de la caja \nSi la bola es Roja el descuento es del 10% \nSi la bola es Azul el descuento es del 30% \nSi la bola es Amarilla el descuento es del 50% \nSi la bola es Blanca el descuento es del 100%")
    import random
    bola=random.randint(1,4)
    print("\n\n")
    if bola ==1:
        descuento=(valorCompra*0.1)
        totPago= valorCompra-descuento
        print("El valor de su compra es: ",valorCompra,"\nEl color de la bola que saco es: Roja \nGano un descuento del 10% \nTotal a pagar es: ",totPago)
    elif bola ==2:
        descuento=(valorCompra*0.3)
        totPago= valorCompra-descuento
        print("El valor de su compra es: ",valorCompra,"\nEl color de la bola que saco es: Azul \nGano un descuento del 30% \nTotal a pagar es: ",totPago)
    elif bola ==3:
        descuento=(valorCompra*0.5)
        totPago= valorCompra-descuento
        print("El valor de su compra es: ",valorCompra,"\nEl color de la bola que saco es: Amarillo \nGano un descuento del 50% \nTotal a pagar es: ",totPago)
    elif bola ==4:
        totPago = 0
        print("El valor de su compra es: ",valorCompra,"\nEl color de la bola que saco es: Blanca \nGano un descuento del 100% \nTotal a pagar es: ",totPago)
