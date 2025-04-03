import numpy as np
import matplotlib.pyplot as plt

# Definir la función y su derivada analítica
def f(x):
    return x**3 - 2*x**2 + x

def df_analytical(x):
    return 3*x**2 - 4*x + 1

# Métodos de diferencias finitas
def forward_diff(f, x, h=0.2):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h=0.2):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h=0.2):
    return (f(x + h) - f(x - h)) / (2*h)

# Rango de valores para evaluar
x_vals = np.arange(-1, 2 + 0.2, 0.2)  # Intervalo [-1, 2] con paso h=0.2
df_exact = df_analytical(x_vals)

# Aproximaciones numéricas
df_forward = forward_diff(f, x_vals)
df_backward = backward_diff(f, x_vals)
df_central = central_diff(f, x_vals)

# Errores absolutos
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Crear una figura con dos subgráficos
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# --- Primera gráfica: Comparación de derivadas ---
ax[0].plot(x_vals, f(x_vals), '-', label='Función f(x) = x^3 - 2x^2 + x')
ax[0].plot(x_vals, df_exact, 'k-', label='Derivada Analítica f\'(x) = 3x^2 - 4x + 1')
ax[0].plot(x_vals, df_forward, 'r--', label='Diferencias hacia adelante')
ax[0].plot(x_vals, df_backward, 'g-.', label='Diferencias hacia atrás')
ax[0].plot(x_vals, df_central, 'b:', label='Diferencias centradas')
ax[0].set_xlabel('x')
ax[0].set_ylabel("Derivada")
ax[0].legend()
ax[0].set_title("Comparación de Métodos de Diferenciación Numérica")
ax[0].grid()

# --- Segunda gráfica: Errores ---
ax[1].plot(x_vals, error_forward, 'r--', label='Error Hacia adelante')
ax[1].plot(x_vals, error_backward, 'g-.', label='Error Hacia atrás')
ax[1].plot(x_vals, error_central, 'b:', label='Error Centrada')
ax[1].set_xlabel('x')
ax[1].set_ylabel("Error absoluto")
ax[1].legend()
ax[1].set_title("Errores en Diferenciación Numérica")
ax[1].grid()

# Mostrar ambas gráficas en una sola ventana
plt.tight_layout()
plt.show()