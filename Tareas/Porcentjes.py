#Declaración de variables.
run = True
sumaDatos = 0
porcentajes = []
valores = []
i = 1

#Bucle While para cantidad de datos
while run == True:
    valor = int(input(f"Ingrese el dato número {i}:"))
    i = i + 1
    valores.append(valor)
    sumaDatos = sumaDatos + valor
    if valor == 0:
        run = False

#Calculos
for e in valores:
    porcentaje = e / sumaDatos * 100
    porcentajes.append(str(porcentaje) + "%")

#Salida de datos
print(f"Los porcentajes son: {str(porcentajes).rstrip(", '0.0%']")+"%']"}")