numeros = []
maximo = float
minimo = float
firstInput = 0
opcion = int
print("Este programa identificará el valor más alto y más bajo de una secuencia de 10 numeros entregados por usted.")
for i in range(10):
    numeros.append(float(input(f"Ingrese el valor numero {i+1}: ")))
    if firstInput == 0:
        maximo = numeros[i]
        minimo = numeros[i]
        firstInput = 1
    if maximo < numeros[i]:
        maximo = numeros[i]
    elif minimo > numeros[i]:
        minimo = numeros[i]

print(f"El valor más bajo es {minimo} y el más alto es {maximo}")