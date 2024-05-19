import psycopg2
import params

conn = psycopg2.connect(**params.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO r_temp (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono, area)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""
data = {}
j = 0
with open("data/restaurantes.csv", "r", encoding='mac_roman') as file:
    lineas = file.readlines()
    for i in range(1, len(lineas)):
        lineas[i] = lineas[i].strip().split(";")

        data[j] = lineas[i]
        j += 1

i = 0


for index, row in data.items():
    nombre = row[0]
    vigente = row[1]
    estilo = row[2]
    reparto_min = row[3]
    sucursal = row[4]
    direccion = row[5]
    telefono = row[6]
    area = row[7]

    try:
        cur.execute("""
                    INSERT INTO r_temp (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono, area)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                    (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono, area))
        conn.commit()
        print(f'{i} - OK\n')

    except psycopg2.IntegrityError as e:
        conn.rollback()
        print(f"{i} - NOK")
        print(data[i])

    except psycopg2.Error as e:
        # error de insercion
        conn.rollback()  # Deshacer cualquier cambio pendiente
        print(f"{i} - NOK2 {str(e).strip()}")

        if str(e).strip() == "value too long for type character varying(11)":
            # hay que acortar el numero de telefono
            print('ACORTAR NUMERO DE TELEFONO')
            cur.execute("""
                    INSERT INTO r_temp (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono, area)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                        (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono[:11], area))
            print(f"{i} - NOK2 fixed {telefono}\n")
            conn.commit()

            # reinsertar

        elif str(e).strip() == "value too long for type character varying(60)":
            # direccion MUY larga
            print('ACORTAR DIRECCION')
            # reinsertar
            cur.execute("""
                    INSERT INTO r_temp (nombre, vigente, estilo, reparto_min, sucursal, direccion, telefono, area)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                        (nombre, vigente, estilo, reparto_min, sucursal, direccion[30:], telefono[:11], area))
            print(f"{i} - NOK2 fixed direccion")
            conn.commit()

    i += 1

cur.close()
conn.close()
