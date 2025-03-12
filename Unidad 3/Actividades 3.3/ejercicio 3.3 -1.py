import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definir el sistema de ecuaciones del ejercicio
A = np.array([[10, -1, 2, 0, 0],
              [-1, 11, -1, 3, 0],
              [2, -1, 10, -1, 0],
              [0, 3, -1, 8, -2],
              [0, 0, 0, -2, 10]])

b = np.array([6, 25, -11, 15, -10])

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

def gauss_jordan_pivot_determinante(A, b):
    """
    Resuelve un sistema de ecuaciones Ax = b mediante el método de Gauss-Jordan con pivoteo parcial
    e imprime el determinante de A para verificar si el sistema tiene solución única.
    """
    n = len(A)
    
    # Verificar dimensiones de A y b
    if A.shape[0] != A.shape[1] or A.shape[0] != len(b):
        print("Error: Las dimensiones de A y b no son compatibles.")
        return None, None
    
    # Matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    
    # Cálculo del determinante de A
    det_A = np.linalg.det(A)
    
    # Verificar si el sistema es determinado o indeterminado
    if np.isclose(det_A, 0):
        mensaje = f"Determinante de A: {det_A:.5f}. El sistema es indeterminado o no tiene solución única."
        print(mensaje)
        return None, det_A
    
    mensaje = f"Determinante de A: {det_A:.5f}. El sistema tiene solución única."
    print(mensaje)
    
    # Aplicación del método de Gauss-Jordan con pivoteo
    for i in range(n):
        # Pivoteo parcial
        max_row = np.argmax(abs(Ab[i:, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        # Verificar si el pivote es cero
        if np.isclose(Ab[i, i], 0):
            print("Error: Pivote cero encontrado. El sistema no tiene solución única.")
            return None, det_A

        # Normalización de la fila pivote
        Ab[i] = Ab[i] / Ab[i, i]

        # Eliminación en otras filas
        for j in range(n):
            if i != j:
                Ab[j] -= Ab[j, i] * Ab[i]

    # Extraer la solución
    x = Ab[:, -1]
    return x, det_A

def generar_tabla_y_grafica(variables, solucion, det_A):
    """
    Genera una tabla y una gráfica de los resultados de la solución del sistema de ecuaciones.
    """
    # Crear una tabla con los resultados
    df = pd.DataFrame({'Variable': variables, 'Valor': solucion})
    print("\nTabla de resultados:")
    print(df)

    # Generar gráfica y tabla de resultados
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Primera subgráfica: Solución del sistema
    axs[0].bar(variables, solucion, color='blue')
    axs[0].set_xlabel("Variables")
    axs[0].set_ylabel("Valores")
    axs[0].set_title("Solución del sistema de ecuaciones")
    axs[0].grid(True)

    # Segunda subgráfica: Tabla de resultados
    axs[1].axis('off')
    table_data = [["Variable", "Valor"]]
    table_data += [[variables[i], f"{solucion[i]:.6f}"] for i in range(len(variables))]
    table_data += [["", ""], ["Determinante de A", f"{det_A:.5f}"]]
    table = axs[1].table(cellText=table_data, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    # Guardar y mostrar la figura combinada
    plt.tight_layout()
    plt.savefig("solucion_sistema_ecuaciones.png")
    plt.show()

# Definir el sistema de ecuaciones para el Ejercicio 2
A = np.array([[3, -2, 5, 4, 4, 2, -3, 1, 2],
              [-2, 4, 3, 4, 5, -1, 2, -4, 3],
              [5, -1, -2, 3, 4, 5, -2, 3, -1],
              [1, -3, 2, -4, 5, -6, -2, -8, 4],
              [2, 3, -3, -4, 4, 5, -3, 8, -2],
              [-3, 1, -2, 3, 4, -5, -2, -8, 9],
              [4, -1, -3, 2, 3, -6, -2, 7, 10],
              [1, -3, 2, 4, -3, 2, -8, 3, 9],
              [3, -2, 5, 3, 4, 5, 2, -7, -2]], dtype=float)

b = np.array([-8, 7, -6, 5, 12, -9, 10, 3, -2], dtype=float)

# Resolver el sistema
solucion, det_A = gauss_jordan_pivot_determinante(A, b)

# Imprimir la solución si existe
if solucion is not None:
    print(f"Determinante de A: {det_A:.5f}. El sistema tiene solución única.")
    print("Solución del sistema:", solucion)

    # Crear una tabla con los resultados y generar la gráfica
    variables = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
    generar_tabla_y_grafica(variables, solucion, det_A)
else:
    print(f"Determinante de A: {det_A:.5f}. El sistema es indeterminado o no tiene solución única.")
