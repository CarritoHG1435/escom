from os import wait
from sys import exception

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy.printing import latex 
import secante
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


if metodo_seleccionado == 'Secante':
    
    st.title("Metodo de la secante con Steffenson")

    # Se hacen los campos para ingresar los datos

    entrada = st.text_input("Funcion:" , value="x**3 -  5 * x +2")
    a = st.number_input("Punto a:", value=3)
    b = st.number_input("Punto b:", value=3)
    i = st.number_input("Numero de iteraciones", value=5)

    # Se convierte la entrada a una funcion interpretable por el programa

    x = sp.Symbol('x')
    expr = sp.sympify(entrada)
    f = sp.lambdify(x, expr, "numpy")
    lat_text = sp.latex(expr) 

    # Se aplica secante
    
    try:

        df, resul = secante.secante(f, a, b, i)

        # Se hace el plot de la funcion

        x = np.linspace(-20, 20, 1000)
        y = f(x)


        fig, ax = plt.subplots()
        ax.plot(x,y)
        ax.scatter(a, f(a), label="Punto A")
        ax.scatter(b, f(b), label="Punto B")
        ax.scatter(resul, f(resul), label="Raiz")

        ax.plot(x, ((f(b) - f(a))/(b - a)) * (x - b) + f(b))

        ax.axhline(0, color="black", linewidth=1.2)
        ax.axvline(0, color="black", linewidth=1.2)

        ax.set_ylim(-15,15)
        ax.set_xlim(-5,5)


        ax.set_title(f"$f(x) = {sp.latex(expr)}$")
        ax.legend()

        # Se despliega el plot y la tabla de valores del metodo

        st.pyplot(fig)
        st.text(f"Resultado: {resul}")
        st.dataframe(df)
    except:
        st.text("Division entre 0, Verifica tus puntos o reduce tus iteraciones")

