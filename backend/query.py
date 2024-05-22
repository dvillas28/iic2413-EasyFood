import backend.params as p
import backend.queries as q
import psycopg2 as psy2


def get_query_result(query_dict: dict) -> dict:
    """
    Recibe input del front end y retorna un diccionario con la respuesta.
    Formato de respuesta:
    data = {
        'labels': (...)
        'rows': (...)
    }
    """

    queries: dict = q.queries  # diccionario con boilerplate de las consultas

    query_type = query_dict['query_type']  # llave de la consulta
    args = query_dict['data']  # argumentos
    sql = queries[query_type]  # boilerplate sql de la consulta

    # TODO: tratar las inyecciones en las consultas inestructuradas
    if query_type == 0.0:
        query = f"{sql['SELECT']} {args[0]} {sql['FROM']} {args[1]};"

    elif query_type == 0.1:
        query = f"{sql['SELECT']} {args[0]} {sql['FROM']} {args[1]} {sql['WHERE']} {args[2]};"

    else:
        # consulta estructurada
        pass

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    try:
        cur.execute(query)

        labels = (desc[0] for desc in cur.description)
        rows = cur.fetchall()

        conn.commit()

        result = {
            'result': 1,
            'labels': labels,
            'rows': rows
        }

    except psy2.Error as e:
        conn.rollback()
        print(e)

        result = {
            'result': 0,
            'labels': [],
            'rows': []
        }

    cur.close()
    conn.close()

    return result
