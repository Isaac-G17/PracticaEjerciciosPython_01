Kilometros = int(input("Por favor ingrese los kilometros recorridos ="))
Minutos = int(input("Por favor ingrese el tiempo del recorrido en minutos ="))

if Minutos < 10:
    print("El valor a pagar es de 5000")

else: 
    Total = 800 * Kilometros
    print ("El valor a pagar es", Total)

    