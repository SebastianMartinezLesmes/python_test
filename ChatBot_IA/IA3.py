import config
import openai
openai.api_key = config.api_key3

#contexto del asistente
messages=[{"role": "system", "content": "Eres un asistente de traduccion muy util"}]

while True:
    
    content = input("Hola \n¿En que te puede ayudar este humilde ChatBot el dia de hoy? \n")
    
    if content == "salir":
        print("gracias por usar este humilde ChatBot \nHasta la proxima")
        break
    
    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
    
    response_content = response.choices[0].message.content
    
    messages.append({"role": "assistant", "content": content})

    print(response_content)
