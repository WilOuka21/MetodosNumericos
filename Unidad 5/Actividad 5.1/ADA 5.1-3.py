import numpy as np
import matplotlib.pyplot as plt

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Datos del ejercicio 3
x_points = np.array([2.0, 4.0, 6.0, 8.0])
y_points = np.array([2500, 2300, 2150, 2050])
x_eval = 5.0
y_eval = lagrange_interpolation(x_eval, x_points, y_points)
print(f"Consumo esperado a {x_eval} km: {y_eval:.4f} kg/h")

# Graficar
x_vals = np.linspace(2.0, 8.0, 200)
y_vals = [lagrange_interpolation(x, x_points, y_points) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="Interpolación de Lagrange", color="blue", linewidth=2)
plt.scatter(x_points, y_points, color="red", label="Datos originales", zorder=5)
plt.scatter([x_eval], [y_eval], color="green", label=f"x = {x_eval}", zorder=5)

# Anotaciones para los puntos originales
for i, (x, y) in enumerate(zip(x_points, y_points)):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(-15, 10), ha='center', fontsize=9)

# Anotación para el punto interpolado con consumo esperado
plt.annotate(f"({x_eval:.2f}, {y_eval:.2f})\nConsumo: {y_eval:.4f} kg/h", 
             (x_eval, y_eval), textcoords="offset points", xytext=(-70, -30), 
             ha='center', fontsize=10, color="green", bbox=dict(boxstyle="round,pad=0.3", edgecolor="green", facecolor="white"))

plt.title("Interpolación - Consumo de combustible en aeronaves")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.grid(True)
plt.legend()
plt.show()
