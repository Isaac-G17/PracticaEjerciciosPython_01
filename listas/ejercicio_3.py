#Invertir el orden de una lista sin usar funciones propias del lenguaje
numeros = [1,22,53,41,5,26,17,88,9,10]

print(numeros)

for i in numeros:
    reversed_numbers = numeros[::-1]
    
print(reversed_numbers)