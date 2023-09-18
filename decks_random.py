'''
Claro, puedo mostrarte un ejemplo de un programa en Python que crea manos de cartas y utiliza conceptos de probabilidad para contar cuántos pares, ases, picas y corazones hay en una mano de cartas aleatoria de una baraja estándar. Para este ejemplo, usaremos la biblioteca random para simular la selección aleatoria de cartas de la baraja.

'''
import random

# Define los palos y las cartas de figuras
palos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
cartas_figuras = ['Jota', 'Reina', 'Rey', 'As']

# Crea una lista de todas las cartas en una baraja estándar
baraja = [(numero, palo) for numero in range(2, 11) for palo in palos]  # Cartas numeradas
baraja.extend([(figura, palo) for figura in cartas_figuras for palo in palos])  # Cartas de figuras

def crear_mano(numero_cartas=5):
    """
    Crea una mano de cartas aleatorias.
    """
    mano = random.sample(baraja, numero_cartas)
    return mano

def contar_caracteristicas(mano):
    """
    Cuenta cuántos pares, ases, picas y corazones hay en una mano de cartas.
    """
    pares = 0
    ases = 0
    picas = 0
    corazones = 0

    for carta in mano:
        numero, palo = carta
        if numero == 'As':
            ases += 1
        elif mano.count(carta) == 2:
            pares += 1
        if palo == 'Picas':
            picas += 1
        elif palo == 'Corazones':
            corazones += 1

    return pares, ases, picas, corazones

# Crear una mano de 7 cartas
mano_de_cartas = crear_mano(7)

# Contar las características en la mano
pares, ases, picas, corazones = contar_caracteristicas(mano_de_cartas)

# Mostrar la mano y las características
print("Mano de Cartas:")
for carta in mano_de_cartas:
    print(f"{carta[0]} de {carta[1]}")

print("\nCaracterísticas de la Mano:")
print(f"Pares: {pares}")
print(f"Ases: {ases}")
print(f"Picas: {picas}")
print(f"Corazones: {corazones}")



'''
Este programa crea una mano de cartas aleatorias y luego cuenta cuántos pares, ases, picas y corazones hay en esa mano. Cada vez que ejecutes el programa, obtendrás una mano de cartas diferente y verás las características correspondientes de esa mano.
'''