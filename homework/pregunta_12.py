"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():

    sumar_letras = {}
    
    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas = linea.strip().split()
            letras = columnas[0]   
            valor = columnas[4].split(',')  
             
# Calcular la suma de los valores en la columna 5
            valor_sum = sum(int(number.split(':')[1]) for number in valor) 

# Actualizar el diccionario sumando los valores
            if letras in sumar_letras:
                sumar_letras[letras] += valor_sum
            else:
                sumar_letras[letras] = valor_sum
   
# Ordenar el diccionario alfabéticamente por claves
    resultados = dict(sorted(sumar_letras.items()))
    return resultados  


if __name__ == "__main__":
    resultados = pregunta_12()
    if resultados is not None:
        print("El resultado:", resultados)








    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
