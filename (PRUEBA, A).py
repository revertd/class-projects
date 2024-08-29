print("Ingresa números, la cantidad es al gusto del usuario, el programa contará cuántos de estos números son pares e impares. Para salir, ingresa la palabra 'fin'.")
par = 0
impar = 0
while True:
    a = input("Ingresa un número (o 'fin' para salir): ")
    if a == 'fin':
        break
    try:
        num = int(a)
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    except ValueError:
        print("Por favor, ingresa un número válido o 'fin' para salir.")
print(f"La cantidad total de números impares es: {impar} y la cantidad total de números pares es: {par}")
