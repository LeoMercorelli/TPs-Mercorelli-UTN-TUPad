'''
import random
from statistics import mode, median, mean

# EJERCICIO 1):
# Solicita la edad al usuario
edad = int(input("Ingresa tu edad: "))
# Verifica si el usuario es mayor de edad
if edad >= 18:
    print("Es mayor de edad")
'''

'''
# EJERCICIO 2):
# Solicita una nota al usuario
nota = float(input("Ingresa tu nota: "))
# Evalúa si la nota es aprobatoria o no
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
'''

'''
# EJERCICIO 3):
# Solicita un número entero al usuario
numero = int(input("Ingresa un número: "))
# Verifica si el número es par usando el operador módulo
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
'''

'''
# EJERCICIO 4):
# Solicita la edad del usuario y clasifica en diferentes rangos etarios
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
'''

'''
# EJERCICIO 5):
# Solicita una contraseña al usuario
contraseña = input("Ingresa tu contraseña: ")
# Verifica si la longitud de la contraseña está en el rango permitido
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
'''

'''
# EJERCICIO 6):
# Generar lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular moda, mediana y media
try:
    moda = mode(numeros_aleatorios)
except:
    moda = "No hay una sola moda"  # Manejar el caso en que no haya una moda única
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar tipo de sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Distribución atípica"

# Imprimir resultados
print(f"Lista de números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Tipo de sesgo: {sesgo}")
'''

'''
# EJERCICIO 7):
# Solicita una palabra o frase al usuario
texto = input("Ingresa una palabra o frase: ")
# Verifica si el último carácter es una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)
'''

'''
# EJERCICIO 8):
# Solicita un nombre al usuario
nombre = input("Ingresa tu nombre: ")
# Pide al usuario que elija cómo desea formatear su nombre
opcion = int(input("Elige una opción (1, 2 o 3):\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n"))

if opcion == 1:
    print(nombre.upper())  # Convierte el nombre a mayúsculas
elif opcion == 2:
    print(nombre.lower())  # Convierte el nombre a minúsculas
elif opcion == 3:
    print(nombre.title())  # Capitaliza la primera letra de cada palabra
else:
    print("Opción no válida")
'''

'''
# EJERCICIO 9):
# Solicita la magnitud de un terremoto al usuario
magnitud = float(input("Ingresa la magnitud del terremoto: "))
# Clasifica la magnitud en diferentes categorías
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
'''

'''
# EJERCICIO 10):
# Solicita al usuario el hemisferio, el mes y el día para determinar la estación
hemisferio = input("¿En qué hemisferio te encuentras (N/S)? ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == "N":
    # Determina la estación para el hemisferio norte
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and dia <= 20):
        print("Invierno")
    elif 3 <= mes <= 6 and dia <= 20:
        print("Primavera")
    elif 6 <= mes <= 9 and dia <= 20:
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    # Determina la estación para el hemisferio sur
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and dia <= 20):
        print("Verano")
    elif 3 <= mes <= 6 and dia <= 20:
        print("Otoño")
    elif 6 <= mes <= 9 and dia <= 20:
        print("Invierno")
    else:
        print("Primavera")
'''