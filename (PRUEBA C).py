#crea un programa que permita calcular el volumen de los siguientes cuerpos geometricos. el usuario debe de eligir el cuerpo y debe ingresar
#los parametros necesarios para calcular, el programa debe preguntar una vez hecho si el usuario quiere calcular el volumen de otro cuerpo

def calcular_volumen():
    pi = 3.14
    print("Selecciona el cuerpo geométrico:")
    print("1. Cubo")
    print("2. Prisma")
    print("3. Cilindro")
    print("4. Esfera")
    opcion = input("Ingresa el número de la opción que quieres: ")
    if opcion == "1":
        lado = float(input("Ingresa la longitud del lado del cubo: "))
        volumen = lado ** 3
        print(f"El volumen del cubo es: {volumen:.2f}")
    elif opcion == "2":
        base = float(input("Ingresa el área de la base del prisma: "))
        altura = float(input("Ingresa la altura del prisma: "))
        volumen = base * altura
        print(f"El volumen del prisma es: {volumen:.2f}")
    elif opcion == "3":
        radio = float(input("Ingresa el radio de la base del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        volumen = pi * radio ** 2 * altura
        print(f"El volumen del cilindro es: {volumen:.2f}")
    elif opcion == "4":
        radio = float(input("Ingresa el radio de la esfera: "))
        volumen = (4/3) * pi * radio ** 3
        print(f"El volumen de la esfera es: {volumen:.2f}")
    else:
        print("Opción inválida. Por favor, selecciona un número del 1 al 4.")
    
    otra_vez = input("Deseas calcular el volumen de otro cuerpo geométrico? (s/n): ")
    if otra_vez() == "s":
        calcular_volumen()

calcular_volumen()
