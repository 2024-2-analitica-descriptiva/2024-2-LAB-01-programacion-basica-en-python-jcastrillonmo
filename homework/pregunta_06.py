"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_06():
    valores = {}
    
    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas = linea.strip().split()  # Dividir la línea en columnas separadas por espacio
            
            # Procesar los pares clave:valor de la columna 5
            pares = columnas[4].split(',')
            for par in pares:
                clave, valor = par.split(':')
                valor = int(valor)
                
                if clave not in valores:
                    valores[clave] = {'min': valor, 'max': valor}
                else:
                    valores[clave]['min'] = min(valores[clave]['min'], valor)
                    valores[clave]['max'] = max(valores[clave]['max'], valor)
   
    # Convertir el diccionario en una lista de tuplas
    resultados = sorted([(clave, data['min'], data['max']) for clave, data in valores.items()])
    return resultados

if __name__ == "__main__":
    resultados = pregunta_06()
    if resultados is not None:
        print("El resultado:", resultados)

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
