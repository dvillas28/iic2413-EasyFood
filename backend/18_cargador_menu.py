import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Menu ---- \n')

    # cargar los datos brutos
    lineas1 = get_data("platos")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas1:
        tupla = (fila[0],  # plato_id
                 fila[10],  # restaurante_nombre
                 fila[7],  # porcion
                 fila[9],  # tiempo_preparacion
                 fila[3],  # disponibilidad
                 fila[2],  # descripcion
                 fila[8]  # precio
                 )
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO menu (plato_id, restaurante_nombre, porcion, tiempo_preparacion, disponibilidad, descripcion, precio)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    subidos = 0
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

    print(f"\nSubidas correctamente: {subidos} tuplas")

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    # conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    load()
