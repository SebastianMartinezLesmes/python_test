instructores2503816 = {}

while True:
    print("Menú: \n1. Agregar/modificar \n2. Buscar \n3. Borrar \n4. Listar \n5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del instructor: ")

        if nombre in instructores2503816:
            print(f"Materia: {instructores2503816[nombre]['materia']}")
            print(f"Teléfono: {instructores2503816[nombre]['telefono']}")
            modificar = input("¿Desea modificar los datos? (s/n): ")
            if modificar.lower() == "s":
                materia = input("Ingrese la nueva materia: ")
                telefono = input("Ingrese el nuevo teléfono: ")
                instructores2503816[nombre]['materia'] = materia
                instructores2503816[nombre]['telefono'] = telefono
        else:
            materia = input("Ingrese la materia: ")
            telefono = input("Ingrese el teléfono: ")
            instructores2503816[nombre] = {'materia': materia, 'telefono': telefono}

    elif opcion == "2":
        busqueda = input("Ingrese un texto de búsqueda: ")
        for nombre, datos in instructores2503816.items():
            if nombre.startswith(busqueda):
                print(f"{nombre}: {datos['materia']}, {datos['telefono']}")
            else:
                    print('Instructor inexistente')    

    elif opcion == "3":
        nombre = input("Ingrese el nombre del instructor a borrar: ")
        if nombre in instructores2503816:
            borrar = input(f"¿Desea borrar a {nombre}? (s/n): ")
            if borrar.lower() == "s":
                del instructores2503816[nombre]
                print(f"{nombre} ha sido eliminado de la lista.")
        else:
            print(f"{nombre} no se encuentra en la lista.")

    elif opcion == "4":
        print("Lista de instructores:")
        for nombre, datos in instructores2503816.items():
            print(f"{nombre}: {datos['materia']}, {datos['telefono']}")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
