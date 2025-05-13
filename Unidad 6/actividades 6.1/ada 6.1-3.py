import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros térmicos
T_amb = 25  # °C
k = 0.07    # Coeficiente de enfriamiento

# Definición de la EDO: dT/dt = -k*(T - T_amb)
def f(t, T):
    return -k * (T - T_amb)

# Condiciones iniciales
t0 = 0
T0 = 90     # °C
tf = 30     # minutos
n = 30

# Paso
h = (tf - t0)/n

# Inicialización de listas
t_vals = [t0]
T_vals = [T0]

# Método de Euler
t = t0
T = T0
for i in range(n):
    T = T + h * f(t, T)
    t = t + h
    t_vals.append(t)
    T_vals.append(T)

# Solución analítica
def sol_analitica(t):
    return T_amb + (T0 - T_amb) * np.exp(-k*t)

# Calcular solución analítica
T_analitica = [sol_analitica(t) for t in t_vals]

# Crear tabla de resultados
data = {
    "t (min)": t_vals,
    "T_aproximada (°C)": T_vals,
    "T_analitica (°C)": T_analitica,
    "Error": [abs(T_vals[i] - T_analitica[i]) for i in range(len(t_vals))]
}
df = pd.DataFrame(data)
csv_path = "ejercicio3_resultados.csv"
df.to_csv(csv_path, index=False)

# Graficar ambas soluciones
plt.figure(figsize=(10, 6))
plt.plot(t_vals, T_vals, 'o-', label='Solución aproximada (Euler)', color='blue')
plt.plot(t_vals, T_analitica, '-', label='Solución analítica', color='red')
plt.title('Enfriamiento de un cuerpo (Ley de Newton)')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()
image_path = "ejercicio3_solucion.png"
plt.savefig(image_path)
plt.show()

# Mostrar tabla de resultados
print("Tabla de resultados para el Ejercicio 3:")
print(df)