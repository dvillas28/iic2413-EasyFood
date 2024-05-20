import psycopg2
import params

try:
    conn = psycopg2.connect(**params.conn_params)
    print("Connected!")
    query = ""
    cur = conn.cursor()

    try:
        cur.execute(query)

        row = cur.fetchone()

        print(row)

    except psycopg2.Error as e:
        print(e.pgcode)
        print(e)

except Exception as e:
    print(e)
