import numpy as np
from sympy import *

def simpson(f,a,b,N):
    if N%2 == 1:
        print("N tiene que ser par")

    delta = (b-a)/N # Determinar delta x
    x = np.linspace(a,b,N+1) # Crear lista de marcadores en x
    y = f(x) # Obtener el valor de la funcion evaluada en cada valor de x

    '''
    Sumar con la regla 1-4-1
    El primer rango suma todos los valores con indice par del primero al penultimo (avanza de dos en dos hasta el penultimo)
    El segundo multiplica el valor de "y" en indices impares (avanza de dos en dos comenzando por el indice 1)
    El ultimo hace lo mismo que el primero solo que comienza desde el indice 2 y considera el ultimo valor
    '''
    suma = delta/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

    return suma

def first_diff(x, f, x_point):
    f_prima = f.diff(x)
    f_prima = lambdify(x, f_prima)

    return f_prima(x_point)

def second_diff(x, f, x_point):
    f_prima = f.diff(x)
    f_biprima = f_prima.diff(x)
    f_biprima = lambdify(x, f_biprima)

    return f_biprima(x_point)

get_kappa = lambda x: (abs(second_diff(xs, f, x)))/((1+(first_diff(xs, f, x))**2)**(3/2))

def get_radius(xs, f, point):
    get_kappa = lambda x: (abs(second_diff(xs, f, x)))/((1+(first_diff(xs, f, x))**2)**(3/2))
    k = get_kappa(point)

    return 1/k

def get_length(xs, f, a, b):
    f_prima = f.diff(xs)
    f_prima = lambdify(xs, f_prima)

    f_2_int = lambda x: np.sqrt(1+(f_prima(x))**2)

    return simpson(f_2_int, a, b, 10000)

def find_minmax(x, f_x):
    ymin = min(f_x)
    xmin = x[np.where(f_x == ymin)]
    xmin = xmin[0]

    ymax = max(f_x)
    xmax = x[np.where(f_x == ymax)]
    xmax = xmax[0]

    return [[xmin, ymin], [xmax, ymax]]


def eq_tangente(f, symbol, xpoint, ypoint):
    m = first_diff(symbol,f,xpoint)
    f = lambda x: m*(x-xpoint)+ypoint
    return f

max_speed = lambda x: 3.6*np.sqrt(9.81*2.1*x)
    
    