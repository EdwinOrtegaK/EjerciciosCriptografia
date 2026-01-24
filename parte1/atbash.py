def cifrado_atbash(texto):
    resultado = ""

    for c in texto:
        if c.isalpha():
            if c.isupper():
                resultado += chr(90 - (ord(c) - 65))
            else:
                resultado += chr(122 - (ord(c) - 97))
        else:
            resultado += c

    return resultado

mensaje = "Hola Mundo"
cifrado = cifrado_atbash(mensaje)
descifrado = cifrado_atbash(cifrado)

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", descifrado)
