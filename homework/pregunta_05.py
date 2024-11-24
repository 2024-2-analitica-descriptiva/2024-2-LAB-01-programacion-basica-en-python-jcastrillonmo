"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    Dicc = {}
    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas = linea.strip().split()
            if columnas:  # Asegurarse de que la línea no esté vacía
                letras = columnas[0]
                valor = int(columnas[1])

                if letras not in Dicc:
                    Dicc[letras] = []  # Inicializar la lista si la letra no existe
                Dicc[letras].append(valor)  # Agregar el valor a la lista correspondiente

    # Crear la lista de resultados con el máximo y mínimo
    resultado = []
    for letras, valores in Dicc.items():
        valor_max = max(valores)
        valor_min = min(valores)
        resultado.append((letras, valor_max, valor_min))

    # Ordenar el resultado alfabéticamente por la letra
    resultado.sort(key=lambda x: x[0])
    return resultado

if __name__ == "__main__":
    resultado = pregunta_05()
    if resultado is not None:
        print("El resultado:", resultado)

 

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
