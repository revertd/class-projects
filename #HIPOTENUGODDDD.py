#crea un codigo que permita calcular la hiporenusa de un triangulo rectangulo ingresando por teclado sus catetos y demostrar por pantalla
#el siguiente mensage: la hipotenusa del tirangulo rectangulo es:
    
def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
    return hipotenusa

def main():
    cateto1 = float(input("Ingrese la longitud del primer cateto: "))
    cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

    hipotenusa = calcular_hipotenusa(cateto1, cateto2)

    print("La hipotenusa del triángulo rectángulo es:", hipotenusa)

if __name__ == "__main__":
    main()
