"""
Constructor y metodos de la clase Estadio
"""
class Estadio:
    """Clase Estadio es una clase que representa un Estadio de futbol donde se jugarán los juegos de la Eurocopa 2024\n
    
    Atributos:\n
    id: string que representa el id del estadio\n
    name: string que representa el nombre del estadio\n
    city: string que representa la ciudad del estadio\n
    capacity: string que representa la capacidad del estadio\n
    restaruants: lista que representa los restaruants que se encuentran en el estadio\n
    
    Metodos:\n
    show: Muestra la informacion del estadio"""

    #Constructor de la clase Estadio
    def __init__(self, id, name, city, capacity, restaurantes):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurantes = restaurantes

    def show(self):
        """Muestra en la consola los datos del estadio"""
        print(f"Id: {self.id}\nNombre: {self.name}\nCiudad: {self.city}\nCapacidad: {self.capacity}\nRestaruantes: ")
        for restaruant in self.restaurantes:
            print(restaruant.name)
            
    def nombre_show(self):
        """Muestra en la cosola el nombre de un estadio"""
        print(self.name)