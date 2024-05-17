import re

def verificar_email(email):
    # Expresión regular mejorada para permitir letras y números en el TLD
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$'
    
    # Si toda la cadena coincide con la expresión regular, es un correo válido
    if re.fullmatch(regex, email):
        return True
    else:
        return False

# Pruebas
emails = [
    'gonzamatus5@gmail.com',   # Válido
    'usuario@dominio',         # Inválido
    'usuario@dominio.c',       # Inválido
    'usuario@dominio.com',     # Válido
    'usuario@dominio.c0m',     # Válido
    'user@sub.domain.co.uk',   # Válido
    'user@domain-xyz.com',     # Válido
    'user@domain..com',        # Inválido
    'user@domain.-com',        # Inválido
    'user@-domain.com',        # Inválido
    'user@domain.c_m',         # Inválido
]

for email in emails:
    print(f"'{email}': {verificar_email(email)}")
