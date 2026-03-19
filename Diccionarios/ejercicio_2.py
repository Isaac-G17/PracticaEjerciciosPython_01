# Dado un diccionario de estudiantes y sus notas, calcular el promedio general.

notas = {
    "Isaac": [2,4,5,4],
    "Humberto": [2,2,5,5,5],
    "Caleb": [5,4,4,3]
}

# Suma el total de elementos dentro del diccionario
numero_notas = sum(len(lista) for lista in notas.values())

# Suma el total de notas dentro del diccionario
total_notas = sum(sum(lista) for lista in notas.values())

# Calcula el promedio general de los estudiantes
promedio_general = total_notas / numero_notas

print(total_notas)

# Muestra el promedio general de los estudiantes
print(f"El promedio general de los estudiantes es: {promedio_general}")