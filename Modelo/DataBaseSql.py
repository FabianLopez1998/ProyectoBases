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
            sql='insert into Factura(fecha, id_sucursal, id_cliente) values ( %s, %s, %s)'
            puntero.execute(sql, (data[0], data[1],data[2]))
            print('objeto insertado correctamente')
        elif tabla=='Factura_Producto':
            sql='insert into factura_producto(id_producto, id_factura, cantidad,precio_unitario) values ( %s, %s, %s, %s)'
            puntero.execute(sql, (data[0], data[3],data[1],data[2]))
            print('objeto insertado correctamente')
        elif tabla=='Inventario':
            sql=('insert into Inventario(id_sucursal, id_producto, cantidad, precio_base, fecha) '
                 'values ( %s, %s,%s, %s,%s)')
            valores=(data[0],data[1],data[2],data[3],data[4])
            puntero.execute(sql,valores)
            print('Datos insertados correctamente')
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
                 ' where producto.nombre = %s')
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
            sql='select * from factura_producto'
            puntero.execute(sql)
            factura_producto = puntero.fetchall()
            return factura_producto
        elif tabla=='Inventario':
            sql='select * from inventario'
            puntero.execute(sql)
            fabricante = puntero.fetchall()
            return fabricante
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
            sql='update Sucursal set nombre=%s, direccion=%s where id= %s'
            valores=(data[1],data[2],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Categoria':
            sql='update Categoria set nombre = %s, categoria_padre = %s where id = %s'
            valores=(data[2],data[1],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Cliente':
            sql=('update cliente set nombre=%s, apellido=%s, direccion=%s,'
                 'email=%s, telefono=%s, es_socio=%s where id= %s')
            valores=(data[1],data[2],data[3],data[4],data[5],data[6],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Fabricante':
            sql='update Fabricante set nombre=%s, direccion=%s where id= %s'
            valores=(data[1],data[2],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Factura':
            print('insert')
        elif tabla=='Factura_Producto':
            print('insert')
        elif tabla=='Inventario':
            print('insert')
        elif tabla=='Marca':
            sql='update Marca set nombre=%s where id= %s'
            valores=(data[1],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Producto':
            sql='update Producto set nombre=%s, tamanio=%s, medida=%s, id_marca=%s where id= %s'
            valores=(data[1],data[2],data[3],data[4],data[0])
            puntero.execute(sql,valores)
            print('Datos modificados correctamente')
        elif tabla=='Producto_Categoria':
            print('insert')
        else:print('ocurrio un error, Tabla no encontrada')
        self.conexion.commit()
    def searchIdAllTables(self,tabla,id):
        puntero=self.conexion.cursor()
        if tabla=='Sucursal':
            sql='select id from Sucursal where nombre=%s'
            puntero.execute(sql,(id,))
            idSucursal=puntero.fetchone()
            return idSucursal
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

    def getLastIdFact(self):
        puntero=self.conexion.cursor()
        sql=' select max(id) from Factura'
        puntero.execute(sql)
        ultimoId=puntero.fetchone()[0]
        #print('base ',ultimoId[0])
        if ultimoId is None:
            return 0
        else:
            return ultimoId
    def dameTablaPorFechaVentas(self, fecha):
        puntero=self.conexion.cursor()
        sql=('''SELECT
                     f.id AS id_factura,
                     s.nombre AS nombre_sucursal,
                     f.id_cliente,
                     f.fecha,
                     SUM(fp.cantidad * fp.precio_unitario) AS precio_total
                FROM
                    Factura f
                JOIN
                    Sucursal s ON f.id_sucursal = s.id
                JOIN
                    Factura_Producto fp ON f.id = fp.id_factura
                WHERE
                    f.fecha = %s 
                GROUP BY
                    f.id, s.nombre, f.id_cliente, f.fecha
                ORDER BY
                    f.fecha DESC; 
        ''')
        puntero.execute(sql,(fecha,))
        detalles=puntero.fetchall()
        return detalles
    def dameTablaVentas(self):
        puntero=self.conexion.cursor()
        sql=('''SELECT
                    f.id AS id_factura,
                    s.nombre AS nombre_sucursal,
                    f.id_cliente,
                    f.fecha,
                    SUM(fp.cantidad * fp.precio_unitario) AS precio_total
                FROM
                    Factura f
                JOIN
                    Sucursal s ON f.id_sucursal = s.id
                JOIN
                    Factura_Producto fp ON f.id = fp.id_factura
                GROUP BY
                    f.id, s.nombre, f.id_cliente, f.fecha
                ORDER BY
                    f.fecha DESC;
            ''')
        puntero.execute(sql)
        detalles=puntero.fetchall()
        return detalles
#======================================Codigo Abastecimiento==============================================================#

    def getTablaProductosPorProveedor(self, fab):
        puntero=self.conexion.cursor()
        sql='''SELECT P.id, P.nombre, M.nombre, P.tamanio, P.medida
            FROM Fabricante F
            JOIN Marca M ON F.id = M.id_fabricante
            JOIN Producto P ON M.id = P.id_marca
            WHERE F.nombre = %s'''
        puntero.execute(sql,(fab,))
        tabla=puntero.fetchall()
        return tabla

    def SearchIdTableProducto(self, id):
        puntero=self.conexion.cursor()
        sql=('select producto.nombre, marca.nombre, producto.tamanio, producto.medida'
             ' from producto '
             ' join marca on marca.id = producto.id_marca '
             ' where producto.id = %s ')
        puntero.execute(sql,(id,))
        producto=puntero.fetchone()
        return producto

    def dameTablaPorFecha(self, fecha):
        puntero=self.conexion.cursor()
        sql=('''SELECT
             s.nombre AS nombre_sucursal,
             p.nombre AS nombre_producto,
             i.cantidad,
             i.precio_base,
             i.fecha
             FROM
             Inventario i
             JOIN
             Sucursal s ON i.id_sucursal = s.id
             JOIN
             Producto p ON i.id_producto = p.id
             WHERE
             i.fecha = %s
             ORDER BY
             i.fecha DESC; 
             ''')
        puntero.execute(sql,(fecha,))
        detalles=puntero.fetchall()
        return detalles
    def dameTablaAbastecimientos(self):
        puntero=self.conexion.cursor()
        sql=('''SELECT
                    s.nombre AS nombre_sucursal,
                    p.nombre AS nombre_producto,
                    i.cantidad,
                    i.precio_base,
                    i.fecha
                FROM
                    Inventario i
                JOIN
                    Sucursal s ON i.id_sucursal = s.id
                JOIN
                    Producto p ON i.id_producto = p.id
                ORDER BY
                    i.fecha DESC; 
            ''')
        puntero.execute(sql)
        detalles=puntero.fetchall()
        return detalles

#============================dar precio base====================================
    def getPriceBase(self,id):
        puntero=self.conexion.cursor()
        sql=('SELECT i.precio_base '
             ' FROM Inventario i '
             ' JOIN ( '
             ' SELECT id_producto, MAX(fecha) AS max_fecha '
             ' FROM Inventario '
             ' GROUP BY id_producto '
             ' ) subquery ON i.id_producto = subquery.id_producto AND i.fecha = subquery.max_fecha '
             ' WHERE i.id_producto = %s '
             ' limit 1 ')
        puntero.execute(sql,id)
        precioBase=puntero.fetchone()
        return precioBase
#==================================================Extras=================================
    def dameProductoMarcaId(self, id, marca):
        puntero=self.conexion.cursor()
        sql=('select producto.tamanio, producto.medida as nombreProducto, marca.nombre as nombreMarca '
             ' from producto '
             ' join marca on marca.id = producto.id_marca '
             ' where producto.nombre = %s and marca.id = %s')
        puntero.execute(sql,(id,marca))
        producto=puntero.fetchone()
        return producto
    def modificarProducto(self, data):
        puntero=self.conexion.cursor()
        sql='update Producto set nombre=%s, tamanio=%s, medida=%s, id_marca=%s where id= %s and id_marca = %s'
        valores=(data[1],data[2],data[3],data[4],data[0], data[4])
        puntero.execute(sql,valores)
        print('Datos modificados correctamente')
    def buscarProducto_Categoria(self, prod, cat):
        puntero=self.conexion.cursor()
        sql=('select producto_categoria.id_producto, producto_categoria.id_categoria'
             ' from producto_categoria '
             ' where producto_categoria.id_producto = %s and producto_categoria.id_categoria = %s')
        puntero.execute(sql,(prod,cat))
        producto=puntero.fetchone()
        return producto


    def clienteConDescuento(self):
        puntero=self.conexion.cursor()
        sql='select * from cliente where cliente.es_socio'
        puntero.execute(sql)
        cliente=puntero.fetchall()
        return cliente

    def darTablaInventarioAbastecimiento(self):
        puntero=self.conexion.cursor()
        sql=('SELECT id_sucursal,id_producto, '
             ' SUM(cantidad) AS total_cantidad, '
             ' MAX(precio_base) AS max_precio '
             ' FROM Inventario '
             ' GROUP BY'
             ' id_sucursal,id_producto')
        puntero.execute(sql)
        datos=puntero.fetchall()
        return datos
    def ingresarTablaNueva(self,data):
        puntero=self.conexion.cursor()
        sql='select cantidad from inventariofactura where id_sucursal = %s and id_producto = %s'
        puntero.execute(sql,(data[0],data[1]))
        resultado=puntero.fetchone()
        if resultado is None:
            sql='insert into InventarioFactura(id_sucursal,id_producto,cantidad,precio) values (%s, %s, %s, %s)'
            puntero.execute(sql,(data[0],data[1],data[2],data[3]))
        else:
            cantidadSumada=str(int(resultado[0])+int(data[2]))
            sql2='update  InventarioFactura set cantidad=%s where id_sucursal = %s and id_producto = %s'
            valores=(cantidadSumada,data[0],data[1])
            puntero.execute(sql2,valores)
        self.conexion.commit()

    def vaciarTablaNueva(self):
        puntero=self.conexion.cursor()
        sql='delete from  InventarioFactura'
        puntero.execute(sql)
        self.conexion.commit()
    def restarCantidadNuevaTabla(self,datos):
        puntero=self.conexion.cursor()
        sql=('SELECT cantidad '
             ' FROM InventarioFactura '
             ' WHERE id_sucursal = %s AND id_producto = %s')
        puntero.execute(sql,(datos[2],datos[0]))
        cantidadActual=puntero.fetchone()
        cantidadARestar=datos[1]
        cantidadRestada=str(int(cantidadActual[0])-int(cantidadARestar))
        sql2=('update inventarioFactura '
              ' set cantidad = %s'
              'where id_sucursal = %s and id_producto = %s')
        puntero.execute(sql2,(cantidadRestada,datos[2],datos[0]))

        self.conexion.commit()

#================== INVENTARIO DEL SUPERMERCADO CONSULTAS ========================
    def dameTablaPorCategoriaInventario(self, sucursal, categoria):
        puntero=self.conexion.cursor()
        sql=('''SELECT
                    p.id,
                    p.nombre AS nombre_producto,
                    i.cantidad,
                    i.precio
                FROM
                    InventarioFactura i
                JOIN
                    Sucursal s ON i.id_sucursal = s.id
                JOIN
                    Producto p ON i.id_producto = p.id
                JOIN
                    Producto_Categoria pc ON p.id = pc.id_producto
                JOIN
                    Categoria c ON pc.id_categoria = c.id
                WHERE
                    s.nombre = %s AND c.nombre = %s; 
            ''')
        puntero.execute(sql,(sucursal, categoria))
        detalles=puntero.fetchall()
        return detalles
    def dameTablaInventario(self, sucursal):
        puntero=self.conexion.cursor()
        sql=('''SELECT
                    p.id,
                    p.nombre AS nombre_producto,
                    i.cantidad,
                    i.precio
                FROM
                    InventarioFactura i
                JOIN
                    Sucursal s ON i.id_sucursal = s.id
                JOIN
                    Producto p ON i.id_producto = p.id
                WHERE
                    s.nombre = %s; 
                ''')
        puntero.execute(sql,(sucursal,))
        detalles=puntero.fetchall()
        return detalles

#=================== MANEJO DE VISTAS ====================
    def crearVistaTemporal(self):
        puntero = self.conexion.cursor()
        sql = '''
            CREATE TEMPORARY VIEW vista_temporal AS
                SELECT
                    i.id AS id_inventario,
                    s.nombre AS nombre_sucursal,
                    p.nombre AS nombre_producto,
                    i.cantidad,
                    i.fecha,
                    i.precio_base
                FROM
                    Inventario i
                JOIN
                    Sucursal s ON i.id_sucursal = s.id
                JOIN
                    Producto p ON i.id_producto = p.id;

        '''
        puntero.execute(sql)
        self.conexion.commit()

    def AgregarDatosVista(self,id_suc, id_pro, cantidad, precio, fecha):
        # Inserción en la vista temporal
        puntero = self.conexion.cursor()
        sql = '''
            INSERT INTO vista_temporal (id_factura, nombre_sucursal, id_cliente, fecha, precio_total)
            VALUES (%s, %s, %s, %s, %s);
        '''
        puntero.execute(sql, (id_suc, id_pro, cantidad, precio, fecha))
        self.conexion.commit()
