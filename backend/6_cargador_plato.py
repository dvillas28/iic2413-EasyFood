import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas = get_data("platos")

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas:
    tupla = (fila[0], fila[4], fila[1], fila[5], fila[6])
    if tupla not in data_no_repetidos:
        data_no_repetidos.append(tupla)

print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO plato (id, estilo, nombre, restriccion, ingredientes) VALUES (%s, %s, %s, %s, %s);
"""

subidos = 0
no_subidos = 0
tuplas_malas = []

for dato in data_no_repetidos:
    try:
        cur.execute(insert_query, dato)
        subidos += 1
        # conn.commit()
    except psy2.Error as e:
        print(e)
        conn.rollback()
        tuplas_malas.append(dato)

if tuplas_malas:
    try:
        cur.execute(
            "ALTER TABLE plato ALTER COLUMN restriccion TYPE VARCHAR(30);")
        print("Tabla plato: restriccion INT to restriccion VARCHAR(30)")
        # conn.commit()
    except psy2.Error as e:
        conn.rollback()
        print("Error al modificar la tabla:", e)

    for dato in tuplas_malas:
        try:
            cur.execute(insert_query, dato)
            subidos += 1
        except psy2.Error as e:
            conn.rollback()
            no_subidos += 1
            print(e)

    if tuplas_malas:
        try:
            cur.execute(
                "ALTER TABLE plato ALTER COLUMN ingredientes TYPE TEXT;")
            print("Tabla plato: ingredientes VARCHAR(30) to ingredietes TEXT")
            # conn.commit()
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


# conn.commit()
cur.close()
conn.close()

print(f"Total subidos: {subidos}")
print(f"Total no subidos: {no_subidos}")
