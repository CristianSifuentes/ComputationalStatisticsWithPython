'''
Claro, aquí tienes un programa en Python avanzado que implementa el Teorema del Límite Central de manera avanzada. Este programa generará una distribución de muestras aleatorias a partir de una distribución exponencial y demostrará cómo, a medida que aumenta el tamaño de la muestra, la distribución de las medias de esas muestras se aproxima a una distribución normal.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm

# Parámetros de la distribución exponencial
lmbda = 0.5  # Parámetro de tasa de la distribución exponencial

# Tamaño de la muestra y número de muestras
tamano_muestra = 30
numero_muestras = 1000

# Generar muestras de una distribución exponencial
muestras = expon(scale=1/lmbda).rvs((numero_muestras, tamano_muestra))

# Calcular las medias de las muestras
medias_muestras = np.mean(muestras, axis=1)

# Crear un histograma de las medias
plt.figure(figsize=(10, 5))
plt.hist(medias_muestras, bins=30, density=True, alpha=0.6, color='b', label='Medias de Muestras')

# Calcular la media y la desviación estándar de la distribución normal teórica
media_normal = 1 / lmbda
desviacion_normal = 1 / (lmbda * np.sqrt(tamano_muestra))

# Crear una distribución normal teórica para comparar
x = np.linspace(media_normal - 3 * desviacion_normal, media_normal + 3 * desviacion_normal, 100)
pdf_normal = norm(media_normal, desviacion_normal).pdf(x)
plt.plot(x, pdf_normal, 'r', lw=2, label='Distribución Normal Teórica')

plt.title('Teorema del Límite Central')
plt.xlabel('Medias de Muestras')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()

'''
Este programa realiza lo siguiente:

Genera numero_muestras muestras de tamaño tamano_muestra a partir de una distribución exponencial con el parámetro de tasa lmbda.

Calcula las medias de cada una de las muestras.

Crea un histograma de las medias de las muestras y superpone una distribución normal teórica con la misma media y desviación estándar calculadas.

Muestra un gráfico que demuestra cómo la distribución de las medias de las muestras se aproxima a una distribución normal a medida que numero_muestras aumenta.

Este programa ilustra el Teorema del Límite Central al demostrar cómo las medias de las muestras se comportan de manera similar a una distribución normal, independientemente de la forma de la distribución original, cuando el tamaño de la muestra es lo suficientemente grande.
'''
