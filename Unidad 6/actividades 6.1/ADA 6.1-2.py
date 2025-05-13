import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros físicos
g = 9.81  # m/s^2
m = 2     # kg
k = 0.5   # kg/s

# Definición de la EDO: dv/dt = g - (k/m)*v
def f(t, v):
    return g - (k/m)*v

# Condiciones iniciales
t0 = 0
v0 = 0
tf = 10
n = 50

# Paso
h = (tf - t0)/n

# Inicialización de listas
t_vals = [t0]
v_vals = [v0]

# Método de Euler
t = t0
v = v0
for i in range(n):
    v = v + h * f(t, v)
    t = t + h
    t_vals.append(t)
    v_vals.append(v)

# Solución analítica
def sol_analitica(t):
    return (m*g)/k * (1 - np.exp(-(k/m)*t))

# Calcular solución analítica
v_analitica = [sol_analitica(t) for t in t_vals]

# Crear tabla de resultados
data = {
    "t": t_vals,
    "v_aproximada": v_vals,
    "v_analitica": v_analitica,
    "Error": [abs(v_vals[i] - v_analitica[i]) for i in range(len(t_vals))]
}
df = pd.DataFrame(data)
csv_path = "ejercicio2_resultados.csv"
df.to_csv(csv_path, index=False)

# Graficar ambas soluciones
plt.figure(figsize=(10, 6))
plt.plot(t_vals, v_vals, 'o-', label='Solución aproximada (Euler)', color='blue', markersize=4)
plt.plot(t_vals, v_analitica, '-', label='Solución analítica', color='red')
plt.title('Caída libre con resistencia del aire')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()
image_path = "ejercicio2_solucion.png"
plt.savefig(image_path)
plt.show()

# Mostrar tabla de resultados
print("Tabla de resultados para el Ejercicio 2:")
print(df)