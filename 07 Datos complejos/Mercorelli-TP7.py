'''
#EJERCICIO 1):
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Ejercicio 1:", precios_frutas)
'''

'''
# EJERCICIO 2):
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Ejercicio 2:", precios_frutas)
'''

'''
# EJERCICIO 3):
frutas_solas = list(precios_frutas.keys())
print("Ejercicio 3:", frutas_solas)
'''

'''
# EJERCICIO 4):
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese un nombre para consultar su numero: ")
if consulta in agenda:
    print(f"Numero de {consulta}: {agenda[consulta]}")
else:
    print("El nombre no esta en la agenda.")
'''

'''
# EJERCICIO 5):
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("Palabras unicas:", palabras_unicas)
print("Frecuencia de palabras:", contador)
'''

'''
# EJERCICIO 6):
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3)) //Expresion generadora
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")
'''

'''
# EJERCICIO 7):
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
'''

'''
# EJERCICIO 8):
stock = {}
producto = input("Ingrese el nombre del producto a consultar/agregar: ")
if producto in stock:
    cantidad = int(input("Cuantas unidades desea agregar? "))
    stock[producto] += cantidad
else:
    cantidad = int(input("Producto no existente. Ingrese cantidad inicial: "))
    stock[producto] = cantidad
print(f"Stock actualizado de {producto}: {stock[producto]}")
'''

'''
# EJERCICIO 9):
agenda_eventos = {("Lunes", "10:00"): "Reunion", ("Martes", "14:00"): "Clase"}
consulta_dia = input("Ingrese elida: ")
consulta_hora = input("Ingrese la hora: ")
evento = agenda_eventos.get((consulta_dia, consulta_hora), "No hay eventos programados.")
print("Evento:", evento)
'''

'''
# EJERCICIO 10):
paises = {"Argentina": "Buenos Aires", "Francia": "Paris", "Japon": "Tokio"}
capitales = {capital: pais for pais, capital in paises.items()} //Expresion generadora
print("Diccionario invertido:", capitales)
'''