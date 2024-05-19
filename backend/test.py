import chardet

# Detect encoding
with open('data/restaurantes.csv', 'rb') as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
encoding = result['encoding']
confidence = result['confidence']

print(f"Detected encoding: {encoding} with confidence {confidence}")
