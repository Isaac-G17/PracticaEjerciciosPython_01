# Contar cuántas veces aparece cada palabra en una frase usando un diccionario.

diccionario = {
    "frase": "¡Hola, mundo! Esta es una frase de ejemplo que se repite. Esta es una frase de ejemplo"
}

from collections import Counter
frecuencia = Counter(diccionario["frase"].split())
print(frecuencia)