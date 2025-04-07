import subprocess

def mostrar_menu():
    print("\n¿Qué archivo desea crear?")
    print("1. Excel")
    print("2. Word")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción (número o nombre): ").strip().lower()

    if opcion in ["1", "excel"]:
        print("Esta opción convierte un archivo JSON a Excel.")
        confirmar = input("¿Desea continuar? (s/n): ").strip().lower()
        if confirmar in ["s", "si"]:
            subprocess.run(["python", "gen_excel.py"])
        else:
            print("Operación cancelada. Volviendo al menú...")

    elif opcion in ["2", "word"]:
        subprocess.run(["python", "gen_word.py"])

    elif opcion in ["0", "salir"]:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
