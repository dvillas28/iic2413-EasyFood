import chardet
import os

# Detect encoding
ruta_relativa = os.path.join('backend','data','suscripciones.csv')
with open(ruta_relativa, 'rb') as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
encoding = result['encoding']
confidence = result['confidence']

print(f"Detected encoding: {encoding} with confidence {confidence}")
