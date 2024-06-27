"""
Constructor y metodos de la clase Venta
"""

class Venta_Restaurant:
    """Clase Venta_Restaurant es una clase que representa la venta de productos de un restaurant a un cliente\n
    
    Atributos:\n
    cliente: referencia al objeto cliente\n
    productos: lista de referencias a objeto Producto\n
    Descuento: descuento por C.I = nro. perfecto\n
    Total: total de la venta\n
    
       
    Metodos:\n
    show: Muestra los datos de la venta"""
    
    #Constructor de la clase Venta_Restaurant 
    def __init__(self, cliente, productos, descuento, total):
        self.cliente = cliente
        self.productos = productos
        self.descuento = descuento
        self.total = total
        
    def show(self):
        """Muestra en la consola los datos de la venta"""
        print(f"Cliente: {self.cliente.name}\nC.I: {self.cliente.cedula}\nProductos: {self.productos}\nDescuento: {self.descuento}\nTotal: {self.total}\n")