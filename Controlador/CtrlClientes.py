from Modelo.DataBaseSql import DataBaseSql

class CtrlCliente:
    def __init__(self,conexion):
        self.conexion=conexion
        self.insertar=DataBaseSql(self.conexion)
        #self.id,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.socio = datos

    def guardarCliente(self,datos):
        self.id,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.socio = datos
        self.insertar.Insert('Cliente', (self.id, self.nombre, self.apellido, self.direccion,
                                         self.email, self.telefono, self.socio))

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