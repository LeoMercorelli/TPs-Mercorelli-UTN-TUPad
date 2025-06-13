'''
#EJERCICIO 1):
# Creamos una lista con números del 4 al 100, de 4 en 4
multiplos_de_4 = list(range(4, 101, 4))

# Mostramos la lista
print(multiplos_de_4)
'''

'''
# EJERCICIO 2):
# Creamos una lista con 5 elementos
elementos = ["manzana", "banana", "naranja", "uva", "sandia"]

# Mostramos el penultimo elemento
print(elementos[-2])
'''

'''
# EJERCICIO 3):
# Creamos una lista vacia
lista_vacia = []

# Agregamos tres palabras
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")

# Mostramos la lista
print(lista_vacia)
'''

'''
# EJERCICIO 4):
# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos los valores
animales[1] = "loro"
animales[-1] = "oso"

# Mostramos la lista
print(animales)
'''

'''
# EJERCICIO 5):
El programa crea una lista de numeros, elimina el valor maximo de esa lista usando remove(max(lista)) y luego imprime la lista resultante.
En este caso, borra el 22 porque era el mayor.
'''

'''
# EJERCICIO 6):
# Creamos la lista
numeros = list(range(10, 31, 5))

# Mostramos los dos primeros
print(numeros[:2])
'''

'''
# EJERCICIO 7):
# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos los valores
autos[1] = "coupe"
autos[2] = "utilitario"

# Mostramos la lista
print(autos)
'''

'''
# EJERCICIO 8):
# Lista vacia
dobles = []

# Agregamos los valores
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Mostramos la lista
print(dobles)
'''

'''
# EJERCICIO 9):
# Lista original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# Mostramos la lista final
print(compras)
'''

'''
# EJERCICIO 10):
# Creamos la lista anidada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

# Mostramos la lista
print(lista_anidada)
'''