"""
Constructor y metodos de la clase Venta
"""

class Venta_Restaurant:
    """Clase Venta_Restaurant es una clase que representa la venta de productos de un restaurant a un cliente\n
    
    Atributos:\n
    cliente: referencia al objeto cliente\n
    productos: lista de referencias a objeto Producto\n
    Total: total de la venta\n
    
    Metodos:\n
    show: Muestra los datos de la venta"""
    
    #Constructor de la clase Venta_Restaurant 
    def __init__(self, cliente, productos, restaurante, total):
        self.cliente = cliente
        self.productos = productos
        self.restaurante = restaurante
        self.total = total

        
    def show(self):
        """Muestra en la consola los datos de la venta"""
        print(f"Cliente: {self.cliente.nombre}\nC.I: {self.cliente.cedula}\nProductos: {self.productos}\nNombre Restaurante: {self.restaurante}\nTotal: {self.total}\n")
        
    #Metodo para formato en archivo txt      
    def __str__(self):
        """Formato para escribir informacion del equipo en archivo txt"""
        return f": {self.total}"