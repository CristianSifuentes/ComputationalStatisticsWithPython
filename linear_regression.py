'''
Claro, aquí tienes un ejemplo de cómo realizar una regresión lineal simple en Python utilizando la biblioteca Matplotlib y NumPy. En este ejemplo, ajustaremos una línea recta a un conjunto de datos de muestra y la graficaremos.

Primero, asegúrate de tener las bibliotecas Matplotlib y NumPy instaladas. Si no las tienes, puedes instalarlas utilizando pip:
'''
'''
pip install matplotlib numpy

'''

import numpy as np
import matplotlib.pyplot as plt

# Datos de muestra
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.8, 3.6, 4.5, 5.1, 6.0, 6.8, 7.5, 8.2, 9.0, 10.1])

# Calcular la pendiente (coeficiente b1) y la ordenada al origen (coeficiente b0) de la regresión lineal
n = len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)
b1 = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
b0 = mean_y - b1 * mean_x

# Calcular las predicciones
y_pred = b0 + b1 * x

# Graficar los datos y la línea de regresión
plt.scatter(x, y, label='Datos de Muestra')
plt.plot(x, y_pred, color='red', label='Línea de Regresión')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (Y)')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# Imprimir los coeficientes de la regresión lineal
print(f"Coeficiente b0 (ordenada al origen): {b0:.2f}")
print(f"Coeficiente b1 (pendiente): {b1:.2f}")


'''
En este código:

Definimos un conjunto de datos de muestra x e y que representan las variables independiente y dependiente, respectivamente.

Calculamos la pendiente b1 y la ordenada al origen b0 de la regresión lineal utilizando fórmulas matemáticas.

Calculamos las predicciones y_pred utilizando la ecuación de regresión lineal.

Graficamos los datos de muestra como puntos y la línea de regresión utilizando Matplotlib.

Mostramos la gráfica y los coeficientes de la regresión lineal.

Este ejemplo demuestra cómo realizar una regresión lineal simple y visualizarla utilizando Matplotlib en Python.
'''