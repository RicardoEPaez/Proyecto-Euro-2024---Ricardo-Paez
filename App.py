#Importamos json, la libreria math, la libreria requests, y la liberia urllib.request
import json
import math
import urllib.request
import requests
#Importamos las clases que creamos anteriormente a este clase
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Producto import Producto
from Restaurant import Restaurant
from Cliente import Cliente
from Ticket import Ticket
from Venta import Venta_Restaurant
from Utilitarios import *


#Modulo Principal de la Aplicacion Euro 2024
class App:
    #Constructor de la clase APP
    def __init__(self):
        '''Listas para almacenar la informacion de las APIs y las que se generen en la App'''
        self.equipos = []
        self.estadios = []
        self.partidos = []
        #self.restaurantes = []
        #self.productos = []
        self.clientes = []
        self.tickets = []
        
#Metodo para la garga e incio de la aplicacion
    def run(self):
        '''Metodo para la garga e incio de la aplicacion'''
        self.informacion_partidos()
        print("Bienvenido a la aplicación EURO 2024")
        while True:
            #Despliegue Menu Principal
            print("\n================================================")
            print("              APLICACIÓN EURO 2024")
            print("================================================\n")
            print("------------------------------------------------")
            print("                 Menú Principal")
            print("------------------------------------------------\n")
            print("1. Gestión de Partidos y Estadios")
            print("2. Gestión de Ventas de Entradas")
            print("3. Gestión de Asistencia de Partidos")
            print("4. Gestión de Restaruantes")
            print("5. Gestión de Ventas de Restarauntes")
            print("6. Indicadores de Gestión (Estadísticas)")
            print("7. Salir del programa de la EURO 2024")
            #Solicitud de opcion y llamada a la funcion respectiva
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
 
#Metodo Gestion de Partidos y Estadios            
    def gestion_partidos_estadios(self):
        '''Metodo Gestion de Partidos y Estadios '''
        while True:
            print("\n------------------------------------------------")
            print("       Menú Gestión de Partidos y Estadios")
            print("------------------------------------------------\n")
            print("1. Mostrar todos los partidos de un pais")
            print("2. Mostrar todos los partidos que se jugarán en un estadio específico")
            print("3. Mostrar todos los partidos que se jugarán en una fecha determinada")
            print("4. Regresar al Menú Principal\n")
            opcion = input("\nIngrese un valor numérico del 1 al 4: ")
            while not opcion.isnumeric() or int(opcion) == 0 or int(opcion) > 4:
                opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1 al 4: ")
            opcion = int(opcion)
            if opcion == 1:
                respuesta = input("\nIngrese el nombre del país que desea consultar: ").lower()
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
            
#Metodo Gestion de Ventas de Entradas            
    def gestion_ventas_entradas(self):
        '''Metodo Gestion de Ventas de Entradas'''
        print("\n------------------------------------------------")
        print("          Gestión de Ventas de Entradas")
        print("------------------------------------------------\n")
        print(" Datos del cliente")
        print("------------------\n")
        #Les preguntamos al usuario sus datos y hacemos su respectiva validacion por cada input
        nombre_cliente = input("Ingrese el nombre del cliente: ").lower()
        while not nombre_cliente.isalpha():
            nombre_cliente = input("\nIngrese un nombre válido: ").lower()    
        
        ci_cliente = input("Ingrese la Cédula de Identidad (C.I) del cliente (No utilice puntos, ni letras. Ejem: 332321): ")    
        while not ci_cliente.isdigit():
            ci_cliente = input("\nC.I. inválida. Indique un valor de C.I. correcto: ") 
        
        edad_cliente = input("Ingrese la edad del cliente: ")
        while not edad_cliente.isnumeric() or not int(edad_cliente) > 0:
            edad_cliente = input("\nIngrese una edad válida: ")
       
        #Hacemos un breve menú donde el usuario pordra ver la opcion de entradas
        print("\n----Opcion de Entrada----")
        print("1. VIP")
        print("2. General\n")
        #Les preguntamos el usuario que entrada desea comprar y hacemos la validacion 
        tipo_entrada = input("\nIngrese 1 ó 2 para seleccionar el tipo de entrada: ")
        while tipo_entrada != "1" and tipo_entrada != "2":
            tipo_entrada = input("\nOpción Inválida. Ingrese de nuevo un número (1 o 2) para seleccionar el tipo de entrada: ")
        #Validamos si el usuario marco (1 o 2) y se lo asignamos a la variable entrada_vip_general
        if tipo_entrada == "1":
            tipo_entrada = "vip"
        elif tipo_entrada == "2":
            tipo_entrada = "general"
        
        #Recorremos partido en self.partidos
        print("\nLista de partidos posibles")
        print("--------------------------\n")
        for partido in self.partidos:
            partido.show()
        
        #Le preguntamos al usuario que ingrese un numero de acuerdo a lista de partido y hacemos la validacion
        nro_partido = input("\nIngrese el número de partido a seleccionar: ")
        while not nro_partido.isnumeric() or int(nro_partido) > len(self.partidos) or int(nro_partido) == 0:
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
        print("\n---------------------------------------------------------------")
        print(f"Mapa de Asientos del Estadio: {partido_stadium.name}")
        print("---------------------------------------------------------------\n")
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
        
        #Llamado a la funcion es_vampiro para validar si la C.I. es un numero vampiro o no   
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
        print("\n----------------------------------------------------------------")
        print("                     FACTURA DEL CLIENTE")
        print("----------------------------------------------------------------")
        print(f"Asiento: {asiento_asig}")
        print(f"Precio Entrada: {precio}")
        print(f"Descuento: {precio_descuento}")
        print(f"Subtotal: {precio - precio_descuento}")
        print(f"IVA (16%): {iva}")
        print("-----------------------------------------------------------------")
        print(f"                                             Total: ${precio_total}")
    
        #Le preguntamos al usuario si desea realizar la compra    
        pago_ticket = input("\nDesea realizar la compra del ticket (Si o No)?: ").lower()
        while pago_ticket != "si" and pago_ticket != "no":
            pago_ticket = input("Respuesta inválida, ingrese Si o No: ").lower()
        if pago_ticket == "si":
            print("\nSu compra ha sido existosa")
            codigo_seguridad = generar_codigo_seguridad() #Se genra el codigo seguridad unico
            ticket = Ticket(ci_cliente, partido, tipo_entrada, asiento_asig, codigo_seguridad, precio_total)
            self.clientes.append(datos_cliente)        
            self.tickets.append(ticket)
            print("******************************************************************************************")
            print(f"                               TICKET {ticket.tipo_de_asiento}")                           
            print(f"                          {partido.home.name}  vs {partido.away.name} ")
            print(f"                       Estadio: {partido_stadium.name}")
            print(f"                         Fecha: {partido.date}")
            print(f"                       Codigo seguridad: {codigo_seguridad}")
            print("******************************************************************************************")
            if tipo_entrada == "vip":
                partido.asientos_ocupados_vip.append(asiento_asig)
            elif tipo_entrada == "general":
                partido.asientos_ocupados_general.append(asiento_asig)
        else:
            print("La compra no ha sido procesada ni registrada por solicitud del cliente")
    
#Metodo Gestion de Asistencias a Partidos
    def gestion_asistencia_partidos(self):
        '''Metodo Gestion de Asistencias a Partidos'''
        print("\n----------------------------------------------------------------")
        print("                      Listado de Partidos")
        print("----------------------------------------------------------------\n")
        for partido in self.partidos:
            partido.show()
            
        nro_partido = input("Ingrese el número de partido del ticket que desea consultar: ")
        while not nro_partido.isnumeric() or int(nro_partido) > len(self.partidos):
                nro_partido = input("\nOpción Invalida. Asegúrese de ingresar un valor numérico válido: ")               
        nro_partido = int(nro_partido)
        for partido in self.partidos:
            if partido.number == nro_partido:
                break
            
        ticket_valido = False
        codigo_seguridad = input("Ingrese el código de seguridad del ticket: ")
        for ticket in self.tickets:
            if ticket.codigo_seguridad == codigo_seguridad and ticket.partido.number == nro_partido:
                if ticket.asistencia == False:
                    ticket.asistencia = True
                    print(f"Ticket: {codigo_seguridad} válido. Se registró asistencia")
                    ticket_valido = True
                    break
                else:
                    print(f"Ticket: {codigo_seguridad} inválido. El ticket ya ha sido registrado previamente con aistencia")
                    ticket_valido = True                  
        if ticket_valido == False:
            print(f"Ticket: {codigo_seguridad} inválido. No existente")            
                 
 #Metodo Gestion de Restaurantes           
    def gestion_restaurantes(self): 
        '''Metodo Gestion de Restaurantes '''
        print("\n---------------------------------------------------------------------")
        print("                       Gestion de Restaurantes")
        print("---------------------------------------------------------------------\n")
        print("                         Listado de Estadios")
        print("---------------------------------------------------------------------\n")
        for i, estadio in enumerate(self.estadios):
            i += 1
            print(i)
            estadio.nombre_show()
        opcion=input("\nSeleccione el número del estadio donde se ubica el restaurante a gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(self.estadios):
            opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
        index_estadio = int(opcion) - 1
        estadio = self.estadios[index_estadio]
        
        print(f"\nListado de Restaurantes ubicados en {estadio.name}")
        print("----------------------------------------------------------------------------------\n")
        for i, restaurante in enumerate(estadio.restaurantes):
            i += 1
            print(i)
            restaurante.nombre_show()
        opcion=input("\nSeleccione el número de restaurante que desea gestionar: ")
        while not opcion.isnumeric() or int(opcion) > len(estadio.restaurantes):
            opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
        index_restaurante = int(opcion) - 1
        restaurante = estadio.restaurantes[index_restaurante]

        while True:
            print("\n-----------------------------------------------------------------------------")
            print(f"  Gestion del Restaurante {restaurante.name}")
            print("-----------------------------------------------------------------------------\n")
            print("1. Buscar Productos por nombre")
            print("2. Buscar Productos por tipo")
            print("3. Buscar Productos por rango de precio")
            print("4. Regresar al Menu Principal\n")
            opcion = input("Ingrese la opción deseada (1-4): ")
            while not opcion.isnumeric() or int(opcion) > 4 or int(opcion) == 0:
                opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1-4: ")
            opcion = int(opcion)  
            #Opcion 1: Busqueda de un producto por nombre 
            if opcion == 1:
                encontrado = False
                print(f"\nBúsqueda de productos del restaurant {restaurante.name} por nombre de producto")
                print("-----------------------------------------------------------------------------------------\n")
                nombre_producto = input("\nIntroduzca el nombre del producto que desea buscar: ").title()
                print(nombre_producto)
                for producto in restaurante.products:
                    if producto.name == nombre_producto:
                        print("\n--------------------------------------------------------")
                        print(f"Información del producto:")
                        print(f"----------------------------------------------------------")
                        producto.show()
                        encontrado = True
                        break
                if not encontrado:
                    print(f"\nProducto {nombre_producto} no encontrado. Intente otra búsqueda")
            #Opcion 2: Busqueda de un producto por tipo
            elif opcion == 2:
                print(f"\nBúsqueda de productos del restaurant {restaurante.name} por tipo de producto")
                print("------------------------------------------------------------------------------------------\n")
                print("1. Alimento")
                print("2. Bebida")
                opcion = input("\nSeleccione el número (1 o 2) del tipo de producto que desea consultar: ")
                while not opcion.isnumeric() or int(opcion) > 2:
                    opcion = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1-2: ")    
                opcion = int(opcion)
                encontrado = False
                #Opcion 1: Producto por tipo Alimento
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
                    #Opcion 2: Producto por tipo Bebida
                    print("\n-----------------------------")
                    print(f"Productos del Tipo Bebida:")
                    print(f"-----------------------------\n")
                    for producto in restaurante.products:
                        if producto.clasificacion == "bebida":
                            producto.show()
                            encontrado = True
                    if not encontrado:
                        print(f"\nNo existen productos de tipo Bebida. Intente otra búsqueda")
            #Opcion 3: Busqueda de un producto por rango de precio        
            elif opcion == 3:
                print(f"\nBúsqueda de productos del restaurante {restaurante.name} por rango de precio")
                print("----------------------------------------------------------------------------------------------\n")
                precio_minimo = input("Ingrese el precio mínimo con IVA): ")
                while not precio_minimo.isnumeric() or float(precio_minimo) < 0:
                    precio_minimo = input("\n:Precio inválido. El precio mínimo debe ser un valor numerico mayor o igual a 0: ") 
                precio_minimo = round(float(precio_minimo) ,2)
                precio_maximo = input("\nIngrese el precio máximo con IVA: ")
                while not precio_maximo.isnumeric() or float(precio_maximo) < precio_minimo:
                    precio_maximo = input("\n:Precio inválido. El precio máximo debe ser un valor numérico mayor o igual al precio mínimo : ")
                precio_maximo = round(float(precio_maximo),2)    
                print("\n---------------------------------------------------------------------------------------------")
                print(f"\nListado de productos con precio entre {precio_minimo} y {precio_maximo}")
                print("---------------------------------------------------------------------------------------------\n")
                encontrado = False
                for producto in restaurante.products:
                    if precio_minimo <= producto.price <= precio_maximo:
                        producto.show()
                        encontrado = True
                if not encontrado:
                        print(f"\nNo existen productos con precio entre {precio_minimo} y {precio_maximo}")           
            #Regresar al Menu Principal
            elif opcion == 4:
                break
        
#Metodo Gestion de Ventas de Restaurantes
    def gestion_ventas_restaurantes(self):
        '''Metodo Gestion de Ventas de Restaurantes'''
        print("\n----------------------------------------------------------------")
        print("                Gestion de Venta en Restaurantes")
        print("----------------------------------------------------------------\n")
        print("                      Listado de Estadios")
        print("----------------------------------------------------------------\n")

        for i, estadio in enumerate(self.estadios):
            i += 1
            print(i)
            estadio.nombre_show()
        respuesta=input("\nSeleccione el número del estadio donde se ubica el restaurante a gestionar: ")
        while not respuesta.isnumeric() or int(respuesta) > len(self.estadios):
            respuesta = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
        index_estadio = int(respuesta) - 1
        estadio = self.estadios[index_estadio]
        print(f"\nListado de Restaurantes ubicados en {estadio.name}")
        print("--------------------------------------------------------------\n")
        for i, restaurante in enumerate(estadio.restaurantes):
            i += 1
            print(i)
            restaurante.nombre_show()
        respuesta=input("\nSeleccione el número del restaurante que desea gestionar: ")
        while not respuesta.isnumeric() or int(respuesta) > len(estadio.restaurantes):
            respuesta = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
        index_restaurante = int(respuesta) - 1
        restaurante = estadio.restaurantes[index_restaurante]
        
        while True:
            print("\n============================================================================")
            print(f" Gestion de Ventas Restaurante {restaurante.name}")
            print("=============================================================================\n")
            print("1. Procesar Ventas del Restaurante")
            print("2. Regresar al Menu Principal\n")
            respuesta = input("\nIngrese la opción deseada (1-2): ")
            while not respuesta.isnumeric() or int(respuesta) > 2:
                respuesta = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico del 1-2: ")
            respuesta = int(respuesta)  
            if respuesta == 1:
                productos_por_vender = [] 
                cedula_identidad = input("\nIngrese su C.I: ")
                encontrado = False
                for cliente in self.clientes:
                    if cliente.cedula == cedula_identidad:
                        encontrado = True        
                        if cliente.entrada == "vip":
                            print(f"\nLista de productos disponibles del restaruant {restaurante.name}")
                            print("---------------------------------------------------------------------------")
                            for i, producto in enumerate(restaurante.products):
                                i += 1
                                print(i)
                                producto.show()
                            while True:
                                num_product = input("Ingrese el número del producto que desea vender: ")
                                while not num_product.isnumeric() or int(num_product) > len(restaurante.products):
                                    num_product = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
                                index_product = int(num_product) - 1
                                producto = restaurante.products[index_product]
                                if producto.adicional == "alcoholic" and int(cliente.edad) < 18:
                                    print("\nEste producto es una bebida alcoholica. No se puede efectuar la venta ")
                                else:
                                    productos_por_vender.append(producto)
                                    respuesta = input("\nEl cliente desea otro producto (Si o No): ").lower()
                                    while respuesta != "si" and respuesta != "no":
                                        respuesta = input("\nRespuesta inválida, debe ser (Si o No): ").lower()
                                    if respuesta == "no":
                                        monto_total = 0
                                        print("\n----------------------------------------------------------------")
                                        print("                 Factura del cliente                            ")
                                        print("----------------------------------------------------------------\n")
                                        print(f"           Restaurante: {restaurante.name}\n")
                                        for producto_facturado in productos_por_vender:
                                            print(f"Nombre del Producto: {producto_facturado.name}")
                                            print(f"Precio del Producto (Incluye IVA): {producto_facturado.price}")
                                            print(f"Tipo del Producto: {producto_facturado.clasificacion} - {producto_facturado.adicional}\n")
                                            monto_total += producto_facturado.price
                                        print(f"\nSubtotal: {monto_total}")
                                            
                                        if es_perfecto(cedula_identidad):
                                            print(f"\nLa C.I del cliente es un número perfecto, por lo tanto tiene un descuento del 15%: {monto_total * 0.15}  ")
                                            rebaja = monto_total * 0.15
                                            monto_total = monto_total - rebaja
                                        print("\n----------------------------------------------------------------")
                                        print(f"                                   Monto total: {monto_total}")
                                        respuesta = input("\nEl cliente desea realizar la venta (Si o No): ").lower()
                                        while respuesta != "si" and respuesta != "no":
                                                respuesta = input("\nRespuesta invalida, debe ser (Si o No): ").lower()  
                                        if respuesta == "si":
                                            for producto_facturado in productos_por_vender:
                                                producto_facturado.stock -= 1
                                            print("\nVenta realizada existosamente")
                                            ventas_facturadas = Venta_Restaurant(cliente, productos_por_vender, monto_total)
                                            restaurante.ventas.append(ventas_facturadas)   
                                            break
                                        else:
                                            print("\nNo se ha procesado ni registrado la venta por solicitud del usuario")
                                            break                           
                        else:
                            print("\nLa CI no corresponde a un cliente VIP, por lo que no puede efectuar compras")
                if not encontrado:
                    print("\nCliente no encontrado. Intente con otra CI")
            elif respuesta == 2:
                break
                
#Metodo Indicadores de Gestion
    def indicadores_gestion(self):
        '''Metodo Indicadores de Gestion'''
        while True:
            print("\n----------------------------------------------------------------")
            print("             Menú Gestión de Indicadores de Gestión")
            print("------------------------------------------------------------------\n")
            print("1. Mostar el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)? ")
            print("2. Mostrar lista con la asistencia de los partidos de mejor a peor")
            print("3. Mostar el Partido con mayor asistencia")
            print("4. Mostrar el Partido con mayor boletos vendidos")
            print("5. Mostrar los Top 3 productos mas vendidos en el restaurante")
            print("6. Mostrar los Top 3 clientes(los que compraron más boletos)")
            print("7. Realiza un gráfico con las estadísticas")
            print("8. Regresar al Menú Principal")
            opcion = input("\nIngrese la opción deseada (1-8): ")
            while not opcion.isnumeric() or int(opcion) > 8 or int(opcion) == 0:
                opcion = input("\nOpción Inválida. Asegurese de ingresar un valor numérico del 1-8: ")
            opcion = int(opcion)
            # Opcion 1. que muestra el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)? ")
            if opcion ==1:
                #Desplegamos la lista de partidos al usuario para conocer el numero de partido a seleccionar
                print("\n------------------------------------------------")
                print("Promedio de gastos de clientes VIP en un partido")
                print("------------------------------------------------\n")
                print("\nLista de partidos\n")
                print("-----------------\n")
                #Solicitamos el numero de partido
                for partido in self.partidos:
                    partido.show()    
                nro_partido = input("\nIngrese el número de partido: ")
                while not nro_partido.isnumeric() or int(nro_partido) > len(self.partidos) or int(nro_partido) == 0:
                    nro_partido = input("\nOpción Inválida. Asegúrese de ingresar un valor numérico válido: ")
                nro_clientes_partido = 0
                total_de_gastos_tickets = 0
                #Recorremos la lista de tickets para conocer el numero de clientes y costo de los tickets VIP
                for ticket in self.tickets:
                    if int(ticket.partido.number) == int(nro_partido) and ticket.tipo_de_asiento == "vip":
                        nro_clientes_partido += 1
                        total_de_gastos_tickets += ticket.precio_total
                total_de_gastos_restaurantes = 0
                #Recorremos la lista de partidos para conocer el id del estadio
                for partido in self.partidos:
                    if int(partido.number) == int(nro_partido):
                        estadio_id = partido.stadium_id
                        break
                #Recorremos la lista de restaurantes para conocer el total de gastos en restaurantes
                for estadio in self.estadios:
                    if estadio.id == estadio_id:
                        for restaurante in estadio.restaurantes:
                            for venta in restaurante.ventas:
                                total_de_gastos_restaurantes += venta.total  
                        break     
                #Calculamos el promedio y desplegamos la informacion               
                promedio = (total_de_gastos_tickets + total_de_gastos_restaurantes) / nro_clientes_partido
                print("\n--------------------------------------------------------------------------------------------")
                print("Promedio de gastos de clientes VIP en un partido (ticket + restaurante) ") 
                print("-------------------------------------------------------------------------------------------------\n")       
                print(f"Nro. de Clientes VIP en el partido Nro. {nro_partido}: {nro_clientes_partido}")
                print(f"Total de Ventas en Tickets: {total_de_gastos_tickets}")
                print(f"Total Gastos en Restaurantes del estadio {estadio.name}: {total_de_gastos_restaurantes}\n") 
                print("------------------------------------------------------------------------------------------------")              
                print(f"Promedio de gastos por cliente: {promedio}")
                print("------------------------------------------------------------------------------------------------\n")
                break
            # Opcion 2. que muestra lista con la asistencia de los partidos de mejor a peor")
            elif opcion ==2:
                boletos_vendidos = 0
                boletos_asistencia = 0
                partidos_ordenados = []
                #Recorremos la lista de partidos para obtener la informacion solicitada de cada partido
                for partido in self.partidos:
                    nombre_home = partido.home.name 
                    nombre_away = partido.away.name
                    stadium_id = partido.stadium_id
                    #Recorremos la lista de estadio buscar el id del equipo y conocer su nombre
                    for estadio in self.estadios:
                        if estadio.id == stadium_id:
                            nombre_estadio = estadio.name
                            break
                    #Recorremos la lista de los tickets para conocer los tickets vendidos y la asistencia
                    for ticket in self.tickets:
                        if partido.id == ticket.partido.id:
                            boletos_vendidos += 1
                            if ticket.asistencia == True:
                                boletos_asistencia += 1
                    #Calculamos la relacion asistencia / boletos vendidos
                    if boletos_vendidos == 0:
                        relacion = "N/A"
                    else:
                        relacion = round(boletos_asistencia / boletos_vendidos,2) 
                    #Creamos un dato tipo diccionario para guardar la iformacion a mostrar 
                    diccionario = {"local": nombre_home, "visitante": nombre_away, "estadio": nombre_estadio, "vendidos": boletos_vendidos, "asistencia": boletos_asistencia, "relacion": relacion} 
                    #Agregamos el dato tipo diccionario a la lista partidos_ordenados 
                    partidos_ordenados.append(diccionario)
                #Ordenamos la lista partidos_ordenado de mayor a menor de acuerdo a la asistencia
                for i in range(len(partidos_ordenados)):
                    for j in range(i+1, len(partidos_ordenados)):
                        if partidos_ordenados[i]["asistencia"] < partidos_ordenados[j]["asistencia"]:
                            partidos_ordenados[i], partidos_ordenados[j] = partidos_ordenados[j], partidos_ordenados[i]
                #Mostramos la informacion cabecera y datos
                print("Equipo Local   Equipo Visitante    Estadio    Boletos Vendidos    Asistencia Relación Asistencia/Venta")
                print("-------------------------------------------------------------------------------------------")
                for match in partidos_ordenados:
                    print(f"{match["local"]}    {match["visitante"]}    {match["estadio"]}    {match["vendidos"]}   {match["asistencia"]}   {match["relacion"]}")                             
            # Opcion 3. que muestra el Partido con mayor asistencia
            elif opcion ==3:
                #Cremamos lista total_asistencia donde se totaliza el numero de tickets que asistieron por juego y se inicializa en 0
                total_de_asistencia = [0] * 36         
                nro_partido_con_mas_asistencia = []
                for ticket in self.tickets:
                    if ticket.asistencia == True:
                        index_partido = int(ticket.partido.number) - 1
                        total_de_asistencia[index_partido] += 1
                #Calculamos cual es el maximo de ticket que asistieron
                max_asistencia = max(total_de_asistencia)
                #Creamos lista con los numeros de partidos con mayor numero de ticket que asistieron
                for i in range(0, len(total_de_asistencia)):
                    if int(total_de_asistencia[i]) == int(max_asistencia):
                        nro_partido_con_mas_asistencia.append(i+1)
                print("\n----------------------------------------------------------------------------")
                print("                    Partido con Mayor Asistencia")
                print("----------------------------------------------------------------------------\n")
                #Mostramos la informacion de los partidos con mayor numero de tickets que asistieron
                for i in range(0, len(nro_partido_con_mas_asistencia)):
                    for partido in self.partidos:
                        if int(partido.number) == int(nro_partido_con_mas_asistencia[i]):
                            partido.show()           
                print("----------------------------------------------------------------------------")
                print(f"Total de partidos con Mayor Asistencia: {max_asistencia}")
                print("----------------------------------------------------------------------------\n")                    
            # Opcion 4. que muestra el Partido con mayor boletos 
            elif opcion == 4:
                #Cremamos lista total_ticket_partido donde se totaliza el numero de tickets por juego y se inicializa en 0
                total_ticket_partido = [0] * 36
                nro_partido_con_mas_tickets = []
                for ticket in self.tickets:
                    index_partido = int(ticket.partido.number) - 1
                    total_ticket_partido[index_partido] += 1  
                #Calculamos cual es el maximo de ticket
                max_tickets = max(total_ticket_partido)
                #Creamos lista con los numeros de partidos con mayor numero de ticket
                for i in range(0, len(total_ticket_partido)):
                    if int(total_ticket_partido[i]) == int(max_tickets):
                        nro_partido_con_mas_tickets.append(i+1)
                print("\n----------------------------------------------------------------------------")
                print("                    Partido con Mayor Boletos Vendidos")
                print("----------------------------------------------------------------------------\n")
                #Mostramos la informacion de los partidos con mayor numero de tickets
                for i in range(0, len(nro_partido_con_mas_tickets)):
                    for partido in self.partidos:
                        if int(partido.number) == int(nro_partido_con_mas_tickets[i]):
                            partido.show()
                print("----------------------------------------------------------------------------")
                print(f"Total de boletos vendidos: {max_tickets}")
                print("----------------------------------------------------------------------------\n")           
            # Opcion 5. que muestra los Top 3 productos mas vendidos en el restaurante
            elif opcion == 5:
                pass
            # Opcion 6. que muestra los Top 3 clientes(los que compraron mas boletos)
            elif opcion ==6:
                clientes_ordenados = []
                #Recorremos la lista de clientes para contabilizar los ticket para cada uno de los clientes
                
                for cliente in self.clientes:
                    #Recorremos la lista de los tickets para conocer los tickets vendidos y la asistencia
                    encontrado = 0
                    ci_cliente = cliente.cedula
                    if len(clientes_ordenados) > 0:
                        for i in range(len(clientes_ordenados)):
                            if int(ci_cliente) == int(clientes_ordenados[i]["cedula"]):
                                clientes_ordenados[i]["tickets"] += 1
                                encontrado = 1
                                break
                        if encontrado == 0:
                            diccionario = {"cedula": ci_cliente, "tickets": 1}
                            clientes_ordenados.append(diccionario)  
                    else:
                        diccionario = {"cedula": ci_cliente, "tickets": 1}
                        clientes_ordenados.append(diccionario)   
               #temporal
                print(clientes_ordenados)
                
                #Ordenamos la lista clientes_ordenados de mayor a menor de acuerdo a la cantidad de tickets
                for i in range(len(clientes_ordenados)):
                    for j in range(i+1, len(clientes_ordenados)):
                        if clientes_ordenados[i]["tickets"] < clientes_ordenados[j]["tickets"]:
                            clientes_ordenados[i], clientes_ordenados[j] = clientes_ordenados[j], clientes_ordenados[i]
                #Mostramos los 3 primeros clientes de la lista clientes_ordenados            
                print("------------------------------------------------------------")
                print("    Listado de Top 3 clientes que más compraron boletos")
                print("------------------------------------------------------------")
                for i in range(len(clientes_ordenados)):  # para el caso que hayan menos de 3 clientes
                    if i == 3: break #Detenemos el bucle para solo mostrar los tres primeros elementos de la lista clientes_ordenados
                    for cliente in self.clientes:
                        if int(cliente.cedula) == int(clientes_ordenados[i]["cedula"]):
                            print(f"           TOP {i+1}")
                            print(f"Nombre: {cliente.nombre}")
                            print(f"   C.I: {cliente.cedula}")
                            print(f" Edad:: {cliente.edad}")
                            print(f"Tickets comprados: {clientes_ordenados[i]["tickets"]}")
                            break
                    print("------------------------------------------------------------")
                            
            # Opcion 7. que muestra un grafico con las estadisticas
            elif opcion == 7:
                pass
            # Opcion 8. para regresar al Menu Principal 
            elif opcion == 8:
                break 
                
#Metodo que permite obtener la informacion de las API y carga de datos en listas
    def informacion_partidos(self):
        '''Metodo que permite obtener la informacion de las API y carga de datos en listas'''
        #Url de los equipos , estadios , partidos 
        url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        url_estadios = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        #Obtenemos la informacion de equipos, estadios, y partidos mediante los URL usando (urllib.request.urlopen)
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