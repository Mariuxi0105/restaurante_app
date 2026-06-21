# Importamos las clases desde sus respectivos módulos
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import GestorRestaurante

def ejecutar_sistema():
    print("=== INICIALIZANDO SISTEMA DE GESTIÓN DE RESTAURANTE ===\n")
    
    # 1. Instanciar el servicio principal
    mi_restaurante = GestorRestaurante("Sabor Gourmet")

    # 2. Crear objetos de la clase Producto
    prod1 = Producto(101, "Hamburguesa Artesanal", 8.50)
    prod2 = Producto(102, "Papas Fritas Grandes", 3.00)
    prod3 = Producto(103, "Te Helado de la Casa", 1.75)
    
    # 3. Registrar los productos en el servicio
    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)
    mi_restaurante.registrar_producto(prod3)

    # 4. Crear objetos de la clase Cliente
    cliente1 = Cliente("1725489631", "Carlos Andrade")
    cliente2 = Cliente("0914785236", "Elena Mendoza")

    # 5. Registrar los clientes en el servicio
    print("")
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    # 6. Simular pedidos asociando productos a los clientes
    cliente1.agregar_pedido(prod1)
    cliente1.agregar_pedido(prod3)  # Carlos consumió hamburguesa y té
    
    cliente2.agregar_pedido(prod2)
    cliente2.agregar_pedido(prod3)  # Elena consumió papas y té

    # 7. Mostrar la información final organizada en consola
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_reporte_ventas()

if __name__ == "__main__":
    # Arranca la aplicación solo si este archivo se ejecuta directamente
    ejecutar_sistema()
