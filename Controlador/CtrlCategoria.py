from Modelo.DataBaseSql import DataBaseSql

class CtrlCategoria():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarCategoria(self,datos):
        self.nombre,self.idCategoria=datos
        self.insertar.Insert('Categoria',(self.nombre,self.idCategoria))

    def cargarDatosCategoria(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Categoria',nombre)
        return datos

    def modificarCategoria(self,datos):
        self.idCategoria,self.idCategoriaPadre,self.nuevoNombreCategoria = datos
        self.insertar.Edit('Categoria',(self.idCategoria,self.idCategoriaPadre,self.nuevoNombreCategoria))

    def eliminarCategoria(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Categoria',nombre)

    def cargarTablaCategoria(self):
        categoria=self.insertar.searchAllTables('Categoria')
        return categoria
    def cargarIdCategoria(self,nombre):
        self.nombre=nombre
        idCategoria=self.insertar.searchIdAllTables('Categoria',nombre)
        return idCategoria