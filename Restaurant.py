"""
Constructor y metodos de la clase Restaurant
"""
class Restaurant:
    """Clase Restaurant es una clase que representa un restaurant de alguno de los estadios de la Eurocopa 2024\n
    
    Atributos:\n
    name: String que representa el nombre del restaurante\n
    products: Lista de strings que representan los productos que ofrece el restaurante\n
       
    Metodos:\n
    show: Muestra el nombre y los productos de un restaurant"""  
    
    
    #Constructor de la Clase Restaurant
    def __init__(self, name, products):
        self.name = name
        self.products = products
        
    def show(self):
        """Muestra en la cosola el nombre y los productos de un restaurant"""
        print(f"Name: {self.name}\nProducts: {self.products}\n")
    
    def nombre_show(self):
        """Muestra en la cosola el nombre de un restaurant"""
        print(self.name)