import Funciones as f

#Declaración de variables.
estudiantes = []
asignaturas = []
end = 0
promedio = 0.0

#Se pide al usuario que ingrese sus parámetros + bienvenida.
print("Bienvenido al Sistema de Cálculo de Promedios.")
cantEstudiantes = int(input("Ingrese la cantidad de estudiantes del curso: "))
for i in range(cantEstudiantes):
    estudiantes.append(input(f"Ingrese el nombre del estudiante numero {i+1}: "))

cantAsignaturas = int(input("Ingrese la cantidad de asignaturas del curso: "))

for i in range(cantAsignaturas):
    asignaturas.append(input(f"Ingrese el nombre de la asignatura numero {i+1}: "))
notasDisponibles = cantAsignaturas

for i in range(cantEstudiantes):
    notasEstudiante = []
    promedioAsignatura = []
    promedioFinal = 0.0
    sumaNotasFinal = 0.0
    for e in range(cantAsignaturas):
        notasEstudianteAsignatura = []
        while end == 0:
            cantNotasAsigntura = int(input(f"Ingrese la cantidad de notas de la asignatura {asignaturas[e]} para {estudiantes[i]}: "))
            if cantNotasAsigntura == 0:
                end = 1
                notasEstudianteAsignatura.append(str("No hay notas"))
                promedio = str("No hay notas")
                notasDisponibles -= 1
            else:
                sumNotas = 0.0
                for a in range(cantNotasAsigntura):
                    notasEstudianteAsignatura.append(float(input(f"Ahora está ingresando la nota numero {a+1} (Si es decimal, ingrese la nota de la forma xx.xx, sin usar comas): ")))
                    sumNotas += float(notasEstudianteAsignatura[a])
                promedio = f.calcularPromedio(sumNotas, cantNotasAsigntura)
                sumaNotasFinal += promedio
                end = 1
        end = 0
        print(f"Las notas del estudiante {estudiantes[i]} en la asignatura {asignaturas[e]} son: {notasEstudianteAsignatura}")
        print(f"Y su promedio (redondeado) es: {promedio}")
        promedioAsignatura.append(promedio)
        promedio = 0.0
        sumNotas = 0.0
    promedioFinal = f.calcularPromedio(sumaNotasFinal, notasDisponibles)
    print(f"Los promedios en las asignaturas del estudiante {estudiantes[i]} son: {promedioAsignatura}")
    print(f"Y su promedio general (redondeado) es: {promedioFinal}")
    notasDisponibles = cantAsignaturas

print("hola")
print("Gracias por usar el Sistema de Cálculo de Promedios!")
