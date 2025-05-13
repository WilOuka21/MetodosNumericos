import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0  # masa (kg)
k = 1.0  # constante del resorte (N/m)
c = 0.2  # coeficiente de amortiguamiento (kg/s)

def f(t, Y):
    y1, y2 = Y
    return np.array([y2, (-c*y2 - k*y1)/m])

def runge_kutta_4_sistema(f, t0, Y0, t_end, h):
    t_vals = [t0]
    Y_vals = [Y0]
    
    t = t0
    Y = np.array(Y0)
    
    print(f"{'t (s)':>10} {'Posición':>15} {'Velocidad':>15}")
    
    while t < t_end:
        k1 = f(t, Y)
        k2 = f(t + h/2, Y + h/2 * k1)
        k3 = f(t + h/2, Y + h/2 * k2)
        k4 = f(t + h, Y + h * k3)
        
        Y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        
        print(f"{t:10.4f} {Y[0]:15.6f} {Y[1]:15.6f}")
        
        t_vals.append(t)
        Y_vals.append(Y.copy())
    
    return t_vals, np.array(Y_vals)

# Parámetros iniciales
t0 = 0
Y0 = [1.0, 0.0]  # [posición inicial, velocidad inicial]
t_end = 5
h = 0.1

# Solución numérica
t_vals, Y_vals = runge_kutta_4_sistema(f, t0, Y0, t_end, h)

# Graficar posición vs tiempo
plt.figure(figsize=(10,6))
plt.plot(t_vals, Y_vals[:,0], 'm-', label="Posición")
plt.plot(t_vals, Y_vals[:,1], 'c-', label="Velocidad")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición/Velocidad")
plt.title("Dinámica de un resorte amortiguado")
plt.grid(True)
plt.legend()
plt.savefig("ejercicio3_rk4_posicion.png")
plt.show()

# Gráfico de fase (posición vs velocidad)
plt.figure(figsize=(8,8))
plt.plot(Y_vals[:,0], Y_vals[:,1], 'b-')
plt.plot(Y_vals[0,0], Y_vals[0,1], 'ro', label="Inicio")
plt.xlabel("Posición")
plt.ylabel("Velocidad")
plt.title("Diagrama de fase del resorte amortiguado")
plt.grid(True)
plt.legend()
plt.savefig("ejercicio3_rk4_fase.png")
plt.show()