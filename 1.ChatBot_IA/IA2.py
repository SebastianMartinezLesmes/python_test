import openai
import config

# Configura tu clave de API
openai.api_key = config.api_key1  # Utiliza la clave de API correctamente

# Lista de palabras clave para terminar la conversación
palabras_clave_terminar = ["salir", "adios", "chao", "cerrar", "finalizar", "terminar", ""]

def crear_respuesta(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=50  # Ajusta este valor según tus necesidades
    )
    return response.choices[0].text

# Ejemplo de conversación con el chatbot
while True:
    usuario_input = input("Tú: ")
    input_en_minusculas = usuario_input.lower()  # Convertir a minúsculas para hacer coincidencia sin importar mayúsculas o minúsculas

    if input_en_minusculas in palabras_clave_terminar:
        print("Chatbot: Gracias por usar este humilde ChatBot")
        break
    respuesta = crear_respuesta(f"Tú: {usuario_input}\nChatbot:")
    print("Chatbot: ", respuesta)
