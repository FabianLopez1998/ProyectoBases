from conection import DataBaseConection

class DataBaseSql():
    def __init__(self,conexion):
        self.conexion=conexion

    def Insercion(self,tabla,objeto):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            sql='insert into Sucursal(nombre, direccion) values ( %s, %s)'
            puntero.execute(sql, (objeto.nombre,objeto.direccion))
            print('objeto insertado correctamente')
        if tabla=='Categoria':
            print('insert')
        if tabla=='Cliente':
            print('insert')
        if tabla=='Fabricante':
            print('insert')
        if tabla=='Factura':
            print('insert')
        if tabla=='Factura_Producto':
            print('insert')
        if tabla=='Inventario':
            print('insert')
        if tabla=='Marca':
            print('insert')
        if tabla=='Producto':
            print('insert')
        if tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
        #puntero.close()
