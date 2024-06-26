"""Módulo Utilitario\n
Contiene funciones utilitarias que utiliza App\n

Funciones:\n 
generar_codigo_seguridad()\n
es_vampiro
es_perfecto
"""

import uuid #Libreria que contiene el metodo uuid4 que sirve para generar un codigo de seguridad unico.

def generar_codigo_seguridad():
    """Función que sirve para generar un código de seguridad único\n
    
    Parámetros:\n
    Sin parametros\n
    
    Retorno:\n
    Un string con el codigo de seguridad generado"""
    return str(uuid.uuid4())[:12] #12 representa la longitud del string


def es_vampiro(numero):
    """Función que sirve para conocer si un numero es vampiro o no.\n
    
    Parámetros:\n
    numero: string que representa el numero a evaluar\n
    
    Retorno:\n
    True: el numero es vampiro\n
    False: el numero no es vampiro"""
    
    numero = int(numero)
    digitos = list(str(numero))
    num_digitos = len(digitos)
    # Comprobación de los factores
    for i in range(1, round((int(numero)**0.5)+1)):
        if numero % i == 0:
            factor1 = str(i)
            factor2 = str(numero // i)
            factores = factor1 + factor2
            # Comprobación de la permutación
            if sorted(digitos) == sorted(factores) and len(factor1) == len(factor2):
                return True
    return False

def es_perfecto(numero):
    """Función que sirve para conocer si un numero es perfecto o no.\n
    
    Parámetros:\n
    numero: string que representa el numero a evaluar\n
    
    Retorno:\n
    True: el numero es perfecto\n
    False: el numero no es perfecto"""
    
    numero = int(numero)
    digitos = list(str(numero))
    num_digitos = len(digitos)
    # Comprobación de los factores
    for i in range(1, round((int(numero)**0.5)+1)):
        if numero % i == 0:
            factor1 = str(i)
            factor2 = str(numero // i)
            factores = factor1 + factor2
            # Comprobación de la permutación
            if sorted(digitos) == sorted(factores) and len(factor1) == len(factor2):
                return True
            