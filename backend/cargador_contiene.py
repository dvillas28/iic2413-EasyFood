import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("pedidos")

# quitamos las tuplas repetidas
new = []
for fila in lineas:
    new.append([fila[0], fila[4].split('  ')])

data_no_repetidos = []
for fila in new:
    for e in fila[1]: 
      tupla = (fila[0], e)
      if tupla not in data_no_repetidos:
          data_no_repetidos.append(tupla)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO contiene (plato_id, pedido_id) VALUES (%s, %s);
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
