import sys

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


from Vista.ventana import Ui_MainWindow
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal
from Controlador.CtrlClientes import CtrlCliente

class ControladorPrincipal(QMainWindow):

    def __init__(self,conexion):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conexion=conexion
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                           self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
        #--------------------------Pagina princpal--------------------------
        self.ui.btn_inicio.clicked.connect(self.panelSucursal)
        self.ui.btn_factura.clicked.connect(self.pagfactura)
        self.ui.btn_abastecer.clicked.connect(self.pagabastecer)
        self.ui.btn_agregarproducto.clicked.connect(self.pagagregarproducto)
        self.ui.btn_registrar.clicked.connect(self.pagregistrar)
        self.ui.btn_info.clicked.connect(self.paginfo)

        #----------------------Seccion Clientes---------------------------------#
        self.ui.btn_agregaruser.clicked.connect(self.obtencionDatosCliente)
        self.ui.btn_buscarUser.clicked.connect(self.buscarCliente)
        self.ui.btn_eliminaruser.clicked.connect(self.eliminarCliente)
        self.ui.btn_modificaruser.clicked.connect(self.modificarCliente)

        #--------------------------Seccion Sucursal--------------------------#
        self.ui.btnAgrSuc.clicked.connect(self.obtencionDatosSucursal)
        self.ui.btnBuscSuc.clicked.connect(self.buscarSucursal)
        self.ui.btnEditSuc.clicked.connect(self.modificarSucursal)
        self.ui.btnElimSuc.clicked.connect(self.eliminarSucursal)
        self.ui.btn_factura.clicked.connect(self.pagfactura)
        self.ui.btn_abastecer.clicked.connect(self.pagabastecer)
        self.ui.btn_agregarproducto.clicked.connect(self.pagagregarproducto)
        self.ui.btn_registrar.clicked.connect(self.panelClientes)
        self.ui.btn_info.clicked.connect(self.paginfo)
    # def paginicio(self):
    #     self.ui.stackedWidget.setCurrentIndex(0)

    def pagfactura(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def pagabastecer(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def pagagregarproducto(self):
        self.ui.stackedWidget.setCurrentIndex(3)

#-----------------------Obtecion de Datos Cliente---------------------------
    def panelClientes(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.tablaClientes()
        self.llenarDatosClientes()

    def obtencionDatosCliente(self):
        id=self.ui.txtIdentificacion.text()
        nombre=self.ui.txtNombres.text()
        apellido=self.ui.txtApellidos.text()
        direccion=self.ui.txtDireccion.text()
        email=self.ui.txtEmail.text()
        telefono=self.ui.txtTelefono.text()
        if self.ui.radiobtn_siuser.isChecked():
            socio=True
        elif self.ui.radiobtn_nouser.isChecked():
            socio=False

        datos=(id,nombre,apellido,direccion,email,telefono,socio)
        self.cliente=CtrlCliente(self.conexion)
        self.cliente.guardarCliente(datos)

    def buscarCliente(self):
        id=self.ui.txtIdentificacion.text()
        self.cliente=CtrlCliente(self.conexion)
        datosCliente=self.cliente.cargarDatosCliente(id)
        self.ui.txtNombres.setText(datosCliente[1])
        self.ui.txtApellidos.setText(datosCliente[2])
        self.ui.txtDireccion.setText(datosCliente[3])
        self.ui.txtEmail.setText(datosCliente[4])
        self.ui.txtTelefono.setText(datosCliente[5])
        if datosCliente[6]:
            self.ui.radiobtn_siuser.setChecked(True)
        elif datosCliente[6]==False:
            self.ui.radiobtn_nouser.setChecked(True)
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                           self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True)

    def eliminarCliente(self):
        id=self.ui.txtIdentificacion.text()
        self.cliente=CtrlCliente(self.conexion)
        self.cliente.eliminarCliente(id)
        self.vaciarCamposCliente()
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                           self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)

    def modificarCliente(self):
        id=self.ui.txtIdentificacion.text()
        nombre=self.ui.txtNombres.text()
        apellido=self.ui.txtApellidos.text()
        direccion=self.ui.txtDireccion.text()
        email=self.ui.txtEmail.text()
        telefono=self.ui.txtTelefono.text()
        if self.ui.radiobtn_siuser.isChecked():
            socio=True
        elif self.ui.radiobtn_nouser.isChecked():
            socio=False

        datos=(id,nombre,apellido,direccion,email,telefono,socio)
        self.cliente=CtrlCliente(self.conexion)
        self.cliente.modificarCliente(datos)
        self.vaciarCamposCliente()
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                           self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)

    def tablaClientes(self):
        self.ui.tablaClientes.setColumnCount(7)
        nombres_columnas = ["Cedula", "Nombres", "Apellidos", "Direccion", "Email", "Telefono", "Si es Socio"]
        self.ui.tablaClientes.setHorizontalHeaderLabels(nombres_columnas)


    def llenarDatosClientes(self):
        self.cliente=CtrlCliente(self.conexion)
        datosClientes=self.cliente.cargarTablaClientes()

        for row_num, datos in enumerate(datosClientes):
            self.ui.tablaClientes.insertRow(row_num)
            for col_num, valor in enumerate(datos):
                item = QTableWidgetItem(str(valor))
                self.ui.tablaClientes.setItem(row_num, col_num, item)

    def vaciarCamposCliente(self):
        self.ui.txtIdentificacion.setText('')
        self.ui.txtNombres.setText('')
        self.ui.txtApellidos.setText('')
        self.ui.txtDireccion.setText('')
        self.ui.txtEmail.setText('')
        self.ui.txtTelefono.setText('')
        self.ui.radiobtn_siuser.setChecked(False)
        self.ui.radiobtn_nouser.setChecked(False)


    def paginfo(self):
        self.ui.stackedWidget.setCurrentIndex(5)

        #Probando
        self.ui.btn_buscarUser.clicked.connect(lambda: self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True))

    #-------------------------------SUCURSAL------------------------------------------#
    def panelSucursal(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.tablaSucursal()
        self.llenarDatosSucursal()

    def cargarCmbSucursal(self):
        sucursal=


    def obtencionDatosSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        datos=(nombre,direccion)
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.guardarSucursal(datos)

    def buscarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        self.sucursal=CtrlSucursal(self.conexion)
        datosSucursal=self.sucursal.cargarDatosSucursal(nombre)
        self.ui.txtDirSucur.setText(datosSucursal[2])

    def modificarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        datos=(nombre,direccion)
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.modificarSucursal(datos)
        self.vaciarCamposSucursal()

    def eliminarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.eliminarSucursal(nombre)
        self.vaciarCamposSucursal()

    def tablaSucursal(self):
        self.ui.tableWidget.setColumnCount(3)
        nombres_columnas = ["Id", "Nombre", "Direccion"]
        self.ui.tableWidget.setHorizontalHeaderLabels(nombres_columnas)


    def llenarDatosSucursal(self):
        self.sucursal=CtrlSucursal(self.conexion)
        datosSucursal=self.sucursal.cargarTablaSucursal()

        for row_num, datos in enumerate(datosSucursal):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, valor in enumerate(datos):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(row_num, col_num, item)


    def vaciarCamposSucursal(self):
        self.ui.txtNomSucur.setText('')
        self.ui.txtDirSucur.setText('')

    def pagfactura(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def pagabastecer(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def pagagregarproducto(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def pagregistrar(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def paginfo(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def manejoBotones(self, buscar, agregar, modificar, eliminar, estado):
        buscar.setEnabled(not estado)
        agregar.setEnabled(not estado)
        modificar.setEnabled(estado)
        eliminar.setEnabled(estado)
