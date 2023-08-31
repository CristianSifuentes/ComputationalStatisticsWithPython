'''
En este ejemplo, estamos calculando el n-ésimo número de Fibonacci utilizando programación dinámica. 
La lista dp almacena los valores calculados previamente, 
lo que evita el cálculo repetitivo de números de Fibonacci en iteraciones posteriores.

La idea detrás de la programación dinámica en este caso es que estamos dividiendo 
el problema de calcular el n-ésimo número de Fibonacci en subproblemas más pequeños: 
calcular los números de Fibonacci más pequeños y combinar sus resultados para obtener 
el número de Fibonacci deseado.

Este enfoque mejora significativamente la eficiencia de cálculo 
en comparación con un enfoque recursivo ingenuo, ya que evita r
ecalcular los mismos valores una y otra vez.
'''

def fibonacci_dynamic(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 12334
fibonacci_result = fibonacci_dynamic(n)
print(f"The {n}-th Fibonacci number is: {fibonacci_result}")
