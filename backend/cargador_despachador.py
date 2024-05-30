import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\nCargando datos de la tabla Despachador\n')

    # cargar los datos brutos
    lineas = get_data("cldeldes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas:
        dato = (fila[12], fila[11])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO despachador (telefono, nombre) VALUES (%s, %s);
    """

    subidos = 0
    no_subidos = 0
    tuplas_malas = []

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    for dato in data_no_repetidos:
        try:
            cur.execute(insert_query, dato)
            subidos += 1
            conn.commit()
        except psy2.Error as e:
            print(
                f"telefono: {dato[1]} se sobrepasa del limite de 11 caracteres")
            print(e)
            conn.rollback()
            tuplas_malas.append(dato)

    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:

        print(f'No subidas: {len(tuplas_malas)} tuplas')

        try:
            cur.execute(
                "ALTER TABLE despachador ALTER COLUMN telefono TYPE VARCHAR(20);")
            print(
                "\n Cambio restriccion tabla despachador: telefono CHAR(11) to telefono VARCHAR(20)\n")
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

    print(f"Total subidos: {subidos} tuplas")
    print(f"Total no subidos: {no_subidos} tuplas")
