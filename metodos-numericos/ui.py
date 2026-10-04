import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy.printing import latex 
import secante
import biseccion
import sympy as sp

st.sidebar.title("Menu")
metodo_seleccionado = st.sidebar.radio(
    "Selecciona un metodo:",
    ["Biseccion", "Secante", "Newton-Raphson"]
)

st.sidebar.divider()
st.sidebar.info("Metodos Numericos - ESCOM")
st.sidebar.text("Hernandez Carrillo Hugo")
st.sidebar.text("Legaria Mendoza Fernando")


# Se convierte la entrada a una funcion interpretable por el programa

entrada = st.text_input("Funcion:" , value="x**3 -  5 * x +2")
x = sp.Symbol('x')
expr = sp.sympify(entrada)
f = sp.lambdify(x, expr, "numpy")
lat_text = sp.latex(expr) 


x = np.linspace(-20, 20, 1000)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x,y, label='f(x)')
ax.set_ylim(-15,15)
ax.set_xlim(-5,5)
ax.axhline(0, color="black", linewidth=1.2)
ax.axvline(0, color="black", linewidth=1.2)
ax.set_title(f"$f(x) = {sp.latex(expr)}$")
ax.legend()

if metodo_seleccionado == 'Secante':
    
    st.title("Metodo de la secante")

    # Se hacen los campos para ingresar los datos

    a = st.number_input("Punto a:", value=2)
    b = st.number_input("Punto b:", value=3)
    i = st.number_input("Numero de iteraciones", value=5)
    df, resul = secante.secante(f, a, b, i)
    paso = st.number_input("Paso", 0, len(df) - 1)
    
    try:

        # Se hace el plot de la funcion


        a = df['p0'].iloc[paso]
        b = df['p1'].iloc[paso]
        c = df['p2'].iloc[paso]

        ax.scatter(resul, f(resul), label="Raiz")
        ax.scatter(a, f(a), label="Punto $P_0$")
        ax.scatter(b, f(b), label="Punto $P_1$")
        ax.scatter(c, 0, label = "Punto $P_2$")
        ax.plot(x, ((f(b) - f(a))/(b - a)) * (x - b) + f(b))


        # Se despliega el plot y la tabla de valores del metodoa
        ax.legend()
        st.pyplot(fig)
        st.text(f"Resultado: {resul}")
        st.dataframe(df)
    except:
        st.text("Division entre 0, Verifica tus puntos o reduce tus iteraciones")

if metodo_seleccionado == 'Biseccion':
    st.title("Metodo de biseccion")
    a = st.number_input("Punto a (Izquierda)", value=-2.0)
    b = st.number_input("Punto b (Derecha)", value=3.0)
    err_rel = st.number_input("Error relativo minimo", value=0.1)
    df, resul = biseccion.biseccion(a,b,f,err_rel)

    st.text(f"Resultado: {resul}")
    paso = st.number_input("Paso", 0, len(df)-1, value=0)

    a = df['a'].iloc[paso]
    b = df['b'].iloc[paso]

    ax.plot(np.full(len(x), a), x, label='a')
    ax.plot(np.full(len(x), b), x, label='b')
    ax.scatter(resul, 0, label='Raiz')

    ax.legend()
    st.pyplot(fig)
    st.dataframe(df)
    
