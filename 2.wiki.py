import wikipediaapi

def buscar_wikipedia(termino, idioma='es'):
    wiki = wikipediaapi.Wikipedia(idioma)
    pagina = wiki.page(termino)
    
    if not pagina.exists():
        return f"No se encontró información para: {termino}"
    
    return pagina.summary

if __name__ == "__main__":
    termino = input("Introduce un término de búsqueda: ")
    resultado = buscar_wikipedia(termino)
    print("\nResultado:\n", resultado)
