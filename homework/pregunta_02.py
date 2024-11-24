"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    Dicc = {}
    with open("files/input/data.csv" , 'r') as f:
        for linea in f:
            columnas=linea.strip().split()
            if columnas:
                letras = columnas[0]
                if letras in Dicc:
                    Dicc[letras]+=1
                else:
                    Dicc[letras]=1

    resultado = sorted(Dicc.items())
    return resultado
             
if __name__ == "__main__":
    resultado = pregunta_02()
    if resultado is not None:
        print("El resultado es:", resultado)
    
"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
