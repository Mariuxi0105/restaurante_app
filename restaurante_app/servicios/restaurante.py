# Importamos las clases necesarias desde el paquete de modelos
from modelos.producto import Producto
from modelos.cliente import Cliente

class GestorRestaurante:
    """Clase de servicio que administra el menú y los clientes del restaurante."""
    
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.menu_productos = []
        self.clientes_registrados = []

    def registrar_producto(self, producto: Producto) -> None:
        """Añade un nuevo producto al menú del restaurante."""
        self.menu_productos.append(producto)
        print(f"✔ Producto registrado en el menú: {producto.nombre}")

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra a un cliente en la base de datos del restaurante."""
        self.clientes_registrados.append(cliente)
        print(f"✔ Cliente registrado en el sistema: {cliente.nombre}")

    def mostrar_menu(self) -> None:
        """Imprime en consola todos los productos disponibles."""
        print(f"\n--- MENÚ DE {self.nombre_restaurante.upper()} ---")
        if not self.menu_productos:
            print("El menú está vacío.")
        for prod in self.menu_productos:
            print(prod)  # Llama automáticamente al __str__ de Producto

    def mostrar_reporte_ventas(self) -> None:
        """Muestra el consumo detallado de cada cliente registrado."""
        print("\n--- REPORTE DE CONSUMO POR CLIENTE ---")
        for cli in self.clientes_registrados:
            print(cli)  # Llama automáticamente al __str__ de Cliente
            print(f"  Total a pagar: ${cli.calcular_total_consumido():.2f}")
            print("-" * 40)