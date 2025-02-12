import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    """Calcula la aproximación de π usando la serie de Leibniz."""
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# Valor real de π
true_pi = np.pi  

# Valores de N a evaluar
N_values = [10, 100, 1000, 10000]

# Listas para almacenar los errores
errors_abs = []  # Error absoluto
errors_rel = []  # Error relativo
errors_quad = [] # Error cuadrático medio (MSE)

# Calculo de errores para cada N
print(f"{'N':<10} {'Aprox π':<20} {'Error Abs':<20} {'Error Rel':<20} {'Error Cuadrático':<20}")
print("="*90)

for N in N_values:
    approx_pi = leibniz_pi(N)  # Calculamos π aproximado
    error_abs = abs(true_pi - approx_pi)  # Error absoluto
    error_rel = error_abs / true_pi  # Error relativo
    error_quad = (error_abs ** 2)  # Error cuadrático

    # Guardamos en las listas
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_quad.append(error_quad)

    # Imprimimos resultados en tabla
    print(f"{N:<10} {approx_pi:<20.15f} {error_abs:<20.15f} {error_rel:<20.15f} {error_quad:<20.15f}")

# Graficamos los errores
plt.figure(figsize=(8, 6))
plt.plot(N_values, errors_abs, label='Error Absoluto', marker='o', linestyle='-')
plt.plot(N_values, errors_rel, label='Error Relativo', marker='s', linestyle='--')
plt.plot(N_values, errors_quad, label='Error Cuadrático', marker='^', linestyle=':') 

# Configuración de la gráfica
plt.xscale('log')  # Escala logarítmica para N
plt.yscale('log')  # Escala logarítmica para errores
plt.xlabel('Número de términos N')
plt.ylabel('Error')
plt.title('Errores en la Aproximación de π con la Serie de Leibniz')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Mostramos la gráfica
plt.show()
