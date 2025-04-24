def cifrado_vigenere(texto, clave, modo='cifrar'):
    resultado = ''
    clave = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]  # Repetir la clave
    for i, char in enumerate(texto):
        if char.isalpha():
            # Determina si el carácter es mayúscula o minúscula
            start = 65 if char.isupper() else 97
            desplazamiento = ord(clave[i].upper()) - 65  # Obtiene el desplazamiento de la clave
            if modo == 'descifrar':
                desplazamiento = -desplazamiento  # Invertir el desplazamiento al descifrar
            nueva_posicion = (ord(char) - start + desplazamiento) % 26
            resultado += chr(start + nueva_posicion)
        else:
            resultado += char  # Si no es una letra, lo agregamos sin cambios
    return resultado

# Ejemplo de uso
texto = "Hola Mundo"
clave = "clave"
texto_cifrado = cifrado_vigenere(texto, clave, modo='cifrar')
texto_descifrado = cifrado_vigenere(texto_cifrado, clave, modo='descifrar')

print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)


'''
Cifrado Vigenère
El cifrado Vigenère utiliza una clave (una palabra o frase) para desplazar cada letra del texto según una posición determinada por la clave. La clave se repite si es más corta que el texto.
'''