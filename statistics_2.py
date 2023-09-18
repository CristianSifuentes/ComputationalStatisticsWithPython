'''
Claro, puedo mostrarte un ejemplo en Python que utiliza el patrón de diseño Singleton para calcular la media, la varianza y la desviación estándar de un conjunto de datos. El patrón de diseño Singleton garantiza que solo exista una instancia de la clase encargada de realizar estos cálculos en todo el programa.

Primero, definiremos una clase llamada StatisticsCalculator que implementará el patrón Singleton. Luego, utilizaremos esta clase para calcular la media, la varianza y la desviación estándar de un conjunto de datos de ejemplo.
'''


class StatisticsCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StatisticsCalculator, cls).__new__(cls)
            cls._instance.data = []
        return cls._instance

    def add_data_point(self, value):
        self.data.append(value)

    def calculate_mean(self):
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def calculate_variance(self):
        if not self.data:
            return None
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def calculate_standard_deviation(self):
        variance = self.calculate_variance()
        if variance is None:
            return None
        return variance**0.5


# Uso del Singleton StatisticsCalculator
calculator = StatisticsCalculator()

# Agregar datos de ejemplo
data = [12, 15, 18, 24, 10]
for value in data:
    calculator.add_data_point(value)

# Calcular estadísticas
mean = calculator.calculate_mean()
variance = calculator.calculate_variance()
std_deviation = calculator.calculate_standard_deviation()

print(f"Datos: {data}")
print(f"Media: {mean:.2f}")
print(f"Varianza: {variance:.2f}")
print(f"Desviación Estándar : {std_deviation:.2f}")

'''
En este ejemplo, hemos creado una clase StatisticsCalculator que implementa el patrón Singleton. Esto garantiza que solo haya una instancia de esta clase en todo el programa. La clase puede agregar datos, calcular la media, la varianza y la desviación estándar de los datos agregados.

Luego, hemos creado una instancia de StatisticsCalculator, agregado datos de ejemplo y calculado la media, la varianza y la desviación estándar de esos datos. Esto ilustra cómo usar el patrón Singleton para calcular estadísticas de manera eficiente y organizada en Python.

'''
