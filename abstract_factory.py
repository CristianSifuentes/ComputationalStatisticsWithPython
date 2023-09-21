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

# Factory abstracto para crear instancias de OrderService
class OrderServiceFactory:
    @staticmethod
    def create_order_service(country):
        if country == "US":
            return USOrderService()
        elif country == "Canada":
            return CanadaOrderService()
        else:
            raise ValueError("País no compatible")

# Cliente
def main():
    country = "US"  # Cambia el país para probar diferentes implementaciones
    order_service = OrderServiceFactory.create_order_service(country)
    order_service.place_order("camiseta", 5)

if __name__ == "__main__":
    main()
