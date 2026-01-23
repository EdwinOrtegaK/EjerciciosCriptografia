def xor_binario(binario1, binario2):
    binario1 = binario1.replace(" ", "")
    binario2 = binario2.replace(" ", "")

    if len(binario1) != len(binario2):
        print("Error: los binarios deben tener la misma longitud")
        return ""

    resultado = ""

    for i in range(len(binario1)):
        b1 = binario1[i]
        b2 = binario2[i]

        if b1 == b2:
            resultado += "0"
        else:
            resultado += "1"

    return resultado

bin1 = input("Ingrese el primer binario: ")
bin2 = input("Ingrese el segundo binario: ")

resultado = xor_binario(bin1, bin2)
print("El resultado XOR es:", resultado)
