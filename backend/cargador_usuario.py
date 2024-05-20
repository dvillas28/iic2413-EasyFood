import psycopg2 as psy2
import params as p

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO usuario (email, nombre, telefono, clave) VALUES (%s, %s, %s, %s);
"""
data = []
with open('backend/data/clientes.csv', 'r', encoding='mac_roman') as file:
    lineas = file.readlines()
    for i in range(1, len(lineas)):
        lineas[i] = lineas[i].strip().split(';')

for linea in lineas:
    print(linea)

cur.close()
conn.close()
