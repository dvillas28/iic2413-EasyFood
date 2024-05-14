from flask import Flask, render_template, request, redirect, url_for

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
    Consultas Estructuradas
    """
    # TODO: solicitar los datos para colocar en los cuadros desplegables
    data = ['daniel', 'gonzalo', 'nico', 'amogus']  # ejemplo
    return render_template('menu_consultas.html', data=data)


@app.route('/consulta_inestruct')
def consultas_inestruct():
    """
    Consultas Inestructuradas
    """
    return render_template('consultas_inestruct.html')


@app.route('/procesar', methods=['POST'])
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


# TODO: hacer lo mismo para las consultas estructuradas
def process_estruct_query():
    """
    Funcion para procesar los inputs de las consultas estructuradas
    """
    # tomar el tipo de query y los campos
    # enviarselos a result(query_type, args*)
    pass


@app.route('/result_query')
def result():
    """
    La funcion para mostrar el resultado de la consulta
    """
    # obtener el tipo de la consulta 0: inestruc, 1: estruc
    query_type = int(request.args.get('query_type'))

    # TODO: si es una consulta inestrucurada, se crea el diccionario 0 se envia al back
    if query_type == 0:
        # los inputs deberian estar "limpios" en este punto
        texto1 = request.args.get('text1')
        texto2 = request.args.get('text2')
        texto3 = request.args.get('text3')

        inestruct_dict = {query_type: 0,
                          'SELECT': texto1,
                          'FROM': texto2,
                          'WHERE': texto3}

        # FIXME: esto es solo para mostrar de momento
        data = [texto1, texto2, texto3]

    # enviarselos al backend

    # recibir lo que sea del backend

    # formato para mostrar los datos en tabla
    example_data = {
        'labels': ['Name', 'Age', 'Country', 'Height'],
        'rows': [
            ['Daniel', 21, 'Chile', 125],
            ['Gonzalo', 22, 'Chile', 143],
            ['Nico', 23, 'Chile', 134],
            ['Amogus', 24, 'Chile', 134],
        ]
    }

    # y entregarselo al template para mostrar la tabla

    # if error 0, irnos a la pestalla de error y enviar esos datos

    return render_template('result.html', data=data, result=example_data)


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
