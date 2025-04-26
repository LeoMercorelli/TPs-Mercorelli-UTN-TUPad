'''
#EJERCICIO 1):
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
'''

'''
# EJERCICIO 2):
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
'''

'''
# EJERCICIO 3):
numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")
'''

'''
# EJERCICIO 4):
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Ninio/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
'''

'''
# EJERCICIO 5):
contrasena = input("Ingrese una contrasenia (entre 8 y 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contrasenia correcta")
else:
    print("Por favor, ingrese una contrasenia de entre 8 y 14 caracteres")
'''

'''
# EJERCICIO 6):
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")
'''

'''
# EJERCICIO 7):
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)
'''

'''
# EJERCICIO 8):
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1: Todo mayusculas, 2: Todo minusculas, 3: Primera letra mayuscula")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opcion invalida")
'''

'''
# EJERCICIO 9):
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa danios)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar danios significativos)")
else:
    print("Extremo (puede causar graves danios a gran escala)")
'''

'''
# EJERCICIO 10):
dia = int(input("Ingrese el dia (1 al 31): "))
mes = int(input("Ingrese el mes (1 al 12): "))
hemisferio = input("Ingrese el la letra del hemisferio (N o S): ").upper()

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otonio"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otonio"
    estacion_sur = "Primavera"
else:
    print("Fecha invalida.")
    exit()

if hemisferio == "N":
    print(f"Usted esta en {estacion_norte}")
elif hemisferio == "S":
    print(f"Usted esta en {estacion_sur}")
else:
    print("Hemisferio invalido.")
'''