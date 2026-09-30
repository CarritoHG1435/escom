import numpy as np
from math import factorial
import math

f = lambda x : x ** 2 * np.sin(x)

def frac_div(x, init, fin):
    if init == fin:
        return f(x[init])
    else:
        return (frac_div(x, init + 1, fin) - frac_div(x, init, fin - 1)) / (x[fin] - x[init])

def binom(m,n):
    return math.gamma(m+1) / (math.gamma(m-n+1) * factorial(n))


# Polinomio interpolante con un arreglo de valores de x en un intervalo [a,b]
def interpolante(x, s):
    if(x[1] - x[0] != x[2] - x[1]):
        raise Exception('No se define una h fija')
    h = x[1] - x[0]
    suma = 0
    for i in range(len(x)):
        suma += h**i * frac_div(x, 0, i) * binom(s, i) * factorial(i)
    return suma

x = [-2,-1,0,1,2,3]

print(interpolante(x, 4.5))

    

