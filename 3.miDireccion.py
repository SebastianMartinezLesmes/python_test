import subprocess
import sys
from datetime import datetime

def instalar_dependencias():
    try:
        import geocoder
        import folium
    except ImportError:
        print("Instalando dependencias necesarias...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "geocoder", "folium"])
        import geocoder
        import folium
    return geocoder, folium

def obtener_datos_ubicacion():
    geocoder, folium = instalar_dependencias()
    ubicacion = geocoder.ip('me')

    data = {
        "ip": ubicacion.ip if hasattr(ubicacion, 'ip') else "No disponible",
        "latitud": str(ubicacion.latlng[0]) if ubicacion.latlng else "No disponible",
        "longitud": str(ubicacion.latlng[1]) if ubicacion.latlng else "No disponible",
        "ciudad": ubicacion.city if hasattr(ubicacion, 'city') else "No disponible",
        "region": ubicacion.state if hasattr(ubicacion, 'state') else "No disponible",
        "pais": ubicacion.country if hasattr(ubicacion, 'country') else "No disponible",
        "hora_ejecucion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\nDatos de ubicación obtenidos:")
    print("=" * 50)
    for clave, valor in data.items():
        print(f"{clave.capitalize()}: {valor}")
    print("=" * 50)

    if ubicacion.latlng:
        mapa = folium.Map(location=ubicacion.latlng, zoom_start=12)
        folium.Marker(
            location=ubicacion.latlng,
            popup=f"IP: {data['ip']}\nCiudad: {data['ciudad']}\nRegión: {data['region']}\nPaís: {data['pais']}",
            tooltip="Tu ubicación aproximada",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(mapa)

        mapa.save("mapa_interactivo.html")
        print("\n✅ Mapa interactivo generado: 'mapa_interactivo.html'")
    else:
        print("⚠️ No se pudo obtener la ubicación precisa para mostrar el mapa.")

    return data

if __name__ == "__main__":
    obtener_datos_ubicacion()
