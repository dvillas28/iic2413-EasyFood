import psycopg2 as psy2
import params as p
import csv

# cargar los datos brutos
lineas = []
with open('backend/data/clientes.csv', mode='r', encoding='mac_roman') as file:
    reader = csv.reader(file, delimiter=';')
    encabezado = next(reader) # Saltar la fila de encabezado
    for fila in reader:
        lineas.append(fila)

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    dato = (fila[1], fila[0], fila[2], str(hash(fila[3]))[:30] )
    if dato not in data_no_repetidos:
        data_no_repetidos.append(dato)

# for dato in data:
#     print(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO usuario (email, nombre, telefono, clave) VALUES (%s, %s, %s, %s);
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

print(
    f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()
