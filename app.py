from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# TODO: hacer el diccionario de tapos
# TODO: hacer cada una de las consultas
data = ["daniel", "gonzalo", "nico", "amogus"]

example_data = {
    "labels": ["Name", "Age", "Country", "Height"],
    "rows": [
        ["Daniel", 21, "Chile", 125],
        ["Gonzalo", 22, "Chile", 143],
        ["Nico", 23, "Chile", 134],
        ["Amogus", 24, "Chile", 134],
    ]
}


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
    return render_template('menu_consultas.html', data=data)


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

    # FIXME: example data deberia ser extraido desde procesar()
    return render_template('result.html', data=data, result=example_data)


if __name__ == '__main__':
    app.run(debug=True)
