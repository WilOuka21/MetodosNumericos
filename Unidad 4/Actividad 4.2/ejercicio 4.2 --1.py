import numpy as np
import matplotlib.pyplot as plt

# Definir la función a integrar
def f(x):
    return x**2 + 3*x + 1

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n_values = [10, 20, 50]  # Subdivisiones

# Solución exacta de la integral
exact_integral = (2**3 / 3) + (3 * 2**2 / 2) + (2 * 1) - (0)

# Configuración de la figura con subgráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 5))  # 1 fila, 3 columnas

print("n\tAprox\t\tError")
for i, n in enumerate(n_values):
    integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)
    error = abs(exact_integral - integral_approx)
    print(f"{n}\t{integral_approx:.6f}\t{error:.6e}")

    # Graficar la función y la aproximación con trapecios en el subplot correspondiente
    x_fine = np.linspace(a, b, 100)
    y_fine = f(x_fine)

    ax = axes[i]
    ax.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x^2 + 3x + 1$', linewidth=2)
    ax.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
    ax.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")

    # Etiquetas y título
    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.set_title(f"Aproximación con n = {n}")
    ax.legend()
    ax.grid()

# Ajustar el diseño para que no se solapen los títulos
plt.tight_layout()

# Mostrar todas las gráficas juntas
plt.show()
