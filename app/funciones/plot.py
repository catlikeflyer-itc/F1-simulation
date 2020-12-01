import matplotlib.pyplot as plt
import numpy as np

def plotcurve(x, y, x_0, x_f, y_max):
    
    fig = plt.figure(figsize=(20,20))

    plt.plot(x, y, label="Sin Resistencia de Aire")

    plt.grid()
    plt.title("Trayectoria sin resistencia de aire")

    plt.xlim([0,x_f+100])
    plt.ylim([0, y_max+100])

    return fig

def plotcrit(fig, xcurve, ycurve):
    fig2 = fig
    plt.plot(xcurve, ycurve,'.')

    return fig2

