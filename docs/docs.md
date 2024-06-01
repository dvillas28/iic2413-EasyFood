# Documentación
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
