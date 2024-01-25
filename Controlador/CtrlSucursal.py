from Modelo.Sucursal import Sucursal
from Modelo.DataBaseSql import DataBaseSql

class CtrlSucursal():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def Iniciar(self):
        self.guardarDatos()

    def guardarDatos(self):
        id=5
        nombre='cuenca'
        direccion='cuenca'
        crear=Sucursal(id,nombre,direccion)
        self.insertar.Insercion('Sucursaaal',crear)

