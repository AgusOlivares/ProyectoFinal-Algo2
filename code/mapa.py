class GraphNode:
    def __init__(self , key = None , aristas = None , distancia = None):
        self.key = key
        self.list = []    #Esta lista sirve para poner sus nodos adyacentes
        self.connections = aristas
        self.distancia = distancia

class Node:
    def __init__(self , key = None, distancia = None):
        self.key = key
        self.distancia = distancia

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

    def connections(self , dict , aristas):

        for (v1 , v2 , c) in aristas:
            if v1 != v2:
                node = Node(v2, c)
                dict[v1].list.append(node)
            else: #Preguntar si hace falta un nodo conectado con sigo mismo
                node = Node(v1, c)
                dict[v1].list.append(node)
        return dict
