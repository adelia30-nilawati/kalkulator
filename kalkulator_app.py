import streamlit as st
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

st.title("🧮 Aplikasi Kalkulator Integral dan Turunan")

st.markdown("""
### 📌 Deskripsi
Sebuah kalkulator berbasis Python untuk menyelesaikan fungsi aljabar sederhana: integral dan turunan.

### ✨ Fitur:
- Input fungsi aljabar (dalam teks)
- Output: hasil integral atau turunan (simbolik dan numerik)
- Bonus: grafik kurva fungsi dan hasil turunan/integral
""")

# Input fungsi dari user
fungsi_str = st.text_input("Masukkan fungsi aljabar:", value="x**2 + 3*x + 2")

try:
    fungsi = sympify(fungsi_str)
    operasi = st.radio("Pilih operasi:", ["Turunan", "Integral"])

    if operasi == "Turunan":
        hasil = diff(fungsi, x)
        st.latex(f"f'(x) = {hasil}")
    else:
        hasil = integrate(fungsi, x)
        st.latex(r"\int f(x)\,dx = " + str(hasil))

    # Grafik
    x_vals = np.linspace(-10, 10, 400)
    fungsi_lambda = lambdify(x, fungsi, modules=['numpy'])
    hasil_lambda = lambdify(x, hasil, modules=['numpy'])

    y_vals = fungsi_lambda(x_vals)
    y_hasil_vals = hasil_lambda(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="f(x)")
    ax.plot(x_vals, y_hasil_vals, label="Hasil", linestyle='--')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    
