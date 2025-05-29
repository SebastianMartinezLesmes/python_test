
import requests
from datetime import datetime, timedelta

find_lotery = 'ASTRO'

def obtener_resultados_semana_astro():
    url_base = "https://api-resultadosloterias.com/api/results/"
    hoy = datetime.today()
    lunes = hoy - timedelta(days=hoy.weekday())

    resultados_astro = []

    for i in range(7):
        fecha_actual = lunes + timedelta(days=i)
        fecha_str = fecha_actual.strftime("%Y-%m-%d")
        url = f"{url_base}{fecha_str}"

        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            resultados_dia = datos.get("data", [])

            # Filtrar solo los que contienen "ASTRO" en el nombre de la lotería
            resultados_filtrados = [
                resultado for resultado in resultados_dia
                if find_lotery in resultado.get("lottery", "").upper()
            ]

            if resultados_filtrados:
                resultados_astro.append({
                    "fecha": fecha_str,
                    "resultados": resultados_filtrados
                })
                print(f"✅ Resultados ASTRO obtenidos para {fecha_str}")
            else:
                resultados_astro.append({
                    "fecha": fecha_str,
                    "resultados": []
                })
                print(f"❌ No hubo resultados ASTRO para {fecha_str}")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error obteniendo resultados para {fecha_str}: {e}")

    return resultados_astro

# Ejecutar y mostrar resumen detallado
if __name__ == "__main__":
    semana = obtener_resultados_semana_astro()
    for dia in semana:
        print(f"\n📅 Fecha: {dia['fecha']}")
        for resultado in dia['resultados']:
            print(f"🔮 Lotería {find_lotery}:")
            for clave, valor in resultado.items():
                print(f"   {clave}: {valor}")
