#crea un programa que pida tres números, este programa debe de identificar si los números son diferentes, o 2 iguales.

def identificar_numeros(num1, num2, num3):
    if num1 == num2 == num3:
        print("Los tres números son iguales.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Hay dos números iguales.")
    else:
        print("Los tres números son diferentes.")

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    identificar_numeros(num1, num2, num3)

if __name__ == "__main__":
    main()
