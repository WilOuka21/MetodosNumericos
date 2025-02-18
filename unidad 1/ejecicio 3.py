import matplotlib.pyplot as plt

# Definimos las etiquetas y los errores
# etiquetas: nombres de las categorías
# errores_abs: errores absolutos para cada categoría
# errores_rel: errores relativos para cada categoría
etiquetas = ['Caso 1', 'Caso 2', 'Caso 3', 'Caso 4']
errores_abs = [0.1, 0.05, 0.02, 0.01]
errores_rel = [0.01, 0.005, 0.002, 0.001]

# Crear la gráfica de barras para el error absoluto
plt.bar(etiquetas, errores_abs, label='Error Absoluto', alpha=0.7, color='blue')

# Añadir etiquetas de valor encima de cada barra para el error absoluto
# Esto nos permite visualizar los valores exactos de los errores absolutos directamente en la gráfica.
for i, v in enumerate(errores_abs):
    plt.text(i, v + 0.001, f'{v:.3f}', ha='center', va='bottom')
import matplotlib.pyplot as plt

# Definimos las etiquetas y los errores
# etiquetas: nombres de las categorías
# errores_abs: errores absolutos para cada categoría
# errores_rel: errores relativos para cada categoría
etiquetas = ['Caso 1', 'Caso 2', 'Caso 3', 'Caso 4']
errores_abs = [0.1, 0.05, 0.02, 0.01]
errores_rel = [0.01, 0.005, 0.002, 0.001]

# Crear la gráfica de barras para el error absoluto
plt.bar(etiquetas, errores_abs, label='Error Absoluto', alpha=0.7, color='blue')

# Añadir etiquetas de valor encima de cada barra para el error absoluto
# Esto nos permite visualizar los valores exactos de los errores absolutos directamente en la gráfica.
for i, v in enumerate(errores_abs):
    plt.text(i, v + 0.001, f'{v:.3f}', ha='center', va='bottom')

# Crear la gráfica de barras para el error relativo
plt.bar(etiquetas, errores_rel, label='Error Relativo', alpha=0.7, color='red')

# Añadir etiquetas de valor encima de cada barra para el error relativo
for i, v in enumerate(errores_rel):
    plt.text(i, v + 0.001, f'{v:.3f}', ha='center', va='bottom')

# Configuración de la gráfica
plt.xlabel('Casos de prueba')  # Etiqueta del eje X
plt.ylabel('Errores')  # Etiqueta del eje Y
plt.title('Errores Absoluto y Relativo')  # Título de la gráfica
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar la gráfica

# Supongamos que calcular_errores es una función definida previamente
def calcular_errores(x, y, real):
    # Implementación de la función
    pass

# Llamada a la función calcular_errores
calcular_errores(x, y, real)
# Crear la gráfica de barras para el error relativo
plt.bar(etiquetas, errores_rel, label='Error Relativo', alpha=0.7, color='red')

# Añadir etiquetas de valor encima de cada barra para el error relativo
for i, v in enumerate(errores_rel):
    plt.text(i, v + 0.001, f'{v:.3f}', ha='center', va='bottom')

# Configuración de la gráfica
plt.xlabel('Casos de prueba')  # Etiqueta del eje X
plt.ylabel('Errores')  # Etiqueta del eje Y
plt.title('Errores Absoluto y Relativo')  # Título de la gráfica
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar la gráfica

# Supongamos que calcular_errores es una función definida previamente
def calcular_errores(x, y, real):
    # Implementación de la función
    pass

# Llamada a la función calcular_errores
calcular_errores(x, y, real)