import mapa as m
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-create_map', type=str, help='Carga mapa desde archivo local')
args = parser.parse_args()


if args.create_map:

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

    def serializar_archivo(objeto):  # Se serializa el mapa (Diccionario)
        import pickle

        with open("serializado.txt" , "bw") as ser:
            pickle.dump(objeto , ser)

    def hacer_lectura(archivo):
        import pickle   

        with open(archivo , "br") as map:
            mapa = pickle.load(map)
        return mapa


    V, A = leer_archivo(args.load_map)
    mapa = m.Map(V , A)
    new_map = mapa.createMap(V , A) # Mapa con nodos y aristas
    print(new_map)
    
    serializar_archivo(new_map)
    print(V)





'''

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

def serializar_archivo(objeto):  # Se serializa el mapa (Diccionario)
    import pickle

    with open("serializado.txt" , "bw") as ser:
        pickle.dump(objeto , ser)

def hacer_lectura(archivo):
    import pickle   

    with open(archivo , "br") as map:
        mapa = pickle.load(map)
    return mapa


def load_map(local_path): ## Planteamiento
     V, A = leer_archivo(local_path)
     mapa = m.Map(V , A)
     new_map = mapa.createMap(V , A) # Mapa con nodos y aristas
     serializar_archivo(new_map)
     print(V)

'''
#def load_fix_element(nombre, direccion, map=hacer_lectura("serializado.txt")): ## Planteamiento

"""
V, A = leer_archivo("mapa.txt")
print(V)
print(A)
mapa = m.Map(V , A)
new_map = mapa.createMap(V , A)
serializar_archivo(new_map)
aux = hacer_lectura("serializado.txt")

mapa.insert_fixed(new_map, "H1", [(1, 15), (2, 15)]) #Calle en doble sentido
mapa.insert_fixed(new_map, "H2", [(2, 30), (3, 40)]) #Calle en un sentido
print(mapa.insert_fixed(new_map, "H3", [(2, 30), (3, 60)])) #Ingreso una direccion no válida
mapa.insert_movile(new_map, "P1", [(1, 15), (2, 15)], 150)
print(mapa.insert_movile(new_map, "P1", [(4, 10), (2, 10)], 600))
print(mapa.doble_sentido(new_map , "P1"))

print("hola")

"""

