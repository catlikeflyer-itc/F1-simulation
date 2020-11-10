import numpy as np

def integral_trapecios(f, a, b, N):
    delta = (b-a)/N
    x = np.arange(a, b+delta, delta)
    y = f(x)

    X = x+delta
    Y_diff = f(X)

    areas = delta*((Y_diff+y)/2)

    return sum(areas[:-1])

def integral_simpson(f,a,b,N):
    dx = (b-a)/N # Determinar delta x
    x = np.linspace(a,b,N+1) # Crear lista de marcadores en x
    y = f(x) # Obtener el valor de la funcion evaluada en cada valor de x

    '''
    Sumar con la regla 1-4-1
    El primer rango suma todos los valores con indice par del primero al penultimo (avanza de dos en dos hasta el penultimo)
    El segundo multiplica el valor de "y" en indices impares (avanza de dos en dos comenzando por el indice 1)
    El ultimo hace lo mismo que el primero solo que comienza desde el indice 2 y considera el ultimo valor
    '''
    return dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2]) ,

