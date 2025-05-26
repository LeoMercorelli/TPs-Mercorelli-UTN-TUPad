'''
#EJERCICIO 1):
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Solicitar número al usuario
limite = int(input("Ingrese un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")
'''

'''
# EJERCICIO 2):s
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print()
'''

'''
# EJERCICIO 3):
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")
'''

'''
# EJERCICIO 4):
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número en base decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")
'''

'''
# EJERCICIO 5):
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()
print("Es palíndromo:", es_palindromo(texto))
'''

'''
# EJERCICIO 6):
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")
'''

'''
# EJERCICIO 7):
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(nivel_base)}")
'''

'''
# EJERCICIO 8):
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0-9): "))
print(f"Apariciones del dígito {dig}: {contar_digito(num, dig)}")
'''
