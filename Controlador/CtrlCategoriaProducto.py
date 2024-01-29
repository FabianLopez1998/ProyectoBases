from Modelo.DataBaseSql import DataBaseSql

class CtrlCategoriaProducto():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarCategoriaProducto(self,datos):
        self.productoId,self.categoriaId=datos
        if self.buscarProductoCategoria(datos) == None:
            self.insertar.Insert('Producto_Categoria',( self.productoId,self.categoriaId))
            return True
        else: return False

    def buscarProductoCategoria(self, datos):
        self.productoId,self.categoriaId=datos
        pro_cat = self.insertar.buscarProducto_Categoria(self.productoId, self.categoriaId)
        return pro_cat
