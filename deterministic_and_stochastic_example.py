'''Claro, puedo mostrarte un ejemplo de un programa en Python que ilustra conceptos tanto de programación determinística como estocástica en el contexto de lanzar un dado.

**Programación Determinística:**

En la programación determinística, el resultado es predecible y está determinado por reglas fijas. Cuando lanzas un dado justo de seis caras, cada cara tiene igual probabilidad de aparecer, y el resultado se determina por reglas matemáticas y físicas.

'''

import random

# Programación Determinística: Lanzamiento de un dado justo
numero_caras = 6
resultado_deterministico = random.randint(1, numero_caras)

print(f"Programación Determinística: Resultado del lanzamiento de un dado justo: {resultado_deterministico}")

'''

**Programación Estocástica:**

En la programación estocástica, introducimos la aleatoriedad en el proceso. Simularemos un dado sesgado que tiene más probabilidades de arrojar ciertos números. Este proceso es aleatorio y sigue una distribución de probabilidad definida.

'''

import random

# Programación Estocástica: Lanzamiento de un dado sesgado
distribucion_probabilidad = [0.1, 0.2, 0.3, 0.1, 0.1, 0.2]  # Probabilidad de cada cara
resultado_estocastico = random.choices(range(1, 7), weights=distribucion_probabilidad, k=1)[0]

print(f"Programación Estocástica: Resultado del lanzamiento de un dado sesgado: {resultado_estocastico}")
'''

En este ejemplo, hemos lanzado un dado sesgado utilizando programación estocástica, donde cada cara tiene una probabilidad diferente de aparecer. Mientras que en la programación determinística, el resultado se determina mediante un algoritmo específico, en la programación estocástica, el resultado se determina al azar según una distribución de probabilidad especificada. Esto ilustra la diferencia fundamental entre estos dos enfoques.

'''