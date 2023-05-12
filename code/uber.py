import mapa as m

def leer_archivo(archivo):
    V = []
    A = []
    """
    line.split("=") separa la lista en 2 y luego elejimos el segundo elemento [1]
    luego la funcion eval() toma esa linea como una linea valida de python y 
    le asigna esa lista a la variable lista_e y lista_a respectivamente
    """    
    with open(archivo, "r") as file:
        for line in file:
            if line.startswith("E"):
                # Extraer la lista de E
                V = eval(line.split("=")[1])
            elif line.startswith("A"):
                # Extraer la lista de A
                A = eval(line.split("=")[1])

    return V, A

def serializar_archivo(objeto):
    import pickle

    with open("serializado.txt" , "bw") as ser:
        pickle.dump(objeto , ser)

def hacer_lectura(archivo):
    import pickle   

    with open(archivo , "br") as map:
        mapa = pickle.load(map)
    return mapa

V, A = leer_archivo("mapa.txt")
print(V)
print(A)
mapa = m.Graph(V , A)
new_map = mapa.createGraph(V , A)
serializar_archivo(new_map)
aux = hacer_lectura("serializado.txt")


