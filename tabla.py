#crea las tablas de multiplicar, hasta un nùmero ingresado por teclado, hasta el 12
número = int(input("Ingresa un número del cual se te mostrará su tabla de multiplicar hasta el 12: "))

if número < 1:
    print("Ingresa un número positivo")
else:
    for i in range(1, número + 1):
        print(f"\nTabla de multiplicar del {i}:")
        for j in range(1, 13):
            resultado = i * j 
            print(f"{i} x {j} = {resultado}")
            


