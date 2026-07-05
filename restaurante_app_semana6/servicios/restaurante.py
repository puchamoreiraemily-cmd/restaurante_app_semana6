# servicios/restaurante.py
from modelos.producto import Producto

class Restaurante:
    """Clase controladora encargada de la carta y el inventario."""
    
    def __init__(self, nombre_local: str):
        self.nombre_local = nombre_local
        self.carta_productos = []

    def registrar_item(self, item: Producto):
        """Incorpora un nuevo platillo o bebida al catálogo disponible."""
        self.carta_productos.append(item)
        print(f"-> Agregado a la carta de forma exitosa: {item.nombre}")

    def imprimir_carta_completa(self):
        """Recorre el inventario imprimiendo los detalles específicos por polimorfismo."""
        print(f"\n--- MENÚ OFICIAL: {self.nombre_local.upper()} ---")
        if not self.carta_productos:
            print("Por ahora no tenemos opciones registradas.")
            return

        for elemento in self.carta_productos:
            # Aquí ocurre el polimorfismo dinámico de Python
            print(elemento.obtener_detalles())
        print("-" * 40)