import psycopg2
import params as p

"""
ESTE SCRIPT BORRA TODOS LOS DATOS DE TODAS LAS TABLAS EN EL ESQUEMA PÚBLICO DE LA BASE DE DATOS.
USAR CON MUCHA PRECAUCION!!
"""
# FIXME: la opcion de limpiar tabla esta rota

# Conectar a la base de datos
conn = psycopg2.connect(**p.conn_params)

# Crear un cursor
cur = conn.cursor()

# Consulta para obtener todos los nombres de las tablas en el esquema público
cur.execute("""
    SELECT tablename
    FROM pg_tables
    WHERE schemaname = 'public';
""")

# Obtener los nombres de las tablas
tables = cur.fetchall()

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
        for table in tables:
            truncate_query = f'DROP TABLE {table[0]} CASCADE;'
            cur.execute(truncate_query)
            print(f'Table {table[0]} deleted.')

elif response.lower() == 'c':
    response = input(
        'Se borraran los datos de todas las tablas. ¿Estas seguro? (y/n): ')

    if response != 'y':
        print('Operación cancelada.')

    elif response == 'y':
        print('Borrando datos de las tablas...')
        # Generar y ejecutar los comandos DELETE FROM
        for table in tables:
            delete_query = f'DELETE FROM {table[0]};'
            cur.execute(delete_query)
            print(f'Data from table {table[0]} deleted.')

else:
    print('input no identificado. operación cancelada.')

# Confirmar los cambios
conn.commit()

# Cerrar cursor y conexión
cur.close()
conn.close()
