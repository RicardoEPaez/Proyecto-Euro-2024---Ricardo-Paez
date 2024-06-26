"""
Constructor y metodos de la Clase Partido
"""
class Partido:
    """Clase Partido es una clase que representa un partido de los juegos de la Eurocopa 2024\n
   
    Atributos:\n
    id: string que representa el id del partido\n
    number: string que representa el numero del partido\n
    home: Referencia al objeto equipo\n
    away: Referencia al objeto equipo\n
    date: string que representa la fecha del partido\n
    group: string que representa el grupo al que pertenece el partido\n
    stadium_id: referencia al objeto estadio\n  
    asientos_ocupados_vip: lista de strings con el identificador de los asientos "VIP" ocupados\n
    asientos_ocupados_general: lista de strings con el identificador de los asientos "General" ocupados\n
   
    Metodos:\n
    show: Muestra la informacion del partido"""

    #Constructor de la clase Partido 
    def __init__(self, id, number, home, away, date, group, stadium_id):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id
        self.asientos_ocupados_vip = []
        self.asientos_ocupados_general = []
               
    def show(self):
        """Muestra en la consola los datos del partido"""
        print(f"Número de Partido: {self.number}\nID Partido: {self.id}\nEquipo Local: {self.home.name}\nEquipo Visitante: {self.away.name}\nFecha: {self.date}\nGrupo: {self.group}\nID del Estadio: {self.stadium_id}\n")