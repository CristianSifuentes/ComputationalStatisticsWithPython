'''Claro, puedo mostrarte un ejemplo de un programa en Python que utiliza los conceptos mencionados en probabilidad. En este programa, calcularemos la probabilidad de un evento usando la Ley de Eventos Mutuamente Excluyentes y la Ley Aditiva.

Supongamos que estamos tirando un dado justo (con caras numeradas del 1 al 6) y queremos calcular la probabilidad de obtener un número par o un número impar. Estos dos eventos (obtener un número par y obtener un número impar) son mutuamente excluyentes, ya que no pueden ocurrir al mismo tiempo. Usaremos la Ley Aditiva para calcular la probabilidad total.

python'''
def probability_of_event(event_probability):
    return event_probability

# Probabilidad de obtener un número par en un dado justo
probability_of_even = 3 / 6  # Hay 3 números pares (2, 4, 6) de 6 posibles.

# Probabilidad de obtener un número impar en un dado justo
probability_of_odd = 3 / 6  # Hay 3 números impares (1, 3, 5) de 6 posibles.

# Probabilidad total de obtener un número par o un número impar
total_probability = probability_of_event(probability_of_even) + probability_of_event(probability_of_odd)

print(f"Probabilidad de obtener un número par: {probability_of_even:.2f}")
print(f"Probabilidad de obtener un número impar: {probability_of_odd:.2f}")
print(f"Probabilidad total de obtener un número par o impar: {total_probability:.2f}")


'''En este programa, calculamos la probabilidad de obtener un número par y la probabilidad de obtener un número impar, y luego aplicamos la Ley Aditiva para calcular la probabilidad total de obtener uno de los dos eventos. En este caso, dado que los eventos son mutuamente excluyentes, simplemente sumamos las probabilidades individuales para obtener la probabilidad total. El resultado será 1, ya que garantiza que obtendremos un número par o impar en cada tirada del dado.'''