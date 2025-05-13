import numpy as np
import matplotlib.pyplot as plt

# Función para calcular diferencias divididas de Newton
def newton_divided_diff(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i+1, j-1] - coef[i, j-1]) / (x[i+j] - x[i])
    return coef[0, :]

# Función para evaluar el polinomio de Newton en varios puntos
def newton_interpolation(x_data, y_data, x_vals):
    coef = newton_divided_diff(x_data, y_data)
    n = len(x_data)
    y_interp = np.zeros_like(x_vals)
    for i in range(len(x_vals)):
        term = coef[0]
        product = 1
        for j in range(1, n):
            product *= (x_vals[i] - x_data[j-1])
            term += coef[j] * product
        y_interp[i] = term
    return y_interp

# Datos experimentales: fuerza (N) y deformación (mm)
F_data = np.array([50, 100, 150, 200])
epsilon_data = np.array([0.12, 0.35, 0.65, 1.05])

# Estimación para F = 125 N
F_interp_vals = np.linspace(min(F_data), max(F_data), 200)
epsilon_interp_vals = newton_interpolation(F_data, epsilon_data, F_interp_vals)
epsilon_125 = newton_interpolation(F_data, epsilon_data, np.array([125]))[0]

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(F_data, epsilon_data, 'ro', label='Datos experimentales')
plt.plot(F_interp_vals, epsilon_interp_vals, 'b-', label='Interpolación de Newton')
plt.axvline(x=125, color='g', linestyle='--', label=f'Estimación para F=125 N: {epsilon_125:.3f} mm')
plt.xlabel('Fuerza (N)')
plt.ylabel('Deformación (mm)')
plt.title('Interpolación de Newton - Deformación del material')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("deformacion_material.png")
plt.show()

# Imprimir el valor estimado
print(f"Deformación estimada para 125 N: {epsilon_125:.3f} mm")
