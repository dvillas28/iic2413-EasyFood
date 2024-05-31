import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla De ---- \n')

    # cargar los datos brutos
    lineas = get_data("restaurantes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas:
        tupla = (fila[0], fila[6])
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO de (restaurante_nombre, sucursal_telefono) VALUES (%s, %s);
    """

    subidos = 0
    no_subidos = 0
    tuplas_malas = []

    for tupla in data_no_repetidos:
        try:
            cur.execute(
                insert_query, tupla)
            conn.commit()
            subidos += 1

        except psy2.Error as e:
            conn.rollback()
            print(tupla)
            print(e)
            no_subidos += 1
    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:
        print(f'No subidas: {no_subidos} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    load()
