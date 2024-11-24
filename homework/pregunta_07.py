"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    with open("files/input/data.csv", 'r') as f:
        datos = [linea.split() for linea in f.readlines()]

    # Crear la lista de tuplas
    resultado = []
    valores_columna_2 = sorted(set(int(fila[1]) for fila in datos))  # Valores únicos de la columna 2
    
    for valor in valores_columna_2:
        # Filtrar letras asociadas al valor actual de la columna 2
        letras_asociadas = [fila[0] for fila in datos if int(fila[1]) == valor]
        resultado.append((valor, letras_asociadas))
    
    return resultado

if __name__ == "__main__":
    resultados = pregunta_07()
    if resultados is not None:
        print("El resultado:", resultados)


    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
