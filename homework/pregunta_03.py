"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    Dicc = {}
    with open("files/input/data.csv" , 'r') as f:
        for linea in f:
            columnas=linea.strip().split()
            if columnas:
                letras = columnas[0]
                Valor = int(columnas[1])
                if letras in Dicc:
                    Dicc[letras]+=Valor
                else:
                    Dicc[letras]=Valor

    resultado = sorted(Dicc.items())
    return resultado
             
if __name__ == "__main__":
    resultado = pregunta_03()
    if resultado is not None:
        print("El resultado", resultado)

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
