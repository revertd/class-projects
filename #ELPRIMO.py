def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
        return True
def generar_primos(limit):
    primos = []
    for i in range(2, limit + 1):
        if es_primo(i):
            primos.append(i)
    return primos
    
limit = int(input("Ingresa un número para que se muestren los números primos de este"))
primos = generar_primos(limit)

print(f"Los números primos hasta {limit} son:")
print(primos)
