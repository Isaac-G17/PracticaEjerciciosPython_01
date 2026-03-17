#Dada una lista de números, contar cuántos son pares y cuántos impares.
numeros = [1,22,53,41,5,26,17,88,9,10]
pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}, números impares: {impares}")