import psycopg2 as psy2
import params as p
from archivos import get_data


def load():

    print(f'\n ---- Cargando datos de la tabla Contiene ---- \n')

    # cargar los datos brutos

    # pedidos.csv
    pedidos_csv = get_data("pedidos")

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
    for pedido in pedidos_csv:
        contiene_platos = pedido[4].split(" ")
        for indice_plato in contiene_platos:
            for plato_csv in platos_csv:
                if plato_csv[0] == indice_plato:
                    (nombre, estilo, restriccion, ingredientes) = (
                        plato_csv[1], plato_csv[4], plato_csv[5], plato_csv[6])
                    restaurante = plato_csv[10]
                    for plato in tabla_plato:
                        if (plato[1], plato[2], plato[3], plato[4]) == (estilo, nombre, restriccion, ingredientes):
                            indice = plato[0]
                            tupla = (indice, pedido[0], restaurante)
                            data_no_repetidos.append(tupla)

    insert_query = """
        INSERT INTO contiene (plato_id, pedido_id, restaurante_nombre) VALUES (%s, %s, %s);
    """

    subidos = 0
    no_subidos = 0
    for tupla in data_no_repetidos:
        try:
            cur.execute(
                insert_query, tupla)
            conn.commit()
            subidos += 1

        except psy2.Error as e:
            conn.rollback()
            print(tupla)
            print(e)
            no_subidos += 1

    print(f'\nSubidas correctamente: {subidos} tuplas')

    cur.close()
    conn.close()


if __name__ == '__main__':
    load()
