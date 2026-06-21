class Cliente:
    """Clase que representa a un cliente del restaurante."""
    
    def __init__(self, cedula: str, nombre: str):
        # Inicializa los atributos del cliente y una lista para sus pedidos
        self.cedula = cedula
        self.nombre = nombre
        self.historial_pedidos = []

    def agregar_pedido(self, producto) -> None:
        """Agrega un objeto Producto al historial del cliente."""
        self.historial_pedidos.append(producto)

    def calcular_total_consumido(self) -> float:
        """Suma el precio de todos los productos consumidos."""
        total = sum(producto.precio for producto in self.historial_pedidos)
        return total

    def __str__(self) -> str:
        # Retorna el estado actual del cliente y cuántos items ha pedido
        return f"Cliente: {self.nombre} (ID: {self.cedula}) - Items pedidos: {len(self.historial_pedidos)}"