class GraphNode:
    def __init__(self , key = None , aristas = None , distancia = None):
        self.key = key
        self.list = []    #Esta lista sirve para poner sus nodos adyacentes
        self.connections = aristas
        self.distancia = distancia

class Node: # clase creada para ser insertada 
    def __init__(self , key = None, distancia = None):
        self.key = key
        self.distancia = distancia

class Ubicacion: # Nodo que representa una ubicacion fija
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion # forma direccion lista con 2 tuplas (<ex, d>, <ey, d>)
        self.list = []
        

class Movil(Ubicacion):
    def __init__(self, nombre, direccion, monto):
        super().__init__(nombre, direccion)
        self.monto = monto
        
class Graph:
    def __init__(self , vertices = None , aristas = None):
        self.vertices = vertices
        self.aristas = aristas
        
    def createGraph(self , vertices, aristas):
        dict = {}
        #Agrego las esquinas
        for key in range(len(vertices)):
            pos = vertices[key]
            dict[pos] = GraphNode(pos)

        dict = self.connections(dict , aristas)
        return dict
    
    def insert(self, mapa, nodo, esquina_x , esquina_y): # Inserta nodo individual

        if esquina_x != None:
            v1_node = Node(esquina_x, nodo.direccion[0][1])
            mapa[nodo.nombre].list.append(v1_node)

        if esquina_y != None:
            v2_node = Node(esquina_y, nodo.direccion[1][1])
            mapa[nodo.nombre].list.append(v2_node)
        


    def connections(self , dict , aristas):

        for (v1 , v2 , c) in aristas:
            if v1 != v2:
                node = Node(v2, c)
                dict[v1].list.append(node)
            else: #Preguntar si hace falta un nodo conectado con sigo mismo
                node = Node(v1, c)
                dict[v1].list.append(node)
        return dict
    
    def insert_fixed(self, mapa, nombre, direccion):

        suma_aux = direccion[0][1] + direccion[1][1]

        node = Ubicacion(nombre, direccion)
        tupla_x = direccion[0] # tupla 
        tupla_y = direccion[1]

        v1 = tupla_x[0] # 
        v2 = tupla_y[0]

        flag1 = False
        flag2 = False

        #La calle va de v2 a v1
        for objeto in mapa[v2].list:
            if objeto.key == v1:
                flag1 = True
                if suma_aux != objeto.distancia:
                    return "La direccion ingresada no es válida"


        #La calle va de v1 a v2
        for objeto in mapa[v1].list:
            if objeto.key == v2:
                flag2 = True
                if suma_aux != objeto.distancia:
                    return "La direccion ingresada no es válida"


        if flag1 == True and flag2 == True: ## la calle es doble mano
            
            mapa[node.nombre] = node # agregamos una nueva ubicacion en el mapa

            self.insert(mapa, node , v1 , v2) # Insertamos en la ubicacion las esquinas adyacentes y las distancias

            # Insertamos en las esquinas la nueva adyacencia
            aux = Node(node.nombre, tupla_x[1]) 
            mapa[v1].list.append(aux) 
            aux = Node(node.nombre, tupla_y[1]) 
            mapa[v2].list.append(aux)
            
        elif flag1 == True:     #La calle va de v2 a v1
            mapa[node.nombre] = node 
            self.insert(mapa , node , v1 , None)

            aux = Node(node.nombre , tupla_y[1])
            mapa[v2].list.append(aux)
        else:                   #La calle va de v1 a v2
            mapa[node.nombre] = node 
            self.insert(mapa , node , None , v2)

            aux = Node(node.nombre , tupla_x[1])
            mapa[v1].list.append(aux)

        #Al crear un insert movil vamos a tener algo similar solo que le agrego el campo monto




