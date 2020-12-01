import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from curva import *
from funciones.mate import *

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

x = np.linspace(x_0, x_f,100)
y = f(x)
ax.plot(x, y,'k', linewidth='20')

def init():
    return ln,

def update(frame):
    xdata = [frame]
    ydata = [f(frame)]
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(x_0, x_f, 30),init_func=init, blit=True)

plt.show()