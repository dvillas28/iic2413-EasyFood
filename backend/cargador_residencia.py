import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Residencia ---- \n')

    # cargar los datos brutos
    clientes_csv = get_data("clientes")

    comunas_csv = get_data("comuna")

    # quitamos las tuplas repetida
    data_no_repetidos = []
    for cliente in clientes_csv:
        for comuna in comunas_csv:
            if cliente[5] == comuna[0]:
                tupla = (cliente[1], cliente[4], comuna[1])
                if tupla not in data_no_repetidos:
                    data_no_repetidos.append(tupla)

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO residencia (usuario_email, direccion_calle, direccion_comuna) VALUES (%s, %s, %s);
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
            print(dato)
            no_subidos += 1
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
