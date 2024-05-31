import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Realiza ---- \n')

    # cargar los datos brutos
    lineas = get_data("pedidos")

    # quitamos las tuplas repetida

    data_no_repetidos = []
    for fila in lineas:
        dato = (fila[0], fila[1])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO realiza (pedido_id, usuario_email) VALUES (%s, %s);
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
            print(e)
            conn.rollback()
            tuplas_malas.append(dato)

    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    load()
