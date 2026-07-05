# modelos/bebida.py
from modelos.producto import Producto

class Bebida(Producto):
    """Especialización para representar líquidos y refrescos del bar."""
    
    def __init__(self, nombre: str, costo_al_publico: float, mililitros: int, en_stock: bool = True):
        # Vinculación con el constructor principal
        super().__init__(nombre, costo_al_publico, en_stock)
        # Atributo particular de las bebidas
        self.mililitros = mililitros

    def obtener_detalles(self) -> str:
        """Modifica la salida base sumando el tamaño de la porción en ml."""
        datos_base = super().obtener_detalles()
        return f" [Bebida] {datos_base} | Porción: {self.mililitros}ml"