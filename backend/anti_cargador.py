import psycopg2
import params as p

"""
ESTE SCRIPT BORRA TODOS LOS DATOS DE TODAS LAS TABLAS EN EL ESQUEMA PÚBLICO DE LA BASE DE DATOS.
USAR CON MUCHA PRECAUCION!!
"""

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

# Generar y ejecutar los comandos TRUNCATE TABLE
for table in tables:
    truncate_query = f'TRUNCATE TABLE {table[0]} CASCADE;'
    cur.execute(truncate_query)
    print(f'Table {table[0]} truncated.')

# Confirmar los cambios
conn.commit()

# Cerrar cursor y conexión
cur.close()
conn.close()
