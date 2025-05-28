suma = 0
numeros = [0,0,0,0,0]

print("Este programa sumará los primeros 5 valores que usted ingrese.")
for i in range(5):
    print("Ingrese el valor numero " + str(i+1))
    numeros[i] = input()
    suma = suma + float(numeros[i])
print("la suma total es:" + str(suma))