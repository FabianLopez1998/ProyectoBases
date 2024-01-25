import sys
from Controlador.ControladorPrincipal import ControladorPrincipal
from conection import DataBaseConection
if __name__=="__main__":
    conexion=DataBaseConection()
    puntero=conexion.StarConection()

    controlador = ControladorPrincipal(puntero)
    controlador.Iniciar()
    #probando
    #app.exec()

    conexion.EndConection()
