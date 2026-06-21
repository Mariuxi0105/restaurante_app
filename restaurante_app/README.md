# 🍔 Sistema de Gestión de Restaurante (POO en Python)

## 👤 Información del Estudiante
* **Nombre Completo:** Mariuxi Jessenia Tejada Mayorga
* **Asignatura:** Programación Orientada a Objetos
* **Semana:** Actividad - Semana 4

---

## 📝 Descripción del Sistema
Este proyecto implementa un sistema básico para un restaurante utilizando el paradigma de **Programación Orientada a Objetos (POO)**. Permite administrar de manera automatizada el menú de productos (platillos/bebidas) y registrar el historial de consumo individual de cada cliente para calcular el total a pagar de forma dinámica.

---

## 📁 Estructura del Repositorio
El repositorio respeta estrictamente la organización modular solicitada por la rúbrica:

* **`restaurante_app/`** (Carpeta raíz del software)
  * **`modelos/`**
    * `producto.py`: Clase entidad que modela un producto (ID, nombre, precio) y su representación textual.
    * `cliente.py`: Clase entidad que gestiona los datos del cliente y calcula su consumo acumulado.
  * **`servicios/`**
    * `restaurante.py`: Módulo controlador encargado de centralizar el menú y emitir el reporte final.
  * `main.py`: Punto de arranque que orquesta la ejecución del sistema, instanciando objetos y métodos.

---

## 💡 Reflexión: Importancia de la Modularización y Separación de Responsabilidades
Modularizar el software y separar responsabilidades es fundamental en el desarrollo moderno porque:
1. **Facilita el mantenimiento:** Si se requiere modificar la lógica de los precios, solo se altera el módulo correspondiente sin afectar el flujo del cliente.
2. **Promueve la legibilidad:** Divide un problema complejo en componentes pequeños, ordenados y comprensibles, evitando códigos masivos y desorganizados.
3. **Escalabilidad y reutilización:** Permite reutilizar clases existentes en otros módulos o expandir el sistema (por ejemplo, agregando un módulo de facturación) de manera limpia y sin romper el código base.