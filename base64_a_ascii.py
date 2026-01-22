BASE64_ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def decimal_a_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    while len(binario) < 8:
        binario = "0" + binario
    return binario


def binario_a_decimal(binario):
    decimal = 0
    potencia = 1
    for bit in binario[::-1]:
        if bit == "1":
            decimal += potencia
        potencia *= 2
    return decimal


def base64_a_binario(texto):
    texto = texto.replace(" ", "").replace("\n", "")
    res = ""
    i = 0

    while i < len(texto):
        vals = []
        pad = 0

        for j in range(4):
            c = texto[i+j]
            if c == "=":
                vals.append(0)
                pad += 1
            else:
                k = 0
                while BASE64_ALFABETO[k] != c:
                    k += 1
                vals.append(k)

        bloque = (vals[0] << 18) | (vals[1] << 12) | (vals[2] << 6) | vals[3]

        res += decimal_a_binario((bloque >> 16) & 255)
        if pad < 2:
            res += decimal_a_binario((bloque >> 8) & 255)
        if pad < 1:
            res += decimal_a_binario(bloque & 255)

        i += 4

    return res

def binario_a_ascii(binario):
    texto = ""
    i = 0
    while i < len(binario):
        byte = binario[i:i+8]
        valor = binario_a_decimal(byte)
        texto += chr(valor)
        i += 8
    return texto


texto_base64 = input("Ingrese el texto en Base64: ")

binario = base64_a_binario(texto_base64)
ascii_resultado = binario_a_ascii(binario)

print("El ASCII es:", ascii_resultado)
