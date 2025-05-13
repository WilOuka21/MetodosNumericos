import numpy as np
import matplotlib.pyplot as plt

# Datos: Presión (kPa) y Caudal (L/min)
x = np.array([50, 70, 90, 110, 130])
y = np.array([15, 21, 27, 33, 39])

# Cálculo de coeficientes de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

# R^2
y_pred = a + b * x
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2 = 1 - ss_res / ss_tot

print("Ecuación de la recta: y = {:.2f} + {:.2f}x".format(a, b))
print("Coeficiente de determinación R² = {:.4f}".format(r2))

# Predecir caudal cuando la presión es 100 kPa
x_pred = 100
y_pred_point = a + b * x_pred
print("Caudal estimado para presión de 100 kPa: {:.2f} L/min".format(y_pred_point))

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, a + b * x, '-', color='blue', label=f'Ajuste: y = {a:.2f} + {b:.2f}x')
plt.axvline(x=x_pred, linestyle='--', color='gray')
plt.axhline(y=y_pred_point, linestyle='--', color='gray')
plt.plot(x_pred, y_pred_point, 's', color='green', label=f'Estimación en x={x_pred}: y={y_pred_point:.2f}')

# Anotación de la ecuación, R² y estimación
plt.text(60, 35, f"Ecuación: y = {a:.2f} + {b:.2f}x\nR² = {r2:.4f}\nEstimado: y({x_pred}) = {y_pred_point:.2f} L/min",
         fontsize=10, color='blue', bbox=dict(boxstyle="round,pad=0.3", edgecolor="blue", facecolor="white"))

plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Regresión lineal - Caudal en Tuberías')
plt.legend()
plt.grid(True)
plt.savefig('regresion_caudal.png', dpi=300)
plt.show()
