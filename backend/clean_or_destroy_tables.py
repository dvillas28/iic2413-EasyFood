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

print('d: DELETE - Borra todas las tablas')
print('c: CLEAN - Borra todos los datos de todas las tablas')
response = input("Selecciona la accion a ejecutar (d/c): ")

if response.lower() == 'd':
    response = input('Se borraran TODAS LAS TABLAS. ¿Estas seguro? (y/n): ')
    if response != 'y':
        print('Operación cancelada.')

    elif response == 'y':
        print('Borrando tablas...')
        # Generar y ejecutar los comandos TRUNCATE TABLE
        for table in table_names:
            truncate_query = f'DROP TABLE {table} CASCADE;'
            cur.execute(truncate_query)
            print(f'Table {table} deleted.')

elif response.lower() == 'c':
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
