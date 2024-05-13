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
except Exception as e:
    print(e)
