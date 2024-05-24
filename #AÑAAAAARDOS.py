#crea un programa que permita ingresar 2 años por teclado, el programa debe identificar si el año número uno está antes o después que el año 2 y los años que en pasado entre estos

def comparar_años(año1, año2):
    if año1 < año2:
        print(f"{año1} está antes que {año2}")
        print("Años que faltan entre los dos años:")
        for año in range(año1 + 1, año2):
            print(año)
    elif año1 > año2:
        print(f"{año1} está después que {año2}")
        print("Años que han pasado entre los dos años:")
        for año in range(año2 + 1, año1):
            print(año)
    else:
        print("Los dos años son iguales")

def main():
    print("Este programa te ayuda a comparar años: ")
    año1 = int(input("Ingrese el primer año: "))
    año2 = int(input("Ingrese el segundo año: "))

    comparar_años(año1, año2)

if __name__ == "__main__":
    main()
   
