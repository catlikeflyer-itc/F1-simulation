import streamlit as st
from funciones.mate import *
from sympy import *
from funciones.plot import plotcurve, plotcrit

'''
Variables a usar
'''
# Inicial
x_0 = 300
y_0 = 1100

# Inflexión
x1 = st.slider('Punto medio x: ', min_value=-2000, max_value=2000, step=100, value=800)
y1 = st.slider('Punto medio y: ', min_value=-2000, max_value=2000, step=100, value=1400)

# Crítico
x2 = st.slider('Curva critica x: ', min_value=-2000, max_value=2000, step=100, value=1400)
y2 = st.slider('Curva critica y: ', min_value=2000, max_value=5000, step=100, value=3500)

# Final
x_f = 1800
y_f = 1200

r_crit = 50

'''
Generacion de funcion y sus constantes
'''
x = np.array([x_0,x1,x2,x_f])
y = np.array([y_0,y1,y2,y_f])
z = np.polyfit(x,y,3)
f = np.poly1d(z)
print(f)
print(z)

a = z[0]
b = z[1]
c = z[2]
d = z[3]

xi = Symbol('xi')
fa = a*xi**3+b*xi**2+c*xi+d
diff1 = fa.diff(xi)

x_1 = np.arange(x_0, x_f, 1)
y_1 = f(x_1)

'''
Generacion de grafica
'''
fig1 = plotcurve(x_1,y_1,x_0,x_f,y2)

st.pyplot(fig1)


'''
Longitud de la curva
'''
length = get_length(xi, fa, x_0, x_f)
print(length, "metros")

'''
Minimo y maximo
'''
x_minmax = np.linspace(x_0, x_f, 10000)
y_minmax = f(x_minmax)
min_, max_ = find_minmax(x_minmax, y_minmax)
xmin = min_[0]
xmax = max_[0]

'''
Zonas criticas
'''


r1 = get_radius(xi, fa, x_1)

crit_index1 = np.where(r1 <= r_crit)

xcurve1 = np.array([x_1[i] for i in crit_index1])


rcrit = min(np.array([r1[i] for i in crit_index1]))
ycurve1 = np.array([y_1[i] for i in crit_index1])

print(xcurve1)
print(rcrit)

'''
Graficas zonas criticas
'''
fig2 = plotcrit(fig1, xcurve1, ycurve1)

st.pyplot(fig2)