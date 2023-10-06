import seaborn as sns
import matplotlib.pyplot as plt
# pip install seaborn

# Cargar el conjunto de datos de iris
iris = sns.load_dataset("iris")

# Crear un gráfico de caja para visualizar la distribución de las características de iris
sns.boxplot(x="species", y="sepal_length", data=iris)

# Mostrar el gráfico
plt.title('Gráfico de Caja de Sepal Length por Especie')
plt.show()
