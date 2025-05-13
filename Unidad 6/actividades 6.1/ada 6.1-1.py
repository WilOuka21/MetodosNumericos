import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Parámetros del circuito RC
R = 1000  # Ohms
C = 0.001  # Farads
V_fuente = 5  # Voltios

# Definición de la EDO: dV/dt = (V_fuente - V)/(R*C)
def f(t, V):
    return (V_fuente - V) / (R * C)

# Condiciones iniciales
t0 = 0
V0 = 0
tf = 5
n = 20

# Paso
h = (tf - t0) / n

# Inicialización para Euler
t_vals = [t0]
V_vals = [V0]
t = t0
V = V0

for i in range(n):
    V = V + h * f(t, V)
    t = t + h
    t_vals.append(t)
    V_vals.append(V)

# Inicialización para Euler Mejorado (Heun)
t_vals_heun = [t0]
V_vals_heun = [V0]
t = t0
V = V0

for i in range(n):
    V_pred = V + h * f(t, V)  # Paso de predicción
    V = V + (h / 2) * (f(t, V) + f(t + h, V_pred))  # Paso corregido
    t = t + h
    t_vals_heun.append(t)
    V_vals_heun.append(V)

# Solución analítica
def sol_analitica(t):
    return V_fuente * (1 - np.exp(-t / (R * C)))

V_analitica = [sol_analitica(t) for t in t_vals]

# Calcular errores
errores_euler = [abs(V_vals[i] - V_analitica[i]) for i in range(len(t_vals))]
errores_heun = [abs(V_vals_heun[i] - V_analitica[i]) for i in range(len(t_vals_heun))]

# Crear DataFrame con todos los resultados
df = pd.DataFrame({
    "t (s)": t_vals,
    "V_Euler": V_vals,
    "V_Heun": V_vals_heun,
    "V_Analitica": V_analitica,
    "Error_Euler": errores_euler,
    "Error_Heun": errores_heun
})

# Guardar tabla en CSV con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_path = f"resultados_RC_{timestamp}.csv"
df.to_csv(csv_path, index=False)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t_vals, V_vals, 'o-', label='Euler', color='blue')
plt.plot(t_vals_heun, V_vals_heun, 's--', label='Euler mejorado (Heun)', color='green')
plt.plot(t_vals, V_analitica, '-', label='Solución analítica', color='red')
plt.title('Carga de un capacitor - Comparación de métodos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.legend()
image_path = f"grafico_RC_{timestamp}.png"
plt.savefig(image_path)
plt.show()

# Mostrar tabla
print("\nTabla de resultados:")
print(df)
print(f"\nResultados guardados en: {csv_path}")
print(f"Gráfico guardado en: {image_path}")
