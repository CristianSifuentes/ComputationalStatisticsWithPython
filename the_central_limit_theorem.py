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
