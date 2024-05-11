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
    return render_template('menu_consultas.html')


@app.route('/consulta_inestruct')
def consultas_inestruct():
    """
    Consultas Inestructuradas
    """
    return render_template('consultas_inestruct.html')


@app.route('/procesar', methods=['POST'])
def procesar():
    """
    Funcion para procesar los inputs raw del usuario de las consultas inestructuradas
    """
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']

    print("Preprocesamiento de raw text")
    print(f'SELECT {text1}')
    print(f'FROM {text2}')
    print(f'WHERE {text3}')

    # TODO: verificar que text1 y text2 sean no nulos
    # enviar a una pagina de error o reiniciar el formulario con un mensaje que se yo

    # enviamos estos argumentos a la funcion result, en la ruta /resultado, y ejecutarla
    return redirect(url_for('result', text1=text1, text2=text2, text3=text3))


@app.route('/result_query')
def result():
    """
    La funcion para mostrar el resultado de la consulta
    """
    # los inputs deberian estar "limpios" en este punto
    texto1 = request.args.get('text1')
    texto2 = request.args.get('text2')
    texto3 = request.args.get('text3')
    data = [texto1, texto2, texto3]

    # enviarselos al backend

    # recibir lo que sea del backend

    # y entregarselo al template para mostrar la tabla

    # TODO: hacer la tabla con la libreria del js
    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
