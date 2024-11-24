"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
# Crear la lista para almacenar resultados
    resultado = []

    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas=linea.strip().split()
            letras = columnas[0]
            columna_4 = columnas[3]  
            columna_5 = columnas[4]  
            
# Contar la cantidad de elementos separados por coma en las columnas 4 y 5
            count_col4 = len(columna_4.split(","))
            count_col5 = len(columna_5.split(",")) 

# Crear una tupla con la letra y las cantidades de las columnas 4 y 5
            resultado.append((letras, count_col4, count_col5))

    return resultado
             
if __name__ == "__main__":
    resultado = pregunta_10()
    if resultado is not None:
        print("El resultado", resultado)



    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
