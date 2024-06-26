"""
Constructor y metodos de la clase Producto
"""
class Producto:
    """Clase Producto es una clase que representa un producto para la venta en alguno de los restaurantes de los estadios de la Eurocopa 2024\n
    
    Atributos:\n
    name: string que representa el nombre del producto\n
    quantity: string que representa la cantidad del producto\n
    price: flotante que representa el precio del producto mas el IVA\n
    stock: string que representa la cantidad de stock del producto\n
    Clasificacion: string que representa la clasificacion del producto: alimento o bebida\n
    adicional: string que representa la categoria del producto: plate, alcoholic, non-alcoholic, package\n
       
    Metodos:\n
    show: Muestra los datos del producto de venta en un restaurant""" 
    
    #Constructor de la clase Producto
    def __init__(self, name, quantity, price, stock, clasificacion, adicional):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.clasificacion = clasificacion
        self.adicional = adicional
        
    
    def show(self):
        """Muestra en la consola los datos del producto de venta en un restaurant"""
        print(f"Nonmbre del Producto: {self.name}\nCantidad: {self.quantity}\nPrecio (incluye IVA): {self.price}\nInventario Disponible: {self.stock}\nClasificación: {self.clasificacion}\nAdicional: {self.adicional}\n")
    
    def __str__(self):
        """Formato para escribir informacion del producto en archivo txt"""
        return f"Nombre Producto: {self.name}, Cantidad: {self.quantity}, Precio (incluye IVA): {self.price}, Inventario: {self.stock}, Clasificación: {self.clasificacion}, Adicional: {self.adicional}"