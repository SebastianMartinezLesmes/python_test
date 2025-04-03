import requests
import sys

# 🎨 Colores para mejorar la visualización en la terminal
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"

def obtener_todas_tasas(base="USD"):
    """Obtiene todas las tasas de cambio desde una API y las almacena en caché."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()  # Lanza un error si hay problemas con la respuesta
        return respuesta.json().get("rates", {})
    except requests.RequestException as e:
        print(RED + f"❌ Error al obtener tasas de cambio: {e}" + RESET)
        return {}

def convertir_moneda(cantidad, base, destino, tasas):
    """Convierte una cantidad de base a destino usando las tasas obtenidas."""
    if destino in tasas:
        return cantidad * tasas[destino]
    else:
        print(RED + f"❌ No se encontró la tasa de cambio de {base} a {destino}." + RESET)
        return None

def main():
    print(GREEN + "💰 Conversor de Monedas 💰" + RESET)

    while True:
        try:
            cantidad = float(input(CYAN + "\nIngrese la cantidad a convertir: " + RESET))
            base = input("Ingrese la moneda de origen (ej. USD, EUR, MXN): ").upper().strip()
            destino = input("Ingrese la moneda de destino (ej. USD, EUR, MXN): ").upper().strip()

            tasas = obtener_todas_tasas(base)

            if not tasas:
                print(RED + "❌ No se pudo obtener la tasa de cambio. Intente más tarde." + RESET)
                continue

            resultado = convertir_moneda(cantidad, base, destino, tasas)

            if resultado is not None:
                print(f"\n✅ {GREEN}{cantidad} {base}{RESET} equivale a {GREEN}{round(resultado, 2)} {destino}{RESET}.")

            opcion = input("\n¿Desea realizar otra conversión? (s/n): ").strip().lower()
            if opcion != 's':
                print(GREEN + "👋 ¡Gracias por usar el conversor de monedas!" + RESET)
                break

        except ValueError:
            print(RED + "❌ Error: Ingrese un número válido." + RESET)
        except KeyboardInterrupt:
            print(RED + "\n❌ Operación cancelada por el usuario." + RESET)
            sys.exit()

if __name__ == "__main__":
    main()
