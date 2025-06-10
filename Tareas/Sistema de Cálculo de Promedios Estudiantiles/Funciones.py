def calcularPromedio(notas, cantNotas):
    promedio = int((notas/ cantNotas) * 10 + 0.5) / 10
    return(promedio)

def escribir(estudiante, promedio):
    archivo = open("Notas Curso.txt", "w")
    archivo.write(f"{estudiante}, {promedio}")
