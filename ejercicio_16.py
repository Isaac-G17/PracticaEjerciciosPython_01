Nota_1 = int(input("Por favor ingrese su primera nota ="))
Nota_2 = int(input("Por favor ingrese su segunda nota ="))
Nota_3 = int(input("Por favor ingrese su tercera nota ="))

Total_De_Notas = Nota_1 + Nota_2 + Nota_3

Promedio = Total_De_Notas / 3


if Promedio >= 60:
    print("El estudiante aprobó")

elif Promedio >= 55 and Promedio <= 59:
    print("Va a habilitación")

else:
    print("El estudiante reprobó")
