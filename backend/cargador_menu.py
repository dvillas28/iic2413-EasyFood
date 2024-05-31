import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Menu ---- \n')

    # platos.csv
    platos_csv = get_data("platos")

    # plato
    query = "SELECT * FROM plato;"

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    cur.execute(query)
    tabla_plato = cur.fetchall()

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for plato_csv in platos_csv:
        for plato in tabla_plato:
            if (plato[1], plato[2], plato[3], plato[4]) == (plato_csv[4], plato_csv[1], plato_csv[5], plato_csv[6]):
                plato_id = plato[0]
                tupla = (plato_id, plato_csv[10], plato_csv[7],
                         plato_csv[9], plato_csv[3], plato_csv[2], plato_csv[8])
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
            conn.commit()
        except psy2.Error as e:
            print(f"Error: {e}")
            print(f"Failed to insert: {dato}")
            conn.rollback()
            tuplas_malas.append(dato)

    print(f"\nSubidas correctamente: {subidos} tuplas")

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    cur.close()
    conn.close()


if __name__ == "__main__":
    load()
