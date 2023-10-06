import plotly.express as px
import plotly.graph_objects as go
# pip install plotly==5.11.0
# pip install cufflinks
# $ sudo pip install plotly 


# Crear un gráfico de barras interactivo
data = px.data.tips()
fig = px.bar(data, x="day", y="total_bill", color="sex", title="Total Bill by Day and Gender")

# Mostrar el gráfico interactivo
fig.show()
