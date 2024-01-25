import sys
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal

class ControladorPrincipal():
    def __init__(self):
        self.base=DataBaseConection()
        self.Sucursal()


    def Iniciar(self):
        self.base=DataBaseConection()
        #self.conexion=self.Base.StarConection()

    def Sucursal(self):
        self.conexion=self.base.StarConection()
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.Iniciar()
