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

