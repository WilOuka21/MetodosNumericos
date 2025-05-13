import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del ejercicio
longitud = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
deflexion = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])

# Interpolaciones
lineal_interp = interp1d(longitud, deflexion, kind='linear')
cuadratica_interp = interp1d(longitud, deflexion, kind='quadratic')
cubica_interp = interp1d(longitud, deflexion, kind='cubic')

# Valores para graficar con mayor resolución
longitud_interp = np.linspace(longitud.min(), longitud.max(), 100)
deflexion_lineal = lineal_interp(longitud_interp)
deflexion_cuadratica = cuadratica_interp(longitud_interp)
deflexion_cubica = cubica_interp(longitud_interp)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(longitud, deflexion, color='red', label='Datos experimentales')
plt.plot(longitud_interp, deflexion_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(longitud_interp, deflexion_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(longitud_interp, deflexion_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('Longitud (m)')
plt.ylabel('Deflexión (mm)')
plt.title('Análisis de Deflexión de Viga mediante Interpolación')
plt.legend()
plt.grid(True)
plt.savefig('deflexion_viga_interpolacion.png')
plt.show()

print("Análisis de las interpolaciones:")
print("La interpolación lineal conecta los puntos con líneas rectas, lo que puede no capturar la curvatura real de la deflexión.")
print("La interpolación cuadrática utiliza polinomios de segundo grado para ajustar los puntos, permitiendo una mejor representación de la curvatura.")
print("La interpolación cúbica emplea polinomios de tercer grado, ofreciendo una mayor flexibilidad para ajustarse a las variaciones en los datos.")
print("\nAl observar la gráfica, se puede analizar qué método de interpolación se ajusta visualmente mejor a los datos experimentales.")
print("Generalmente, una interpolación de mayor orden (como la cúbica) puede proporcionar un ajuste más suave y preciso si la deflexión real de la viga es una función suave.")
print("Sin embargo, es importante evitar el sobreajuste (overfitting), donde la interpolación se ajusta demasiado a los puntos específicos y no representa bien el comportamiento general.")
print("Para determinar el método más adecuado, se podría considerar el comportamiento físico esperado de la deflexión de una viga bajo una carga distribuida. En muchos casos, una curva suave es esperada, lo que sugeriría que la interpolación cuadrática o cúbica podrían ser más apropiadas que la lineal.")