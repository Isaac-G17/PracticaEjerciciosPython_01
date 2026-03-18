# Dada una lista de notas, calcular el promedio y mostrar si el estudiante aprueba (>= 3.0).

notas = []
total_notas = 0

#Entrada de datos para ingresar las notas del estudiante 
while True:
    try:
        nota = float(input("Ingrese su nota: "))
        print()

        print(f"La {nota} fue ingresada corretamente\n")

        notas.append(nota)

        continuar = input("¿Quiere ingresar otra nota? (Si/No): ").lower()

        print()
        
        if continuar != "si":
            print("----Calculando promedio----\n".upper())
            break  
    except ValueError:
        print("Error: Solo se permite ingresar números")
        continue

numero_de_notas = len(notas)

#Bucle para sumar el total de notas
for n in notas:
    total_notas += n

# Operacion para sacar el promedio de notas del estudiante
promedio = total_notas / numero_de_notas

# Condicional para saber si el estudiante aprobo o reprobo
if promedio >= 3.0:
    print(f"Sus notas fueron: {notas}\n")
    print(f"El estudiante aprobo con un promedio de {promedio}\n")

else:
    print(f"Sus notas fueron: {notas}\n")
    print(f"El estudiante reprobo con un promedio de {promedio}\n")

    
