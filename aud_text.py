import speech_recognition as sr
import time
import threading

# Función para la cuenta regresiva
def contador_regresivo(tiempo_limite):
    for i in range(tiempo_limite, 0, -1):
        print(f"\rContando: {i} segundos...", end="")
        time.sleep(1)
    print("\n¡Tiempo para hablar!")

# Función para grabar el audio y transcribir
def grabar_y_transcribir(tiempo_limite):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("¡Habla ahora!")

        try:
            audio = recognizer.listen(source, timeout=tiempo_limite, phrase_time_limit=tiempo_limite)
        except sr.WaitTimeoutError:
            return "No se detectó ningún sonido."

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender lo que dijiste."
    except sr.RequestError as e:
        return f"Error al conectar con el servicio de reconocimiento: {e}"

# Función principal que coordina la grabación y el contador
def ejecutar_grabacion_y_contador(tiempo_limite=5):
    # Crear un hilo para el contador
    contador_thread = threading.Thread(target=contador_regresivo, args=(tiempo_limite,))
    contador_thread.start()

    # Grabar y transcribir mientras el contador se ejecuta
    resultado = grabar_y_transcribir(tiempo_limite)

    # Esperar a que termine el hilo del contador
    contador_thread.join()

    print("Texto transcrito:", resultado)

# Ejecutar el programa
ejecutar_grabacion_y_contador(5)  # Puedes cambiar el número de segundos

