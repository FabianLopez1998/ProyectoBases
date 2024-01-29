from datetime import datetime

from Modelo.DataBaseSql import DataBaseSql

class CtrlFacturaProducto():
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarFacturaProducto(self,datos):
        self.idProducto,self.cantidad,self.precioUnitario,self.idFactura=datos
        self.insertar.Insert('Factura_Producto',(self.idProducto,self.cantidad,
                                                 self.precioUnitario,self.idFactura))

    # def cargarDatosProducto(self,nombre):
    #     self.nombre=nombre
    #     datos=self.insertar.SearchIdTable('Producto',nombre)
    #     return datos
    #
    # def modificarProducto(self,datos):
    #     self.idProducto,self.nombre,self.tamanio,self.medida,self.idMarca= datos
    #     self.insertar.Edit('Producto',(self.idProducto,self.nombre,self.tamanio,self.medida,self.idMarca))
    #
    # def eliminarProducto(self,nombre):
    #     self.nombre=nombre
    #     self.insertar.Delete('Producto',nombre)
    #
    # def cargarTablaProducto(self):
    #     producto=self.insertar.searchAllTables('Producto')
    #     return producto
    def cargarIdUltimaFactura(self):
        idUltimaFactura=self.insertar.getLastIdFact()
        return idUltimaFactura


    def cargarTabla(self, fecha):
        try:
            if fecha == '':
                ventas = self.insertar.dameTablaVentas()
            else:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
                ventas = self.insertar.dameTablaPorFechaVentas(fecha)
            return ventas
        except:
            return []
