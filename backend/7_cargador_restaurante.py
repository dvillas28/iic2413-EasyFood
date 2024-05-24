import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("restaurantes")

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    dato = (fila[0], fila[1], fila[2], fila[3])
    if dato not in data_no_repetidos:
        data_no_repetidos.append(dato)

print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO restaurant (nombre, vigente, estilo, precio_min_reparto_gratis) VALUES (%s, %s, %s, %s);
"""

subidos = 0
no_subidos = 0
for dato in data_no_repetidos:
    try:
        cur.execute(
            insert_query, dato)
        conn.commit()
        subidos += 1

    except psy2.Error as e:
        conn.rollback()
        print(dato)
        print(e)
        no_subidos += 1

print(f"Total subidos: {subidos} tuplas")
print(f"Total no subidos: {no_subidos} tuplas")
cur.close()
conn.close()
