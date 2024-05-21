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
    queries: dict = q.queries

    query_type = query_dict['query_type']
    args = query_dict['data']

    query = queries[query_type]

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    try:
        print(f'QUERY_SELECTED: {query}')
        print(f'ARGS: {args}')

        cur.execute(
            query, args)

        labels = (desc[0] for desc in cur.description)
        rows = cur.fetchall()

        # conn.commit()

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
