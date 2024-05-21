import os
import csv


diccionario_data = {

    "calificacion": {
        "path": os.path.join('backend', 'data', 'calificacion.csv'),
        "encoding": "ascii"
    },

    "cldeldes": {
        "path": os.path.join('backend', 'data', 'cldeldes.csv'),
        "encoding": "ascii"
    },

    "clientes": {
        "path": os.path.join('backend', 'data', 'clientes.csv'),
        "encoding": "ascii"
    },

    "comuna": {
        "path": os.path.join('backend', 'data', 'comuna.csv'),
        "encoding": "mac_roman"
    },

    "pedidos": {
        "path": os.path.join('backend', 'data', 'pedidos.csv'),
        "encoding": "windows-1252"
    },

    "platos": {
        "path": os.path.join('backend', 'data', 'platos.csv'),
        "encoding": "utf-8"
    },

    "restaurantes": {
        "path": os.path.join('backend', 'data', 'restaurantes.csv'),
        "encoding": "mac_roman"
    },

    "suscripciones": {
        "path": os.path.join('backend', 'data', 'suscripciones.csv'),
        "encoding": "ascii"
    },


}


def get_data(file_name: str) -> list:
    lineas = []
    with open(diccionario_data[file_name]["path"], mode='r', encoding=diccionario_data[file_name]["encoding"]) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) # Saltar la fila de encabezado
        for fila in reader:
            lineas.append(fila)
    return lineas
