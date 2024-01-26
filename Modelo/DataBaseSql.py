from conection import DataBaseConection

class DataBaseSql():
    def __init__(self,conexion):
        self.conexion=conexion

    def Insert(self, tabla, data):
        puntero=self.conexion.cursor()

        if tabla=='Sucursal':
            sql='insert into Sucursal(nombre, direccion) values ( %s, %s)'
            #puntero.execute(sql, (data.nombre, data.direccion))
            print('objeto insertado correctamente')
        elif tabla=='Categoria':
            print('insert')

        elif tabla=='Cliente':
            sql=('insert into Cliente(id,nombre,apellido,direccion,email,telefono,es_socio) '
                 'values ( %s, %s,%s, %s,%s, %s,%s)')
            valores=(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            puntero.execute(sql,valores)
            print('Datos insertados correctamente')
        elif tabla=='Fabricante':
            print('insert')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            print('insert')
        elif tabla=='Producto':
            print('insert')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
        #puntero.close()

    def SearchClient(self,id):
        puntero=self.conexion.cursor()
        sql='select * from cliente where id = %s'
        puntero.execute(sql,(id,))
        cliente=puntero.fetchone()
        return cliente

    def searchAllTables(self,tabla):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            print('objeto modificados correctamente')
        elif tabla=='Categoria':
            print('insert')

        elif tabla=='Cliente':
            sql='select * from cliente'
            puntero.execute(sql)
            cliente=puntero.fetchall()
            return cliente
        elif tabla=='Fabricante':
            print('insert')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            print('insert')
        elif tabla=='Producto':
            print('insert')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()

    def deleteClient(self,id):
        puntero=self.conexion.cursor()
        sql='delete from Cliente where id = %s'
        puntero.execute(sql,(id,))
        self.conexion.commit()
        print('Cliente eliminado correctamente')

    def Edit(self,tabla,data):
        puntero=self.conexion.cursor()

        if tabla=='Sucursal':
            print('objeto modificados correctamente')
        elif tabla=='Categoria':
            print('insert')

        elif tabla=='Cliente':
            sql=('update cliente set nombre=%s, apellido=%s, direccion=%s,'
                 'email=%s, telefono=%s, es_socio=%s where id= %s')
            valores=(data[1],data[2],data[3],data[4],data[5],data[6],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Fabricante':
            print('insert')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            print('insert')
        elif tabla=='Producto':
            print('insert')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
