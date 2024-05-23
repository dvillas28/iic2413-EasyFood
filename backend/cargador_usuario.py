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
tuplas_malas = []

for dato in data_no_repetidos:
    try:
        cur.execute(insert_query, dato)
        subidos += 1
        conn.commit()
    except psy2.Error as e:
        conn.rollback()
        print(dato)
        print(e)
        tuplas_malas.append(dato)

if tuplas_malas:
    try:
        cur.execute("ALTER TABLE restaurant ALTER COLUMN email TYPE VARCHAR(40);")
        conn.commit()
    except psy2.Error as e:
        conn.rollback()
        print("Error al modificar la tabla:", e)

    for dato in tuplas_malas:
        try:
            cur.execute(insert_query, dato)
            subidos += 1
        except psy2.Error as e:
            conn.rollback()
            print("Error al reintentar insertar la tupla:", dato)
            print(e)
            no_subidos += 1

conn.commit()
cur.close()
conn.close()

print(f"Total subidos: {subidos}")
print(f"Total no subidos: {no_subidos}")
