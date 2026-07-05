# modelos/producto.py

class Producto:
    """Clase base para la gestión de ítems del menú."""
    
    def __init__(self, nombre: str, costo_al_publico: float, en_stock: bool = True):
        self.nombre = nombre
        # Atributo privado para cumplir con la encapsulación
        self.__precio = 0.0
        self.actualizar_precio(costo_al_publico)
        self.en_stock = en_stock

    # Métodos de lectura y escritura (Getter y Setter)
    def consultar_precio(self) -> float:
        """Retorna el precio resguardado del producto."""
        return self.__precio

    def actualizar_precio(self, nuevo_valor: float):
        """Valida que el monto sea un valor positivo y real antes de asignarlo."""
        if nuevo_valor > 0:
            self.__precio = nuevo_valor
        else:
            print(f" Alerta: El valor ${nuevo_valor} para '{self.nombre}' no es válido.")

    def obtener_detalles(self) -> str:
        """Construye la línea base de información del producto."""
        disponibilidad = "Disponible" if self.en_stock else "No disponible"
        return f"{self.nombre} -> Precio: ${self.__precio:.2f} [{disponibilidad}]"