import streamlit as st
from funciones.mate import *
from sympy import *
from funciones.plot import plotcurve, plotcrit
from funciones.gif_show import show_gif
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from funciones.mate import eq_tangente, max_speed

def cargar():
    st.header("SImula tu curva")
    # Inicial
    x_0 = 300
    y_0 = 1100

    # Inflexión
    x1 = st.slider('Punto medio x: ', min_value=-2000, max_value=2000, step=100, value=800)
    y1 = st.slider('Punto medio y: ', min_value=-2000, max_value=2000, step=100, value=1400)

    # Crítico
    x2 = st.slider('Curva critica x: ', min_value=-2000, max_value=2000, step=100, value=1400)
    y2 = st.slider('Curva critica y: ', min_value=2000, max_value=5000, step=100, value=3500)

    speed = st.slider('Velocidad al curvar: ', min_value=60, max_value=350, step=10, value=120)
    # Final
    x_f = 1800
    y_f = 1200

    r_crit = 50

    x = np.array([x_0,x1,x2,x_f])
    y = np.array([y_0,y1,y2,y_f])
    z = np.polyfit(x,y,3)
    f = np.poly1d(z)

    a = z[0]
    b = z[1]
    c = z[2]
    d = z[3]

    xi = Symbol('xi')
    fa = a*xi**3+b*xi**2+c*xi+d
    diff1 = fa.diff(xi)

    x_1 = np.arange(x_0, x_f, 1)
    y_1 = f(x_1)
    
    st.write(f"{a}x^3 + {b}x^2 + {c}x + {d}")

    fig1 = plotcurve(x_1,y_1,x_0,x_f,y2)

    st.pyplot(fig1)

    length = get_length(xi, fa, x_0, x_f)


    x_minmax = np.linspace(x_0, x_f, 10000)
    y_minmax = f(x_minmax)
    min_, max_ = find_minmax(x_minmax, y_minmax)
    xmin = min_[0]
    xmax = max_[0]


    r1 = get_radius(xi, fa, x_1)

    crit_index1 = np.where(r1 <= r_crit)

    xcurve1 = np.array([x_1[i] for i in crit_index1])
    rcrit = np.array([r1[i] for i in crit_index1])
    ycurve1 = np.array([y_1[i] for i in crit_index1])

    xcurve1 = xcurve1.flatten()
    rcrit = rcrit.flatten()
    ycurve1 = ycurve1.flatten()

    fig, ax = plt.subplots()
    ln, = plt.plot([], [], 'ro')

    x = np.linspace(x_0, x_f,100)
    y = f(x)

    st.write(max_speed(rcrit))
    
    def derrape(rlist, speed):
        i = 0
        for r in rlist:
            if speed > max_speed(r):
                i = np.where(rlist == r)
                return i, False
            else: 
                return i, True 

    b, no_derrapa = derrape(rcrit, speed)


    xi = Symbol('xi')
    tan = eq_tangente(fa, xi, xcurve1[b], ycurve1[b])
    x_tan = np.linspace(xcurve1[b], xcurve1[b]+300)
    y_tan = tan(x_tan)

    ax.plot(x, y,'k', linewidth='20')

    if no_derrapa == False:
        ax.plot(x_tan, y_tan, 'c', linewidth='10')

    def init():
        return ln,

    def update(frame):
        if no_derrapa:
            xdata = [frame]
            ydata = [f(frame)]

            ln.set_data(xdata, ydata)
            return ln,

        if frame < xcurve1[b]:
            xdata = [frame]
            ydata = [f(frame)]
        else:
            xdata = [frame]
            ydata = [tan(frame)]
        
        ln.set_data(xdata, ydata)

        return ln,
        
    ani = FuncAnimation(fig, update, frames=np.linspace(x_0, x_f, 60),init_func=init, blit=False)
    ani.save("bnimation1.gif", writer="imagemagik", fps=60)

cargar()
show_gif(1)


