"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    suma = 0
    with open("files/input/data.csv" , 'r') as f:
        for linea in f:
            columnas=linea.strip().split()
            suma += int(columnas[1])
    return suma

if __name__ == "__main__":
    resultado = pregunta_01()
    if resultado is not None:
        print("La suma es:", resultado)

"""
Retorne la suma de la segunda columna.

    Rta/
    214

    """
