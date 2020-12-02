from funciones.mate import *
from sympy import *
import streamlit as st
# Iniciales
x_0 = 300
y_0 = 1100

# Final
x_f = 1800
y_f = 1200

r_crit = 50

def get_tramo():
# Inflexión
    x1 = st.slider('Punto medio x: ', min_value=-2000, max_value=2000, step=100, value=800)
    y1 = st.slider('Punto medio y: ', min_value=-2000, max_value=2000, step=100, value=1400)

    # Crítico
    x2 = st.slider('Curva critica x: ', min_value=-2000, max_value=2000, step=100, value=1400)
    y2 = st.slider('Curva critica y: ', min_value=2000, max_value=5000, step=100, value=3500)

    x0 = np.array([x_0,x1,x2,x_f])
    y0 = np.array([y_0,y1,y2,y_f])
    z = np.polyfit(x0,y0,3)
    f = np.poly1d(z)

    return z, f

z, f = get_tramo()

a = z[0]
b = z[1]
c = z[2]
d = z[3]

xi = Symbol('xi')
f_para_derivar = a*xi**3+b*xi**2+c*xi+d
derivada = f_para_derivar.diff(xi)

x = np.arange(x_0, x_f, 1)
y = f(x)

length = get_length(xi, f_para_derivar, x_0, x_f)

min_, max_ = find_minmax(x, y)

xmin = min_[0]
xmax = max_[0]
ymin = min_[1]
ymax = max_[1]

r1 = get_radius(xi, f_para_derivar, x)
crit_index1 = np.where(r1 <= r_crit)

rcrit = min(np.array([r1[i] for i in crit_index1]))
ycurve1 = np.array(y[i] for i in crit_index1)
xcurve1 = np.array([x[i] for i in crit_index1])

print(x)
print(xcurve1)