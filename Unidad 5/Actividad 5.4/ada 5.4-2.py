import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([0, 2, 4, 6, 8])
y = np.array([100, 92, 85, 78, 71])

# Cálculo de coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

# Predicciones
y_pred = a + b * x

# R^2
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2 = 1 - ss_res / ss_tot

print("Ecuación de la recta: y = {:.2f} + {:.2f}x".format(a, b))
print("Coeficiente de determinación R² = {:.4f}".format(r2))

# Estimación en x = 5
x_est = 5
y_est = a + b * x_est
print(f"Temperatura estimada en x = 5 cm: {y_est:.2f} °C")

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', color='red', label=f'Ajuste lineal')
plt.plot(x_est, y_est, 's', color='green', label=f'Estimado en x={x_est}: y={y_est:.2f}')

# Anotación de la ecuación, R² y estimación
plt.text(1, 95, f"Ecuación: y = {a:.2f} + {b:.2f}x\nR² = {r2:.4f}\nEstimado: y({x_est}) = {y_est:.2f} °C",
         fontsize=10, color='blue', bbox=dict(boxstyle="round,pad=0.3", edgecolor="blue", facecolor="white"))

plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Regresión Lineal - Transferencia de Calor')
plt.legend()
plt.grid(True)
plt.savefig('regresion_calor.png', dpi=300)
plt.show()
