"""
Constructor y metodos de la clase Ticket
"""

class Ticket:
    """Clase Ticket es una clase que representa el ticket asignado a un cliente que ha comprado una entrada para asisitir a un juego de la Eurocopa 2024\n
    
    Atributos:\n
    cedula: string que representa la cedula del cliente\n
    partido: referencia al objeto partido\n
    tipo_de_asiento: string que representa el tipo de asiento del cliente: VIP o General\n
    asiento: string que representa la identificacion del asiento del cliente\n
    asistencia: booleano que representa si el cliente ha asistido al juego True: Asistio, False: no asistio\n
    codigo_seguridad: string que representa el codigo de seguridad del ticket\n
    precio_total: monto total facturado (con descuento si aplica)
       
    Metodos:\n
    show: Muestra los datos del ticket"""
    
    #Constructor de la clase Ticket
    def __init__(self, cedula, partido, tipo_de_asiento, asiento, codigo_seguridad, precio_total):
        self.cedula = cedula
        self.partido = partido
        self.tipo_de_asiento = tipo_de_asiento
        self.asiento = asiento
        self.asistencia = False
        self.codigo_seguridad = codigo_seguridad
        self.precio_total = precio_total
      
    def show(self):
        """Muestra en la consola los datos del ticket"""
        print(f"C.I: {self.cedula}\nPartido: {self.partido}\nTipo de asiento: {self.tipo_de_asiento}\nAsiento: {self.asiento}\nCodigo seguridad: {self.codigo_seguridad}\nMonto Total: {self.precio_total}\n")