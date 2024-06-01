# EasyFood

## Instrucciones ejecución Cargadores

Al momento de la entrega del proyecto, la base de datos se encuentra poblada con los datos que se entregaron al inicio de esta. Para demostrar el funcionamiento de la carga de datos, se encuentran los siguentes scripts, que tienen que ser ejecutados desde la ruta  `/home/grupo15/EasyFood`.

1. Ejecutar el siguente script 

    ```bash
    python3 backend/clear_or_destroy_tables.py
    ```

    Y luego elegir la opcion `c` y luego `y`. Esta opcion borra toda la informacion de todas las tablas de la base de datos. Todas las tablas quedan vacias.

2. Ejecutar el siguente script

    ```
    python3 backend/run_all_cargadores.py
    ```

    Este script toma carga todos los archivos .csv ubicados en el directorio /backend/data y ejecuta los cargadores para poblar con datos a todas las tablas.

Si el ayudante tiene que cargar nuevos datos para corregir la entrega, es cosa de reemplazar los viejos por los nuevos en el directorio `backend/data`, limpiar las tablas y ejecutar los cargadores de nuevo.


## Instrucciones ejecución Pagina Web

Colocarse en la ruta `/home/grupo15/EasyFood` y ejecutar el siguente comando en la terminal

```bash
source venv/bin/activate
```

y posteriormente

```bash
python3 app.py
```

A continuacion en la terminal aparecerá la URL donde se encuentra corriendo la aplicacion, esta es:

```bash
pavlov.ing.puc.cl:8015
```


## Documentación
### Instalación de dependencias

1. Descargar las dependencias de python que estan en `requirements.txt`
    - para no confundir con las que cada uno tenga instalada, usar con un environment `.venv`, creo que vscode la puede crear automaticamente 
    - si es que van metiendo mas dependencias, agregar con `pip freeze > requirements.txt`

2. `python3 app.py`

### Formato de que entrega el frontend
```python
# Consulta inestructurada
data = [text_select, text_from, text_where]

query_dict = {
    'query_type': 0,
    'SELECT': data[0],
    'FROM': data[1],
    'WHERE': data[2]
}

# Consulta estructurada
query_dict = {
    'query_type': int(1,10),
    'data': list[str]
}

```

### Fomato para entregar al frontend
```python
example_data = {
    "labels": ["Name", "Age", "Country"], # nombre de los atributos
    "rows": [ # tuplas/listas con los resultados
        ["Daniel", 21, "Chile"],
        ["Gonzalo", 22, "Chile"],
        ["Nico", 23, "Chile"],
        ["Amogus", 24, "Chile"],
    ]
}
```

### Formato para reportar errores
```python
err = {
    "error_type": {} # tipo del error (input nulo, falla de sintaxis de en la consulta),
    "message": {} # mensaje a mostrar del error

}
```
