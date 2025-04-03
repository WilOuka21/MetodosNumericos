import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral, x, fx

# Parámetros de integración
a, b = 0.1, 0.3  # Intervalo
k = 200  # Constante del resorte

def funcion(x):
    return k * x

# Valores de n a evaluar
n_values = [6, 10, 20, 30]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, n in enumerate(n_values):
    try:
        resultado, x_points, y_points = simpson_rule(funcion, a, b, n)
        
        x_vals = np.linspace(a, b, 100)
        y_vals = funcion(x_vals)
        
        axes[i].plot(x_vals, y_vals, label=r"$f(x) = kx$", color="blue")
        axes[i].fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
        axes[i].scatter(x_points, y_points, color="red", label="Puntos de interpolación")
        axes[i].set_title(f"Aproximación con n={n}, Integral={resultado:.4f}")
        axes[i].set_xlabel("x")
        axes[i].set_ylabel("f(x)")
        axes[i].legend()
        axes[i].grid()
    except ValueError as e:
        print(f"Error con n={n}: {e}")

plt.tight_layout()
plt.show()
