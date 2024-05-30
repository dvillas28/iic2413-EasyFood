import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\nCargando datos de la tabla Delivery\n')

    # cargar los datos brutos
    lineas = get_data("cldeldes")

    # quitamos los datos repetidos
    data_no_repetidos = []
    for fila in lineas:
        dato = (fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO delivery (nombre, vigente, telefono, tiempo_reparto, precio_unitario_despacho, precio_sus_mensual, precio_sus_anual)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
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

    if not tuplas_malas:
        print(f'No hubo tuplas mal subidas')

    conn.commit()
    cur.close()
    conn.close()

    print(f"Total subidos: {subidos}")
    print(f"Total no subidos: {no_subidos}")
