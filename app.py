from flask import Flask, render_template, request, redirect, url_for
from backend import query as q

app = Flask(__name__)


@app.route('/')
def index():
    """
    La funcion principal con los cuadros de texto para la consulta
    """
    return render_template('index.html')


@app.route('/menu_consultas')
def consultas_estruct():
    """
    Funcion para mostrar el menu inicial desplegable de las consultas estructuradas
    """
    return render_template('menu_consultas.html')


@app.route('/consulta_inestruct')
def consultas_inestruct():
    """
    Consultas Inestructuradas
    """
    return render_template('consultas_inestruct.html')


@app.route('/procesar_inestruct', methods=['POST'])
def process_inestruct_query():
    """
    Funcion para procesar los inputs raw del usuario de las consultas inestructuradas
    """
    # solicitar los textos de los campos SELECT, FROM Y WHERE
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']

    # verificar que text1 y text2 sean no nulos
    if text1 and text2:
        # enviamos estos argumentos a la funcion result, en la ruta /resultado, y ejecutarla
        return redirect(url_for('result',
                                query_type=0,
                                text1=text1,
                                text2=text2,
                                text3=text3))

    else:
        return redirect(url_for('error',
                                error_type='NullInput',
                                message='Campo SELECT/FROM vacio'))


@app.route('/procesar_estruct', methods=['POST'])
def process_estruct_query():
    """
    Funcion para procesar los inputs raw de las consultas estructuradas
    """
    # tomar el tipo de query y los campos
    button_number = int(request.form['button'])

    text_value = request.form.get(f'text{button_number}')
    data = [text_value]

    print(f'button number raw: {button_number}')
    print(f'data raw: {data}')
    # enviarselos a result(query_type, args*)

    return redirect(url_for('result',
                            query_type=button_number,
                            query_data=data))


@app.route('/result_query')
def result():
    """
    La funcion para mostrar el resultado de la consulta
    """
    # obtener el tipo de la consulta 0.%: inestruc, 1: estruc
    query_type = int(request.args.get('query_type'))

    # empaquetamiento de datos consulta inestructurada
    if query_type == 0:
        text1 = request.args.get('text1')
        text2 = request.args.get('text2')
        text3 = request.args.get('text3')
        data = [text1, text2, text3]

        if text3:
            query_dict = {"query_type": 0.1,
                          'data': (data[0], data[1], data[2])}
        else:
            query_dict = {"query_type": 0.0,
                          'data': (data[0], data[1])}

    # empaquetamiento de datos consulta estructurada
    elif query_type != 0:
        data = request.args.get('query_data')

        # las consultas 3, 7 y 8, 9 no reciben input
        if not data and query_type not in [3, 7, 8, 9]:
            return redirect(url_for('error',
                                    error_type='EmptyFieldError',
                                    message='Consulta con campo vacio'))

        query_dict = {"query_type": query_type,
                      'data': data}

    # recibir lo que sea del backend
    result_dict = q.get_query_result(query_dict)

    # if error 0, irnos a la pestalla de error y enviar esos datos
    if result_dict['result'] == 0:
        # TODO: retornar error
        return redirect(url_for('error',
                                error_type=result_dict['error_type'],
                                message=result_dict['error']))
    else:
        # y entregarselo al template para mostrar la tabla
        return render_template('result.html',
                               result=result_dict)


@app.route('/error')
def error():
    """
    Funcion para mostrar un mensaje de error
    """
    error_type = request.args.get('error_type')
    message = request.args.get('message')

    err = {
        'error_type': error_type,
        'message': message
    }

    return render_template('error.html', err=err)


if __name__ == '__main__':
    app.run(debug=True)
