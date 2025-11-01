"""
Excepciones en Python
"""
try:
    print(10/0)  # Esto funciona bien
except Exception as e:
    print(f"Ha ocurrido un error: {e}")