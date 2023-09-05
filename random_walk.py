'''
Sí, en programación y matemáticas, un "camino aleatorio" (en inglés, "random walk") es un concepto que se utiliza para describir una secuencia de pasos aleatorios en un espacio discreto, donde cada paso se toma de manera independiente y tiene una probabilidad de dirección o movimiento asociada.

Los caminos aleatorios se utilizan en una variedad de aplicaciones y campos, incluyendo:

1. **Física:** En física, los caminos aleatorios se utilizan para modelar el movimiento de partículas en un medio, como el movimiento browniano de partículas suspendidas en un líquido.

2. **Finanzas:** En finanzas, los caminos aleatorios se utilizan para modelar el comportamiento de los precios de los activos financieros, como las acciones en el mercado de valores.

3. **Biología:** En biología, los caminos aleatorios se utilizan para modelar el movimiento de animales y el comportamiento de microorganismos.

4. **Ciencias de la computación:** En ciencias de la computación, los caminos aleatorios se utilizan en algoritmos de optimización y en la generación de números aleatorios.

5. **Simulación:** Los caminos aleatorios se utilizan en la simulación de sistemas complejos para modelar la incertidumbre y la variabilidad.

Un ejemplo simple de un camino aleatorio en una dimensión unidimensional podría ser el siguiente: comienzas en el punto cero en una línea, y en cada paso, lanzas una moneda justa. Si sale cara, das un paso hacia adelante (+1 en la línea), y si sale cruz, das un paso hacia atrás (-1 en la línea). Repites este proceso varias veces para ver hacia dónde te lleva el camino.

La teoría de los caminos aleatorios es una rama importante de las matemáticas y la probabilidad, y se ha utilizado en una amplia variedad de aplicaciones para modelar comportamientos estocásticos y fenómenos aleatorios en el mundo real.

'''


import random

def random_walk(steps):
    position = 0  # La posición inicial es 0 en la línea.
    
    for _ in range(steps):
        # Genera un número aleatorio entre 0 y 1.
        # Si es 0, da un paso hacia atrás; si es 1, da un paso hacia adelante.
        step = random.choice([-1, 1])
        position += step
        
        # Imprime la posición después de cada paso.
        print(f"Posición actual: {position}")
    
    return position

# Número de pasos en el camino aleatorio
num_steps = 20

final_position = random_walk(num_steps)
print(f"Posición final después de {num_steps} pasos: {final_position}")


'''
En este programa, random_walk simula un camino aleatorio dado un número de pasos steps. En cada paso, se genera un número aleatorio que determina si el agente da un paso hacia adelante (+1) o hacia atrás (-1). La posición se actualiza en consecuencia y se imprime después de cada paso.

Puedes ajustar num_steps para cambiar la longitud del camino aleatorio. Cada vez que ejecutes el programa, obtendrás una secuencia de pasos aleatorios y una posición final diferente. Este es un ejemplo simple de un camino aleatorio en una dimensión, pero los conceptos se pueden expandir y utilizar en problemas más complejos y aplicaciones en física, estadísticas, y más.
'''