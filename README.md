# ProyectoFinal-Algo2
Para crear el mapa: python uber.py -create_map mapa.txt
Para crear una ubicación fija es: python uber.py -load_fix_element H1 "<e8,20> <e10,30>"
Para crear una ubicación movil es: python uber.py -load_movil_element P1 "<e8,10> <e10,40>" 2000

Para crear un viaje: python uber.py -create_trip P2 H1
                                  python uber.py -create_trip P4 "<e3,10> <e2,40>"

### Importante 
    ## Dejar al menos un solo espacio entre <> y <> al ingresar una dirección
    ## Realizar los comados requeridos luego de haber creado el mapa (da error en caso contrario)
    ## Al momento de escojer un auto indicar con un valor numero según la opcion, ejemplo: 
                    Opcion 1: Auto C3 monto $X  
                    Opcion 2: Auto C4 monto $X
                    Opcion 3: Auto C1 monto $X

        Si queremos elegir el auto C4, solamente apretar 2 (y enter)

    ## Al momento de aceptar o denegar el viaje escribir Y/N en mayúsculas