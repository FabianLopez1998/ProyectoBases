from Modelo.Sucursal import Sucursal
from Modelo.DataBaseSql import DataBaseSql

class CtrlSucursal():
    def __init__(self,conexion):
        self.conexion=conexion
        #self.insertar=DataBaseSql(self.conexion)

    def Iniciar(self):
        None

    def guardarDatos(self):
        nombre='cuenca'
        direccion='cuenca'
        crear=Sucursal(id,nombre,direccion)
        #self.insertar.Insercion('Sucursal',crear)

