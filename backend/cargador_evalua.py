import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Evalua ---- \n')

    # cargar los datos brutos
    calificacion_csv = get_data("calificacion")
    cldeldes_csv = get_data("cldeldes")
    pedidos_csv = get_data("pedidos")

    # quitamos las tuplas repetida
    data_no_repetidos = []
    for pedido in pedidos_csv:
        for despachador in cldeldes_csv:
            if pedido[3] == despachador[11]:
                despachador_telefono = despachador[12]
                break
        for delivery in cldeldes_csv:
            if pedido[2] == delivery[4]:
                delivery_telefono = delivery[6]
                break
        for calificacion in calificacion_csv:
            if pedido[0] == calificacion[0]:
                eval_despachador = calificacion[2]
                break
        else:
            eval_despachador = None
        tupla = (pedido[0], despachador_telefono,
                 delivery_telefono, eval_despachador)
        if tupla not in data_no_repetidos:
            data_no_repetidos.append(tupla)

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO evalua (pedido_id, despachador_telefono, delivery_telefono, eval_despachador) VALUES (%s, %s, %s, %s);
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
