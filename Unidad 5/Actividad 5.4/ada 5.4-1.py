import numpy as np
import matplotlib.pyplot as plt

# Datos de carga (kN) y elongación (mm)
x = np.array([5, 10, 15, 20, 25])
y = np.array([0.6, 1.2, 1.9, 2.5, 3.1])

# Cálculo de los coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
y_pred = a + b * x

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')

# Anotación de los coeficientes en la gráfica
plt.text(10, 2.8, f'Coeficientes:\na = {a:.4f}\nb = {b:.4f}', 
         fontsize=10, color='blue', bbox=dict(boxstyle="round,pad=0.3", edgecolor="blue", facecolor="white"))

plt.xlabel('Carga (kN)')
plt.ylabel('Elongación (mm)')
plt.title('Regresión Lineal - Elongación vs Carga')
plt.legend()
plt.grid(True)
plt.savefig('regresion_elongacion.png', dpi=300)  # Guarda la figura
plt.show()
