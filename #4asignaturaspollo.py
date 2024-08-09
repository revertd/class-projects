def ingresar_notas():
    notas = {}
    asignaturas = ['Matemáticas', 'Lenguaje', 'Inglés', 'Programación']
    
    for asignatura in asignaturas:
        while True:
            try:
                nota = float(input(f"Ingrese la nota de {asignatura} (entre 1 y 7): "))
                if 1 <= nota <= 7:
                    notas[asignatura] = nota
                    break
                else:
                    print("La nota debe estar entre 1 y 7. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
    
    return notas

def calcular_promedio(notas):
    return sum(notas.values()) / len(notas)

def main():
    estudiantes = []
    mejores_promedios = {'Matemáticas': ('', 0), 'Lenguaje': ('', 0), 'Inglés': ('', 0), 'Programación': ('', 0)}

    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        notas = ingresar_notas()
        promedio = calcular_promedio(notas)
        
        estudiantes.append((nombre, notas, promedio))
        
        for asignatura in mejores_promedios.keys():
            if notas[asignatura] > mejores_promedios[asignatura][1]:
                mejores_promedios[asignatura] = (nombre, notas[asignatura])
        
        continuar = input("¿Desea ingresar otro estudiante? (Y/N): ").upper()
        if continuar != 'Y':
            break

    print("\nPromedios de cada estudiante:")
    for estudiante in estudiantes:
        nombre, notas, promedio = estudiante
        print(f"{nombre}: {promedio:.2f}")

    print("\nEstudiante con el mejor promedio en cada asignatura:")
    for asignatura, (nombre, nota) in mejores_promedios.items():
        print(f"{asignatura}: {nombre} con una nota de {nota:.2f}")

if __name__ == "__main__":
    main()
