# index.py

import urllib.request
import json
from config import URL_PERFIL, URL_REPOS
from model import Usuario, Repositorio

def obtener_datos(url):
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print("❌ Error al hacer la solicitud:", e)
        return None

def main():
    perfil_data = obtener_datos(URL_PERFIL)
    if perfil_data:
        usuario = Usuario(
            nombre=perfil_data.get("name"),
            login=perfil_data.get("login"),
            bio=perfil_data.get("bio"),
            total_repos=perfil_data.get("public_repos"),
            ubicacion=perfil_data.get("location"),
            email=perfil_data.get("email"),
            seguidores=perfil_data.get("followers")
        )
        usuario.mostrar()

    repos_data = obtener_datos(URL_REPOS)
    if repos_data:
        print("\n📂 Repositorios:")
        for repo in repos_data:
            repositorio = Repositorio(
                nombre=repo.get("name"),
                lenguaje=repo.get("language")
            )
            repositorio.mostrar()

if __name__ == "__main__":
    main()
