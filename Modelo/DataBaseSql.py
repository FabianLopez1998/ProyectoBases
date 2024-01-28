from conection import DataBaseConection

class DataBaseSql():
    def __init__(self,conexion):
        self.conexion=conexion

    def Insert(self, tabla, data):
        puntero=self.conexion.cursor()

        if tabla=='Sucursal':
            sql='insert into Sucursal(nombre, direccion) values ( %s, %s)'
            puntero.execute(sql, (data[0], data[1]))
            print('objeto insertado correctamente')
        elif tabla=='Categoria':
            sql='insert into Categoria(nombre, categoria_padre) values ( %s, %s)'
            puntero.execute(sql, (data[0], data[1]))
            print('objeto insertado correctamente')
        elif tabla=='Cliente':
            sql=('insert into Cliente(id,nombre,apellido,direccion,email,telefono,es_socio) '
                 'values ( %s, %s,%s, %s,%s, %s,%s)')
            valores=(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
            puntero.execute(sql,valores)
            print('Datos insertados correctamente')
        elif tabla=='Fabricante':
            sql='insert into Fabricante(nombre, direccion) values ( %s, %s)'
            puntero.execute(sql, (data[0], data[1]))
            print('objeto insertado correctamente')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql='insert into Marca(nombre, id_fabricante) values ( %s, %s)'
            puntero.execute(sql, (data[0], data[1]))
            print('objeto insertado correctamente')
        elif tabla=='Producto':
            sql=('insert into Producto(nombre,tamanio,medida,id_marca) '
                 'values ( %s, %s,%s, %s)')
            valores=(data[0],data[1],data[2],data[3])
            puntero.execute(sql,valores)
            print('Datos insertados correctamente')
        elif tabla=='Producto_Categoria':
            sql=('insert into Producto_Categoria(id_producto,id_categoria) '
                 'values ( %s, %s)')
            valores=(data[0],data[1])
            puntero.execute(sql,valores)
            print('Datos insertados correctamente')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
        #puntero.close()

    def SearchIdTable(self,tabla, id):
        puntero=self.conexion.cursor()

        if tabla=='Sucursal':
            sql='select * from Sucursal where nombre=%s'
            puntero.execute(sql, (id,))
            sucursal=puntero.fetchone()
            return sucursal
        elif tabla=='Categoria':
            sql=('select categoria.categoria_padre '
                 ' from categoria '
                 ' where categoria.nombre = %s')
            puntero.execute(sql, (id,))
            idCategoriaPadre=puntero.fetchone()
            sql2=('select categoria.nombre '
                  ' from categoria '
                  ' where categoria.id = %s')
            puntero.execute(sql2, (idCategoriaPadre,))
            nombreCategoriaPadre=puntero.fetchone()

            return nombreCategoriaPadre

        elif tabla=='Cliente':
            sql='select * from cliente where id = %s'
            puntero.execute(sql, (id,))
            cliente=puntero.fetchone()
            return cliente
        elif tabla=='Fabricante':
            sql='select * from Fabricante where nombre=%s'
            puntero.execute(sql, (id,))
            fabricante=puntero.fetchone()
            return fabricante
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            None
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql=('select marca.nombre as nombreMarca, fabricante.nombre as nombreFabricante '
                 ' from marca '
                 ' join fabricante on marca.id_fabricante = fabricante.id '
                 ' where marca.nombre = %s')
            puntero.execute(sql, (id,))
            marca=puntero.fetchone()
            return marca
        elif tabla=='Producto':
            sql=('select producto.tamanio, producto.medida as nombreProducto, marca.nombre as nombreMarca '
                 ' from producto '
                 ' join marca on marca.id = producto.id_marca '
                 ' where producto.nombre = %s ')
            puntero.execute(sql,(id,))
            producto=puntero.fetchone()
            return producto
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
        #puntero.close()


    def searchAllTables(self,tabla):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            sql='select * from sucursal'
            puntero.execute(sql)
            sucursal=puntero.fetchall()
            return sucursal
        elif tabla=='Categoria':
            sql='select * from categoria'
            puntero.execute(sql)
            categoria=puntero.fetchall()
            return categoria
        elif tabla=='Cliente':
            sql='select * from cliente'
            puntero.execute(sql)
            cliente=puntero.fetchall()
            return cliente
        elif tabla=='Fabricante':
            sql='select * from fabricante'
            puntero.execute(sql)
            fabricante = puntero.fetchall()
            return fabricante
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql='select * from marca'
            puntero.execute(sql)
            marca = puntero.fetchall()
            return marca
        elif tabla=='Producto':
            sql='select * from producto'
            puntero.execute(sql)
            producto = puntero.fetchall()
            return producto
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()

    def Delete(self, tabla, id):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            sql='delete from Sucursal where nombre = %s'
            puntero.execute(sql,(id,))
            print('Sucursal eliminado correctamente')
        elif tabla=='Categoria':
            sql='delete from Categoria where nombre = %s'
            puntero.execute(sql,(id,))
            print('Categoria eliminado correctamente')
        elif tabla=='Cliente':
            sql='delete from Cliente where id = %s'
            puntero.execute(sql,(id,))
            print('Cliente eliminado correctamente')
        elif tabla=='Fabricante':
            sql='delete from Fabricante where nombre = %s'
            puntero.execute(sql,(id,))
            print('Fabricante eliminado correctamente')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql='delete from Marca where nombre = %s'
            puntero.execute(sql,(id,))
            print('Marca eliminado correctamente')
        elif tabla=='Producto':
            sql='delete from Producto where nombre = %s'
            puntero.execute(sql,(id,))
            print('Producto eliminado correctamente')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()

    def Edit(self,tabla,data):
        puntero=self.conexion.cursor()

        if tabla=='Sucursal':
            sql='update Sucursal set nombre=%s, direccion=%s where nombre= %s'
            valores=(data[0],data[1],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Categoria':
            print('Datos modificados correctamente')

        elif tabla=='Cliente':
            sql=('update cliente set nombre=%s, apellido=%s, direccion=%s,'
                 'email=%s, telefono=%s, es_socio=%s where id= %s')
            valores=(data[1],data[2],data[3],data[4],data[5],data[6],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Fabricante':
            sql='update Fabricante set nombre=%s, direccion=%s where nombre= %s'
            valores=(data[0],data[1],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql=('SELECT marca.nombre '
                 ' FROM marca '
                 ' JOIN fabricante ON marca.id_fabricante = fabricante.id '
                 ' WHERE fabricante.nombre = %s')
            puntero.execute(sql,(data[0],))

            nombreActualMarca=puntero.fetchone()
            sql2='update Marca set nombre=%s where nombre= %s'
            valores=(data[1],nombreActualMarca)
            puntero.execute(sql2,valores)
            print('Datos modificados correctamente')
        elif tabla=='Producto':
            print('insert')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
    def searchIdAllTables(self,tabla,id):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            None
        elif tabla=='Categoria':
            sql='select id from Categoria where nombre=%s'
            puntero.execute(sql,(id,))
            idCategoria=puntero.fetchone()
            return idCategoria
        elif tabla=='Cliente':
            None
        elif tabla=='Fabricante':
            sql='select id from Fabricante where nombre=%s'
            puntero.execute(sql,(id,))
            idFabricante=puntero.fetchone()
            return idFabricante
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql='select id from Marca where nombre = %s'
            puntero.execute(sql,(id,))
            idMarca=puntero.fetchone()
            return idMarca
        elif tabla=='Producto':
            sql='select id from Producto where nombre = %s'
            puntero.execute(sql,(id,))
            idProducto=puntero.fetchone()
            return idProducto
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()

#======================================Codigo Factura==============================================================#
    def getNameProduct(self,codigo):
        puntero=self.conexion.cursor()
        sql='select nombre from producto where id = %s'
        puntero.execute(sql,(codigo,))
        nombre=puntero.fetchone()
        return nombre