from Modelo.DataBaseSql import DataBaseSql

class CtrlProducto():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarProductp(self,datos):
        self.nombre,self.tamanio,self.medida,self.marcaId=datos
        self.insertar.Insert('Producto',(self.nombre,self.tamanio,self.medida,self.marcaId))

    def cargarDatosProducto(self,nombre):
        self.nombre=nombre
        datos=self.insertar.SearchIdTable('Producto',nombre)
        return datos

    def modificarCategoria(self,datos):
        self.nombreCategoriaCmb,self.nuevoNombreCategoria = datos
        self.insertar.Edit('Categoria',(self.nombreCategoriaCmb,self.nuevoNombreCategoria))

    def eliminarProducto(self,nombre):
        self.nombre=nombre
        self.insertar.Delete('Producto',nombre)

    def cargarTablaProducto(self):
        producto=self.insertar.searchAllTables('Producto')
        return producto
    def cargarIdProducto(self,nombre):
        self.nombre=nombre
        idProducto=self.insertar.searchIdAllTables('Producto',nombre)
        return idProducto

    def cargarNombreProducto(self,codigo):
        self.codigo=codigo
        return self.insertar.getNameProduct(self.codigo)