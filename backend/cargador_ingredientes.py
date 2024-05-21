import psycopg2 as psy2
import params as p
import csv

# cargar los datos brutos
lineas = []
with open('backend/data/platos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    encabezado = next(reader) # Saltar la fila de encabezado
    for fila in reader:
        lineas.append(fila)

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    ingredientes = map(lambda x: tuple([x.strip(' ').strip('.')]), fila[6].split(','))
    for tupla in ingredientes:
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)


conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO ingrediente (nombre) VALUES (%s);
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
