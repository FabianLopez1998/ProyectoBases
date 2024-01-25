class DataBaseSql():
    def __init__(self,conexion):
        self.conexion=conexion

    def Insercion(self,tabla,objeto):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            print('entro a sucursal')
            sql='insert into Sucursal(id,nombre,direccion) values (:1, :2, :3)'
            puntero.execute(sql, (objeto.id,objeto.nombre,objeto.direccion))
            print('objeto insertado correctamente')
        else:print('ocurrio un error')
        puntero.close()
