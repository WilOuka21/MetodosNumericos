import matplotlib.pyplot as plt
import math
import pandas as pd

def f(x):
    """Define la función f(x) = e^(-x) - x."""
    return math.exp(-x) - x

def bisection_method(a, b, tol=1e-5, max_iter=100):
    """
    Implementa el método de bisección para encontrar la raíz de la función f(x).
    
    Parámetros:
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    tol (float): Tolerancia para el criterio de parada.
    max_iter (int): Número máximo de iteraciones.
    
    Retorna:
    iterations (list): Lista de valores de c en cada iteración.
    errors (list): Lista de errores absolutos en cada iteración.
    """
    # Verificar si el método de bisección puede aplicarse
    if f(a) * f(b) >= 0:
        print("El método de bisección no puede aplicarse.")
        return [], []

    iterations = []  # Lista para almacenar los valores de c en cada iteración
    errors = []  # Lista para almacenar los errores absolutos en cada iteración
    c_old = a  # Valor inicial de c_old

    for _ in range(max_iter):
        c = (a + b) / 2.0  # Calcular el punto medio del intervalo
        iterations.append(c)  # Almacenar el valor de c
        error = abs(c - c_old)  # Calcular el error absoluto
        errors.append(error)  # Almacenar el error

        # Verificar si el valor de f(c) es cercano a cero o si el error es menor que la tolerancia
        if abs(f(c)) < tol or error < tol:
            break

        # Actualizar los límites del intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c  # Actualizar c_old
    
    return iterations, errors

# Intervalo [0, 1] y tolerancia 10^-5
a, b = 0, 1
iterations, errors = bisection_method(a, b)

if not iterations:
    print("No se encontró una raíz válida en el intervalo dado.")
else:
    # Crear un DataFrame con las iteraciones y errores
    df = pd.DataFrame({
        'Iteración': range(1, len(iterations) + 1),
        'c': iterations,
        'f(c)': [f(c) for c in iterations],
        'Error': errors
    })

    # Graficar la función y la convergencia
    fig, ax = plt.subplots(1, 3, figsize=(21, 5))
    
    # Valores de x para graficar la función
    x_vals = [a + (b - a) * i / 100 for i in range(101)]
    y_vals = [f(x) for x in x_vals]
    
    # Gráfica de la función f(x)
    ax[0].plot(x_vals, y_vals, label='f(x) = e^(-x) - x', color='b')
    ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea horizontal en y=0
    ax[0].scatter(iterations, [f(c) for c in iterations], color='red', label='Iteraciones')  # Puntos de iteraciones
    ax[0].set_xlabel('x')  # Etiqueta del eje X
    ax[0].set_ylabel('f(x)')  # Etiqueta del eje Y
    ax[0].set_title("Convergencia del Método de Bisección")  # Título de la gráfica
    ax[0].legend()  # Mostrar la leyenda
    ax[0].grid()  # Mostrar la cuadrícula
    
    # Gráfica de convergencia del error
    ax[1].plot(range(1, len(errors)+1), errors, marker='o', linestyle='-', color='r')
    ax[1].set_yscale("log")  # Escala logarítmica para el eje Y
    ax[1].set_xlabel("Iteración")  # Etiqueta del eje X
    ax[1].set_ylabel("Error Absoluto")  # Etiqueta del eje Y
    ax[1].set_title("Error Absoluto en cada Iteración")  # Título de la gráfica
    ax[1].grid()  # Mostrar la cuadrícula

    # Mostrar la tabla de iteraciones
    ax[2].axis('tight')
    ax[2].axis('off')
    table = ax[2].table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    
    plt.show()  # Mostrar las gráficas y la tabla
    
    # Mostrar iteraciones en la consola
    print("\nIteraciones del Método de Bisección:")
    print(df.to_string(index=False))
