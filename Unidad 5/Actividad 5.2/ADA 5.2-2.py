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

# Datos experimentales: temperatura (°C) y eficiencia (%)
T_data = np.array([200, 250, 300, 350, 400])
eficiencia_data = np.array([30, 35, 40, 46, 53])

# Estimación para T = 275 °C
T_interp_vals = np.linspace(min(T_data), max(T_data), 200)
eficiencia_interp_vals = newton_interpolation(T_data, eficiencia_data, T_interp_vals)
eficiencia_275 = newton_interpolation(T_data, eficiencia_data, np.array([275]))[0]

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(T_data, eficiencia_data, 'ro', label='Datos experimentales')
plt.plot(T_interp_vals, eficiencia_interp_vals, 'b-', label='Interpolación de Newton')
plt.axvline(x=275, color='g', linestyle='--', label=f'Estimación para T=275 °C: {eficiencia_275:.3f} %')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Eficiencia (%)')
plt.title('Interpolación de Newton - Eficiencia del motor térmico')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("eficiencia_motor.png")
plt.show()

# Imprimir el valor estimado
print(f"Eficiencia estimada para 275 °C: {eficiencia_275:.3f} %")
