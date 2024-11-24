"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    Dicc = {}
    with open("files/input/data.csv" , 'r') as f:
        for linea in f:
            columnas=linea.strip().split()
            if columnas:
                Primera_fecha = columnas[2].split('-')[1]
                if Primera_fecha in Dicc:
                    Dicc[Primera_fecha]+=1
                else:
                    Dicc[Primera_fecha]=1

    resultado = sorted(Dicc.items())
    return resultado
             
if __name__ == "__main__":
    resultado = pregunta_04()
    if resultado is not None:
        print("El resultado es:", resultado)

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
