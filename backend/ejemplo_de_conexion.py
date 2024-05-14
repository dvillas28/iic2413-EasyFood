import psycopg2

NOMBRE = "grupo15e2"
USER = "grupo15"
HOST = "pavlov.ing.puc.cl"
PORT = 5432
PASSWORD = "putobdd"

try:
    conn = psycopg2.connect(
        f'dbname={NOMBRE} user={USER} host={HOST} port={PORT} password={PASSWORD}')
    print("Connected!")
    query = "SELECT * FROM test;"
    cur = conn.cursor()

    try:
        cur.execute(query)

        row = cur.fetchone()

        while row:
            print(row)
            row = cur.fetchone()

    except psycopg2.Error as e:
        print(e.pgcode)

except Exception as e:
    print(e)
