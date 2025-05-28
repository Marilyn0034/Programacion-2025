def añadirArticulo():
    articuloNuevo = ""
    f = open("Articulos.txt") #Abriendo y leyendo el archivo.
    lista = f.readlines()
    print(lista)

    articuloNuevo = str(input("Ingrese el nombre del artículo nuevo."))
    articuloNuevo = "{0},{1}".format(articuloNuevo,str(float(input("Ingrese la cantidad (en números) del nuevo artículo"))))
    lista = lista.append[articuloNuevo]

    for i in range(len(lista)):
        linea = lista[i]
        linea = linea[:-1]
        linea = linea.strip()
        print(linea)
    f.close()

def editarArticulo():
    añadirArticulo()

def elimnarArticulo():
    añadirArticulo()

def consultarArticulos():
    with open("Articulos.txt") as f: #Abriendo y leyendo el archivo.
        linea = f.readline()
        while linea != '':
            print(linea.rstrip())
            linea = f.readline()