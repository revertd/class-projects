def contar_letras_a(palabra):
    return palabra.lower().count('a')

def main():
    palabras = []
    
    print("Por favor, ingresa 4 palabras:")
    for i in range(4):
        palabra = input(f"Palabra {i + 1}: ")
        palabras.append(palabra)

    print("\nConteo de letras 'a' en cada palabra:")
    for i, palabra in enumerate(palabras):
        conteo = contar_letras_a(palabra)
        print(f"La palabra '{palabra}' tiene {conteo} letra(s) 'a'.")

if __name__ == "__main__":
    main()