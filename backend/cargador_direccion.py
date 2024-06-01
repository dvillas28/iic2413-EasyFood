import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Direccion ---- \n')

    # cargar los datos brutos
    clientes_csv = get_data("clientes")
    restaurantes_csv = get_data("restaurantes")

    comunas_csv = get_data("comuna")

    # quitamos las tuplas repetidas
    data_no_repetidos = []

    # direcciones clientes
    for cliente in clientes_csv:
        for comuna in comunas_csv:
            if cliente[5] == comuna[0]:
                tupla = (comuna[1], cliente[4])
                if tupla not in data_no_repetidos:
                    data_no_repetidos.append(tupla)

    # direcciones sucursales
    for sucursal in restaurantes_csv:
        tupla = (sucursal[7], sucursal[5])
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
            print(e)
            conn.rollback()
            tuplas_malas.append(dato)

    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    load()
