pesoBebe=int(input("ingrese el peso del bebe: "))
mesesBebe=int(input("ingrese los meses del bebe: "))
dosisVacuna=(((pesoBebe+10)/(mesesBebe*10))*8)

print("la dosis que toca suministrarle al bebe es: ",dosisVacuna)