import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Plato ---- \n')

    # cargar los datos brutos
    lineas = get_data("platos")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas:
        tupla = (fila[4], fila[1], fila[5], fila[6])
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO plato (estilo, nombre, restriccion, ingredientes) VALUES (%s, %s, %s, %s);
    """

    subidos = 0
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

    print(f"\nSubidas correctamente: {subidos} tuplas")

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    load()
