N1 = int(input("Por favor ingrese su primer número ="))
N2 = int(input("Por favor ingrese su segundo número ="))

if N1 > N2:
    print("Este es el número mayor", N1)
elif N2 > N1:
    print("Este es el número mayor", N2)
else:
    print("Los dos números son iguales")