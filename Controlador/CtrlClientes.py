from Modelo.DataBaseSql import DataBaseSql

class CtrlCliente:
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)

    def guardarCliente(self,datos):
        self.id,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.socio = datos
        if self.cargarDatosCliente(self.id) == None:
            self.insertar.Insert('Cliente', (self.id, self.nombre, self.apellido, self.direccion,
                                             self.email, self.telefono, self.socio))
            return True
        else: return False

    def cargarDatosCliente(self,id):
        self.id=id
        datos=self.insertar.SearchIdTable('Cliente',id)
        return datos

    def eliminarCliente(self,id):
        self.id=id
        self.insertar.Delete('Cliente', id)

    def modificarCliente(self,datos):
        self.id,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.socio = datos
        self.insertar.Edit('Cliente',(self.id, self.nombre, self.apellido, self.direccion,
                                      self.email, self.telefono, self.socio))

    def cargarTablaClientes(self):
        clientes=self.insertar.searchAllTables('Cliente')
        return clientes

    def cargarTablaClientesConDescuento(self):
        clientes=self.insertar.clienteConDescuento()
        return clientes