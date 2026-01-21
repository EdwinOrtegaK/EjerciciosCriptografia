def ascii_a_binario(texto):
    return " ".join(format(ord(c), "08b") for c in texto)

texto = input("Ingrese una palabra o frase: ")
binario = ascii_a_binario(texto)

print("El binario es:", binario)
