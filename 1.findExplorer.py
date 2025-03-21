import webbrowser

def buscar_en_google():
    print("=== BUSCADOR DE GOOGLE ===")
    consulta = input("¿Qué deseas buscar en Google?: ")

    # Formamos la URL de búsqueda con la consulta del usuario
    url = f"https://www.google.com/search?q={consulta}"

    # Abrimos el navegador con la URL de búsqueda
    webbrowser.open(url)

    print(f"Buscando '{consulta}' en Google...")
while True:
    buscar_en_google()
