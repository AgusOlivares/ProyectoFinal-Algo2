import mapa as m
import argparse
import re


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
                    V = line.split("{")[1].split("}")[0].split(",")
                    V = [element.strip() for element in V]
                elif line.startswith("A"):
                    # Extraer la lista de A

                    elementos = re.findall(r"<(.*?)>", line) # Elementos con el formato <e1, e2, d>

                    for aristas in elementos:
                        valores = tuple(map(str.strip, aristas.split(",")))
                        A.append(tuple(valores))
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



## LA DIRECCION TIENE EL FORMATO DE {NOMBRE, <DIRECCION>}
# Creo el parser
parser = argparse.ArgumentParser()
parser.add_argument('-create_map', type=str, metavar='archivo.txt', help='Carga mapa desde archivo local')
#parte modifcada
parser.add_argument('-load_fix_element', nargs=2, metavar=("nombre", "<direccion>"), help='Carga un elemento fijo')
parser.add_argument('-load_movil_element', nargs=3, metavar=("nombre", "<direccion>", "monto"), help='Funcion para insertar autos o personas al mapa')
parser.add_argument('-consult', type=str, metavar='Ubicacion/Auto/Persona', help='Busco la direccion del objeto de interes')
parser.add_argument("-create_trip", type=None, )
args = parser.parse_args()


if args.create_map:
    # Carga el mapa desde un archivo local
    V, A = leer_archivo(args.create_map)
    mapa = m.Map(V , A)
    new_map = mapa.createMap(V , A) # Mapa con nodos y aristas
    #print(new_map)
    mapa.dijkstraInNodes(new_map) #Calculo Dijkstra para cada MapNode 
    print("--"*10)

    new_map["autos"] = [] ### Creo una lista para llevar el registro de los autos que se van a ingresar

    serializar_archivo(new_map)
    print("Map created succesfully") #esto solo se hacia para verificar funcionalidad


if args.load_fix_element:


    ######## EXPERIMENTAL
    mapa = m.Map() # Con crear solamente esto, esta bien para poder utilizar las funciones? 

    new_map = hacer_lectura("serializado.txt")
    
    ## Tengo que deserializar el archivo, creo que un problema va a ser que necesito un un objeto Map
    ## arriba por ejemplo tenia el objeto mapa

    nombre = args.load_fix_element[0]

    direccion_info = args.load_fix_element[1].split()

    direccion = []
    for elementos in direccion_info:
        esquina, distancia = elementos.strip("<>").split(",")
        direccion.append((esquina.strip(), int(distancia.strip())))

    mapa.insert_fixed(new_map, nombre, direccion) 
    serializar_archivo(new_map)

    print(new_map)

if args.load_movil_element:


    mapa = m.Map() # Con crear solamente esto, esta bien para poder utilizar las funciones? 

    new_map = hacer_lectura("serializado.txt")
    
    ## Tengo que deserializar el archivo, creo que un problema va a ser que necesito un un objeto Map
    ## arriba por ejemplo tenia el objeto mapa

    nombre = args.load_movil_element[0]

    monto = args.load_movil_element[2]

    direccion_info = args.load_movil_element[1].split()

    direccion = []
    for elementos in direccion_info:
        esquina, distancia = elementos.strip("<>").split(",")
        direccion.append((esquina.strip(), int(distancia.strip())))

    mapa.insert_movile(new_map, nombre, direccion, monto) 

    if nombre[0] == "C":
        new_map["autos"].append(nombre) ### Esto lo agregue para tener un registro de los autos que creamos

    serializar_archivo(new_map)

    print(new_map)

if args.consult:
    
    new_map = hacer_lectura("serializado.txt")

    if args.consult in new_map:
        print(new_map[args.consult].direccion)
    else:
        print("El objeto no existe")




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
''' Codigo para probar dijkstra
V, A = leer_archivo("test_dijkstra.txt") #Recordar que es el test de Dijkstra , no el mapa
print(V)
print(A)
mapa = m.Map(V , A)
new_map = mapa.createMap(V , A)
#print(mapa.Dijkstra(new_map, new_map["s"]))
print(mapa.dijkstraInNodes(new_map))
serializar_archivo(new_map)
aux = hacer_lectura("serializado.txt")
'''

#Codigo para probar Dijkstra en cada nodo
'''
V, A = leer_archivo("mapa-ejemplo.txt") 
print(V)
print(A)
mapa = m.Map(V , A)
new_map = mapa.createMap(V , A)
print(mapa.Dijkstra(new_map, new_map["e1"]))
serializar_archivo(new_map)

'''
#A partir del mapa de prueba cargado voy a trabajar para implementar el create_trip (No contiene los nodos fijos y moviles todavia)
aux = hacer_lectura("serializado.txt")
mapa = m.Map()
mapa.ranking_autos(aux , "P1" , "H1")
print("--"*10)

