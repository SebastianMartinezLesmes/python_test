import random
import string
import json

temas_palabras = {
    "astronomía": ["planeta", "galaxia", "estrella", "cometa", "nebulosa", "luz", "saturno"],
    "música": ["melodía", "nota", "guitarra", "piano", "ritmo", "voz", "bajo"],
    "gastronomía": ["receta", "sabor", "ingrediente", "chef", "cocina", "plato", "horno"],
    "videojuegos": ["consola", "pantalla", "nivel", "juego", "control", "avatar", "enemigo"],
    "escritores": ["novela", "autor", "cuento", "poesía", "libro", "letras", "ensayo"],
    "emociones": ["alegría", "miedo", "enojo", "tristeza", "amor", "sorpresa", "ansiedad"],
    "Tecnología": ["robot", "código", "internet", "pantalla", "teclado", "red", "chip", "algoritmo", "wifi", "programa"],
    "Ciencia": ["átomo", "molecular", "física", "química", "biología", "laboratorio", "experimento", "genética", "astro", "químico"],
    "Educación": ["escuela", "alumno", "maestro", "estudio", "clase", "examen", "biblioteca", "comunidad", "educación", "aprendizaje"],
    "Salud y bienestar": ["medicina", "ejercicio", "nutrición", "salud", "cuerpo", "bienestar", "dieta", "vacuna", "cura", "tratamiento"],
    "Medio ambiente": ["ecología", "contaminación", "bosque", "río", "sostenible", "reciclaje", "naturaleza", "clima", "planeta", "verde"],
    "Economía y finanzas": ["mercado", "inversión", "ahorro", "banco", "activo", "dinero", "crédito", "prestamo", "inflación", "capital"],
    "Arte y cultura": ["música", "pintura", "danza", "teatro", "escultura", "fotografía", "cine", "poesía", "literatura", "mural"],
    "Historia": ["antiguo", "medieval", "imperio", "guerrero", "dinastía", "época", "revolución", "historia", "batalla", "guerra"],
    "Psicología": ["mente", "emociones", "conducta", "cerebro", "psiquiatría", "terapia", "estrés", "ansiedad", "depresión", "autoconocimiento"],
    "Deportes": ["fútbol", "balón", "correr", "atletismo", "natación", "gimnasia", "básquet", "tenis", "boxeo", "rugby"],
    "Videojuegos": ["juego", "nivel", "consola", "avatar", "pantalla", "enemigos", "jugador", "puzzle", "acertijo", "control"],
    "Filosofía": ["ética", "moral", "existencia", "sabiduría", "razón", "metafísica", "conocimiento", "pensamiento", "logos", "idealismo"],
    "Política": ["gobierno", "estado", "leyes", "partido", "candidato", "democracia", "sociedad", "voto", "congreso", "política"],
    "Viajes y turismo": ["avión", "hotel", "destino", "excursión", "mapa", "guía", "pasaporte", "vacaciones", "playa", "excursión"],
    "Alimentación y nutrición": ["fruta", "verdura", "dieta", "caloría", "proteína", "minerales", "carbohidrato", "salud", "comida", "nutrición"],
    "Desarrollo personal": ["crecimiento", "autoayuda", "liderazgo", "motivación", "metas", "superación", "habilidades", "propósito", "mente", "objetivos"],
    "Música": ["melodía", "nota", "guitarra", "piano", "ritmo", "bajo", "voz", "tambores", "composición", "canción"],
    "Literatura": ["novela", "cuento", "poesía", "ensayo", "libro", "escritor", "relato", "trama", "género", "cuento"],
    "Cine y televisión": ["película", "actor", "guion", "directores", "series", "episodio", "teatro", "cine", "documental", "reparto"],
    "Religión y espiritualidad": ["fe", "dios", "oración", "meditación", "alma", "espíritu", "creencias", "iglesia", "templo", "biblia"],
    "Emprendimiento y negocios": ["empresa", "inversión", "capital", "negocios", "startup", "innovación", "liderazgo", "mercado", "estrategia", "ventas"]
}

def crear_sopa(tamano):
    return [[' ' for _ in range(tamano)] for _ in range(tamano)]

def colocar_palabra(sopa, palabra):
    tamano = len(sopa)
    palabra_len = len(palabra)
    direccion = random.choice(['horizontal', 'vertical'])
    colocada = False

    while not colocada:
        if direccion == 'horizontal':
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - palabra_len)
            if all(sopa[fila][columna + i] == ' ' for i in range(palabra_len)):
                for i in range(palabra_len):
                    sopa[fila][columna + i] = palabra[i]
                colocada = True
        else:
            fila = random.randint(0, tamano - palabra_len)
            columna = random.randint(0, tamano - 1)
            if all(sopa[fila + i][columna] == ' ' for i in range(palabra_len)):
                for i in range(palabra_len):
                    sopa[fila + i][columna] = palabra[i]
                colocada = True

def rellenar_sopa(sopa):
    for i in range(len(sopa)):
        for j in range(len(sopa[i])):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(string.ascii_uppercase)

def guardar_sopa_jugable_html(sopa, tema, palabras, archivo="sopa_jugable.html"):
    tamano = len(sopa)
    palabras_upper = [p.upper() for p in palabras]
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Sopa de Letras Interactiva</title>
<style>
    body {{
        font-family: 'Segoe UI', sans-serif;
        background: #f2f2f2;
        padding: 20px;
    }}
    h1 {{
        color: #2c3e50;
    }}
    .palabras {{
        font-size: 18px;
        margin-bottom: 20px;
    }}
    table {{
        border-collapse: collapse;
    }}
    td {{
        border: 1px solid #ccc;
        width: 35px;
        height: 35px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        background-color: white;
        cursor: pointer;
    }}
    td.selected {{
        background-color: #74b9ff;
        color: white;
    }}
    td.found {{
        background-color: #55efc4;
        color: black;
    }}
</style>
</head>
<body>

<h1>Tema: {tema.capitalize()}</h1>
<div class="palabras"><strong>Palabras ocultas:</strong> {', '.join(palabras)}</div>
<table id="sopa">
""")
        for i, fila in enumerate(sopa):
            f.write("<tr>\n")
            for j, letra in enumerate(fila):
                f.write(f'<td data-row="{i}" data-col="{j}">{letra}</td>\n')
            f.write("</tr>\n")
        f.write(f"""</table>

<script>
const palabras = {json.dumps(palabras_upper)};
let seleccion = [];
let seleccionActual = "";

document.querySelectorAll("#sopa td").forEach(celda => {{
    celda.addEventListener("mousedown", () => {{
        seleccion = [celda];
        celda.classList.add("selected");
    }});

    celda.addEventListener("mouseover", e => {{
        if (e.buttons === 1) {{
            if (!seleccion.includes(celda)) {{
                seleccion.push(celda);
                celda.classList.add("selected");
            }}
        }}
    }});

    celda.addEventListener("mouseup", () => {{
        const palabraSeleccionada = seleccion.map(c => c.textContent).join('');
        const palabraInversa = palabraSeleccionada.split('').reverse().join('');
        if (palabras.includes(palabraSeleccionada) || palabras.includes(palabraInversa)) {{
            seleccion.forEach(c => {{
                c.classList.remove("selected");
                c.classList.add("found");
            }});
        }} else {{
            seleccion.forEach(c => c.classList.remove("selected"));
        }}
        seleccion = [];
    }});
}});
</script>

</body>
</html>""")

def generar_sopa_interactiva(tamano=12):
    tema = random.choice(list(temas_palabras.keys()))
    palabras = random.sample(temas_palabras[tema], 5)
    palabras_mayus = [p.upper() for p in palabras]

    sopa = crear_sopa(tamano)
    for palabra in palabras_mayus:
        colocar_palabra(sopa, palabra)
    rellenar_sopa(sopa)

    guardar_sopa_jugable_html(sopa, tema, palabras)

# Ejecutar
generar_sopa_interactiva()
