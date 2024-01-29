from datetime import datetime

from Modelo.DataBaseSql import DataBaseSql
from conection import DataBaseConection


class CtrlAbastecer():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)
        self.conexion2 = DataBaseConection()

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

    def crearVistaTemporal(self):
        self.insertar.crearVistaTemporal()
    def agregarDatosVista(self, id_suc, id_pro, cantidad, precio, fecha):
        self.insertar.AgregarDatosVista(id_suc, id_pro, cantidad, precio, fecha)

    def agregarDatosAInventario(self):
        self.insertar.pasar_datos()
        self.insertar.eliminarVista()

    def eliminarVista(self):
        self.insertar.eliminarVista()
        self.conexion2.EndConection()
        self.conexion2.StarConection()

    def dameVista(self):
        return self.insertar.dameVista()