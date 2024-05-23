import psycopg2 as psy2
import params as p
from schema import table_scheme

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

for i in range(len(table_scheme)):
    try:
        cur.execute(table_scheme[i])
        conn.commit()

        print(f'{i+1} CREATE TABLE')

    except psy2.Error as e:
        conn.rollback()
        print(table_scheme[i])
        print(e)


cur.close()
conn.close()
