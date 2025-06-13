import math

'''
#EJERCICIO 1):
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
'''

'''
# EJERCICIO 2):
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("\nIngrese su nombre: ")
print(saludar_usuario(nombre))
'''

'''
# EJERCICIO 3):
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
'''

'''
# EJERCICIO 4):
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("\nIngrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
'''

'''
# EJERCICIO 5):
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("\nIngrese una cantidad de segundos: "))
print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas")

'''

'''
# EJERCICIO 6):
def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)
'''

'''
# EJERCICIO 7):
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("\nIngrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {mult}\nDivisión: {div}")
'''

'''
# EJERCICIO 8):
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("\nIngrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")
'''

'''
# EJERCICIO 9):
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("\nIngrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
'''

'''
# EJERCICIO 10):
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("\nIngrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")

'''