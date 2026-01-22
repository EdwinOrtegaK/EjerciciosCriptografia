def decimal_a_binario(numero):
    binario = ""

    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    while len(binario) < 8:
        binario = "0" + binario

    return binario

def ascii_a_binario(texto):
    resultado = ""

    for caracter in texto:
        ascii_decimal = ord(caracter)
        binario = decimal_a_binario(ascii_decimal)
        resultado += binario + " "

    return resultado.strip()


texto = input("Ingrese una palabra o frase: ")
binario = ascii_a_binario(texto)

print("El binario es:", binario)
