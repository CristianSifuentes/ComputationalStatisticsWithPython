'''
En este ejemplo, hemos utilizado sys.setrecursionlimit(1500) para aumentar el límite de recursión a 1500.
 Esto permitirá que la función recursiva fibonacci_recursive se llame más veces antes de alcanzar 
 el límite de recursión predeterminado.

Sin embargo, ten en cuenta que modificar el límite de recursión no es una solución ideal 
para problemas de eficiencia, ya que podría llevar a un desbordamiento de la pila en 
casos extremos. En lugar de eso, es preferible utilizar enfoques de programación dinámica o 
iterativa para mejorar la eficiencia de tus algoritmos.
'''


import sys

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Aumentar el límite de recursión (solo con fines de demostración, no recomendado en la práctica)
sys.setrecursionlimit(1500)

n = 10
fibonacci_result = fibonacci_recursive(n)
print(f"The {n}-th Fibonacci number is: {fibonacci_result}")
