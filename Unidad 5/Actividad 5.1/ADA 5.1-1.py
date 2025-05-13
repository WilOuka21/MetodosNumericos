import numpy as np
import matplotlib.pyplot as plt

# Datos del problema (posición y deformación)
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

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

# a) Deformación en x = 1.25 m
x_target = 1.25
y_target = lagrange_interpolation(x_target, x_points, y_points)
print(f"Deformación esperada en x = {x_target} m: {y_target:.4f} mm")

# b) Graficar la interpolación
x_values = np.linspace(0.5, 2.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue", linewidth=2)
plt.scatter(x_points, y_points, color="red", label="Puntos originales", zorder=5)
plt.scatter([x_target], [y_target], color="green", label=f"Interpolado en x={x_target}", zorder=5)

# Anotaciones para los puntos originales
for i, (x, y) in enumerate(zip(x_points, y_points)):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(-15, 10), ha='center', fontsize=9)

# Anotación para el punto interpolado con deformación esperada
plt.annotate(f"({x_target:.2f}, {y_target:.2f})\nDeformación: {y_target:.4f} mm", 
             (x_target, y_target), textcoords="offset points", xytext=(-70, -30), 
             ha='center', fontsize=10, color="green", bbox=dict(boxstyle="round,pad=0.3", edgecolor="green", facecolor="white"))

plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.title("Interpolación de Lagrange - Deformación en una Viga")
plt.legend()
plt.grid(True)
plt.show()
