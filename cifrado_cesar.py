def cifrado_cesar(texto, desplazamiento, modo='cifrar'):
    resultado = ''
    for char in texto:
        if char.isalpha():
            # Determina si el carácter es mayúscula o minúscula
            start = 65 if char.isupper() else 97
            # Calcula el nuevo valor desplazado
            nueva_posicion = (ord(char) - start + (desplazamiento if modo == 'cifrar' else -desplazamiento)) % 26
            resultado += chr(start + nueva_posicion)
        else:
            # Si no es una letra, lo agregamos sin cambios
            resultado += char
    return resultado

# Ejemplo de uso
texto = "Hola Mundo"
desplazamiento = 3
texto_cifrado = cifrado_cesar(texto, desplazamiento, modo='cifrar')
texto_descifrado = cifrado_cesar(texto_cifrado, desplazamiento, modo='descifrar')

print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)
