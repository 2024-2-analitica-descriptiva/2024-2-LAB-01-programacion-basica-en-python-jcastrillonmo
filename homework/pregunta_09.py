"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    contar_claves = {}
    
    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas = linea.strip().split()  # Dividir la línea en columnas separadas por espacio
            pares = columnas[4].split(',')

            # Procesar los pares clave:valor de la columna 
            for par in pares:
                clave, valor = par.split(':')
                valor = int(valor)
                
                if clave in contar_claves:
                    contar_claves[clave]+=1
                else:
                    contar_claves[clave]=1
   
    # Convertir el diccionario en una lista de tuplas
    resultados = dict(sorted(contar_claves.items()))
    
    return resultados

if __name__ == "__main__":
    resultados = pregunta_09()
    if resultados is not None:
        print("El resultado:", resultados)


"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
