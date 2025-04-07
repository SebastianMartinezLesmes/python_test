import json
from openpyxl import Workbook
from tkinter import Tk, filedialog

# Ocultar la ventana principal de tkinter
Tk().withdraw()

# Abrir un selector de archivos para que el usuario elija el JSON
ruta_json = filedialog.askopenfilename(
    title="Selecciona el archivo JSON",
    filetypes=[("Archivos JSON", "*.json")]
)

# Verificar si el usuario seleccionó un archivo
if not ruta_json:
    print("No se seleccionó ningún archivo.")
else:
    # Cargar datos desde el archivo JSON seleccionado
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    # Crear un nuevo libro de Excel
    wb = Workbook()
    hoja = wb.active
    hoja.title = "Datos"

    # Verificar que haya datos
    if datos:
        # Usar las claves del primer objeto como encabezados
        encabezados = list(datos[0].keys())
        hoja.append(encabezados)

        # Agregar los datos fila por fila
        for fila in datos:
            hoja.append([fila[campo] for campo in encabezados])
        
        # Guardar el archivo Excel
        nombre_salida = ruta_json.replace(".json", ".xlsx")
        wb.save(nombre_salida)
        print(f"Archivo Excel creado exitosamente como: {nombre_salida}")
    else:
        print("El archivo JSON está vacío.")
