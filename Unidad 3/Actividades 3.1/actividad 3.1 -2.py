import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        # Pivoteo parcial
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]].copy()
            b[[i, max_row]] = b[[max_row, i]].copy()
        
        # Eliminación hacia adelante
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    
    # Sustitución regresiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

# Definición del sistema de ecuaciones
A = np.array([[6, -2, 3, -1, 2], 
              [-3, 5, -2, 4, -1], 
              [4, 3, 7, -5, 3], 
              [-2, 6, -3, 4, -4], 
              [1, -3, 2, -5, 6]], dtype=float)
b = np.array([15, -6, 20, -4, 7], dtype=float)

# Resolución del sistema
sol = gauss_elimination(A.copy(), b.copy())

# Imprimir la solución
print("Solución del sistema:")
print(sol)

# Creación de tabla con resultados
variables = ['x', 'y', 'z', 'w', 'v']
df = pd.DataFrame({'Variable': variables, 'Valor': sol})
print("\nTabla de resultados:")
print(df)

# Análisis de errores
residuo = np.dot(A, sol) - b
error = np.linalg.norm(residuo)
print("\nAnálisis de errores:")
print("Residuo del sistema:", residuo)
print("Norma del error:", error)

# Generar gráfica y tabla de resultados
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Primera subgráfica: Solución del sistema
axs[0].bar(variables, sol, color='blue')
axs[0].set_xlabel("Variables")
axs[0].set_ylabel("Valores")
axs[0].set_title("Solución del sistema de ecuaciones")
axs[0].grid(True)

# Segunda subgráfica: Tabla de resultados y análisis de errores
axs[1].axis('off')
table_data = [["Variable", "Valor"]]
table_data += [[variables[i], f"{sol[i]:.6f}"] for i in range(len(variables))]
table_data += [["", ""], ["Residuo", f"{residuo}"], ["                    error", f"{error:.6e}"]]
table = axs[1].table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Guardar y mostrar la figura combinada
plt.tight_layout()
plt.savefig("solucion_sistema_ecuaciones.png")
plt.show()
