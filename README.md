# EasyFood

## Instrucciones ejecución Cargadores

Al momento de la entrega del proyecto, la base de datos se encuentra poblada con los datos que se entregaron al inicio de esta. Para demostrar el funcionamiento de la carga de datos, se encuentran los siguentes scripts, que tienen que ser ejecutados desde la ruta  `/home/grupo15/EasyFood`.

1. Ejecutar el siguente script 

    ```bash
    python3 backend/clear_tables.py
    ```

    Y luego elegir la opcion `c` y luego `y`. Esta opcion borra toda la informacion de todas las tablas de la base de datos. Todas las tablas quedan vacias.

2. Ejecutar el siguente script

    ```
    python3 backend/run_all_cargadores.py
    ```

    Este script toma carga todos los archivos `.csv` ubicados en el directorio `/backend/data` y ejecuta los cargadores para poblar con datos a todas las tablas de la base de datos.

Si el ayudante tiene que cargar nuevos datos para corregir la entrega, es cosa de reemplazar los viejos por los nuevos en el directorio `backend/data`, limpiar las tablas (paso 1.) y ejecutar los cargadores de nuevo (paso 2.).


## Instrucciones ejecución Pagina Web

Colocarse en la ruta `/home/grupo15/EasyFood` y ejecutar el siguente comando en la terminal para activar el ambiente de Python

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
