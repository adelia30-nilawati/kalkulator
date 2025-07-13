import streamlit as st
from sympy import symbols, diff, integrate, sympify, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')

st.title("🧮 Kalkulator Turunan & Integral + Grafik")

fungsi_str = st.text_input("Masukkan fungsi aljabar (misal: x**2 + 3*x + 2):", "x**2 + 3*x + 2")
try:
    fungsi = sympify(fungsi_str)

    operasi = st.radio("Pilih operasi:", ['Turunan', 'Integral'])

    if operasi == 'Turunan':
        hasil = diff(fungsi, x)
        st.latex(r"f'(x) = " + str(hasil))
    else:
        hasil = integrate(fungsi, x)
        st.latex(r"\int f(x)\,dx = " + str(hasil))

    # Plot
    x_vals = np.linspace(-10, 10, 400)
    fungsi_lambda = lambdify(x, fungsi, modules=['numpy'])
    hasil_lambda = lambdify(x, hasil, modules=['numpy'])

    y_vals = fungsi_lambda(x_vals)
    y_hasil_vals = hasil_lambda(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.plot(x_vals, y_hasil_vals, label="Hasil", linestyle='--')
    ax.set_title("Grafik Fungsi dan Hasil Operasi")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
except Exception as e:
    st.error(f"Terjadi error: {e}")
    
