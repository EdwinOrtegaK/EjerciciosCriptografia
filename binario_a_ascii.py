def binario_a_decimal(binario):
    decimal = 0
    potencia = 1

    for bit in binario[::-1]:
        if bit == "1":
            decimal += potencia
        potencia *= 2

    return decimal


def binario_a_ascii(binario):
    binario = binario.replace(" ", "").replace("\n", "")
    texto = ""

    i = 0
    while i < len(binario):
        byte = binario[i:i+8]
        valor = binario_a_decimal(byte)
        texto += chr(valor)
        i += 8

    return texto


binario = input("Ingrese el binario: ")
print("El ASCII es:", binario_a_ascii(binario))
