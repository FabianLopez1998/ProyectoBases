from Modelo.DataBaseSql import DataBaseSql

class CtrlFabricante():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarFabricante(self,datos):
        self.nombre,self.direccion=datos
        if self.cargarDatosFabricante(self.nombre) == None:
            self.insertar.Insert('Fabricante',(self.nombre,self.direccion))
            return True
        else: return False

    def cargarDatosFabricante(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Fabricante',nombre)
        return datos

    def modificarFabricante(self,datos):
        self.idFabricante,self.nombre,self.direccion = datos
        self.insertar.Edit('Fabricante',(self.idFabricante,self.nombre,self.direccion))

    def eliminarFabricante(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Fabricante',nombre)

    def cargarTablaFabricante(self):
        fabricante=self.insertar.searchAllTables('Fabricante')
        return fabricante

    def cargarIdFabricante(self,nombre):
        self.nombre=nombre
        idFabricante=self.insertar.searchIdAllTables('Fabricante',nombre)
        return idFabricante