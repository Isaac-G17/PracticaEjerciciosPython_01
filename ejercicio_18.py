Ancho = int(input("Por favor ingrese el ancho de cuarto en metros ="))
Largo = int(input("Por favor ingrese el largo de cuarto en metros ="))

Area = Ancho * Largo 

if Area < 12:
    print("El cuarto es pequeño")

elif Area >= 12 and Area <= 20:
    print ("El cuarto es mediano")

else:
    print("El cuarto es grande")