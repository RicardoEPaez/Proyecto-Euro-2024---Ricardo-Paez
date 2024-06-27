#Importamos las clases que creamos anteriormente a este clase
import json
import math
import urllib.request
import requests
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Producto import Producto
from Restaurant import Restaurant
from Cliente import Cliente
from Ticket import Ticket
from Utilitarios import *


#Modulo Principal de la Aplicacion Euro 2024
class App:
    #Constructor de la clase APP
    def __init__(self):
        #Se van a guardar las informacion sacadas de las APIS
        self.equipos = []
        self.estadios = []
        self.partidos = []
        #self.restaurantes = []
        #self.productos = []
        self.clientes = []
        self.tickets = []
        
#Este metodo inicia el programa y carga el programa
    def run(self):
        self.informacion_partidos()
        print("Bienvenido a la aplicación EURO 2024")
        while True:
            #Despliegue Menu Principal
            print("\n--------------------------------------")
            print("          APLICACIÓN EURO 2024          ")
            print("--------------------------------------\n")
            print("--------------")
            print("Menú Principal")
            print("-------------- \n")
            print("1. Gestión de Partidos y Estadios")
            print("2. Gestión de Ventas de Entradas")
            print("3. Gestión de Asistencia de Partidos")
            print("4. Gestión de Restaruantes")
            print("5. Gestión de Ventas de Restarauntes")
            print("6. Indicadores de Gestión (Estadísticas)")
            print("7. Salir del programa de la EURO 2024")
        
            opcion = input("\nIngrese la opción deseada: ")
            while not opcion.isnumeric() or int(opcion) > 7:
                opcion = input("\nOpción Invalida. Asegurese de ingresar un valor numérico del 1 al 7:  ")
            opcion = int(opcion)
            if opcion == 1:
                self.gestion_partidos_estadios()
            elif opcion == 2:
                self.gestion_ventas_entradas()
            elif opcion == 3:
                self.gestion_asistencia_partidos()
            elif opcion == 4:
                self.gestion_restaurantes()
            elif opcion == 5:
                self.gestion_ventas_restaurantes()
            elif opcion == 6:
                self.indicadores_gestion()
            elif opcion == 7:
                print("\nUd. ha salido satisfactoriamente de la alplicación EURO 2024. Hasta pronto.\n")
                break
 
#Este metodo inicia la gestion de partidos y estadios            
    def gestion_partidos_estadios(self):
        while True:
            print("\n-------------------------------------")
            print("Menú Gestión de Partidos y Estadios")
            print("----------------------------------- \n")
            print("1. Mostrar todos los partidos de un pais")
            print("2. Mostrar todos los partidos que se jugarán en un estadio específico")
            print("3. Mostrar todos los partidos que se jugarán en una fecha determinada")
            print("4. Regresar al Menú Principal\n")
            opcion = input("\nIngrese un valor numérico del 1 al 4: ")
            while not opcion.isnumeric() or int(opcion) > 4:
                opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1 al 4: ")
            opcion = int(opcion)
            if opcion == 1:
                respuesta = input("\nIngresa el nombre del país que desea consultar: ").lower()
                encontrado = False
                for partido in self.partidos:
                    if partido.home.name.lower() == respuesta or partido.away.name.lower() == respuesta:
                        partido.show()
                        encontrado = True
                if encontrado == False:
                    print(f"\nNo se encontró el pais {respuesta}\n")                        
            elif opcion == 2:
                respuesta = input("\nIngrese el nombre del estadio que desea consultar: ").lower()
                encontrado = False
                for estadio in self.estadios:
                    if estadio.name.lower() == respuesta:
                        estadio.show()
                        encontrado = True
                if encontrado == False:
                    print(f"\nNo se encontró el estadio {respuesta}\n")
            elif opcion == 3:
                respuesta = input("\nIngrese la fecha que desea consultar (aaaa-mm-dd): ").lower()
                encontrado = False 
                for partido in self.partidos:
                    if partido.date.lower() == respuesta:
                        partido.show()
                        encontrado = True 
                if encontrado == False:
                    print(f"\nNo se encontró la fecha {respuesta}\n")
            elif opcion == 4:
                break 
            
#Este metodo se visualiza la gestion de ventas, entradas            
    def gestion_ventas_entradas(self):
        print("---Datos del cliente---")
        #Les preguntamos al usuario sus datos y hacemos su respectiva validacion por cada input
        nombre_cliente = input("Escribe su nombre: ").lower()
        while not nombre_cliente.isalpha():
            nombre_cliente = input("Escribe su nombre valido: ").lower()    
        
        ci_cliente = input("Indique su Cedula de Identidad (No utilice puntos, ni letras. Ejem: 332321): ")    
        while not ci_cliente.isdigit():
            ci_cliente = input("CI. Invalida. Indique un valor de CI correcto: ") 
        
        edad_cliente = input("Indique su Edad: ")
        while not edad_cliente.isnumeric() or not int(edad_cliente) > 0:
            edad_cliente = input("Ingrese una edad valida: ")
       
        #Hacemos un breve menú donde el usuario pordra ver la opcion de entradas
        print("\n----Opcion de Entrada----\n")
        print("1. Vip")
        print("2. General\n")
        #Les preguntamos el usuario que entrada desea comprar y hacemos la validacion 
        tipo_entrada = input("Ingrese un numero para seleccionar la entrada: ")
        while tipo_entrada != "1" and tipo_entrada != "2":
            tipo_entrada = input("Opción Invalida. Ingrese de nuevo un número (1 o 2) para seleccionar el tipo de entrada: ")
        #Validamos si el usuario marco (1 o 2) y se lo asignamos a la variable entrada_vip_general
        if tipo_entrada == "1":
            tipo_entrada = "vip"
        elif tipo_entrada == "2":
            tipo_entrada = "general"
        
        #Recorremos partido en self.partidos y hacemos la enumeracion con inicio 1
        print("Lista de partidos posibles\n")
       
        for partido in self.partidos:
            partido.show()
        
        #Le preguntamos al usuario que ingrese un numero de acuerdo a lista de partido y hacemos la validacion
        nro_partido = input("Ingrese el número de partido a seleccionar: ")
        while not nro_partido.isnumeric() or int(nro_partido) > len(self.partidos):
                nro_partido = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")
        
        nro_partido = int(nro_partido)
        for partido in self.partidos:
            if partido.number == nro_partido:
                break
        
        #Creamos un objeto donde se va a guardar la informacion propoccionada por el cliente
        datos_cliente = Cliente(nombre_cliente, ci_cliente, edad_cliente, partido, tipo_entrada )
        
        #Creamos una variable partido_stadium = partido.satadium_id
        partido_stadium = partido.stadium_id
     
        #Recorremos estadio en todos los estadios
        for estadio in self.estadios:
            #Validamos si el partido estadio va a ser igual al estadio id
            if partido_stadium == estadio.id:
                partido_stadium = estadio

        #Si la entrada es general se le asignada la primera capacidad de asientos  
        if tipo_entrada == "general":
            capacidad_asientos = partido_stadium.capacity[0]
            #Le asignamos a general un valor
            precio = 35
        #Si la entrada es vip se le asigna la segunda capacidad de asientos
        elif tipo_entrada == "vip":
            capacidad_asientos = partido_stadium.capacity[1]
            #Le asignacmos asiento vip un valor
            precio = 75
        
        #Creamos una lista de abecedeario que van hacer las columnas
        columna_asientos = ["A","B","C","D","E","F","G","H","I","J"]
        cantidad_filas = math.ceil(capacidad_asientos/10)
        
     
        #Muestra del Mapa de Asientos
        
        print(f"\nMapa de Asientos del Estadio: {partido_stadium.name}\n")
        print("-----------------------------")
        for nro_fila in range(1, cantidad_filas + 1):
            fila = []
            if nro_fila < cantidad_filas:
                for letra in columna_asientos:
                    fila.append(f"{letra}{nro_fila}")
            elif nro_fila == cantidad_filas:
                for i in range(0, capacidad_asientos % (cantidad_filas - 1)):
                    fila.append(f"{columna_asientos[i]}{nro_fila}")
            print(fila)
            
        
        #Lectura y Validacion del asiento seleccionado
        while True:
            asiento_asig = input("\nIngrese el asiento de su preferencia: ").upper()
            if len(asiento_asig) >= 2: 
                asiento_asig_columna = asiento_asig[0]
                asiento_asig_fila = int(asiento_asig.replace(asiento_asig[0], ""))
                col_asientos_ultfila = columna_asientos[0:capacidad_asientos % (cantidad_filas - 1)]
                if asiento_asig_fila < cantidad_filas:
                    if asiento_asig_columna not in columna_asientos:
                        print("\nAsiento Inválido. Intente de nuevo\n")
                    else:
                        if tipo_entrada == "vip":
                            if asiento_asig in partido.asientos_ocupados_vip:
                                print("\nEste asiento ya esta ocupado. Intente de nuevo\n")
                            else:
                                break
                        else:
                            if asiento_asig in partido.asientos_ocupados_general:
                                print("\nEste asiento ya esta ocupado. Intente de nuevo\n")
                            else:
                                break
                elif asiento_asig_fila == cantidad_filas:
                    if asiento_asig_columna not in col_asientos_ultfila:
                        print("\nAsiento Inválido. Intente de nuevo\n")
                    else:
                        break
                elif asiento_asig_fila > cantidad_filas:
                    print("\nAsiento Invalido. Intente de nuevo\n")
            else:
                print("\nAsiento Invalido. Intente de nuevo\n")
            
        if es_vampiro(ci_cliente):
            precio_descuento = precio / 2
            iva = round(precio_descuento * 0.16, 2)
            precio_total = precio_descuento + iva
            print("\nFelicidades. La C.I. que ingresó es un número vampiro, por lo tanto se aplicará un descuento del 50%\n")
        else:
        #Creamos variables de precio con descuento, iva, total para la cedula no vampiro
            iva = round(precio * 0.16,2)
            precio_total = precio + iva
            precio_descuento = 0
            print("\nLa C.I. que ingresó no es vampiro por lo tanto no ha sido beneficiado con un descuento\n")
           
        #Mostramos una factura al cliente con el Asiento, Subtotal, Desc0uento, Iva, Monto Final        
        print("----- FACTURA DEL CLIENTE ----")
        print(f"Asiento: {asiento_asig}")
        print(f"Precio Entrada: {precio}")
        print(f"Descuento: {precio_descuento}")
        print(f"Subtotal: {precio - precio_descuento}")
        print(f"IVA (16%): {iva}")
        print("---------------------------------------")
        print(f"Total: ${precio_total}")
    
        #Le preguntamos al usuario si desea realizar la compra    
        pago_ticket = input("Desea realizar su compra del ticket(Si o No)?: ").lower()
        if pago_ticket == "si":
            print("Su compra ha sido existosa")
            codigo_seguridad = generar_codigo_seguridad()
            ticket = Ticket(ci_cliente, partido, tipo_entrada, asiento_asig, codigo_seguridad)
            self.clientes.append(datos_cliente)        
            self.tickets.append(ticket)
            print("******************************************************************************************")
            print(f"                        TICKET {ticket.tipo_de_asiento}                                  ")                           
            print(f"                          {partido.home.name}  vs {partido.away.name} ")
            print(f"                       Estadio: {estadio.name}")
            print(f"                         Fecha: {partido.date}")
            print(f"                   Codigo seguridad: {codigo_seguridad}")
            print("******************************************************************************************")
            if tipo_entrada == "vip":
                partido.asientos_ocupados_vip.append(asiento_asig)
            elif tipo_entrada == "general":
                partido.asientos_ocupados_general.append(asiento_asig)
        else:
            print("Su compra no ha sido procesada con éxito")
    

#Este metodo se visualiza la gestion de las asistencias de los partidos
    def gestion_asistencia_partidos(self):
        for partido in self.partidos:
            partido.show()
            
        nro_partido = input("Ingrese el número de partido del ticket que desea consultar: ")
        while not nro_partido.isnumeric() or int(nro_partido) > len(self.partidos):
                nro_partido = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")               
        nro_partido = int(nro_partido)
        for partido in self.partidos:
            if partido.number == nro_partido:
                break
            
        
        codigo_seguridad = input("Ingrese el codigo de seguridad del ticket: ")
        ticket_valido = False
        for ticket in self.tickets:
            if ticket.codigo_seguridad == codigo_seguridad and ticket.partido.number == nro_partido:
                if ticket.asistencia == False:
                    ticket.asistencia = True
                    print(f"Ticket: {codigo_seguridad} Valido. Se registró asistencia")
                    ticket_valido = True
                    break
                else:
                    print(f"Ticket: {codigo_seguridad} invalido. El ticket ya ha sido registrado previamente")
                    ticket_valido = True                  
        if ticket_valido == False:
            print(f"Ticket: {codigo_seguridad} es Invalido. No existente")            
                 
            
    def gestion_restaurantes(self): 
        
        print("\n=======================")
        print("Gestion de Restaurantes")
        print("=======================\n")
        
        print("\nListado de Estadios")
        print("-------------------\n")
        for i, estadio in enumerate(self.estadios):
            i += 1
            print(i)
            estadio.nombre_show()
        opcion=input("\nSeleccione el número del estadio donde se ubica el restaurante a gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(self.estadios):
            opcion = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")
        index_estadio = int(opcion) - 1
        estadio = self.estadios[index_estadio]
        
        print(f"\nListado de Restaurantes ubicados en {estadio.name}")
        print("--------------------------------------------------------------")
        for i, restaurante in enumerate(estadio.restaurantes):
            i += 1
            print(i)
            restaurante.nombre_show()
        opcion=input("\nSeleccione el número del restaurante que desea gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(estadio.restaurantes):
            opcion = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")
        index_restaurante = int(opcion) - 1
        restaurante = estadio.restaurantes[index_restaurante]
    

        while True:
            print("\n========================================================")
            print(f"Gestion del Restaurante {restaurante.name}")
            print("=========================================================\n")
            print("1. Buscar Productos por nombre")
            print("2. Buscar Productos por tipo")
            print("3. Buscar Productos por rango de precio")
            print("4. Regresar al Menu Principal\n")
            opcion = input("Ingrese la opción deseada (1-4): ")
            while not opcion.isnumeric() or int(opcion) > 4:
                opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1-4: ")
            opcion = int(opcion)  
            #Opcion 1: Busqueda de un producto por nombre 
            if opcion == 1:
                encontrado = False
                print(f"\nBúsqueda de productos del restaurant {restaurante.name} por nombre de producto")
                print("======================================================================================\n")
                nombre_producto = input("\nIntroduzca el nombre del producto que desea buscar: ").title()
                print(nombre_producto)
                for producto in restaurante.products:
                    if producto.name == nombre_producto:
                        print("\n------------------------")
                        print(f"Información del producto:")
                        print(f"------------------------\n")
                        producto.show()
                        encontrado = True
                        break
                if not encontrado:
                    print(f"\nProducto {nombre_producto} no encontrado. Intente otra búsqueda")
                    
            elif opcion == 2:
                print(f"\nBúsqueda de productos del restaurant {restaurante.name} por tipo de producto")
                print("=======================================================================================\n")
                print("1. Alimento")
                print("2. Bebida")
                opcion = input("\nSeleccione el número (1 o 2) del tipo de producto que desea consultar: ")
                while not opcion.isnumeric() or int(opcion) > 2:
                    opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1-2: ")    
                opcion = int(opcion)
                encontrado = False
                if opcion == 1:
                    print("\n-----------------------------")
                    print(f"Productos del Tipo: Alimento")
                    print(f"-----------------------------\n")
                    for producto in restaurante.products:
                        if producto.clasificacion == "alimento":
                            producto.show()
                            encontrado = True
                    if not encontrado:
                        print(f"\nNo existen productos de tipo Alimento. Intente otra búsqueda")
                else:
                    print("\n-----------------------------")
                    print(f"Productos del Tipo Bebida:")
                    print(f"-----------------------------\n")
                    for producto in restaurante.products:
                        if producto.clasificacion == "bebida":
                            producto.show()
                            encontrado = True
                    if not encontrado:
                        print(f"\nNo existen productos de tipo Bebida. Intente otra búsqueda")        
            elif opcion == 3:
                print(f"\nBúsqueda de productos del restaurante {restaurante.name} por rango de precio")
                print("=======================================================================================\n")
                precio_minimo = input("Ingrese el precio mínimo con IVA): ")
                while not precio_minimo.isnumeric() or float(precio_minimo) < 0:
                    precio_minimo = input("\n:Precio invalido. El precio minimo debe ser un valor numerico mayor o igual a 0: ") 
                precio_minimo = round(float(precio_minimo) ,2)
                precio_maximo = input("Ingrese el precio máximo con IVA: ")
                while not precio_maximo.isnumeric() or float(precio_maximo) < precio_minimo:
                    precio_maximo = input("\n:Precio inválido. El precio máximo debe ser un valor numérico mayor al precio mínimo : ")
                precio_maximo = round(float(precio_maximo),2)    
                print("---------------------------------------------------------------------------------------------")
                print(f"\nListado de productos con precio entre {precio_minimo} y {precio_maximo}")
                print("---------------------------------------------------------------------------------------------\n")
                encontrado = False
                for producto in restaurante.products:
                    if precio_minimo <= producto.price <= precio_maximo:
                        producto.show()
                        encontrado = True
                if not encontrado:
                        print(f"\nNo existen productos con precio entre {precio_minimo} y {precio_maximo}")           
            elif opcion == 4:
                break
        
   
    
#Este metodo se visualiza la gestion de las ventas de restaurantes
    def gestion_ventas_restaurantes(self):
        print("\n==============================")
        print("Gestion de Venta en Restaurantes")
        print("================================\n")
        print("\nListado de Estadios")
        print("-------------------\n")
        for i, estadio in enumerate(self.estadios):
            i += 1
            print(i)
            estadio.nombre_show()
        opcion=input("\nSeleccione el número del estadio donde se ubica el restaurante a gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(self.estadios):
            opcion = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")
        index_estadio = int(opcion) - 1
        estadio = self.estadios[index_estadio]
        print(f"\nListado de Restaurantes ubicados en {estadio.name}")
        print("--------------------------------------------------------------")
        for i, restaurante in enumerate(estadio.restaurantes):
            i += 1
            print(i)
            restaurante.nombre_show()
        opcion=input("\nSeleccione el número del restaurante que desea gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(estadio.restaurantes):
            opcion = input("\nOpción Invalida. Asegúrese de ingresar un valor numerico válido: ")
        index_restaurante = int(opcion) - 1
        restaurante = estadio.restaurantes[index_restaurante]
        
                
    
    
    
        
#Este metodo se visualiza la gestion de las ventas de restaurantes
    def indicadores_gestion(self):
        while True:
            print("\n-------------------------------------")
            print("Menú Gestión de Indicadores de Gestión")
            print("-------------------------------------- \n")
            print("1. Mostar el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)? ")
            print("2. Mostrar lista con la asistencia de los partidos de mejor a peor")
            print("3. Mostar el Partido con mayor asistencia")
            print("4. Mostrar el Partido con mayor boletos vendidos")
            print("5. Mostar los Top 3 productos mas vendidos en el restaurante")
            print("6. Mostrar los Top 3 clientes(los que compraron mas boletos)")
            print("7. Realiza un grafico con las estadisticas mediante con las librerias de matplotib o Bokeh\n")
            print("8. Regresar al Menú Principal")
            opcion = input("Ingrese la opción deseada (1-8): ")
            while not opcion.isnumeric() or int(opcion) > 8:
                opcion = input("Opción Inválida. Asegurese de ingresar un valor numérico del 1-8: ")
            opcion = int(opcion)
            if opcion ==1:
                pass
            elif opcion ==2:
                pass
            elif opcion ==3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion ==6:
                pass
            elif opcion == 7:
                pass
            elif opcion == 8:
                break 
                
#Esta funcion nos permite sacar la informacion de los partidos donde fueron sacado desde la URL
    def informacion_partidos(self):
        #Url de los equipos , estadios , partidos 
        url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        url_estadios = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        #Sacamos la informacion de equipos, estadios, y partidos mediante los URL usando (urllib.request.urlopen)
        with urllib.request.urlopen(url_equipos) as response:
            body_json = response.read()
        informacion_equipos = json.loads(body_json)
        with urllib.request.urlopen(url_estadios) as response:
            body_json = response.read()
        informacion_estadios = json.loads(body_json)
        with urllib.request.urlopen(url_partidos) as response:
            body_json = response.read()
        informacion_partidos = json.loads(body_json)
        #Recorrer equipo en infomacion de quipos mediante el for
        for equipo in informacion_equipos:
            #Creamos un objeto donde se va a guardar la informacion y agregamos el objeto creado a lista self.equipos
            grupo = Equipo(equipo["id"], equipo["code"],equipo["name"],  equipo["group"])
            self.equipos.append(grupo)
        #Recorrer estadio en la informacion de estadios
        for estadio in informacion_estadios:
            #Creamos una lista vacia donde se va a guardar los restaurantes internos
            restaurantes_internos = []
            #Recorremos restaurant en estadio[restaurants]
            for restaurant in estadio["restaurants"]:
                #Creamos una lista vacia donde se va a guardar los productos internos
                productos_internos = []
                #Recorremos product in restaurants en productos
                for product in restaurant["products"]:
                    #Creamos un objeto donde vamos a guardar la informacion
                    if product["adicional"] == "alcoholic" or product["adicional"] == "non-alcoholic":
                        clasificacion = "bebida"
                    else:
                        clasificacion = "alimento"
                    product = Producto(product["name"], product["quantity"], round(float(product["price"]) * 1.16,2), product["stock"], clasificacion, product["adicional"])
                    #Se le agreamos a la lista vacia de los productos internos le vamos agregando el objeto creado (product) y tambien se lo agregamos self.productos
                    productos_internos.append(product)
                    #self.productos.append(product)
                #Creamos un objeto donde vamos a guardar la informacion, tambien se lo vamos a agregar a restaurantes_internos que es listaaa vacia, y a self.restaruantes
                restaurant = Restaurant(restaurant["name"], productos_internos)
                restaurantes_internos.append(restaurant)
                #self.restaurantes.append(restaurant)
            #Creamos un obejto que se va a llamar recinto donde se va a guardar la informacion y se los vamos a agregar a self.estadios
            recinto = Estadio(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"], restaurantes_internos)
            self.estadios.append(recinto)
        #Recorrer partido en la informacion de partidos
        for partido in informacion_partidos:
            #Creamos strings vacios 
            home = ""
            away = ""
            #Recorrer equipos in self.equipos
            for equipo in self.equipos:
                #Comparamos y se lo asignamos al string vacio
                if partido["home"]["id"] == equipo.id:
                    home = equipo
                elif partido["away"]["id"] == equipo.id:
                    away = equipo 
            #Creamos un objeto donde vamos a guardar la informacion y se los vamos a agregar a self.partidos   
            juego = Partido(partido["id"],partido["number"], home , away , partido["date"],  partido["group"], partido["stadium_id"])
            self.partidos.append(juego)