#crea un programa que permita ingresar por teclado el rut, el nombre completo, dob, y la institución
#luego crea un correo electronico con las siguientes caracteristicas, inicial del primer nombre, primer apellido
#completo, año de nacimiento, -, institución en silabas, @gmail.com
#contraseña: segundo nombre completo, primero 4 digitos del rut, para dos personas, se guarda en diccionario.

print("Este programa te permite crear un correo y una contraseña fácil de recordar.")

def solicitar_el_primer_nombre():
    return input("Ingresa tu primer nombre: ")

def solicitar_el_segundo_nombre():
    return input("Ingresa tu segundo nombre: ")
           
def solicitar_el_primer_apellido():
    return input("Ingresa tu primer apellido: ")
           
def solicitar_el_segundo_apellido():
    return input("Ingresa tu segundo apellido: ")
           
def solicitar_rut():
    return input("Ingresa tu rut (sin puntos, ej: '22300190-7') : ")
    
def solicitar_dob():
    return input("Ingresa tu año nacimiento (ej: '2000')")
    
def solicitar_institución():
    return input("Ingresa el nombre de tu institución en sílabas (ej: Policía de Investigaciones = 'PDI'):")
    
    
def main():
    correo = []
    password = []
    
    for _ in range(2):
         nom1 = solicitar_el_primer_nombre()
         nom2 = solicitar_el_segundo_nombre()
         ape1 = solicitar_el_primer_apellido()
         ape2 = solicitar_el_segundo_apellido()
         rut = solicitar_rut()
         dob = solicitar_dob()
         ins = solicitar_institución()
         
         correo.append((nom1, nom2, ape1, ape2, rut, dob, ins))
         
         password.append((nom1, nom2, ape1, ape2, rut, dob, ins))
         
    print("\nCorreo: ")
    for nom1, nom2, ape1, ape2, rut, dob, ins in correo:
        print(nom1[0],ape1,dob,"-",ins,"@gmail.com", sep="")
        
    print("\nConstraseña: ")
    for nom1, nom2, ape1, ape2, rut, dob, ins in password:
        print(nom2, rut[0:3], sep="")
        
if __name__ == "__main__":
    main()
