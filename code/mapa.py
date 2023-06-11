import copy
class MapNode:
    def __init__(self , key = None , aristas = None , distancia = None):
        self.key = key
        self.list = []    #Esta lista sirve para poner sus nodos adyacentes
        self.peso_minimo = None
        self.padre = None
        self.dijkstra = {}


class Node(MapNode): # clase creada para ser insertada a la lista de adyacencia
    def __init__(self , key = None, distancia = None):
        self.key = key
        self.distancia = distancia

        

class Ubicacion: # Nodo que representa una ubicacion fija
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion # forma direccion lista con 2 tuplas (<ex, d>, <ey, d>)
        self.list = []

class Movil(Ubicacion): # Nodo que representa una Persona o un Auto
    def __init__(self, nombre, direccion, monto):
        super().__init__(nombre, direccion)
        self.monto = monto
        
class Map:
    def __init__(self , vertices = None , aristas = None):
        self.vertices = vertices
        self.aristas = aristas
        
    def createMap(self , vertices, aristas):
        dict = {}
        #Agrego las esquinas
        #Oficial
        #for key in range(len(vertices)):
        #    pos = vertices[key]
        #    dict[pos] = MapNode(pos)

        #Modificacion
        for key in vertices:
            dict[key] = MapNode(key)

        dict = self.connections(dict , aristas)
        #dict["vertices"] = vertices
        #dict["aristas"] = aristas
        return dict
    
    def insert(self, mapa, nodo, esquina_x , esquina_y): # Inserta nodo individual

        if esquina_x != None:
            v1_node = Node(esquina_x, nodo.direccion[0][1])
            mapa[nodo.nombre].list.append(v1_node)

        if esquina_y != None:
            v2_node = Node(esquina_y, nodo.direccion[1][1])
            mapa[nodo.nombre].list.append(v2_node)
    
    # def delete(self, mapa, nodo) #### IMPLEMENTAR FUNCION DELETE PARA MOVILIZAR LOS NODOS (CREATE-TRIP)


    def connections(self , dict , aristas):

        for (v1 , v2 , c) in aristas: # c es el peso de la arista
            if v1 != v2:
                # Oficial
                #node = Node(v2, c)

                #Modificacion
                node = Node(v2, int(c))

                dict[v1].list.append(node)
            else: #Preguntar si hace falta un nodo conectado con sigo mismo
                # Oficial
                #node = Node(v1, c)

                # Modificacion
                node = Node(v1, int(c))

                dict[v1].list.append(node)
        return dict
    
    def insert_fixed(self, mapa, nombre, direccion):

        if nombre in mapa:
            return print("El nombre de la ubicacion ya existe, no sera agregado")

        suma_aux = direccion[0][1] + direccion[1][1]

        node = Ubicacion(nombre, direccion)
        tupla_x = direccion[0] 
        tupla_y = direccion[1]

        v1 = tupla_x[0] 
        v2 = tupla_y[0]

        flag1 = False
        flag2 = False

        #La calle va de v2 a v1
        for objeto in mapa[v2].list:
            if objeto.key == v1:
                flag1 = True
                if suma_aux != objeto.distancia:
                    return print("La direccion ingresada no es válida")


        #La calle va de v1 a v2
        for objeto in mapa[v1].list:
            if objeto.key == v2:
                flag2 = True
                if suma_aux != objeto.distancia:
                    return print("La direccion ingresada no es válida")


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
      

    def insert_movile(self, mapa, nombre, direccion, monto):

        if nombre in mapa:
            return print("El nombre de la ubicacion ya existe") #### VER SI CAMBIAMOS EL MENSAJE DEVUELTO

        suma_aux = direccion[0][1] + direccion[1][1]

        node = Movil(nombre, direccion, monto)
        tupla_x = direccion[0]  
        tupla_y = direccion[1]

        v1 = tupla_x[0] 
        v2 = tupla_y[0]

        flag1 = False
        flag2 = False

        #La calle va de v2 a v1
        for objeto in mapa[v2].list:
            if objeto.key == v1:
                flag1 = True
                if suma_aux != objeto.distancia:
                    return print("La direccion ingresada no es válida")


        #La calle va de v1 a v2
        for objeto in mapa[v1].list:
            if objeto.key == v2:
                flag2 = True
                if suma_aux != objeto.distancia:
                    return print("La direccion ingresada no es válida")


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

    def doble_sentido(self , mapa , nombre_persona):
        persona = mapa[nombre_persona]
        esquina1 = persona.direccion[0][0]
        esquina2 = persona.direccion[1][0]

        #Listas de adyacencia de las esquinas
        adyacentes_1 = mapa[esquina1].list 
        adyacentes_2 = mapa[esquina2].list

        flag1 = False
        flag2 = False

        for nodo in adyacentes_1:
            if nodo.key == esquina2:
                flag1 = True #Dentro de la esquina 1 se encuentra la esquina 2

        for nodo in adyacentes_2:
            if nodo.key == esquina1:
                flag2 = True #Dentro de la esquina 2 se encuentra la esquina 1

        if flag1 == True and flag2 == True: #Si la calle es doble sentido entonces retorna true
            return True


    def initRelax(self, map, nodo_inicial): # Funcion para relajar cada MapNode (esquinas)

        for esquina in map:
            if esquina != nodo_inicial.key:
                map[esquina].peso_minimo = float('inf')
                map[esquina].padre = None
            else:
                map[nodo_inicial.key].peso_minimo = 0
        return map
    
    def Relax(self, esquina1, esquina2 , distancia_e2): # Funcion que actualiza el peso_minimo de cada nodo, excepto el de partida
        #Esquina 1 y esquina 2 son del tipo MapNode y distancia_e2 es la distancia entre la e1 a la e2

        if esquina2.peso_minimo > (esquina1.peso_minimo + distancia_e2):
            esquina2.peso_minimo = esquina1.peso_minimo + distancia_e2
            esquina2.padre = esquina1.key

    def Dijkstra(self, mapa, esquina_inicial):
        new_map = copy.deepcopy(mapa)  #Se crea una copia profunda de mapa, lo que garantiza que todos los objetos y estructuras de datos internos se copien correctamente sin compartir referencias
        self.initRelax(new_map, esquina_inicial)
        visited = set()
        lista_pesos = []
        for key in new_map:
            lista_pesos.append(new_map[key])

        lista_pesos = sorted(lista_pesos, key=lambda x: x.peso_minimo)

        while len(lista_pesos) > 0:
            current_node = lista_pesos.pop(0)
            visited.add(current_node)

            for adyacente in current_node.list:
                aux = new_map[adyacente.key]
                if aux not in visited:
                    self.Relax(current_node, aux, adyacente.distancia)

            lista_pesos = sorted(lista_pesos, key=lambda x: x.peso_minimo)

        return new_map
        

    def dijkstraInNodes(self, mapa):
        new_mapa = {}  # Crear un nuevo diccionario para almacenar los resultados

        for key in mapa:
            current_map = mapa.copy()  # Crear una copia independiente del mapa en cada iteración
            current_map[key].dijkstra = self.Dijkstra(current_map, current_map[key])
            new_mapa[key] = current_map  # Guardar el resultado en el nuevo diccionario

        return new_mapa