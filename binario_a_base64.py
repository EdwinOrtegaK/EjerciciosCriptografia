BASE64_ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def binario_a_decimal(binario):
    decimal = 0
    potencia = 1

    for bit in binario[::-1]:
        if bit == "1":
            decimal += potencia
        potencia *= 2

    return decimal

# Parte del código de esta función fue creado con ayuda de ChatGPT
def binario_a_base64(binario):
    binario = binario.replace(" ", "")

    resultado = ""
    i = 0

    while i < len(binario):
        bloque = binario[i:i+24]

        bits_faltantes = 24 - len(bloque)
        bloque += "0" * bits_faltantes

        for j in range(0, 24, 6):
            grupo6 = bloque[j:j+6]
            valor = binario_a_decimal(grupo6)
            resultado += BASE64_ALFABETO[valor]

        i += 24

    bytes_originales = len(binario) // 8
    if bytes_originales % 3 == 1:
        resultado = resultado[:-2] + "=="
    elif bytes_originales % 3 == 2:
        resultado = resultado[:-1] + "="

    return resultado

binario = input("Ingrese el binario: ")
print("El Base64 es:", binario_a_base64(binario))
