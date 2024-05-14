# Como ejecutar

1. Descargar las dependencias de python que estan en `requirements.txt`
    - para no confundir con las que cada uno tenga instalada, usar con un environment `.venv`, creo qu el vscode la puede crear automaticamente 
    - si es que van metiendo mas dependencias, agregar con `pip freeze > requirements.txt`

2. `python3 app.py`

# Fomato para entregar al frontend
```python
example_data = {
    "labels": ["Name", "Age", "Country"],
    "rows": [
        ["Daniel", 21, "Chile"],
        ["Gonzalo", 22, "Chile"],
        ["Nico", 23, "Chile"],
        ["Amogus", 24, "Chile"],
    ]
}
```
