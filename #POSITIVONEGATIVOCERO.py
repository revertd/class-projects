#crea un programa que identifique si el número ingresado es negativo, positivo o cero

def identificar_numero(num):
    if num > 0:
        print(f"{num} es un número positivo.")
    elif num < 0:
        print(f"{num} es un número negativo.")
    else:
        print("El número ingresado es cero.")

def main():
    num = float(input("Ingrese un número: "))
    identificar_numero(num)

if __name__ == "__main__":
    main()
