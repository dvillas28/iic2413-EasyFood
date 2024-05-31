import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Pedido ---- \n')

    # cargar los datos brutos
    lineas1 = get_data("pedidos")
    lineas2 = get_data("calificacion")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for fila in lineas1:
        for i in lineas2:
            if i[0] == fila[0]:
                dato = (fila[0], i[1], fila[7].lower().strip(
                    " "), fila[6], fila[5])
                if dato not in data_no_repetidos:
                    data_no_repetidos.append(dato)
                break
        else:
            dato = (fila[0], None, fila[7].lower().strip(
                " "), fila[6], fila[5])
            data_no_repetidos.append(dato)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO pedido (id, eval_cliente, estado, hora, fecha)
        VALUES (%s, %s, %s, %s, TO_TIMESTAMP(%s, 'DD-MM-YY'));
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
