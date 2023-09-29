'''
Claro, puedo proporcionarte un ejemplo avanzado en Python que implementa 
el patrón de diseño Observer. En este ejemplo, crearemos un sistema de 
notificación en el que los observadores (suscriptores) recibirán notificaciones 
cuando se produzcan cambios en un objeto observable (sujeto).
'''

from abc import ABC, abstractmethod

# Clase Observable (Sujeto)
class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Clase Observer (Suscriptor)
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Implementación concreta de Observer
class EmailNotifier(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"Enviando correo electrónico a {self._name}: {message}")

# Implementación concreta de Observer
class SMSNotifier(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"Enviando mensaje SMS a {self._name}: {message}")

if __name__ == "__main__":
    # Crear un objeto observable (sujeto)
    subject = Observable()

    # Crear observadores (suscriptores)
    email_notifier = EmailNotifier("Usuario1")
    sms_notifier = SMSNotifier("Usuario2")

    # Registrar observadores en el objeto observable
    subject.add_observer(email_notifier)
    subject.add_observer(sms_notifier)

    # Notificar a los observadores sobre un evento
    subject.notify_observers("Nuevo mensaje: ¡Hola!")

    # Eliminar un observador
    subject.remove_observer(email_notifier)

    # Notificar a los observadores nuevamente
    subject.notify_observers("Otro mensaje: ¡Hola de nuevo!")


    '''
    En este ejemplo:

La clase Observable representa el objeto que puede ser observado y contiene una lista de observadores.

La clase Observer es una clase abstracta que define un método update que los observadores concretos deben implementar.

EmailNotifier y SMSNotifier son implementaciones concretas de observadores que envían notificaciones por correo electrónico y mensajes SMS, respectivamente.

En el bloque principal del programa, creamos un objeto observable llamado subject y dos observadores (email_notifier y sms_notifier). Luego, registramos los observadores en el objeto observable.

Notificamos a los observadores sobre un evento y eliminamos un observador (email_notifier). Luego, notificamos a los observadores nuevamente.

El patrón Observer permite que múltiples observadores se registren para recibir actualizaciones de un objeto observable sin que el observable conozca los detalles de los observadores individuales. Esto facilita la implementación de sistemas de notificación y eventos en los que múltiples partes del sistema deben responder a cambios en un objeto central.
    '''

