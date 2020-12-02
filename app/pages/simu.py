import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import Symbol
from variables import x, y, f, f_para_derivar, x_0, x_f, xmin, ymin
from funciones.mate import eq_tangente

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

x = np.linspace(x_0, x_f,100)
y = f(x)

xi = Symbol('xi')
tan = eq_tangente(f_para_derivar, xi, xmin, ymin)
x_tan = np.linspace(xmin, xmin+300,60)
y_tan = tan(x_tan)

no_derrapa = False

ax.plot(x, y,'k', linewidth='20')
ax.plot(x_tan, y_tan, 'c', linewidth='10')

def init():
    return ln,

def update(frame):
    if no_derrapa:
        xdata = [frame]
        ydata = [f(frame)]

        ln.set_data(xdata, ydata)
        return ln,

    if frame < xmin:
        xdata = [frame]
        ydata = [f(frame)]
    else:
        xdata = [frame]
        ydata = [tan(frame)]
    
    ln.set_data(xdata, ydata)

    return ln,
    
ani = FuncAnimation(fig, update, frames=np.linspace(x_0, x_f, 30),init_func=init, blit=True)

#i = 2
#ani.save(f"bnimation/bnimation{i}.gif", writer="imagemagik", fps=60)
plt.show()