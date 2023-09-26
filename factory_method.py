from abc import ABC, abstractmethod

# Definición de la interfaz OrderService
class OrderService(ABC):
    @abstractmethod
    def place_order(self, item, quantity):
        pass

# Implementación para pedidos en Estados Unidos
class USOrderService(OrderService):
    def place_order(self, item, quantity):
        print(f"Orden en Estados Unidos: {quantity} {item}(s)")

# Implementación para pedidos en Canadá
class CanadaOrderService(OrderService):
    def place_order(self, item, quantity):
        print(f"Orden en Canadá: {quantity} {item}(s)")

# Fábrica base para crear instancias de OrderService
class OrderServiceFactory(ABC):
    @abstractmethod
    def create_order_service(self):
        pass

# Fábrica concreta para crear instancias de OrderService en Estados Unidos
class USOrderServiceFactory(OrderServiceFactory):
    def create_order_service(self):
        return USOrderService()

# Fábrica concreta para crear instancias de OrderService en Canadá
class CanadaOrderServiceFactory(OrderServiceFactory):
    def create_order_service(self):
        return CanadaOrderService()

# Cliente
def main():
    country = "US"  # Cambia el país para probar diferentes implementaciones
    if country == "US":
        factory = USOrderServiceFactory()
    elif country == "Canada":
        factory = CanadaOrderServiceFactory()
    else:
        raise ValueError("País no compatible")

    order_service = factory.create_order_service()
    order_service.place_order("camiseta", 5)

if __name__ == "__main__":
    main()
