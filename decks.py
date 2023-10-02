import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    #print(barajas)
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    #print(mano)
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    tercia = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        print('valores', valores)

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:# dos pares dentro de una mano
                pares += 1
                break

        for val in counter.values():
            if val == 3:# dos pares dentro de una mano
                tercia += 1
                break

    probabilidad_par = pares / intentos
    probabilidad_tercia = tercia / intentos

    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')
    print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} barajas es {probabilidad_tercia}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)