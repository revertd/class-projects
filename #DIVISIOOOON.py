#escribe un programa que pida 2 números enteros y calcule si su división es exacta o no

def division_exacta(num1, num2):
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    elif num1 % num2 == 0:
        print(f"La división entre {num1} y {num2} es exacta.")
    else:
        print(f"La división entre {num1} y {num2} no es exacta.")

def main():
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    division_exacta(num1, num2)

if __name__ == "__main__":
    main()
