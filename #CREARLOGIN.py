def crear_cuenta():
    username = input("Ingresa un nombre de usuario: ")
    
    while True:
         password = input("Ingresa una contraseña (minimo de 6 caracteres, con la letra inicial del nombre de usuario como primer caracter): ")
         if len(password) < 6 and password [0] != username[0]:
             print("La contraseña debe de tener minimo 6 caracteres y debe de tener la letra inicial del nombre de usuario como primer caracter")
         else:
             break
    
    print(f"Cuenta creada correctamente. Nombre de usuario {username}, Contraseña: {password} ")
    return username, password
    
def iniciar_sesion(username, password):
    user_input_username = input("Ingrese el nombre de usuario: ")
    user_input_password = input("Ingrese la contraseña: ")
    
    if user_input_password == password and user_input_username == username:
        print(f"Bienvenido {username}")
    else:
        
        print("Nombre de usuario o contraseña incorrecta, vuelvelo a intentar: ")
            
username, password = crear_cuenta()
iniciar_sesion(username, password)
