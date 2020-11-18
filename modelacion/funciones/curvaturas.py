import numpy as np
from sympy import *

xp = Symbol('xp')
f = -0.000004702*xp**3+0.01412*xp**2-11.4*xp+3375


def first_diff(x, f, x_point):
    f_prima = f.diff(x)
    f_prima = lambdify(x, f_prima)

    return f_prima(x_point)

def second_diff(x, f, x_point):
    f_prima = f.diff(x)
    f_biprima = f_prima.diff(x)
    f_biprima = lambdify(x, f_biprima)

    return f_biprima(x_point)

get_kappa = lambda x: (abs(second_diff(xp, f, x)))/((1+(first_diff(xp, f, x))**2)**(3/2))

def get_radius(point):
    k = get_kappa(point)

    return 1/k
    








    

