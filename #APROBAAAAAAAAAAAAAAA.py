#APROBAAAAAADOOOOOOOOOOOOOOOOOOO

print("Calcula si aproboraron o reprobaron tus 4 estudiantes en la asignatura de programación.")


def solicitar_nombre_estudiante():
    return input("Ingrese el nombre del estudiante: ")  # Solicita al usuario que ingrese el nombre del estudiante.

def solicitar_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante en la asignatura: "))  # Pide al usuario que ingrese la nota del estudiante.
            if nota < 1.0 or nota > 7.0:  # Verifica si la nota está dentro del rango permitido.
                print("La nota debe estar entre 1.0 y 7.0")  # Si la nota está fuera del rango, muestra un mensaje de error.
            else:
                return nota  # Muestra la nota si está dentro del rango permitido.
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Si se produce un error al convertir la entrada a un número, muestra un mensaje de error.

def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 1)  # Calcula el promedio de las notas y lo redondea a un decimal.

def main():
    estudiantes = []  # Crea una lista vacía para almacenar los datos de los estudiantes.

    for _ in range(4):
        nombre = solicitar_nombre_estudiante()  # Pide el nombre del estudiante.
        notas = []
        for _ in range(4):
            nota = solicitar_nota()  # Pide la nota del estudiante.
            notas.append(nota)  # Agrega la nota a la lista de notas.
        estudiantes.append((nombre, notas))  # Agrega el nombre y las notas del estudiante a la lista de estudiantes.

    for nombre, notas in estudiantes:
        promedio = calcular_promedio(notas)  # Calcula el promedio de las notas del estudiante.
        if promedio >= 4.0:
            print(f"{nombre} ha aprobado con un promedio de {promedio}")  # Muestra un mensaje indicando que el estudiante ha aprobado.
        else:
            print(f"{nombre} ha reprobado con un promedio de {promedio}")  # Muestra un mensaje indicando que el estudiante ha reprobado.

if __name__ == "__main__":
    main()