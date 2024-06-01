import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Direccion ---- \n')

    # cargar los datos brutos
    restaurantes_csv = get_data("restaurantes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for sucursal in restaurantes_csv:
        tupla = (sucursal[6], sucursal[5], sucursal[7])
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)


    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO localizado_en (sucursal_telefono, direccion_calle, direccion_comuna) VALUES (%s, %s, %s);
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
            no_subidos+=1
            conn.rollback()
            tuplas_malas.append(dato)

    conn.commit()
    cur.close()
    conn.close()

    print(f"Total subidos: {subidos}")
    print(f"Total no subidos: {no_subidos}")