import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del Ejercicio 2
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
temperatura = np.array([250, 220, 180, 150, 130, 125])

# Interpolaciones
lineal_interp_temp = interp1d(distancia, temperatura, kind='linear')
cuadratica_interp_temp = interp1d(distancia, temperatura, kind='quadratic')
cubica_interp_temp = interp1d(distancia, temperatura, kind='cubic')

# Valores para graficar con mayor resolución
distancia_interp = np.linspace(distancia.min(), distancia.max(), 100)
temperatura_lineal = lineal_interp_temp(distancia_interp)
temperatura_cuadratica = cuadratica_interp_temp(distancia_interp)
temperatura_cubica = cubica_interp_temp(distancia_interp)

# Graficar los resultados del Ejercicio 2
plt.figure(figsize=(10, 6))
plt.scatter(distancia, temperatura, color='red', label='Datos experimentales')
plt.plot(distancia_interp, temperatura_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(distancia_interp, temperatura_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(distancia_interp, temperatura_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('Distancia (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Variación de la Temperatura en un Motor')
plt.legend()
plt.grid(True)
plt.savefig('temperatura_motor_interpolacion.png')
plt.show()

print("Análisis de las interpolaciones para la temperatura del motor:")
print("La interpolación lineal muestra una disminución constante por segmentos, sin capturar posibles cambios de ritmo.")
print("La interpolación cuadrática introduce cierta curvatura, lo que podría representar mejor una disminución no lineal de la temperatura.")
print("La interpolación cúbica ofrece una curva aún más suave, adaptándose potencialmente mejor a las variaciones locales en la distribución de temperatura.")
print("\nLa elección del método más preciso dependerá de la naturaleza real de la distribución de temperatura dentro del motor. Si se espera una variación suave y posiblemente con puntos de inflexión, la interpolación cuadrática o cúbica podrían ser más apropiadas que la lineal.")