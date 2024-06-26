"""Modulo Principal Main\n
Llamado principal a la aplicacion App
"""
from App import App

def main():
    """Esta funcion crea una instancia de la clase App y hace un llamado al metodo app.run() del modulo App"""
    app = App()
    app.run()

main()

