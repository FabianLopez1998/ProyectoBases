import sys
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal

class ControladorPrincipal:
    def __init__(self,conexion):
        self.conexion=conexion


    def Iniciar(self):
        self.Sucursal()

    def Sucursal(self):
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.Iniciar()
