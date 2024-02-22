competidores=[]
tiempo=[]
numero_Competidores=int(input('¿Cuantos competidores son? '))

for i in range(0, numero_Competidores):
    competidor=input('Ingrese el nombre del competidor: ')
    tiempoCompetidor=int(input('Ingrese el tiempo del competidor: '))
    competidores.append(competidor)
    tiempo.append(tiempoCompetidor)

tiempo_minimo = min(tiempo)
ganador = ""

for i in range(len(competidores)):
    print(f"\n{competidores[i]}: {tiempo[i]} segundo/s\n")
    if tiempo[i] == tiempo_minimo:
        ganador = competidores[i]

print(f"El ganador es {ganador} con un tiempo de {tiempo_minimo} segundo/s \n ")
