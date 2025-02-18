import matplotlib.pyplot as plt

# Inicializamos epsilon y listas para registrar datos
epsilon = 1.0
iterations = []
errors = []

# Ciclo para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:
    iterations.append(len(errors) + 1)  # Guardamos el número de iteración
    errors.append(epsilon)  # Guardamos el valor actual de epsilon
    epsilon /= 2  # Reducimos epsilon a la mitad

epsilon *= 2  # Ajustamos epsilon al último valor válido

# Imprimimos el número más bajo encontrado y la cantidad total de iteraciones
print(f"El número más bajo encontrado es: {epsilon}")
print(f"Cantidad total de iteraciones: {len(iterations)}")

# Gráfica
plt.plot(iterations, errors, marker='o')
plt.xlabel('Iteración')
plt.ylabel('Precisión de máquina (ε)')
plt.title('Disminución de ε en cada iteración')
plt.grid(True)

# Agregamos el número más bajo y las iteraciones como texto en la gráfica
plt.text(
    iterations[-1] / 2,  # Posición X (centrado aproximadamente)
    errors[0] / 10,  # Posición Y (un poco abajo del primer valor de error)
    f"Precisión mínima: {epsilon:.2e}\nIteraciones: {len(iterations)}",
    fontsize=10,
    color="red",                                    
    bbox=dict(facecolor="white", alpha=0.8, edgecolor="red")
)

# Mostramos la gráfica
plt.show()
                                                                                                                 