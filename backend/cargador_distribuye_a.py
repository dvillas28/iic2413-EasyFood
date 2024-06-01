import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Distribuye_a ---- \n')

    # cargar los datos brutos
    pedidos_csv = get_data("pedidos")
    platos_csv = get_data("platos")
    cldeldes_csv = get_data("cldeldes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for pedido in pedidos_csv:
        for delivery in cldeldes_csv:
            if delivery[4] == pedido[2]:
                delivery_telefono = delivery[6]
                break
        for plato in pedido[4]:
            for plato_csv in platos_csv:
                if plato == plato_csv[0]:
                    tupla = (delivery_telefono, plato_csv[10])
                    if tupla not in data_no_repetidos:
                        data_no_repetidos.append(tupla)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO distribuye_a (delivery_telefono, restaurante_nombre) VALUES (%s, %s);
    """

    subidos = 0
    no_subidos = 0
    tuplas_malas = []
    for dato in data_no_repetidos:
        try:
            cur.execute(
                insert_query, dato)
            conn.commit()
            subidos += 1

        except psy2.Error as e:
            conn.rollback()
            print(dato)
            print(e)
            no_subidos += 1
            tuplas_malas.append(dato)

    print(f'\nSubidas correctamente: {subidos} registros')
    if tuplas_malas:
        print(f'No subidos: {len(tuplas_malas)} tuplas')

    cur.close()
    conn.close()


if __name__ == '__main__':
    load()
