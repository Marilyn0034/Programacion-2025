import Funciones as f

end = 1
opcion = float

print("Bienvenido al administrador de inventario! Por favor ingrese la acción que desea realizar")
while end == 1:
    opcion = float(input("(1) Añadir un nuevo artículo.\n(2) Editar un artículo existente.\n(3) Eliminar un archivo.\n(4) Consultar la lista de artículos.\n(5) Salir del administrador de inventario.\n"))
    while opcion != 1.0 and opcion != 2.0 and opcion != 3.0 and opcion != 4.0 and opcion != 5.0:
        opcion = float(input("Usted ingresó una opción no válida. Ingrese la opcion deseada nuevamente: "))
    if opcion == 1.0:
        f.añadirArticulo()
    elif opcion == 2.0:
        f
    elif opcion == 3.0:
        f
    elif opcion == 4.0:
        f.consultarArticulos()
    else:
        end = 0
