import altair as alt
import pandas as pd
# pip install altair vega_datasets

# Crear un gráfico de dispersión interactivo de datos de automóviles
data = pd.read_csv('https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.csv')
chart = alt.Chart(data).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']
).interactive()

# Mostrar el gráfico interactivo
chart
