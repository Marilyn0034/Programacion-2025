def calcularPromedio(notas, cantNotas):
    promedio = int((notas/ cantNotas) * 10 + 0.5) / 10
    return(promedio)

def escribirArchivo(estudiante, promedio, archivo):
    archivo.write(f"{estudiante}, {promedio}\n")
