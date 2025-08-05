gastos = []
run = True
gastos_grandes_total = 0.0
limite = 20
i = 1

print("Hola! este programa se encargará de filtrar sus gastos grandes (mayores a 20 dolares) y darle una suma final de todos estos gastos.")
print("Cuando ya no quiera ingresar más gastos, ingrese 0.")

while run == True:
    ingreso = float(input(f"Ingrese el gasto (en dólares) numero {i}:"))
    if ingreso == 0:
        print("Saliendo del ingreso de gastos...")
        run = False
    elif ingreso < 0:
        print("No puede ingresar un gasto negativo.")
    else:
        gastos.append(ingreso)
        i = i + 1

for e in range(i-1):
    if gastos[e] > limite:
        gastos_grandes_total = gastos_grandes_total + gastos[e]

print(f"Sus gastos grandes en total suman: {gastos_grandes_total}")