def contar_vocales(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in palabra if letra in vocales)

def main():
    palabras = []
    
    print("Por favor, ingresa 4 palabras:")
    for i in range(4):
        palabra = input(f"Palabra {i + 1}: ")
        palabras.append(palabra)

    max_vocales = 0
    palabra_max_vocales = ""

    print("\nConteo de vocales en cada palabra:")
    for palabra in palabras:
        conteo = contar_vocales(palabra)
        print(f"La palabra '{palabra}' tiene {conteo} vocal(es).")

        if conteo > max_vocales:
            max_vocales = conteo
            palabra_max_vocales = palabra

    if max_vocales > 0:
        print(f"\nLa palabra con más vocales es '{palabra_max_vocales}' con {max_vocales} vocal(es).")
    else:
        print("\nNo se encontraron vocales en ninguna de las palabras.")

if __name__ == "__main__":
    main()