from datetime import datetime

from Modelo.DataBaseSql import DataBaseSql
from conection import DataBaseConection


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
        self.idSucursal,self.idProducto,self.cantidad,self.precio,self.fecha=datos
        self.insertar.ingresarTablaNueva((self.idSucursal,self.idProducto,self.cantidad,self.precio))

    def vaciarTablaNueva(self):
        self.insertar.vaciarTablaNueva()

    def cargarTabla(self, fecha):
        try:
            if fecha == '':
                abast = self.insertar.dameTablaAbastecimientos()
            else:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
                abast = self.insertar.dameTablaPorFecha(fecha_obj)
            return abast
        except:
            return []


    def cargaTablaInventario(self, sucursal, categoria):
        try:
            if categoria == '':
                inv = self.insertar.dameTablaInventario(sucursal)
            else:
                inv = self.insertar.dameTablaPorCategoriaInventario(sucursal, categoria)
            return inv
        except:
            return []

