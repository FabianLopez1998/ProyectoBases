from Modelo.Sucursal import Sucursal
from Modelo.DataBaseSql import DataBaseSql

class CtrlSucursal():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarSucursal(self,datos):
        self.nombre,self.direccion=datos
        self.insertar.Insert('Sucursal',(self.nombre,self.direccion))

    def cargarDatosSucursal(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Sucursal',nombre)
        return datos

    def modificarSucursal(self,datos):
        self.nombre,self.direccion = datos
        self.insertar.Edit('Sucursal',(self.nombre, self.direccion))

    def eliminarSucursal(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Sucursal',nombre)

    def cargarTablaSucursal(self):
        sucursal=self.insertar.searchAllTables('Sucursal')
        return sucursal