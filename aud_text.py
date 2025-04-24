import speech_recognition as sr

def grabar_y_transcribir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, habla ahora...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce ruido ambiental
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender lo que dijiste."
    except sr.RequestError as e:
        return f"Error al conectar con el servicio de reconocimiento: {e}"

# Uso
resultado = grabar_y_transcribir()
print("Texto transcrito:", resultado)
