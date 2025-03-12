import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Definir el sistema de ecuaciones para el Ejercicio 3
A = np.array([[2, -3, 4, -1, 5, -1, 2, -1, 3, -2],
              [-3, 2, 5, -4, 4, 2, -3, -7, 2, 5],
              [-4, -1, 3, 2, 7, -2, 5, -4, 9, 1],
              [-1, -5, 2, 3, 4, -6, 2, 3, 9, -5],
              [-3, -2, 5, 3, 4, -3, -7, 5, 9, 2],
              [-2, -4, -3, 4, 3, 2, 7, -3, 9, -1],
              [5, -1, -2, 3, 4, -6, 3, 4, -9, 3],
              [3, -2, 4, 5, -6, -3, 7, -8, 2, 9],
              [-2, -3, 4, -3, 5, -6, 3, 2, 9, 6],
              [-3, 1, 2, 4, -3, 6, 5, -7, 9, -4]], dtype=float)

b = np.array([11, -10, 8, -6, 7, -3, 9, 5, 6, -8], dtype=float)

# Resolver el sistema
solucion, det_A = gauss_jordan_pivot_determinante(A, b)

# Imprimir la solución si existe
if solucion is not None:
    print(f"Determinante de A: {det_A:.5f}. El sistema tiene solución única.")
    print("Solución del sistema:", solucion)

    # Crear una tabla con los resultados y generar la gráfica
    variables = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
    generar_tabla_y_grafica(variables, solucion, det_A)
else:
    print(f"Determinante de A: {det_A:.5f}. El sistema es indeterminado o no tiene solución única.")
