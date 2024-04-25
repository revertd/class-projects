print("Calcula el IMC de tus estudiantes.")

def solicita_nombre_estudiante():
    return input("Ingresa el nombre del estudiante: ")

def solicita_edad_estudiante():
    return int(input("Ingresa la edad del estudiante en años: "))

def solicita_altura_estudiante():
    return float(input("Ingresa la altura del estudiante en metros: "))

def solicita_peso_estudiante():
    return float(input("Ingresa el peso del estudiante en kilogramos: "))

def solicita_rut_estudiante():
    return input("Ingresa el RUT del estudiante: ")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def determinar_estado(imc):
    if imc <= 15.99:
        return "delgadez severa"
    elif imc <= 16.99:
        return "delgadez moderada"
    elif imc <= 18.49:
        return "delgadez leve"
    elif imc <= 24.99:
        return "peso normal"
    elif imc <= 29.99:
        return "sobrepeso"
    elif imc <= 34.99:
        return "obesidad leve"
    elif imc <= 39.99:
        return "obesidad media"
    else:
        return "obesidad morbida"

def main():
    estudiantes = []
    
    for _ in range(3):
        nombre = solicita_nombre_estudiante()
        edad = solicita_edad_estudiante()
        altura = solicita_altura_estudiante()
        peso = solicita_peso_estudiante()
        rut = solicita_rut_estudiante()
        
        imc = calcular_imc(peso, altura)
        estado = determinar_estado(imc)
        
        estudiantes.append((nombre, imc, edad, rut, estado))
    
    print("\nResultados:")
    for nombre, imc, edad, rut, estado in estudiantes:
        print(f"Nombre: {nombre}, IMC: {imc:.2f}, Edad: {edad} años, RUT: {rut}, Estado: {estado}")

if __name__ == "__main__":
    main()
