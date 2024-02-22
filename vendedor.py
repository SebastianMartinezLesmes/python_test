PRODUCTOS= 10000
cantidadProductos= int(input("Coloque la cantidad de productos que va a comprar: "))
PagoCliente= int(input("ingrese la cantidad que va a pagar: "))

valorCompra=(cantidadProductos*PRODUCTOS)
cambio=float(valorCompra - PagoCliente)

print("el cliente compra: ",cantidadProductos," producto/s")
print("Paga: ",PagoCliente)

if valorCompra>PagoCliente:
    print("El cliente debe: $",cambio)
else:
    cambio = PagoCliente-valorCompra
    print("Se le deben devolver: $",cambio,"al cliente" )