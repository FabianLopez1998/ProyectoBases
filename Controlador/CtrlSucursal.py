from Modelo.Sucursal import Sucursal
from Modelo.DataBaseSql import DataBaseSql

class CtrlSucursal():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarSucursal(self,datos): #Modificado Alejandro
        self.nombre,self.direccion=datos
        if self.cargarDatosSucursal(self.nombre) == None:
            self.insertar.Insert('Sucursal',(self.nombre,self.direccion))
            return True
        else: return False

    def cargarDatosSucursal(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Sucursal',nombre)
        return datos

    def modificarSucursal(self,datos): #Modificado Alejandro
        self.idSucursal,self.nombre,self.direccion = datos
        self.insertar.Edit('Sucursal',(self.idSucursal,self.nombre, self.direccion))

    def eliminarSucursal(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Sucursal',nombre)

    def cargarIdSucursal(self,nombre):
        self.nombre=nombre
        idSucursal=self.insertar.searchIdAllTables('Sucursal',nombre)
        return idSucursal

    def cargarTablaSucursal(self):
        sucursal=self.insertar.searchAllTables('Sucursal')
        return sucursal