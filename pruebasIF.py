#PRUEBA1
print("    ")
print("PRUEBA 1   ")
print("    ")
num1=int(input("Ingrese el primer numero \n"))
num2=int(input("Ingrese el segundo numero \n"))

if num1>num2:
    print ("El numero mayor es", num1)
elif num2>num1:
    print ("El numero mayor es", num2)
else:
    print ("Los numeros", num1, "y", num2,"son iguales")

#PRUEBA2
print("    ")
print("PRUEBA 2   ")
print("    ")
num1=int(input("Ingrese el primer numero \n"))
num2=int(input("Ingrese el segundo numero \n"))

if num1>num2:
    print ("El numero mayor es", num1)
if num2>num1:
    print ("El numero mayor es", num2)
if num1==num2:
    print ("Los numeros", num1, "y", num2,"son iguales")
else:
    print ("Los datos son incorrectos")

#PRUEBA 3
print("    ")
print("PRUEBA 3   ")
print("    ")
age=int(input("Ingrese su edad: \n"))
if 0< age <=4:
    print("El cliente ingresa gratis")
elif 5<= age <=17:
    print("El cliente debe pagar 20.000 para su ingreso")
elif 18<= age <=60:
    print("El cliente debe pagar 15.000 para su ingreso")
elif age >60:
    print("El cliente debe pagar 3.000 para su ingreso")

#PRUEBA 4
print("    ")
print("PRUEBA 4   ")
print("    ")
leche=input("¿Trajo la leche? \n coloque 's' o 'n/no'")
pan=input("¿Trajo el pan? \n coloque 's' o 'n/no'")
huevos=input("¿Trajo los huevos? \n coloque 's' o 'n/no'")

#MamaLatina
if leche=="s" and huevos=="s" and pan=="s":
    print("Se gano el desayuno")
else:
    print("Prueba de resistencia y dolor")
#MamaOtras
if leche=="s" or huevos=="s" or pan=="s":
    print("Venga a desayunar amor")
else:
    print("Deje asi que yo miro que hago")

#PRUEBA 5
print("    ")
print("PRUEBA 5   ")
print("    ")
print("Piense un numero \n sumale 5 \n ahora multiplicalo por 3 \n ahora restele 15")
n1=int(input("ingrese el resultado obtenido: "))
res=n1/3
print("El numero que pensaste es: ", res)

quest=input("Coloque si o no \n ¿El numero es correcto? \n")
if quest=="si":
    print("Soy todo un genio")
else:
    print("Rectifica tus cuentas y veras que no me equivoco")