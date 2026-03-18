#Eliminar los elementos duplicados de una lista y mostrar la nueva lista.

#Usando set() metodo eficiente pero no conserva el orden de la lista original.
numeros = [1,22,53,41,5,88,17,88,9,10] 
unicos = list(set(numeros))
print(unicos)

print()

#Usando dict.fromkeys() metodo eficiente y mantiene el ordern de la lista original.
numeros = [1,22,53,41,5,88,17,88,9,10] 
unicos = list(dict.fromkeys(numeros))
print(unicos)

