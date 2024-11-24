"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    with open("files/input/data.csv", 'r') as f:
        datos = [linea.split() for linea in f.readlines()]

    # Crear la lista de tuplas
    resultado = []
    valores_columna_2 = sorted(set(int(fila[1]) for fila in datos))  # Valores únicos de la columna 2
    
    for valor in valores_columna_2:
        # Filtrar letras asociadas al valor actual de la columna 2
        letras_asociadas = sorted(set([fila[0] for fila in datos if int(fila[1]) == valor]))
        resultado.append((valor, letras_asociadas))
    
    return resultado

if __name__ == "__main__":
    resultados = pregunta_08()
    if resultados is not None:
        print("El resultado:", resultados)
    
    
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
