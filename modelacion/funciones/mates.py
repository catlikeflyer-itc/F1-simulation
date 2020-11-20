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

def find_minmax(x, f_x):
    ymin = min(f_x)
    xmin = x[np.where(f_x == ymin)]
    xmin = xmin[0]

    ymax = max(f_x)
    xmax = x[np.where(f_x == ymax)]
    xmax = xmax[0]

    return [xmin, ymin], [xmax, ymax]