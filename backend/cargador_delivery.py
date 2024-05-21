import psycopg2
import params
from archivos import get_data

# cargar los datos brutos
lineas = get_data("cldeldes")

# quitamos los datos repetidos
data_no_repetidos = []
for fila in lineas:
    dato = (fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10])
    if dato not in data_no_repetidos:
        data_no_repetidos.append(dato)

conn = psycopg2.connect(**params.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO delivery (nombre, vigente, telefono, tiempo_reparto, precio_unitario_despacho, precio_sus_mensual, precio_sus_anual)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
"""
subidos = 0
no_subidos = 0
for dato in data_no_repetidos:
    try:
        cur.execute(
            insert_query, dato)
        # conn.commit()
        subidos += 1

    except psycopg2.Error as e:
        conn.rollback()
        print(dato)
        print(e)
        no_subidos += 1

print(f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()
