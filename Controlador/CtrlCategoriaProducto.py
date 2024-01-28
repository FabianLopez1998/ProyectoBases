from Modelo.DataBaseSql import DataBaseSql

class CtrlCategoriaProducto():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarCategoriaProducto(self,datos):
        self.productoId,self.categoriaId=datos
        self.insertar.Insert('Producto_Categoria',( self.productoId,self.categoriaId))

    # def cargarDatosMarca(self,nombre):
    #     self.nombre=nombre
    #     datos=self.insertar.SearchIdTable('Marca',nombre)
    #     return datos
    #
    # def modificarMarca(self,datos):
    #     self.nombreProveedor,self.nuevoNombreMarca = datos
    #     self.insertar.Edit('Marca',(self.nombreProveedor,self.nuevoNombreMarca))
    #
    # def eliminarMarca(self,nombre):
    #     self.nombre=nombre
    #     self.insertar.Delete('Marca',nombre)
    #
    # def cargarIdMarca(self,nombre):
    #     self.nombre=nombre
    #     idMarca=self.insertar.searchIdAllTables('Marca',nombre)
    #     return idMarca
    #
    # def cargarTablaMarca(self):
    #     marca=self.insertar.searchAllTables('Marca')
    #     return marca