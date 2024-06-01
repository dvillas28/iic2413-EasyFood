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

else:
    print('input no identificado. operación cancelada.')

# Confirmar los cambios
conn.commit()

# Cerrar cursor y conexión
cur.close()
conn.close()
