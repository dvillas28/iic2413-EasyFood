import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Sucursal ---- \n')

    # cargar los datos brutos
    lineas = get_data("restaurantes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas:
        dato = (fila[4], fila[6])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO sucursal (nombre, telefono) VALUES (%s, %s);
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
            print(
                f"telefono: {dato[1]} se sobrepasa del limite de 11 caracteres")
            print(e)
            conn.rollback()
            tuplas_malas.append(dato)

    print(f"Total subidos: {subidos}")

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    load()
