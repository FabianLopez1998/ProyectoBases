from Modelo.DataBaseSql import DataBaseSql

class CtrlProducto():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarProductp(self,datos):
        self.nombre,self.tamanio,self.medida,self.marcaId=datos
        if self.insertar.dameProductoMarcaId(self.nombre, self.marcaId) == None:
            self.insertar.Insert('Producto',(self.nombre,self.tamanio,self.medida,self.marcaId))
            return True
        else: return False

    def cargarDatosProducto(self,nombre, marca):
        self.nombre=nombre
        datos=self.insertar.dameProductoMarcaId(nombre, marca)
        return datos

    def modificarProducto(self,datos):
        self.idProducto,self.nombre,self.tamanio,self.medida,self.idMarca= datos
        self.insertar.modificarProducto((self.idProducto,self.nombre,self.tamanio,self.medida,self.idMarca))

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


    def extraerProductoPorId(self, codigo):
        producto=self.insertar.SearchIdTableProducto(codigo)
        return producto