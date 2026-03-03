Sueldo = int(input("Por favor ingrese su sueldo mensual ="))

if Sueldo >= 1500000 and Sueldo <= 3000000:
    
    Impuesto = Sueldo * 0.05
    print("Los impuestos a pagar son", Impuesto)
    print("Su sueldo neto es", Sueldo)

elif Sueldo > 3000000:

    Impuesto = Sueldo * 0.10
    print("Los impuestos a pagar son", Impuesto)
    print("Su sueldo neto es", Sueldo)

else: 
    print ("No debe pagar impuestos")
