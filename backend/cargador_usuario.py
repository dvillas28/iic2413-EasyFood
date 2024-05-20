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
        nombres_limpios.append(lineas[i])

data = []
titles = nombres_limpios.pop(0)
for lista in nombres_limpios:
    cliente_dict = {}
    for i in range(len(titles)):
        cliente_dict[titles[i]] = lista[i]
    data.append(cliente_dict)

# for dato in data:
#     print(dato)

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

insert_query = """
    INSERT INTO usuario (email, nombre, telefono, clave) VALUES (%s, %s, %s, %s);
"""

for dato in data:
    try:
        cur.execute(
            insert_query, (dato['email'], dato['cliente'], dato['telefono'], dato['clave']))
        conn.commit()

    except psy2.Error as e:
        conn.rollback()

        state = e.diag.sqlstate

        if state == '23505':  # violacion de unicidad
            print(
                f"{state} - Restriccion de IC: La llave primaria {dato['email']} ya existe - Accion: Ignorar")

        elif state == '22001':  # violacion de integridad
            print(
                f"{state} - Restriccion de IC: existe un campo demasiado largo - Accion: Ignorar")

        continue


cur.close()
conn.close()
