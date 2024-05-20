import psycopg2 as psy2
import params as p

# cargar los datos brutos
with open('backend/data/clientes.csv', 'r', encoding='mac_roman') as file:
    lineas = file.readlines()
    for i in range(len(lineas)):
        lineas[i] = lineas[i].strip().split(';')


nombres_limpios = []
empty_name = ''

# limpiar los nombres mal escritos
for i in range(len(lineas)):

    if len(lineas[i]) == 1:
        empty_name = lineas[i][0]

        if i + 1 < len(lineas):
            if '"' in lineas[i + 1][0]:
                lineas[i + 1][0] = (empty_name + '' + lineas[i + 1][0])[1:-1]

            continue
    else:

        dato = (lineas[i][1], lineas[i][0], lineas[i][2], lineas[i][3])
        nombres_limpios.append(dato)


# quitamos las tuplas repetidas
data_no_repetidos = []
for lista in nombres_limpios:
    if lista not in data_no_repetidos:
        data_no_repetidos.append(lista)

# for dato in data:
#     print(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO usuario (email, nombre, telefono, clave) VALUES (%s, %s, %s, %s);
"""

subidos = 0
no_subidos = 0
for dato in data_no_repetidos:
    try:
        cur.execute(
            insert_query, dato)
        # conn.commit()
        subidos += 1

    except psy2.Error as e:
        conn.rollback()
        print(dato)
        print(e)
        no_subidos += 1

print(
    f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
cur.close()
conn.close()
