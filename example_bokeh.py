from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.sampledata.iris import flowers

output_notebook()
# bokeh info
# bokeh sampledata
# pip install bokeh

# Crear un gráfico de dispersión de iris dataset
p = figure(title="Gráfico de Dispersión Iris", x_axis_label='Petal Length', y_axis_label='Petal Width')

# Asignar colores a las especies de iris
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
flowers['color'] = flowers['species'].map(colors)

# Agregar puntos al gráfico
p.circle('petal_length', 'petal_width', size=10, source=flowers, color='color', legend_field='species')

# Mostrar el gráfico interactivo
show(p)
