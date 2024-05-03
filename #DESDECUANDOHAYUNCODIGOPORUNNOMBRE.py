#Programa que da un codigo secreto por cada nombre

print('Ingresa 5 nombres')

nom = input("Ingresa el primer nombre : ").lower() 
nom2 = input("Ingresa el segundo nombre : ").lower() 
nom3 = input("Ingresa el tercer nombre : ").lower() 
nom4 = input("Ingresa el cuarto nombre : ").lower() 
nom5 = input("Ingresa el quinto nombre : ").lower() 

aic = [nom, nom2, nom3, nom4, nom5]

kkk = input("Desea revisar estos nombres? (responda con 'si' o 'no'): ")

if kkk == 'no':
    input("Presione ENTER para cerrar el programa.")
    
elif kkk == 'si':
    grah = int(input("Cuál nombre quieres revisar? (1, 2, 3, 4, 5) "))
    
    if grah == 1:
        display2 = print(nom)
        if nom == nom : 
            print("Código secreto para", nom, ": ABC123")
        
    elif grah == 2:
        display2 = print(nom2)
        if nom2 == nom2 :  
            print("Código secreto para", nom2, ": XYZ456")
        
    elif grah == 3:
        display2 = print(nom3)
        if nom3 == nom3 : 
            print("Código secreto para", nom3, ": DEF789")
        
    elif grah == 4:
        display2 = print(nom4)
        if nom4 == nom4 :  
            print("Código secreto para", nom4, ": GHI012")
        
    elif grah == 5:
        display2 = print(nom5)
        if nom5 == nom5 :  
            print("Código secreto para", nom5, ": LMN345")

print(display2)
input("Presiona 'ENTER' para cerrar el programa.")
