import psycopg2 as psy2
import params as p
from archivos import get_data

# cargar los datos brutos
lineas1 = get_data("pedidos")
lineas2 = get_data("calificacion")

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas1:
    for i in lineas2: 
        if i[0] == fila[0]: 
            dato = (fila[0], i[1], fila[7], fila[6], fila[5])
            if dato not in data_no_repetidos:
                data_no_repetidos.append(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO pedido (id, eval_cliente, estado, hora, fecha)
    VALUES (%s, %s, %s, %s, TO_TIMESTAMP(%s, 'DD-MM-YY'));
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
        print(f"Error: {e}")
        print(f"Failed to insert: {dato}")
        conn.rollback()
        tuplas_malas.append(dato)

if tuplas_malas:
    new_insert_query = """
        INSERT INTO pedido (id, eval_cliente, estado, hora, fecha)
        VALUES (%s, %s, %s, %s, TO_TIMESTAMP(%s, 'DD-MM-YY'));
    """
    # try:
    #     cur.execute("ALTER TABLE pedido ALTER COLUMN fecha TYPE TIMESTAMP USING TO_TIMESTAMP(fecha, 'DD-MM-YY');")
    #     print("Tabla pedido: fecha DATE to TIMESTAMP using 'DD-MM-YY' format.")
    #     conn.commit()
    # except psy2.Error as e:
    #     conn.rollback()
    #     print("Error al modificar la tabla:", e)

    for dato in tuplas_malas:
        try:
            cur.execute(insert_query, dato)
            subidos += 1
            conn.commit()
        except psy2.Error as e:
            conn.rollback()
            print("Error al reintentar insertar la tupla::", dato)
            print(e)
            no_subidos += 1

print(f"Total subidos: {subidos}")
print(f"Total no subidos: {no_subidos}")

cur.close()
conn.close()