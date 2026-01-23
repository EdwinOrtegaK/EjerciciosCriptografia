BASE64_ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def decimal_a_binario(numero):
    binario = ""

    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    while len(binario) < 8:
        binario = "0" + binario

    return binario

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

        # Prompt del codigo sacado de ChatGPT:
        # Genera el código para reconstruir un bloque de 24 bits a partir de
        # cuatro valores Base64 (con 6 bits cada uno) con el desplazamientos de los mismos,
        # y así extraer los bytes originales de 8 bits aplicando corrimientos
        # teniendo en cuenta el padding que hemos usado
        bloque = (vals[0] << 18) | (vals[1] << 12) | (vals[2] << 6) | vals[3]

        res += decimal_a_binario((bloque >> 16) & 255) + " "
        if pad < 2:
            res += decimal_a_binario((bloque >> 8) & 255) + " "
        if pad < 1:
            res += decimal_a_binario(bloque & 255) + " "

        i += 4

    return res.strip()

texto = input("Ingrese el texto en Base64: ")
print("El binario es:", base64_a_binario(texto))
