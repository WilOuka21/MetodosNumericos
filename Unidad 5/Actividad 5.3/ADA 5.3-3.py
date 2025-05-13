import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del Ejercicio 3
velocidad = np.array([40, 60, 80, 100, 120, 140])
consumo = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])

# Interpolaciones
lineal_interp_consumo = interp1d(velocidad, consumo, kind='linear')
cuadratica_interp_consumo = interp1d(velocidad, consumo, kind='quadratic')
cubica_interp_consumo = interp1d(velocidad, consumo, kind='cubic')

# Valores para graficar con mayor resolución
velocidad_interp = np.linspace(velocidad.min(), velocidad.max(), 100)
consumo_lineal = lineal_interp_consumo(velocidad_interp)
consumo_cuadratica = cuadratica_interp_consumo(velocidad_interp)
consumo_cubica = cubica_interp_consumo(velocidad_interp)

# Graficar los resultados del Ejercicio 3
plt.figure(figsize=(10, 6))
plt.scatter(velocidad, consumo, color='red', label='Datos experimentales')
plt.plot(velocidad_interp, consumo_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(velocidad_interp, consumo_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(velocidad_interp, consumo_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Consumo (L/100 km)')
plt.title('Curva de Consumo de Combustible')
plt.legend()
plt.grid(True)
plt.savefig('consumo_combustible_interpolacion.png')
plt.show()

print("\nAnálisis de las interpolaciones para el consumo de combustible:")
print("La interpolación lineal conecta los puntos con segmentos rectos, lo que simplifica el comportamiento pero no captura la posible no linealidad.")
print("La interpolación cuadrática introduce una curva que puede ajustarse mejor a los cambios en la tasa de consumo a diferentes velocidades.")
print("La interpolación cúbica proporciona una mayor flexibilidad para ajustarse a las variaciones del consumo, aunque podría resultar en un sobreajuste si los datos experimentales tienen ruido.")
print("\nDeterminación de intervalos de comportamiento:")
print("Observando la gráfica y los datos, el comportamiento parece ser aproximadamente lineal entre 60 km/h y 80 km/h, donde la pendiente del consumo con respecto a la velocidad es relativamente constante.")
print("El comportamiento es más curvo en los extremos: a bajas velocidades (40-60 km/h) donde el consumo disminuye más rápidamente al aumentar la velocidad, y a altas velocidades (100-140 km/h) donde el consumo comienza a aumentar nuevamente.")
print("\nPara describir mejor la curva de consumo de combustible, la interpolación cuadrática o cúbica probablemente sean más adecuadas que la lineal, ya que pueden capturar la no linealidad del fenómeno.")