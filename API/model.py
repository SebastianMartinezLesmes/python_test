# model.py

class Usuario:
    def __init__(self, nombre, login, total_repos, ubicacion, email, bio, seguidores):
        self.nombre = nombre
        self.login = login
        self.total_repos = total_repos
        self.ubicacion = ubicacion
        self.email = email
        self.bio = bio
        self.seguidores = seguidores

    def mostrar(self):
        print(f"\n👤 Nombre del perfil: {self.nombre or 'No disponible'}")
        print(f"🔗 Usuario: {self.login}")
        print(f"📧 Email: {self.email or 'No disponible'}")
        print(f"📍 Ubicación: {self.ubicacion or 'No especificada'}")
        print(f"📝 Bio: {self.bio or 'No disponible'}")
        print(f"⭐ Seguidores: {self.seguidores}")
        print(f"📦 Repos públicos: {self.total_repos}")

class Repositorio:
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje or "No especificado"

    def mostrar(self):
        print(f"  - {self.nombre} ({self.lenguaje})")
