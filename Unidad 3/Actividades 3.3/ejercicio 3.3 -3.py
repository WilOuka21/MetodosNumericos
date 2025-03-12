import numpy as np
import matplotlib.pyplot as plt

# Definir el sistema de ecuaciones
A = np.array([[12, -2, 1, 0, 0, 0, 0],
              [-3, 18, -4, 2, 0, 0, 0],
              [1, -2, 16, -1, 1, 0, 0],
              [0, 1, -1, 11, -3, 1, 0],
              [0, 0, -2, 4, 15, -2, 1],
              [0, 0, 0, 1, -3, 2, 13]])

b = np.array([20, 35, -5, 19, -12, 25])

# Solución de mínimos cuadrados para comparar errores
sol_exacta, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

# Criterio de paro
tolerancia = 1e-6
max_iter = 100

# Implementación del método de Jacobi
def jacobi(A, b, tol, max_iter):
    n = A.shape[1]  # Número de incógnitas
    x = np.zeros(n)  # Aproximación inicial
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(A.shape[0]):  # Iterar sobre las ecuaciones
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

# Segunda subgráfica: Iteraciones y errores
axs[1].axis('off')
table_data = [["Iteración", "Error absoluto", "Error relativo", "Error cuadrático"]]
table_data += [["1", "15.367010", "1.820906", "12.221569"],
               ["2", "14.279961", "1.692096", "10.314164"],
               ["3", "16.577537", "1.964346", "12.778369"],
               ["4", "16.814457", "1.992420", "12.816475"],
               ["5", "17.258352", "2.045019", "13.184380"],
               ["6", "17.365865", "2.057759", "13.260630"],
               ["7", "17.440099", "2.066555", "13.314278"],
               ["8", "17.469111", "2.069993", "13.338167"],
               ["9", "17.482441", "2.071573", "13.347090"],
               ["10", "17.489129", "2.072365", "13.352646"],
               ["11", "17.491762", "2.072677", "13.354426"],
               ["12", "17.493180", "2.072845", "13.355571"],
               ["13", "17.493735", "2.072911", "13.355965"],
               ["14", "17.494024", "2.072945", "13.356191"],
               ["15", "17.494144", "2.072959", "13.356279"],
               ["16", "17.494203", "2.072966", "13.356324"],
               ["17", "17.494229", "2.072969", "13.356343"],
               ["18", "17.494241", "2.072971", "13.356352"],
               ["19", "17.494246", "2.072971", "13.356356"],
               ["20", "17.494249", "2.072972", "13.356358"],
               ["21", "17.494250", "2.072972", "13.356359"]]
table = axs[1].table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Guardar y mostrar la figura combinada
plt.tight_layout()
plt.savefig("errores_jacobi_con_iteraciones.png")
plt.show()

# Mostrar la solución aproximada y la solución de mínimos cuadrados
print(f"Solución aproximada (Jacobi): {sol_aprox}")
print(f"Solución de mínimos cuadrados (lstsq): {sol_exacta}")