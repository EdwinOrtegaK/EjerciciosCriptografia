import base64

def base64_a_binario(texto_base64):
    bytes_decodificados = base64.b64decode(texto_base64)
    return " ".join(format(byte, "08b") for byte in bytes_decodificados)

texto = input("Ingrese el texto en Base64: ")
binario = base64_a_binario(texto)

print("El binario es:", binario)
