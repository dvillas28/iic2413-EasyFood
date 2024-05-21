import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("cldeldes")

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    dato = (fila[11], fila[12])
    if dato not in data_no_repetidos:
        data_no_repetidos.append(dato)

# for dato in data:
#     print(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO despachador (telefono, nombre) VALUES (%s, %s);
"""

subidos = 0
no_subidos = 0
for dato in data_no_repetidos:
    try:
        cur.execute(
            insert_query, dato)
        # conn.commit()
        subidos += 1

    except psy2.Error as e:
        conn.rollback()
        print(dato)
        print(e)
        no_subidos += 1

print(
    f'Se subieron {subidos} registros CORERCTOS y no se subieron {no_subidos} registros por estar INCORRECTOS: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()
