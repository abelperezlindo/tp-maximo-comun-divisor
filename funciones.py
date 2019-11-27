# Descripción del algoritmo de Euclides
# Antes de comenzar a programar nuestro algoritmo, es necesario comprender como funciona.

# El algoritmo de Euclides dice que, con a y b como enteros positivos, y siendo siempre a > b:

# Se divide a ÷ b, obteniendo un residuo entero r1 y un cociente q1
# Se demuestra que a = q1· b + r1, por lo que ahora a = b y b = r1. Repetimos el primer paso, obteniendo
#  r2 y q2.
# Se repiten los pasos hasta que el residuo resultante sea igual a 0 (rn == 0), siendo el último residuo
# obtenido  antes del 0 (rn-1) el Máximo Comun Divisor de los números.
# de forma recursiva quedaria de la siguiente forma
# def mcd_recur(a, b):
#     if b == 0:
#         return a
#     return mcd_recur(b, a % b)
import itertools


def mcd(a, b): return a if b == 0 else mcd(b, a % b)


def RestaSucesivas(a, b):
    # el mayor - el menor sucesivamente teda el el cociente y el resto, 
    if a == b:
        return a
    if a > b:
        dividendo = a
        divisor = b
    else:
        dividendo = b
        divisor = a
        
    resto = dividendo
    while resto > divisor:
        resto = resto - divisor
    return RestaSucesivas(resto, divisor) # si entra a la recursividad el resto = divisor (es el mcd), o resto es menor al divisor (en este caso el resto se transforma en el divisor)


def divisorMasPeque(n):
    # devuelve el divisor no trivial más pequeño de n
    d = 2  # para empesar
    while n % d != 0:
        d = d+1
    return d


def factors(n):
    # retorna la factorizacion de n en primos en una lista
    if n == 1:
        return []  # empty list
    else:
        p = divisorMasPeque(n)
    return [p] + factors(n/p)


def mcdFactoresPrimos(a, b):
    # Esta funcion  Retorna MCD (a,b) usando la factorizacion de n en primos
    lista_a = factors(a)  # se genera una lista con los divisores primos  de a
    lista_b = factors(b)  # se genera una lista con los divisores primos  de b
    # se genera un conjunto con los divisores de a sacando los repetidos
    conjunto_a = set(lista_a)
    # se genera un conjunto con los divisores de b sacando los repetidos
    conjunto_b = set(lista_b)
    # inteseccion entre los dos conjuntos
    result = conjunto_a.intersection(conjunto_b)
    if len(result) == 0:
        return 1  # a y b son coprimos
    if len(result) > 0:
        mcd = 1
        for x in range(len(result)):
            aux = result.pop()  # obtenemos un elemento de la interseccion
            # obtenemos el exponente de este elemento
            exponente = min(lista_a.count(aux), lista_b.count(aux))
            mcd = mcd * (aux ** exponente)
        return mcd
