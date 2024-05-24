import psycopg2 as psy2
import params as p
from archivos import get_data
from datetime import datetime


lineas2 = get_data("cldeldes")
lineas1 = get_data("suscripciones")

def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, '%d-%m-%y').strftime('%Y-%m-%d')

# quitamos las tuplas repetidas
data_no_repetidos = []
for fila in lineas1:
    for i in lineas2: 
        if i[1] == fila[0]: 
            dato = (fila[0], i[6], fila[4], convertir_fecha(fila[4]), fila[5], fila[2])
            if dato not in data_no_repetidos:
                data_no_repetidos.append(dato)

print(data_no_repetidos)
# conn = psy2.connect(**p.conn_params)
# cur = conn.cursor()

# insert_query = """
#     INSERT INTO suscrito (email, telefono, pago, fecha, ciclo, estado) VALUES (%s, %s, %s, %s, %s, %s);
# """

# subidos = 0
# no_subidos = 0
# for dato in data_no_repetidos:
#     try:
#         cur.execute(
#             insert_query, dato)
#         # conn.commit()
#         subidos += 1

#     except psy2.Error as e:
#         conn.rollback()
#         print(dato)
#         print(e)
#         no_subidos += 1

# print(
#     f'Se subieron {subidos} registros y no se subieron {no_subidos} registros: {no_subidos / subidos * 100:.2f}%')
# cur.close()
# conn.close()