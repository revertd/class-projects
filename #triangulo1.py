def crear_triangulo(altura):
    for i in range(1, altura + 1):
        espacios = '' * (altura - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
    
altura = int(input("Introduce la altura del triángulo deseado:"))
crear_triangulo(altura)
