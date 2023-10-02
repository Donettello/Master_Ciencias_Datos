"""
En este fichero vamos a leer los archivos de los datos y ha devolver la cadena de valores 0-1.
"""

def data_control():
    """
        Esta función se encarga de la lectura del fichero de los datos de control.
    """
    with open("TEO_INF/Prácticas/data/TrozoC.txt") as f:
        LP, VD = [], []
        # Nos deshacemos de las tres primeras lineas
        cont = 0
        for _ in f:
            if cont < 2:
                cont += 1
            else:
                break
        
        # Obtenemos los datos en bruto
        for line in f:
            d = line.split("\t")
            LP.append(float(d[0].replace(',', '.')))
            VD.append(float(d[1].replace(',', '.'))) 
    return LP, VD  

def data_gaba():
    """
        Esta función se encarga de la lectura del fichero de los datos con Gaba.
    """
    with open("TEO_INF/Prácticas/data/TrozoG.txt") as f:
        LP, VD, Gaba = [], [], []
        # Nos deshacemos de las tres primeras lineas
        cont = 0
        for _ in f:
            if cont < 2:
                cont += 1
            else:
                break
        
        # Obtenemos los datos en bruto
        for line in f:
            d = line.split("\t")
            LP.append(float(d[0].replace(',', '.')))
            VD.append(float(d[1].replace(',', '.')))
            Gaba.append(float(d[2].replace(',', '.'))) 
    return LP, VD, Gaba

def data_reco():
    """
        Esta función se encarga de la lectura del fichero de los datos de recuperación.
    """
    with open("TEO_INF/Prácticas/data/TrozoR.txt") as f:
        LP, VD = [], []
        # Nos deshacemos de las tres primeras lineas
        cont = 0
        for _ in f:
            if cont < 2:
                cont += 1
            else:
                break
        
        # Obtenemos los datos en bruto
        for line in f:
            d = line.split("\t")
            LP.append(float(d[0].replace(',', '.')))
            VD.append(float(d[1].replace(',', '.')))
    return LP, VD

def spiker(cadena, ventana=1, umbral=0.5):
    """
    Dada una cadena de valores, se retorna otra cadena de len(cadena)/ventana
    de valores binarios 1/0.
    """
    pass
LP_c, VD_c = data_control()
print(LP_c[0:3])