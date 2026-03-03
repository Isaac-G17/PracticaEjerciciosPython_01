Precio = int(input("Por favor ingrese el precio de su producto ="))

if Precio > 100000:
    Descuento = Precio * 0.10
    Total = Precio + Descuento
    print("El total a pagar es", Total)
else:
    print ("El total a pagar es",Precio)

