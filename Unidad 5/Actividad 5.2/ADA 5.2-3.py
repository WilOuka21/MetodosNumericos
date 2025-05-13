import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la tabla de diferencias divididas de Newton
def newton_divided_diff(x, y):
    n = len(x)
    coef = np.zeros([n, n])  # Matriz de coeficientes
    coef[:, 0] = y  # Primera columna con los valores de y

    # Rellenar la tabla de diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i+1, j-1] - coef[i, j-1]) / (x[i+j] - x[i])

    return coef[0, :]  # Retorna los coeficientes del polinomio

# Función para evaluar el polinomio de Newton en puntos dados
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

# ============================
# Datos del ejercicio 3
# ============================
V = np.array([10, 20, 30, 40, 50, 60])         # Velocidad (m/s)
Cd = np.array([0.32, 0.30, 0.28, 0.27, 0.26, 0.25])  # Coeficiente de arrastre

# Estimar el Cd para una velocidad de 35 m/s
velocidad_objetivo = 35
Cd_estimado = newton_interpolation(V, Cd, np.array([velocidad_objetivo]))[0]

# ============================
# Graficar resultados
# ============================
x_vals = np.linspace(min(V), max(V), 200)  # Puntos para graficar la interpolación
y_vals = newton_interpolation(V, Cd, x_vals)

plt.figure(figsize=(8, 6))
plt.plot(V, Cd, 'ro', label='Datos experimentales')
plt.plot(x_vals, y_vals, 'b-', label='Interpolación de Newton')
plt.axvline(x=velocidad_objetivo, color='g', linestyle='--',
            label=f'Cd a {velocidad_objetivo} m/s ≈ {Cd_estimado:.4f}')
plt.xlabel('Velocidad del aire (m/s)')
plt.ylabel('Coeficiente de arrastre $C_d$')
plt.title('Estimación del coeficiente de arrastre con interpolación de Newton')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("interpolacion_arrastre.png")
plt.show()

# Imprimir el resultado numérico
print(f"El coeficiente de arrastre estimado para 35 m/s es: {Cd_estimado:.4f}")
