import backend.params as p
import backend.queries_dict as q
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

    # extraccion de los datos recibidos como argumento
    query_type = query_dict['query_type']  # llave de la consulta
    args = query_dict['data']  # argumentos

    sql = queries[query_type]  # boilerplate sql de la consulta

    # tratamiento contra inyecciones para consultas inestructuradas
    if not any(map(lambda kword: kword in ''.join(args) or kword.lower() in ''.join(args), q.harmful_sql_keywords)):

        if query_type == 0.0:
            query = f"{sql['SELECT']} {args[0]} {sql['FROM']} {args[1]};"

        elif query_type == 0.1:
            query = f"{sql['SELECT']} {args[0]} {sql['FROM']} {args[1]} {sql['WHERE']} {args[2]};"

    else:
        return {
            'result': 0,
            'error_type': 'SQLInjection',
            'error': 'Se ha detectado un intento de inyección SQL en la consulta.'
        }

    conn = psy2.connect(**p.conn_params)
    cur = conn.cursor()

    try:

        if type(query_type) == float:  # inestructurada, la consulta ya esta creada
            cur.execute(query)

        else:
            cur.execute(sql, args)  # estructurada, agregamos los argumentos

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
            'error_type': 'SyntaxError',
            'error': 'Error de sintaxis en la consulta. Revisar los campos ingresados.'
        }

    cur.close()
    conn.close()

    return result
