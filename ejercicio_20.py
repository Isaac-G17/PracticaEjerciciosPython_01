Edad = int(input("Por favor ingrese su edad ="))
Estrato = int(input("Por favor ingrese su estrato ="))

if Edad >= 18 and Edad <= 25 and (Estrato == 1 or Estrato == 2 or Estrato ==3):

    print("Aplica para el subsidio")
    
else:

    print("No aplica")