import os

conn_params = {
    "dbname": "grupo15e2",
    "user": "grupo15",
    "host": "pavlov.ing.puc.cl",
    "port": 5432,
    "password": "putobdd"
}


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
