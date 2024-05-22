import psycopg2 as psy2
import params as p
from archivos import get_data
from datetime import datetime

# cargar los datos brutos
lineas1 = get_data("pedidos")
lineas2 = get_data("calificacion")

def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, '%d-%m-%y').strftime('%Y-%m-%d')

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas1:
    for i in lineas2: 
        if i[0] == fila[0]: 
            dato = (fila[0], i[1], fila[7], fila[6], convertir_fecha(fila[5]))
            if dato not in data_no_repetidos:
                data_no_repetidos.append(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO pedido (id, eval_cliente, estado, hora, fecha) VALUES (%s, %s, %s, %s, %s);
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
    f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()