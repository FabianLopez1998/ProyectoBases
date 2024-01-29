from Modelo.DataBaseSql import DataBaseSql

class CtrlMarca():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarMarca(self,datos):
        self.nombre,self.idFabricante=datos
        if self.cargarDatosMarca(self.nombre) == None:
            self.insertar.Insert('Marca',(self.nombre,self.idFabricante))
            return True
        else: return False

    def cargarDatosMarca(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Marca',nombre)
        return datos

    def modificarMarca(self,datos):
        self.idMarca,self.nuevoNombreMarca = datos
        self.insertar.Edit('Marca',(self.idMarca,self.nuevoNombreMarca))

    def eliminarMarca(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Marca',nombre)

    def cargarIdMarca(self,nombre):
        self.nombre=nombre
        idMarca=self.insertar.searchIdAllTables('Marca',nombre)
        return idMarca

    def cargarTablaMarca(self):
        marca=self.insertar.searchAllTables('Marca')
        return marca