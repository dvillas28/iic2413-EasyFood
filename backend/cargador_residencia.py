import psycopg2 as psy2
import params as p
from archivos import get_data


def load() -> None:

    print(f'\n ---- Cargando datos de la tabla Residencia ---- \n')

    # cargar los datos brutos
    lineas = get_data("clientes")

    # quitamos las tuplas repetida


    data_no_repetidos = []
    for fila in lineas:
        newf4 = fila[4].split(',')
        dato = (fila[1], newf4[0], newf4[1])
        if dato not in data_no_repetidos:
            data_no_repetidos.append(dato)

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
            conn.rollback()
            tuplas_malas.append(dato)

    print(f'\nSubidas correctamente: {subidos} tuplas')

    if tuplas_malas:

        print(f'No subidas: {len(tuplas_malas)} tuplas')

        try:
            cur.execute(
                "ALTER TABLE residencia ALTER COLUMN direccion_calle TYPE VARCHAR(50);")
            print(
                "\n Cambio direccion_calle tabla residencia: direccion_calle VARCHAR(30) to direccion_calle VARCHAR(50)\n")
            conn.commit()
        except psy2.Error as e:
            conn.rollback()
            print("Error al modificar la tabla:", e)

        for dato in tuplas_malas:
            try:
                cur.execute(insert_query, dato)
                subidos += 1
            except psy2.Error as e:
                conn.rollback()
                print("Error al reintentar insertar la tupla:", dato)
                print(e)
        
        if tuplas_malas:
          try:
              cur.execute(
                  "ALTER TABLE residencia ALTER COLUMN usuario_email TYPE VARCHAR(50);")
              print(
                  "\n Cambio usuario_email tabla residencia: usuario_email VARCHAR(30) to usuario_email VARCHAR(50)\n")
              conn.commit()
          except psy2.Error as e:
              conn.rollback()
              print("Error al modificar la tabla:", e)

          for dato in tuplas_malas:
              try:
                  cur.execute(insert_query, dato)
                  subidos += 1
              except psy2.Error as e:
                  conn.rollback()
                  print("Error al reintentar insertar la tupla:", dato)
                  print(e)
                  no_subidos += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"Total subidos: {subidos} tuplas")
    print(f"Total no subidos: {no_subidos} tuplas")
