def operaciones_bancarias():
    saldo = 1_000_000  # Saldo inicial
    print("💸 Bienvenido a su banca virtual 💸")
    print(f"Su saldo inicial es de: ${saldo:,}\n")

    while True:
        print("\n=== Menú de Operaciones ===")
        print("1. Retiro")
        print("2. Consignación")
        print("3. Consultar Saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":  # Retiro
            try:
                retiro = int(input("Ingrese el monto a retirar: $"))
                if retiro <= 0:
                    print("⚠️ El monto debe ser mayor a cero.")
                elif retiro > saldo:
                    print("❌ Saldo insuficiente. No puede retirar más de lo que tiene.")
                else:
                    saldo -= retiro
                    print(f"✅ Ha retirado: ${retiro:,}. Saldo actual: ${saldo:,}")

            except ValueError:
                print("⚠️ Error: Debe ingresar un monto válido.")

        elif opcion == "2":  # Consignación
            try:
                consignacion = int(input("Ingrese el monto a consignar: $"))
                if consignacion <= 0:
                    print("⚠️ El monto debe ser mayor a cero.")
                else:
                    saldo += consignacion
                    print(f"✅ Ha consignado: ${consignacion:,}. Saldo actual: ${saldo:,}")

            except ValueError:
                print("⚠️ Error: Debe ingresar un monto válido.")

        elif opcion == "3":  # Consultar Saldo
            print(f"💼 Su saldo actual es: ${saldo:,}")

        elif opcion == "4":  # Salir
            print("Cerrando sesión... ¡Gracias por usar nuestros servicios! 💳")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

# Ejecución del programa
operaciones_bancarias()
