"""
Constructor y metodos de la clase Equipo
"""
class Equipo:
    """Clase Equipo es una clase que representa un Equipo de futbol que participa en la Eurocopa 2024\n
    
    Atributos:\n
    id: string que representa el id del equipo\n
    code: string que representa el codigo del equipo\n
    name: string que representa el nombre del equipo\n
    group: string que representa el grupo al que pertenece el equipo\n
    
    Metodos:\n
    show: Muestra los datos del equipo"""
    
    #Constructor de la clase Equipo
    def __init__(self, id, code, name, group):
        self.id = id
        self.code = code
        self.name = name
        self.group = group
        
    #Metodo que muestra la informacion del equipo    
    def show(self):
        """Muestra en la consola los datos del equipo"""
        print(f"Id: {self.id}\nCódigo: {self.code}\nNombre: {self.name}\Grupo: {self.group}\n")

    #Metodo para formato en archivo txt      
    def __str__(self):
        """Formato para escribir informacion del equipo en archivo txt"""
        return f"ID: {self.id}, Código: {self.code}, Nombre: {self.name}, Grupo: {self.group}"
