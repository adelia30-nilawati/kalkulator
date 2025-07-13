from sympy import symbols, diff, integrate, sympify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

# Input fungsi dari user
fungsi_str = input("Masukkan fungsi aljabar (misal: x**2 + 3*x + 2): ")
fungsi = sympify(fungsi_str)

# Operasi
pilihan = input("Ketik 'd' untuk turunan atau 'i' untuk integral: ")

if pilihan == 'd':
    hasil = diff(fungsi, x)
    print(f"Turunan: {hasil}")
elif pilihan == 'i':
    hasil = integrate(fungsi, x)
    print(f"Integral: {hasil}")

# Plot grafik
x_vals = np.linspace(-10, 10, 400)
fungsi_lambda = lambdify(x, fungsi, modules=['numpy'])
y_vals = fungsi_lambda(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')

if pilihan == 'd':
    turunan_lambda = lambdify(x, hasil, modules=['numpy'])
    plt.plot(x_vals, turunan_lambda(x_vals), label="f'(x)", linestyle='--')
plt.title("Grafik Fungsi dan Turunan/Integral")
plt.legend()
plt.grid(True)
plt.show()

