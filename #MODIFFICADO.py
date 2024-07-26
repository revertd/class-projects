def contar_letras_a(palabra):
    return palabra.lower().count('a')

def main():
    palabras = []
    
    print("Por favor, ingresa 4 palabras:")
    for i in range(4):
        palabra = input(f"Palabra {i + 1}: ")
        palabras.append(palabra)

    max_a = 0
    palabra_max_a = ""

    print("\nConteo de letras 'a' en cada palabra:")
    for palabra in palabras:
        conteo = contar_letras_a(palabra)
        print(f"La palabra '{palabra}' tiene {conteo} letra(s) 'a'.")

        if conteo > max_a:
            max_a = conteo
            palabra_max_a = palabra

    if max_a > 0:
        print(f"\nLa palabra con más letras 'a' es '{palabra_max_a}' con {max_a} letra(s) 'a'.")
    else:
        print("\nNo se encontraron letras 'a' en ninguna de las palabras.")

if __name__ == "__main__":
    main()