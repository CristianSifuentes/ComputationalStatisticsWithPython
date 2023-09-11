'''
La programación estocástica se utiliza comúnmente en situaciones en las que se necesita tomar decisiones bajo incertidumbre. Un ejemplo típico es la planificación de inversiones financieras, donde las tasas de rendimiento de diferentes activos son inciertas. Aquí tienes un ejemplo simple de cómo podrías utilizar la programación estocástica en Python para tomar decisiones de inversión en un escenario de incertidumbre financiera.

Supongamos que tienes una cantidad fija de dinero para invertir y debes decidir cómo distribuirlo entre tres activos financieros: acciones, bonos y efectivo. Las tasas de rendimiento de estos activos varían estocásticamente de año en año. Quieres encontrar la asignación de activos que maximice el valor esperado de tu cartera después de cierto número de años.

Para simular esto, primero necesitamos establecer las tasas de rendimiento como variables estocásticas. Luego, utilizamos un algoritmo de programación estocástica, como el método de Monte Carlo, para generar múltiples escenarios y calcular el valor esperado de la cartera en cada escenario. Finalmente, seleccionamos la asignación de activos que maximiza el valor esperado de la cartera.

Aquí está el código de ejemplo:
'''

import random
import numpy as np

# Configuración de las tasas de rendimiento estocásticas
num_scenarios = 1000  # Número de escenarios simulados
years = 10  # Número de años para la inversión

# Tasas de rendimiento promedio y desviación estándar para los activos
mean_returns = [0.08, 0.04, 0.02]  # Acciones, Bonos, Efectivo
std_devs = [0.2, 0.1, 0.05]  # Desviación estándar de rendimiento

# Dinero inicial para invertir
initial_investment = 100000

# Simulación de múltiples escenarios
portfolio_values = []

for _ in range(num_scenarios):
    portfolio_value = initial_investment
    for _ in range(years):
        asset_returns = np.random.normal(mean_returns, std_devs)
        portfolio_value = np.sum(portfolio_value * (1 + asset_returns))
    portfolio_values.append(portfolio_value)

# Cálculo del valor esperado y desviación estándar de la cartera
expected_value = np.mean(portfolio_values)
std_dev = np.std(portfolio_values)

print(f"Valor esperado de la cartera después de {years} años: ${expected_value:.2f}")
print(f"Desviación estándar de la cartera: ${std_dev:.2f}")

'''
Este código simula múltiples escenarios de inversión a lo largo de varios años, teniendo en cuenta la incertidumbre en las tasas de rendimiento de los activos. Luego, calcula el valor esperado y la desviación estándar de la cartera de inversión en función de esos escenarios. Este tipo de enfoque es útil para la toma de decisiones de inversión cuando se desea considerar la incertidumbre en los rendimientos financieros.
'''