import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("platos")

restriccion = dict()
nombre=[]
indice = 1
for fila in lineas:
    if fila[5] not in nombre and (len(fila[5]) <= 30):
        nombre.append(fila[5])
        restriccion[fila[5]] = indice
        indice += 1

data_no_repetidos = []
for fila in lineas:
    tupla = (fila[0], restriccion[fila[5]])
    if tupla not in data_no_repetidos and (len(fila[1]) <= 30):
        data_no_repetidos.append(tupla)


# quitamos las tuplas repetidas

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO aplica (plato_id, restriccion_id) VALUES (%s, %s);
"""

subidos = 0
no_subidos = 0
for tupla in data_no_repetidos:
    try:
        cur.execute(
            insert_query, tupla)
        # conn.commit()
        subidos += 1

    except psy2.Error as e:
        conn.rollback()
        print(tupla)
        print(e)
        no_subidos += 1

print(
    f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()
