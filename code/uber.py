import mapa as m
import argparse
import re
import os


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
parser.add_argument("-create_trip", nargs=2, metavar='Persona Lugar/<Direccion>', help='Creo un viaje para la persona con los autos que puede pagar')
args = parser.parse_args()


if args.create_map:
    # Carga el mapa desde un archivo local
    V, A = leer_archivo(args.create_map)
    mapa = m.Map(V , A)
    new_map = mapa.createMap(V , A) # Mapa con nodos y aristas
    
    mapa.dijkstraInNodes(new_map) #Calculo Dijkstra para cada MapNode 
    print("--"*10)

    new_map["autos"] = [] # Creo una lista para llevar el registro de los autos que se van a ingresar

    serializar_archivo(new_map)
    print("Map created succesfully")


if args.load_fix_element:

    
    mapa = m.Map() # Creo esto para poder utilizar las funciones

    new_map = hacer_lectura("serializado.txt")

    nombre = args.load_fix_element[0]

    direccion_info = args.load_fix_element[1].split()

    direccion = []
    for elementos in direccion_info:
        esquina, distancia = elementos.strip("<>").split(",")
        direccion.append((esquina.strip(), int(distancia.strip())))

    mapa.insert_fixed(new_map, nombre, direccion) 
    serializar_archivo(new_map)

    #print(new_map)
    print('fix object inserted succesfully')


if args.load_movil_element:


    mapa = m.Map() # Creo esto para poder utilizar las funciones

    new_map = hacer_lectura("serializado.txt")

    nombre = args.load_movil_element[0]

    monto = args.load_movil_element[2]

    direccion_info = args.load_movil_element[1].split()

    direccion = []
    for elementos in direccion_info:
        esquina, distancia = elementos.strip("<>").split(",")
        direccion.append((esquina.strip(), int(distancia.strip())))

    mapa.insert_movile(new_map, nombre, direccion, monto) 

    if nombre[0] == "C" and nombre not in new_map["autos"]:
        new_map["autos"].append(nombre) 

    serializar_archivo(new_map)

    #print(new_map)
    print('movile object inserted succesfully')

if args.consult:
    
    new_map = hacer_lectura("serializado.txt")

    if args.consult in new_map:
        print(new_map[args.consult].direccion)
    else:
        print("El elemento no existe")
        parser.error("El elemento no existe")

if args.create_trip:

    new_map = hacer_lectura("serializado.txt")

    persona = args.create_trip[0]

    if persona not in new_map:
        parser.error("La persona no existe")
        
    mapa = m.Map() # Creo esto para poder utilizar las funciones

    listado_de_ubicaciones = ["H","A","T","S","E","K","I"] # Posibles valores de ubicaciones, no necesariamente existentes

    destino = args.create_trip[1] #Ubicacion o direccion
    
    ubicacion_flag = False

    # En las lineas de abajo determino si el tipo de destino ingresado es UbicacionFija/<Direccion>, condicion de bandera para no ejecutar ambos metodos

    ## Aca determino el destino de tipo ubicacion

    for ubicacion in listado_de_ubicaciones:
        if destino.startswith(ubicacion):
            destino_final = args.create_trip[1]

            if destino_final not in new_map:
                parser.error("El destino indicado no existe")
            ubicacion_flag = True
            break
    else:
        if ubicacion_flag == False:
            if destino[0] == "P" or destino[0] == "C":
                parser.error("El destino no es valido")
            ## Aca determino el destino de tipo <Direccion> y lo devuelvo en forma [(e1, d),(e2, d)]
            destino_final = []
            
            for elementos in destino.split():
                esquina, distancia = elementos.strip("<>").split(",")
                destino_final.append((esquina.strip(), int(distancia.strip())))
            
        else:
            parser.error("El destino indicado no existe")
            
    
    if type(destino_final) != list:
        destino_final_direccion = new_map[destino_final].direccion
    else:
        mapa.insert_fixed(new_map , "Destino" , destino_final)


    ## Devuelvo el ranking de los autos que puede pagar la persona
    
    ranking_autos = mapa.ranking_autos(new_map, persona)
    i=1
    for (auto,monto) in ranking_autos:
        print(f"Opcion {i}: El auto {auto} tiene una tarifa de: {monto}")
        i +=1 

    auto_elegido = int(input("Indique con un numero el auto elegido: "))-1

    Opcion_cliente = input("Acepta el viaje? Y/N: ")

    while Opcion_cliente != "Y" and Opcion_cliente != "N":

        if Opcion_cliente != "Y" and Opcion_cliente != "N":

            print("La opcion seleccionada no es correcta")

        Opcion_cliente = input("Acepta el viaje? Y/N")

    if Opcion_cliente == "Y":
        
        aux_auto = ranking_autos[auto_elegido][0] #key auto
        print(f"El auto elegido es {aux_auto}")
        monto_auto = new_map[aux_auto].monto
        monto_nuevo_persona = int(new_map[persona].monto)-ranking_autos[auto_elegido][1]

        if "Destino" in new_map: # existe nodo destino, por lo que destino_final es <direccion>
            print(f"El recorrido sobre el mapa es: {mapa.short_path(new_map , persona , 'Destino')}")
            mapa.delete(new_map,persona)
            mapa.delete(new_map,aux_auto)
            mapa.insert_movile(new_map, persona, destino_final, monto_nuevo_persona)
            mapa.insert_movile(new_map, aux_auto, destino_final, monto_auto)
            new_map['autos'].append(aux_auto)
            mapa.delete(new_map, "Destino")
        else: # destino_final va a ser una key
            print(f"El recorrido sobre el mapa es: {mapa.short_path(new_map , persona , destino_final)}")
            mapa.delete(new_map,persona)
            mapa.delete(new_map,aux_auto)
            mapa.insert_movile(new_map, persona, destino_final_direccion, monto_nuevo_persona)
            mapa.insert_movile(new_map, aux_auto, destino_final_direccion, monto_auto)
            new_map['autos'].append(aux_auto)


        serializar_archivo(new_map)

    elif Opcion_cliente == "N":
        print("El viaje ha sido cancelado")
    else:
        parser.error("La opcion seleccionada no se encuentra, por favor reiniciar el viaje")


