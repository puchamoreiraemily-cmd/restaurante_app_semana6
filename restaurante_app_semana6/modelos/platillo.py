# modelos/platillo.py
from modelos.producto import Producto

class Platillo(Producto):
    """Especialización para representar alimentos preparados de la cocina."""
    
    def __init__(self, nombre: str, costo_al_publico: float, minutos_cocina: int, en_stock: bool = True):
        # Inicializamos los atributos heredados de la clase padre
        super().__init__(nombre, costo_al_publico, en_stock)
        # Atributo exclusivo de los platos fuertes
        self.minutos_cocina = minutos_cocina

    def obtener_detalles(self) -> str:
        """Modifica la salida base agregando el tiempo estimado de preparación."""
        datos_base = super().obtener_detalles()
        return f" [Cocina] {datos_base} | Prep: {self.minutos_cocina} min."