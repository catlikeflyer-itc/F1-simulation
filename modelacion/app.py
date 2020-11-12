import streamlit as st

a = st.slider('Factor a', -100, 100, 5)
b = st.slider('Factor b', -100, 100, 5)
c = st.slider('Factor c', -100, 100, 5)

xi = st.slider('Punto inicial x', -100, 100, 5)
yi = st.slider('Punto inicial y', -100, 100, 5)

f = lambda x: a*(x-xi)**3+b*(x-xi)**2+c*(x-xi)+yi

x = np.linspace(xi, xi+100, 1000)
y = f(x)

plt.