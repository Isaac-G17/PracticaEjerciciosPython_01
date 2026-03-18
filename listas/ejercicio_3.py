#Invertir el orden de una lista sin usar funciones propias del lenguaje
lista = [1,22,53,41,5,26,17,88,9,10,20]

inicio = 0
fin = len(lista) - 1

while inicio < fin:
    temp = lista[inicio]
    lista[inicio] = lista[fin]
    lista[fin] = temp

    inicio += 1
    fin -= 1

print(lista)