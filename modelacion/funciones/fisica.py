import numpy as np
import matplotlib.pyplot as plt

def fuerza_recta(masa, aceleracion):
    return masa*aceleracion

def energia_cinetica(masa, velocidad):
    return 0.5*masa*velocidad**2

def momento(masa, velocidad):
    return masa*velocidad

def friccion(coef, masa):
    return coef*masa*9.81

def longitud_recta(x1,y1,x2,y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)

def centripeta(masa, vel, radio):
    return (m*v**2)/radio



# http://www.sc.ehu.es/sbweb/fisica/dinamica/circular/din_circular.htm

