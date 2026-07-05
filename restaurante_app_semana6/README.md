# Administracion Modular para Restaurante (POO en Python)

**Nombre del Estudiante:** Emily Silvana Pucha Moreira  
**Materia:** Programacion Orientada a Objetos  
**Periodo:** Semana 6  

## Resumen del Proyecto
Este sistema fue desarrollado con el objetivo de estructurar un control de inventario y menu para un restaurante, separando las responsabilidades logicas en modulos independientes dentro de Python. El programa permite clasificar y manejar productos de manera controlada para evitar inconsistencias en los datos financieros o de stock, simulando un entorno de produccion real.

## Arquitectura de Archivos
Para garantizar un software limpio y mantenible, los componentes se dividieron siguiendo este esquema modular:

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Abstraccion e inicializacion de la clase base.
│   ├── platillo.py       # Extension dedicada a alimentos de cocina.
│   └── bebida.py         # Extension dedicada a productos liquidos de barra.
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Logica de almacenamiento y control del menu general.
└── main.py               # Script de arranque y pruebas del entorno.

## Implementacion de Pilares POO

* **Herencia:** La clase base Producto define las propiedades transversales a cualquier articulo del negocio (nombre, precio, en_stock). Las subclases Platillo y Bebida extienden este comportamiento a traves de super(), acoplando variables especificas del area como los minutos de coccion o el volumen en mililitros sin duplicar codigo.
* **Encapsulacion:** El atributo clave del precio se configuro bajo un nivel de visibilidad privado (__precio). Esto impide que agentes externos al archivo alteren los costos de forma descontrolada. El acceso se realiza formalmente mediante consultar_precio() y su alteracion pasa obligatoriamente por filtros logicos en actualizar_precio(), bloqueando montos de caracter negativo o nulo.
* **Polimorfismo:** Se logra mediante la redefinicion del metodo obtener_detalles(). Cada clase hija altera el formato final de salida de forma independiente. Cuando el servicio recorre la lista general en un ciclo unificado, el interprete resuelve dinamicamente cual comportamiento usar basandose puramente en la identidad del objeto activo.

## Conclusion Personal sobre el Enfoque Modular
El diseno de aplicaciones mediante modulos estructurados en POO ofrece una ventaja invaluable en el mantenimiento del software. Al aislar las entidades del negocio en la carpeta modelos y la persistencia o flujos en servicios, el codigo se vuelve sumamente intuitivo de escalar. Si en un futuro el negocio requiere anadir una categoria como Postres, el cambio se limita a construir un archivo nuevo que herede de la base, sin alterar ni poner en riesgo la estabilidad del flujo principal en main.py.