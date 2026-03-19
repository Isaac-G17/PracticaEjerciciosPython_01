#Crear un diccionario con nombres de 5 productos y sus precios, luego mostrar el producto más caro.

productos = {
    "manzana": 500,
    "uva": 200,
    "pera": 300,
    "naranja": 400,
    "Melon": 800
}

print(f"El producto más caro es: {max(productos, key=productos.get)}")