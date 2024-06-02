import psycopg2
import params as p
from schema import table_names

"""
ESTE SCRIPT BORRA TODOS LOS DATOS DE TODAS LAS TABLAS EN EL ESQUEMA PÚBLICO DE LA BASE DE DATOS.
USAR CON MUCHA PRECAUCION!!
"""

# Conectar a la base de datos
conn = psycopg2.connect(**p.conn_params)

# Crear un cursor
cur = conn.cursor()

print('CLEAN - Borra todos los datos de todas las tablas')

response = input(
    'Se borraran los datos de todas las tablas. ¿Estas seguro? (y/n): ')
if response != 'y':
    print('Operación cancelada.')

elif response == 'y':
    print('Borrando datos de las tablas...')
    # Generar y ejecutar los comandos DELETE FROM
    for table in table_names:
        delete_query = f'DELETE FROM {table};'
        cur.execute(delete_query)
        print(f'Data from table {table} cleaned.')

else:
    print('input no identificado. operación cancelada.')

# Confirmar los cambios
conn.commit()

# Cerrar cursor y conexión
cur.close()
conn.close()
