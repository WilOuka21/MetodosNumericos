import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
V = 10  # Voltios
R = 1000  # Ohms
C = 0.001  # Farads

def f(t, q):
    return (V - q/C)/R

def runge_kutta_4(f, t0, y0, t_end, h):
    t_vals = [t0]
    y_vals = [y0]
    
    t = t0
    y = y0
    
    print(f"{'t (s)':>10} {'q (C)':>15}")
    
    while t < t_end:
        k1 = f(t, y)
        k2 = f(t + h/2, y + h/2 * k1)
        k3 = f(t + h/2, y + h/2 * k2)
        k4 = f(t + h, y + h * k3)
        
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        
        print(f"{t:10.4f} {y:15.6f}")
        
        t_vals.append(t)
        y_vals.append(y)
    
    return t_vals, y_vals

# Parámetros iniciales
t0 = 0
q0 = 0
t_end = 1
h = 0.05

# Solución numérica
t_vals, q_vals = runge_kutta_4(f, t0, q0, t_end, h)

# Graficar
plt.figure(figsize=(10,6))
plt.plot(t_vals, q_vals, 'go-', label="Carga del capacitor", markersize=5)
plt.xlabel("Tiempo (s)")
plt.ylabel("Carga (C)")
plt.title("Carga de un capacitor en circuito RC")
plt.grid(True)
plt.legend()
plt.savefig("ejercicio2_rk4.png")
plt.show()