import psycopg2 as psy2
import params as p
from archivos import get_data
from datetime import datetime


def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, '%d-%m-%y').strftime('%Y-%m-%d')


def load() -> None:
    print(f'\n ---- Cargando datos de la tabla Suscrito ---- \n')

    lineas1 = get_data("suscripciones")
    lineas2 = get_data("cldeldes")

    # quitamos las tuplas repetidas
    data_no_repetidos = []
    for s in lineas1:
        for c in lineas2:
            if c[1] == s[0]:
                dato = [c[6],  # delivery_telefono
                        s[0],  # usuario_email
                        s[3],  # pago
                        convertir_fecha(s[4]),  # fecha
                        s[5],  # ciclo
                        s[2].lower()]  # estado
                if dato not in data_no_repetidos:
                    data_no_repetidos.append(dato)

    print(f'Existen en total {len(data_no_repetidos)} tuplas a subir')

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO suscrito (delivery_telefono, usuario_email, pago, fecha, ciclo, estado) VALUES (%s, %s, %s, %s, %s, %s);
    """

    subidos = 0
    tuplas_malas = []

    for dato in data_no_repetidos:
        try:
            cur.execute(
                insert_query, dato)
            conn.commit()
            subidos += 1
            # print(F'SUCESS {dato}')

        except psy2.Error as e:
            conn.rollback()
            print(dato)
            print(e)

    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:
        print(f'No subidas: {len(tuplas_malas)} tuplas')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    load()
