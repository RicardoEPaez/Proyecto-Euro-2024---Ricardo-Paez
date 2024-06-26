"""
Constructor y metodos de la clase Cliente
"""
class Cliente:
    """Clase Cliente es una clase que representa un cliente que compra un ticket para asisitir a un juego de la Eurocopa 2024\n
    
    Atributos:\n
    nombre: string que representa el nombre del cliente\n
    cedula: string que representa el cedula del cliente\n
    edad: string que representa la edad del cliente\n
    partido: referencia al objeto partido\n
    entrada: referencia al objeto ticket\n
            
    Metodos:\n
    show: Muestra los datos del cliente"""
    
    #Constructor de la clase Cliente que recibe como parametros los atributos de la clase Cliente
    def __init__(self,nombre, cedula, edad, partido, entrada ):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido 
        self.entrada = entrada
               
    def show(self):
        """Muestra en la consola los datos del cliente"""
        print(f"Nombre: {self.nombre}\nC.I.: {self.cedula}\nEdad: {self.edad}\nPartido: {self.partido}\nEntrada: {self.entrada}\n")
        