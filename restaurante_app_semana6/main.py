# main.py
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def arrancar_programa():
    # Instanciamos la administración del negocio
    negocio = Restaurante("Sabores Amazónicos")
    
    print("=== INICIANDO REGISTRO DE LA CARTA ===")
    # Instanciación de platos solicitados
    plato_uno = Platillo("Picaña", 16.50, 20)
    plato_dos = Platillo("Pulpo asado", 18.00, 25)
    
    # Instanciación de las bebidas solicitadas
    bebida_uno = Bebida("Jugo de maracuyá", 2.50, 400)
    bebida_dos = Bebida("Jugo de limón con hierbabuena", 3.00, 450)
    
    # Guardar todo en la lista de servicios
    negocio.registrar_item(plato_uno)
    negocio.registrar_item(plato_dos)
    negocio.registrar_item(bebida_uno)
    negocio.registrar_item(bebida_dos)
    
    # Verificación práctica de la protección de datos (encapsulación)
    print("\n=== VERIFICACIÓN DE CONTROL DE PRECIOS ===")
    print(f"Costo inicial de {bebida_uno.nombre}: ${bebida_uno.consultar_precio():.2f}")
    print("Intentando alterar el precio con un número negativo (-2.00)...")
    bebida_uno.actualizar_precio(-2.00)
    
    # Despliegue del menú final interactuando con el polimorfismo
    negocio.imprimir_carta_completa()

if __name__ == "__main__":
    arrancar_programa()