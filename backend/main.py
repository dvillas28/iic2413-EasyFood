import psycopg2 as psy2
import params as p
import 

conn = psy2.connect(**p.conn_params)
cur = conn.cursor()

for tabla in query_tablas:
    try:
        cur.execute(table)
        # conn.commit()

    except psy2.Error as e:
        conn.rollback()
        print(tabla)
        print(e)


cur.close()
conn.close()