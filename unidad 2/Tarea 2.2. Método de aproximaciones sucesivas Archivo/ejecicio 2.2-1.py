import numpy as np
import matplotlib.pyplot as plt

# Definir la función g(x) para el método de punto fijo
def g(x):
    return (3*x - 1)**0.5  # Transformación de la ecuación x^2 - 3x + 1 = 0

# Criterio de convergencia (derivada de g(x))
def g_prime(x):
    return 1.5 / np.sqrt(3*x - 1)  

# Error absoluto
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)

# Error relativo
def error_relativo(x_new, x_old):
    return abs((x_new - x_old) / x_new)

# Error cuadrático
def error_cuadratico(x_new, x_old):
    return (x_new - x_old)**2

# Método de punto fijo
def punto_fijo(x0, tol=1e-5, max_iter=100):
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []

    x_old = x0
    for i in range(max_iter):
        x_new = g(x_old)
        e_abs = error_absoluto(x_new, x_old)
        e_rel = error_relativo(x_new, x_old)
        e_cuad = error_cuadratico(x_new, x_old)

        iteraciones.append((i+1, x_new, e_abs, e_rel, e_cuad))
        errores_abs.append(e_abs)
        errores_rel.append(e_rel)
        errores_cuad.append(e_cuad)

        if e_abs < tol:
            break

        x_old = x_new

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Parámetro inicial
x0 = 1.5
iteraciones, errores_abs, errores_rel, errores_cuad = punto_fijo(x0)

# Imprimir tabla de iteraciones
print("Iteración | x_n      | Error absoluto | Error relativo | Error cuadrático")
print("-----------------------------------------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e} | {it[3]:.6e} | {it[4]:.6e}")

# Graficar la convergencia y los errores en una sola figura con dos subgráficas
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Primera subgráfica: Convergencia del método de punto fijo
x_vals = np.linspace(0, 2, 100)
y_vals = g(x_vals)
x_points = [it[1] for it in iteraciones]
y_points = [g(x) for x in x_points]

axs[0].plot(x_vals, y_vals, label=r"$g(x) = \sqrt{3x - 1}$", color="blue")
axs[0].plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")
axs[0].scatter(x_points, y_points, color="black", zorder=3)
axs[0].plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")
axs[0].set_xlabel("x")
axs[0].set_ylabel("g(x)")
axs[0].legend()
axs[0].grid(True)
axs[0].set_title("Método de Punto Fijo")

# Agregar las iteraciones en la gráfica de convergencia
for i, (it_num, x_val, _, _, _) in enumerate(iteraciones):
    axs[0].text(x_val, g(x_val), f'{it_num}', fontsize=8, verticalalignment='bottom')

# Segunda subgráfica: Evolución de los errores
axs[1].plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")
axs[1].plot(range(1, len(errores_rel) + 1), errores_rel, marker="s", label="Error relativo")
axs[1].plot(range(1, len(errores_cuad) + 1), errores_cuad, marker="^", label="Error cuadrático")
axs[1].set_xlabel("Iteración")
axs[1].set_ylabel("Error")
axs[1].set_yscale("log")
axs[1].legend()
axs[1].grid(True)
axs[1].set_title("Evolución de los Errores")

# Tercera subgráfica: Tabla de iteraciones
axs[2].axis('off')
table_data = [["Iteración", "x_n", "Error absoluto", "Error relativo", "Error cuadrático"]]
table_data += [[f"{it[0]:9d}", f"{it[1]:.6f}", f"{it[2]:.6e}", f"{it[3]:.6e}", f"{it[4]:.6e}"] for it in iteraciones]
table = axs[2].table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Guardar y mostrar la figura combinada
plt.tight_layout()
plt.savefig("punto_fijo_convergencia_errores.png")
plt.show()
