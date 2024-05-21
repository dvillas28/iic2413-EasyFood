import psycopg2 as psy2
import params as p
import csv

# cargar los datos brutos
lineas = []
with open('backend/data/platos.csv', 'r', encoding='mac_roman') as file:
    reader = csv.reader(file, delimiter=';')
    encabezado = next(reader)  # Saltar la fila de encabezado
    for fila in reader:
        lineas.append(fila)

data_no_repetidos = set()
for fila in lineas: 
  [data_no_repetidos.add((i, )) for i in fila[6].strip('.').strip(' ').split(',')]

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO ingrediente (nombre) VALUES (%s);
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
