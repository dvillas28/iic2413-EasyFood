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
        "path": os.path.join('backend','data','calificacion.csv'),
        "enconding": "ascii"
    },

    "cldeldes": {
        "path": os.path.join('backend','data','cldeldes.csv'),
        "enconding": "ascii"
    },

    "clientes": {
        "path": os.path.join('backend','data','clientes.csv'),
        "enconding": "ascii"
    },

    "comuna": {
        "path": os.path.join('backend','data','comuna.csv'),
        "enconding": "mac_roman"
    },

    "pedidos": {
        "path": os.path.join('backend','data','pedidos.csv'),
        "enconding": "windows-1252"
    },

    "platos": {
        "path": os.path.join('backend','data','platos.csv'),
        "enconding": "utf-8"
    },

    "restaurantes": {
        "path": os.path.join('backend','data','restaurantes.csv'),
        "enconding": "mac_roman"
    },

    "suscripciones": {
        "path": os.path.join('backend','data','suscripciones.csv'),
        "enconding": "ascii"
    },


}
