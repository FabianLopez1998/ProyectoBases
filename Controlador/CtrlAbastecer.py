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
