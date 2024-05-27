def main():
    numeros = []

    for i in range(18):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print("Números pares:")
    for par in pares:
        print(par)

    print("\nNúmeros impares:")
    for impar in impares:
        print(impar)

if __name__ == "__main__":
    main()
