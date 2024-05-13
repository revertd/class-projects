#LISTADEDIEZNOMBRES




def solicitar_primer_nombre():
    return input("Ingresa un nombre: ")
    
def solicitar_segundo_nombre():
    return input("Ingresa un nombre: ")
    
def solicitar_tercer_nombre():
    return input("Ingresa un nombre: ")

def solicitar_cuarto_nombre():
    return input("Ingresa un nombre: ")

def solicitar_quinto_nombre():
    return input("Ingresa un nombre: ")

def solicitar_sexto_nombre():
    return input("Ingresa un nombre: ")

def solicitar_septimo_nombre():
    return input("Ingresa un nombre: ")

def solicitar_octavo_nombre():
    return input("Ingresa un nombre: ")

def solicitar_noveno_nombre():
    return input("Ingresa un nombre: ")

def solicitar_decimo_nombre():
    return input("Ingresa un nombre: ")
    
    
def main():
    lista = []
    
    for _ in range(1):
         a = solicitar_primer_nombre()
         b = solicitar_segundo_nombre()
         c = solicitar_tercer_nombre()
         d = solicitar_cuarto_nombre()
         e = solicitar_quinto_nombre()
         f = solicitar_sexto_nombre()
         g = solicitar_septimo_nombre()
         h = solicitar_octavo_nombre()
         i = solicitar_noveno_nombre()
         j = solicitar_decimo_nombre()
         
         lista.append((a, b, c, d, e, f, g, h, i, j))
        
    print("\nLista:")
    for a, b, c, d, e, f, g, h, i, j in lista:
        print(a, b, c, d, e, f, g, h, i, j)
        lista = [a,b,c,d,e,f,g,h,i,j]
        lista[3], lista[5] = lista[5], lista[3]
        print(lista)
        lista[3], lista[7] = lista[7], lista[3]
        print(lista)
        lista[1], lista[-2] = lista[-2], lista[1]
        print(lista)
    
if __name__ == "__main__":
    main()
