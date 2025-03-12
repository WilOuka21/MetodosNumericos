import numpy as np
import matplotlib.pyplot as plt

# Definir el sistema de ecuaciones del ejercicio 2
A = np.array([[8, 2, -1, 0, 0, 0],
              [3, 15, -2, 1, 0, 0],
              [0, -2, 12, 2, -1, 0],
              [0, 1, -1, 9, -2, 1],
              [0, 0, -2, 3, 14, 1],
              [0, 0, 0, 1, -2, 10]])

b = np.array([10, 24, -18, 16, -9, 22])

# Solución exacta para comparar errores
sol_exacta = np.linalg.solve(A, b) 

# Criterio de paro
tolerancia = 1e-6
max_iter = 100

# Implementación del método de Jacobi
def jacobi(A, b, tol, max_iter):
    n = len(A)
    x = np.zeros(n)  # Aproximación inicial
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i, i]
        
        # Calcular errores
        error_abs = np.linalg.norm(x_new - sol_exacta, ord=1)
        error_rel = np.linalg.norm(x_new - sol_exacta, ord=1) / np.linalg.norm(sol_exacta, ord=1)
        error_cuad = np.linalg.norm(x_new - sol_exacta, ord=2)
        
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)
        
        # Imprimir errores de la iteración
        print(f"Iteración {k+1}: Error absoluto = {error_abs:.6f}, Error relativo = {error_rel:.6f}, Error cuadrático = {error_cuad:.6f}")
        
        # Criterio de convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        
        x = x_new
    
    return x, errores_abs, errores_rel, errores_cuad, k+1

# Ejecutar el método de Jacobi
sol_aprox, errores_abs, errores_rel, errores_cuad, iteraciones = jacobi(A, b, tolerancia, max_iter)

# Graficar los errores
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Primera subgráfica: Convergencia de los errores
axs[0].plot(range(1, iteraciones+1), errores_abs, label="Error absoluto", marker='o')
axs[0].plot(range(1, iteraciones+1), errores_rel, label="Error relativo", marker='s')
axs[0].plot(range(1, iteraciones+1), errores_cuad, label="Error cuadrático", marker='d')
axs[0].set_xlabel("Iteraciones")
axs[0].set_ylabel("Error")
axs[0].set_yscale("log")
axs[0].set_title("Convergencia de los errores en el método de Jacobi")
axs[0].legend()
axs[0].grid()

# Segunda subgráfica: Soluciones
axs[1].axis('off')
table_data = [["Solución", "Valor"]]
table_data += [["Aprox. x" + str(i+1), f"{sol_aprox[i]:.6f}"] for i in range(len(sol_aprox))]
table_data += [["Exacta x" + str(i+1), f"{sol_exacta[i]:.6f}"] for i in range(len(sol_exacta))]
table = axs[1].table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Guardar y mostrar la figura combinada
plt.tight_layout()
plt.savefig("errores_jacobi.png")
plt.show()

# Mostrar la solución aproximada
print(f"Solución aproximada: {sol_aprox}")
print(f"Solución exacta: {sol_exacta}")
