import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("clientes")

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    tupla = (fila[1], fila[0], fila[2], str(hash(fila[3]))[:30] )
    if tupla not in data_no_repetidos:
        data_no_repetidos.append(tupla)


conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO usuario (email, nombre, telefono, clave) VALUES (%s, %s, %s, %s);
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
