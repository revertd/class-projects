con = 0
lista = []
print("Encuentra el número secreto del 1 al 10")
while con < 3:
    a = int(input("Ingresa un número del 1 al 10: "))
    con = con + 1
    lista.append(a)
    if a == 6:
        boom = print("¡Has acertado en", con, "intentos!")
        break
    else:
        grah = input("Has fallado, ¿quieres intentarlo de nuevo? (si/no): ")
        if grah == "si":
            continue
        elif grah == "no":
            boom = exit()
print(boom)
