'''
El movimiento browniano es un tipo de camino aleatorio continuo en el que una partícula 
se mueve aleatoriamente en un fluido debido a la colisión con moléculas del fluido. 
Puedes simular un movimiento browniano en Python utilizando el módulo numpy para la 
generación de números aleatorios y matplotlib para visualizarlo. A continuación, 
te muestro un ejemplo de un movimiento browniano unidimensional:
'''

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_steps = 1000  # Número de pasos en el movimiento browniano
delta_t = 0.01    # Tamaño del paso de tiempo
diffusion_coefficient = 0.1  # Coeficiente de difusión

# Inicialización de arrays para almacenar las posiciones
positions = np.zeros(num_steps)

# Simulación del movimiento browniano
for i in range(1, num_steps):
    # Genera un paso aleatorio con una distribución normal (gaussiana)
    step = np.random.normal(scale=np.sqrt(2 * diffusion_coefficient * delta_t))
    positions[i] = positions[i - 1] + step

# Creación de un array de tiempos
times = np.arange(0, num_steps * delta_t, delta_t)

# Visualización del movimiento browniano
plt.figure(figsize=(10, 4))
plt.plot(times, positions)
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Movimiento Browniano Unidimensional')
plt.grid(True)
plt.show()


'''
En este ejemplo, simulamos un movimiento browniano en una dimensión. 
La partícula se mueve aleatoriamente en el tiempo, y las posiciones 
se registran en un array. Luego, utilizamos matplotlib para 
visualizar el movimiento browniano a lo largo del tiempo.

Puedes ajustar los parámetros como num_steps (el número de pasos), 
delta_t (el tamaño del paso de tiempo) y diffusion_coefficient 
(el coeficiente de difusión) para ver cómo afectan al comportamiento 
del movimiento browniano. Este es solo un ejemplo básico, 
pero muestra cómo puedes simular y visualizar un proceso de movimiento browniano en Python.
'''
