# Codigo que implementa el esquema numerico
# de interpolacion para determinar la raiz de una ecuacion

import numpy as np
import matplotlib.pyplot as plt

# Función original: f(x) = x^3 - 6x^2 + 11x - 6
def f(x):
    """
    Define la función f(x) para la cual se busca la raíz.
    :param x: Valor en el que se evalúa la función
    :return: Resultado de f(x)
    """
    return x**3 - 6*x**2 + 11*x - 6

# Implementación de la interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    """
    Calcula el polinomio interpolante de Lagrange en el punto x.
    :param x: Punto en el que se evalúa el polinomio interpolante
    :param x_points: Lista de puntos de interpolación en x
    :param y_points: Lista de valores de la función en los puntos de interpolación
    :return: Valor del polinomio interpolante en x
    """
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Implementación del método de Bisección con cálculo de errores
def bisect(func, a, b, tol=1e-6, max_iter=100):
    """
    Método de bisección para encontrar la raíz de una función dentro de un intervalo.
    :param func: Función a evaluar
    :param a: Límite inferior del intervalo
    :param b: Límite superior del intervalo
    :param tol: Tolerancia del error para detener el algoritmo
    :param max_iter: Número máximo de iteraciones
    :return: Raíz aproximada y listas de errores
    """
    if func(a) * func(b) > 0:
        raise ValueError("El intervalo no contiene una raíz")

    errores_abs = []  # Lista de errores absolutos
    errores_rel = []  # Lista de errores relativos
    errores_cuad = []  # Lista de errores cuadráticos

    c_old = a  # Inicialización de c_old para calcular errores en la primera iteración
    iteraciones = []  # Lista para registrar las iteraciones
    for i in range(max_iter):
        c = (a + b) / 2  # Punto medio del intervalo
        error_abs = abs(c - c_old)
        error_rel = error_abs / abs(c) if c != 0 else 0
        error_cuad = error_abs ** 2

        # Guardamos los errores en sus respectivas listas
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)
        iteraciones.append((i+1, a, b, c, func(c)))

        # Verificación de criterio de parada
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            return c, errores_abs, errores_rel, errores_cuad, iteraciones

        # Actualización del intervalo según el signo de la función en c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return (a + b) / 2, errores_abs, errores_rel, errores_cuad, iteraciones

# Selección de tres puntos adecuados dentro del intervalo [2.0, 3.0]
x0 = 2.0
x1 = 2.5
x2 = 3.0
x_points = np.array([x0, x1, x2])
y_points = f(x_points)

# Construcción del polinomio interpolante
y_interp = [lagrange_interpolation(x, x_points, y_points) for x in np.linspace(x0, x2, 100)]

# Encontrar la raíz del polinomio interpolante usando bisección
root, errores_abs, errores_rel, errores_cuad, iteraciones = bisect(lambda x: lagrange_interpolation(x, x_points, y_points), x0, x2)

# Generar gráficas de la función y la interpolación
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Primera subgráfica: Función original e interpolación
axs[0].plot(np.linspace(x0, x2, 100), f(np.linspace(x0, x2, 100)), label="$f(x) = x^3 - 6x^2 + 11x - 6$", linestyle='dashed', color='blue')
axs[0].plot(np.linspace(x0, x2, 100), y_interp, label="Interpolación de Lagrange", color='red')
axs[0].axhline(0, color='black', linewidth=0.5, linestyle='--')
axs[0].axvline(root, color='green', linestyle='dotted', label=f"Raíz aproximada: {root:.4f}")
axs[0].scatter(x_points, y_points, color='black', label="Puntos de interpolación")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f(x)")
axs[0].set_title("Interpolación y búsqueda de raíces")
axs[0].legend()
axs[0].grid(True)

# Segunda subgráfica: Tabla de iteraciones
axs[1].axis('off')
table_data = [["Iteración", "a", "b", "c", "f(c)"]]
table_data += [[f"{it[0]}", f"{it[1]:.6f}", f"{it[2]:.6f}", f"{it[3]:.6f}", f"{it[4]:.6e}"] for it in iteraciones]
table = axs[1].table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Guardar y mostrar la figura
plt.tight_layout()
plt.savefig("interpolacion_raices_con_tabla.png")
plt.show()

# Imprimir resultados
print(f"La raíz aproximada usando interpolación es: {root:.4f}")
print("Errores en cada iteración del método de bisección:")
print("Iteración\tError Absoluto\tError Relativo\tError Cuadrático")
for i, (ea, er, ec) in enumerate(zip(errores_abs, errores_rel, errores_cuad)):
    print(f"{i+1}\t{ea:.6e}\t{er:.6e}\t{ec:.6e}")
