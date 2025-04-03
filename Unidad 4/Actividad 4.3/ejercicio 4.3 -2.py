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

# Parámetros de integración para el resorte
a, b = 0.1, 0.3  # Intervalo
k = 200  # Constante del resorte

def funcion_resorte(x):
    return k * x

# Parámetros de integración para el capacitor
C = 1e-6  # Capacitancia en Faradios
T = 5  # Tiempo en segundos

def funcion_capacitor(t):
    return 100 * np.exp(-2 * t)

# Valores de n a evaluar
n_values = [6, 10, 20, 30]

# Crear una figura con subgráficos para ambas funciones
fig, axes = plt.subplots(2, 4, figsize=(20, 10))  # 2 filas, 4 columnas
axes = axes.flatten()

for i, n in enumerate(n_values):
    try:
        # Cálculo para el resorte
        resultado_resorte, x_points, y_points = simpson_rule(funcion_resorte, a, b, n)
        
        x_vals = np.linspace(a, b, 100)
        y_vals = funcion_resorte(x_vals)
        
        ax_resorte = axes[i]
        ax_resorte.plot(x_vals, y_vals, label=r"$f(x) = kx$", color="blue")
        ax_resorte.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
        ax_resorte.scatter(x_points, y_points, color="red", label="Puntos de interpolación")
        ax_resorte.set_title(f"Resorte: n={n}, Integral={resultado_resorte:.4f}")
        ax_resorte.set_xlabel("x")
        ax_resorte.set_ylabel("f(x)")
        ax_resorte.legend()
        ax_resorte.grid()
    except ValueError as e:
        print(f"Error con n={n}: {e}")

for i, n in enumerate(n_values):
    try:
        # Cálculo para el capacitor
        resultado_capacitor, t_points, v_points = simpson_rule(funcion_capacitor, 0, T, n)
        
        t_vals = np.linspace(0, T, 100)
        v_vals = funcion_capacitor(t_vals)
        
        ax_capacitor = axes[i + 4]
        ax_capacitor.plot(t_vals, v_vals, label=r"$V(t) = 100e^{-2t}$", color="blue")
        ax_capacitor.fill_between(t_vals, v_vals, alpha=0.3, color="cyan", label="Área aproximada")
        ax_capacitor.scatter(t_points, v_points, color="red", label="Puntos de interpolación")
        ax_capacitor.set_title(f"Capacitor: n={n}, Q={C * resultado_capacitor:.6f} C")
        ax_capacitor.set_xlabel("t (s)")
        ax_capacitor.set_ylabel("V(t)")
        ax_capacitor.legend()
        ax_capacitor.grid()
    except ValueError as e:
        print(f"Error con n={n}: {e}")

plt.tight_layout()
plt.show()
