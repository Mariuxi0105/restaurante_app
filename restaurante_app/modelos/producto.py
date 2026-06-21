class Producto:
    """Clase que representa un platillo o bebida en el restaurante."""
    
    def __init__(self, id_producto: int, nombre: str, precio: float):
        # Inicializa los atributos básicos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        # Retorna una representación en texto del producto
        return f"[{self.id_producto}] {self.nombre} - ${self.precio:.2f}"