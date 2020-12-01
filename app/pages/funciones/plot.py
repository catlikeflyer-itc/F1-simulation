import matplotlib.pyplot as plt
import numpy as np

def plotcurve(x, y, x_0, x_f, y_max):
    
    fig = plt.figure(figsize=(20,20))

    plt.plot(x, y, label="Forma de la curva")

    plt.grid()
    plt.title("Modelación de la curva con una función de tercer grado")

    plt.xlim([0,x_f+100])
    plt.ylim([0, y_max+100])

    return fig

def plotcrit(x, y, xcurve, ycurve, mini):
    fig2 = plt.figure(figsize=(10,10))

    plt.plot(x, y, label="Forma de la curva")
    plt.plot(xcurve, ycurve,'.', markersize=20)

    plt.grid()
    plt.title("Modelación de la curva con una función de tercer grado")

    plt.xlim([mini[0]-30, mini[0]+30])
    plt.ylim([mini[1]-30, mini[1]+30])

    return fig2

