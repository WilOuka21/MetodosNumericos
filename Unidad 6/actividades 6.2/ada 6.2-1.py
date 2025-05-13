import numpy as np
import matplotlib.pyplot as plt

def f(x, T):
    return -0.25 * (T - 25)

def runge_kutta_4(f, x0, y0, x_end, h):
    x_vals = [x0]
    y_vals = [y0]
    
    x = x0
    y = y0
    
    print(f"{'x (m)':>10} {'T (°C)':>15} {'T exacta':>15}")
    
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        
        exacta = 25 + 75 * np.exp(-0.25 * x)
        print(f"{x:10.4f} {y:15.6f} {exacta:15.6f}")
        
        x_vals.append(x)
        y_vals.append(y)
    
    return x_vals, y_vals

# Parámetros iniciales
x0 = 0
T0 = 100
x_end = 2
h = 0.1

# Solución numérica
x_vals, T_vals = runge_kutta_4(f, x0, T0, x_end, h)

# Solución exacta
T_exacta = [25 + 75 * np.exp(-0.25 * x) for x in x_vals]

# Graficar
plt.figure(figsize=(10,6))
plt.plot(x_vals, T_vals, 'bo-', label="RK4", markersize=5)
plt.plot(x_vals, T_exacta, 'r-', label="Solución exacta")
plt.xlabel("Distancia (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Transferencia de calor en un tubo")
plt.grid(True)
plt.legend()
plt.savefig("ejercicio1_rk4.png")
plt.show()