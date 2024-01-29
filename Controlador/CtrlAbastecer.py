from Modelo.DataBaseSql import DataBaseSql

class CtrlAbastecer():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarAbastecer(self,datos):
        id_sucursal, id_producto, cantidad, precio_base, fecha=datos
        self.insertar.Insert('Inventario',(id_sucursal, id_producto, cantidad, precio_base, fecha))


    def cargarTablaProductosProveedor(self, proveedor):
        productos=self.insertar.getTablaProductosPorProveedor(proveedor)
        return productos

    def cargarPrecioBase(self,id):
        abastecer=self.insertar.getPriceBase(id)
        return abastecer
    def cargarDatosAbastecimiento(self):
        datos=self.insertar.darTablaInventarioAbastecimiento()
        return datos

    def insertarDatosTablaNueva(self,datos):
        self.idSucursal,self.idProducto,self.cantidad,self.precio=datos
        self.insertar.ingresarTablaNueva((self.idSucursal,self.idProducto,self.cantidad,self.precio))

    def vaciarTablaNueva(self):
        self.insertar.vaciarTablaNueva()