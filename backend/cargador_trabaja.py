import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Trabaja ---- \n')

    # cargar los datos brutos
    lineas = get_data("cldeldes")

    # quitamos los datos repetidos
    data_no_repetidos = []
    for fila in lineas:
        dato = (fila[6], fila[12])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO trabaja (delivery_telefono, despachador_telefono)
        VALUES (%s, %s);
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
            print(e)
            conn.rollback()
            tuplas_malas.append(dato)
            no_subidos += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"Total subidos: {subidos}")
    print(f"Total no subidos: {no_subidos}")
