"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    sumar_letras = {}
    
    with open("files/input/data.csv", 'r') as f:
        for linea in f:
            columnas = linea.strip().split()  
            valor = int(columnas[1])  
            letras = columnas[3].split(",")  
            
    # Actualizar las sumas en el diccionario
            for letter in letras:
                if letter not in sumar_letras:
                    sumar_letras[letter] = 0
                sumar_letras[letter] += valor
    
    # Ordenar el diccionario por las claves
   
    resultados = dict(sorted(sumar_letras.items()))
    
    return resultados

if __name__ == "__main__":
    resultados = pregunta_11()
    if resultados is not None:
        print("El resultado:", resultados)


    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
