import numpy as np

def get_slopes(f,a,b):
    x = np.arange(a,b, 10)
    y = f(x)

    slopelist = []

    for i in range(1,len(y)):
        # Calcula la nueva pendiente
        this_slope = (y[i]-y[i-1])/(x[i]-x[i-1])
        slopelist.append(this_slope)

    return slopelist

'''
Buscar desde que curvatura se considera una curva peligrosa. La diferencia de curvaturas se puede optener utilizadno el angulo entre
dos rectas tangentes consecutivas
'''

def get_anglediff(slopes):
    anglelist = []

    for i in range(1, len(slopes)):
        angle = np.arctan((slopes[i]-slopes[i-1])/(1+slopes[i]*slopes[i-1]))
        anglelist.append(angle)

    return anglelist


def get_tangents(f,a,b):
    slopes = get_slopes(f,a,b)
    angles = get_anglediff(slopes)

    return slopes, angles

