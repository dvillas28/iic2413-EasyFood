import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\nCargando datos de la tabla Direccion\n')

    # cargar los datos brutos
    lineas = get_data("clientes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas:
        tupla = (fila[4].split(',')[1], fila[4].split(',')[0])
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO direccion (comuna, calle) VALUES (%s, %s);
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
            print(f"calle: {dato[1]} se sobrepasa del limite de 30 caracteres")
            conn.rollback()
            tuplas_malas.append(dato)
    a = 0
    if tuplas_malas:
        try:
            cur.execute(
                "ALTER TABLE direccion ALTER COLUMN calle TYPE VARCHAR(60);")
            print("Tabla direccion: calle VARCHAR(30) to calle VARCHAR(60)")
            conn.commit()
            a += 1
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

    print(f'Tuplas malas corregidas: {a}')
    print(f"Total subidos: {subidos}")
    print(f"Total no subidos: {no_subidos}")
