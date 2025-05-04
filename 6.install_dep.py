import subprocess
import os
import sys

# 1. Pedir al usuario la ruta del archivo
ruta = input("Introduce la ruta del archivo Python a ejecutar: ").strip()

if not os.path.isfile(ruta):
    print("Error: el archivo no existe.")
    sys.exit(1)

# 2. Generar o usar requirements.txt para instalar dependencias
directorio = os.path.dirname(os.path.abspath(ruta))
requirements_path = os.path.join(directorio, "requirements.txt")

# Si no existe un requirements.txt, intentar generarlo con pipreqs
if not os.path.exists(requirements_path):
    print("Generando requirements.txt con pipreqs...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pipreqs"])
    subprocess.run(["pipreqs", directorio, "--force"])

# Instalar las dependencias
print("Instalando dependencias...")
instalacion = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], capture_output=True, text=True)

print("Dependencias instaladas:\n")
print(instalacion.stdout)

# 3. Ejecutar el archivo principal
# print(f"Ejecutando: {ruta}\n")
# subprocess.run([sys.executable, ruta])
