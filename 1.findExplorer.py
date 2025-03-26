import webbrowser

def buscar_en_google():
    print("=== BUSCADOR DE GOOGLE ===")
    consulta = input("¿Qué deseas buscar en Google?: ")

    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    
    print(f"Buscando '{consulta}' en Google...")
while True:
    buscar_en_google()
