import matplotlib.pyplot as plt
import numpy as np
# Debian / Ubuntu: sudo apt-get install python3-matplotlib

# Crear un histograma de datos aleatorios
data = np.random.randn(1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color='b', label='Datos Aleatorios')
plt.title('Histograma de Datos Aleatorios')
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
