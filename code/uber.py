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




def tuples_f(parametros):
                               #e1        #d1             #e2       #d2
    patron = r'(\w+)\s+\[\(\s*(\w+), \s*(\d+)\), \s*\(\s*(\w+), \s*(\d+)\)\]' #\w+: letras. \s+: espacios.  \d+: digitos  gracias al "+" se analizan los sgtes, si no es en singular
    match = re.match(patron, parametros)

    if match:
        nombre = match.group(1)
        e1 = int(match.group(2))   ### En este caso le agrego int() ya que los nodos de mi mapa tienen key numerica
        d1 = int(match.group(3))
        e2 = int(match.group(4))   ### En este caso le agrego int() ya que los nodos de mi mapa tienen key numerica
        d2 = int(match.group(5))
        return (nombre, [(e1, d1), (e2, d2)]) 
    else:
        return argparse.ArgumentTypeError('formato invalido, probar este formato "nombre [(e1, d1), (e2, d2)]"')
    

def tuples_m(parametros):                                                       #Monto
                               #e1        #d1             #e2       #d2     #a partir de aca cree yo
    patron = r'(\w+)\s+\[\(\s*(\w+), \s*(\d+)\), \s*\(\s*(\w+), \s*(\d+)\)\]\s+(\d+)' #\w+: letras. \s+: espacios.  \d+: digitos  gracias al "+" se analizan los sgtes, si no es en singular
    match = re.match(patron, parametros)

    if match:
        nombre = match.group(1)
        e1 = int(match.group(2))   ### En este caso le agrego int() ya que los nodos de mi mapa tienen key numerica
        d1 = int(match.group(3))
        e2 = int(match.group(4))   ### En este caso le agrego int() ya que los nodos de mi mapa tienen key numerica
        d2 = int(match.group(5))
        monto = int(match.group(6))
        return (nombre, [(e1, d1), (e2, d2)], monto) 
    else:
        return argparse.ArgumentTypeError('formato invalido, probar este formato "nombre [(e1, d1), (e2, d2)] monto"')


## LA DIRECCION TIENE EL FORMATO DE {NOMBRE, <DIRECCION>}
# Creo el parser
parser = argparse.ArgumentParser()
parser.add_argument('-create_map', type=str, metavar='archivo.txt', help='Carga mapa desde archivo local')
parser.add_argument('-load_fix_element', type=tuples_f , metavar='nombre [(e1, d1), (e2, d2)]', help='Carga un elemento fijo')
parser.add_argument('-load_movil_element', type=tuples_m, metavar='nombre [(e1, d1), (e2, d2)] monto', help='Funcion para insertar autos o personas al mapa')
parser.add_argument('-consult', type=str, metavar='Ubicacion/Auto/Persona', help='Busco la direccion del objeto de interes')
parser.add_argument("-create_trip", type=None, )
args = parser.parse_args()


####### Problema carga el primer elemento valido con exito, al cargar el segundo valido, me reemplaza el primero, y al cargar uno invalido, me borra el elemento valido
####### Creo que ya se lo que pasa, no estoy garantizando la persistencia de los objetos moviles y fijos, por lo que cada vez que ingreso uno, no me guarda los anteriores
####### CREAR FORMA DE PODER MANTENER LOS OBJETOS FIJOS Y MOVILES (EN UN ARCHIVO DISTINTO DEL MAPA? puede que no, pero ya vemos)

if args.create_map:
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

    '''
    V, A = leer_archivo(args.create_map)
    mapa = m.Map(V , A)
    new_map = mapa.createMap(V , A) # Mapa con nodos y aristas
    #print(new_map)
    
    serializar_archivo(new_map)
    print("Map created succesfully") #esto solo se hacia para verificar funcionalidad

if args.load_fix_element:
    
    '''

    ######## ESTOY REPITIENDO LINEAS DE CODIGO A PROPOSITO, REVISAR COMO MEJORARLO

    def hacer_lectura(archivo):
        import pickle   

        with open(archivo , "br") as map:
            mapa = pickle.load(map)
        return mapa
    
    def serializar_archivo(objeto):  # Se serializa el mapa (Diccionario)
        import pickle

        with open("serializado.txt" , "bw") as ser:
            pickle.dump(objeto , ser)

    ########
    '''

    ######## EXPERIMENTAL
    mapa = m.Map() # Con crear solamente esto, esta bien para poder utilizar las funciones? 

    new_map = hacer_lectura("serializado.txt")
    
    ## Tengo que deserializar el archivo, creo que un problema va a ser que necesito un un objeto Map
    ## arriba por ejemplo tenia el objeto mapa

    nombre, [(e1, d1), (e2, d2)] = args.load_fix_element
    print(nombre, [(e1, d1), (e2, d2)])

    mapa.insert_fixed(new_map, nombre, [(e1, d1), (e2, d2)]) 
    serializar_archivo(new_map)

    print(new_map)

if args.load_movil_element:

    '''

    ######## ESTOY REPITIENDO LINEAS DE CODIGO A PROPOSITO, REVISAR COMO MEJORARLO

    def hacer_lectura(archivo):
        import pickle   

        with open(archivo , "br") as map:
            mapa = pickle.load(map)
        return mapa
    
    def serializar_archivo(objeto):  # Se serializa el mapa (Diccionario)
        import pickle

        with open("serializado.txt" , "bw") as ser:
            pickle.dump(objeto , ser)

    ########

    '''
    ######## EXPERIMENTAL
    mapa = m.Map() # Con crear solamente esto, esta bien para poder utilizar las funciones? 

    new_map = hacer_lectura("serializado.txt")
    
    ## Tengo que deserializar el archivo, creo que un problema va a ser que necesito un un objeto Map
    ## arriba por ejemplo tenia el objeto mapa

    nombre, [(e1, d1), (e2, d2)], monto = args.load_movil_element
    print(nombre, [(e1, d1), (e2, d2)], monto)

    mapa.insert_movile(new_map, nombre, [(e1, d1), (e2, d2)], monto) 
    serializar_archivo(new_map)

    print(new_map)

if args.consult:
    '''
    def hacer_lectura(archivo):
        import pickle   

        with open(archivo , "br") as map:
            mapa = pickle.load(map)
        return mapa
    '''
    
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


#def load_fix_element(nombre, direccion, map=hacer_lectura("serializado.txt")): ## Planteamiento

V, A = leer_archivo("test_dijkstra.txt") #Recordar que es el test de Dijkstra , no el mapa
print(V)
print(A)
mapa = m.Map(V , A)
new_map = mapa.createMap(V , A)
print(mapa.Dijkstra(new_map, new_map["s"]))
serializar_archivo(new_map)
aux = hacer_lectura("serializado.txt")
'''

"""
mapa.insert_fixed(new_map, "H1", [(1, 15), (2, 15)]) #Calle en doble sentido
mapa.insert_fixed(new_map, "H2", [(2, 30), (3, 40)]) #Calle en un sentido
print(mapa.insert_fixed(new_map, "H3", [(2, 30), (3, 60)])) #Ingreso una direccion no válida
mapa.insert_movile(new_map, "P1", [(1, 15), (2, 15)], 150)
print(mapa.insert_movile(new_map, "P1", [(4, 10), (2, 10)], 600))
print(mapa.doble_sentido(new_map , "P1"))

print("hola")
"""


