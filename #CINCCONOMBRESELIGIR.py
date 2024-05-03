#Crea un programa que permite ingresar cinco nombres por teclado luego que el usuario pueda elegir un nombre y se le devuelva.

#SIGNO ZODIACAL



print('Ingresa 5 nombres')


nom = input("Ingresa el primer nombre : ").lower() 
nom2 = input("Ingresa el segundo nombre : ").lower() 
nom3 = input("Ingresa el tercer nombre : ").lower() 
nom4 = input("Ingresa el cuarto nombre : ").lower() 
nom5 = input("Ingresa el quinto nombre : ").lower() 

aic = [nom,nom2,nom3,nom4,nom5]

kkk = input("Desea revisar estos nombres? (responda con 'si' o 'no'): ")

if kkk == 'no':
    input("Presione ENTER para cerrar el programa.")
    
elif kkk == 'si':
    grah = int(input("Cuál nombre quieres revisar? (1,2,3,4,5) "))
    
    if grah == '1' :
        display2 = print(nom)
        
    elif grah == '2' :
        display2 = print(nom2)
        
    elif grah == '3' :
        display2 = print(nom3)
        
    elif grah == '4' :
        display2 = print(nom4)
        
    elif grah == '5' :
        display2 = print(nom5)

print(display2)
input("Presiona 'ENTER' para cerrar el programa.")
