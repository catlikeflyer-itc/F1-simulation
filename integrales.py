import numpy as np

f = lambda x: x**2 # Función que define la ecuación
a = 0 # Límite inferior
b = 5 # Límite superior
delta = 0.0001 # Delta

# Calcula el área bajo la curva sumando los rectángulos y triángulos
def integral_ineficiente(a, b, delta, f):
    x = np.arange(a, b+delta, delta)
    y = f(x)

    area_rect = sum(y[:-1]*delta) 

    X = x+delta
    Y_diff = (f(X)-y)

    area_tri = sum((Y_diff*delta)/2)

    area_total = area_rect + area_tri

    return area_total

# Calcula el área bajo la curva utilizando el trapecio formado
def integral_trapecios(a, b, delta, f):
    x = np.arange(a, b+delta, delta)
    y = f(x)

    X = x+delta
    Y_diff = f(X)

    areas = delta*((Y_diff+y)/2)

    return sum(areas[:-1])

print(integral_ineficiente(a,b,delta,f))
print(integral_trapecios(a,b,delta,f))









