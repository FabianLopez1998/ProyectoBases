import sys
from datetime import datetime

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt6.uic.properties import QtWidgets

from Controlador.CtrlCategoria import CtrlCategoria
from Controlador.CtrlCategoriaProducto import CtrlCategoriaProducto
from Controlador.CtrlFabricante import CtrlFabricante
from Controlador.CtrlMarca import CtrlMarca
from Controlador.CtrlProducto import CtrlProducto
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
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)
        #--------------------------Pestañas parte superior--------------------------
        self.ui.btn_inicio.clicked.connect(self.paginicio)
        self.ui.btn_factura.clicked.connect(self.pagfactura)
        self.ui.btn_abastecer.clicked.connect(self.pagabastecer)
        self.ui.btn_agregarproducto.clicked.connect(self.pagagregarproducto)
        self.ui.btn_registrar.clicked.connect(self.pagregistrar)
        self.ui.btn_inventario.clicked.connect(self.paginventario)
        self.ui.btn_infoVentas.clicked.connect(self.pagventas)
        self.ui.btn_info_2.clicked.connect(self.pagDetallesAbast)
        self.ui.btn_info.clicked.connect(self.paginfo)

# <<<<<<< HEAD
#         #----------------------Seccion Clientes---------------------------------#
#         self.ui.btn_agregaruser.clicked.connect(self.obtencionDatosCliente)
#         self.ui.btn_buscarUser.clicked.connect(self.buscarCliente)
#         self.ui.btn_eliminaruser.clicked.connect(self.eliminarCliente)
#         self.ui.btn_modificaruser.clicked.connect(self.modificarCliente)
#
#         #--------------------------Seccion Sucursal--------------------------#
#         self.ui.btnAgrSuc.clicked.connect(self.obtencionDatosSucursal)
#         self.ui.btnBuscSuc.clicked.connect(self.buscarSucursal)
#         self.ui.btnEditSuc.clicked.connect(self.modificarSucursal)
#         self.ui.btnElimSuc.clicked.connect(self.eliminarSucursal)
#         self.ui.btn_factura.clicked.connect(self.pagfactura)
#         self.ui.btn_abastecer.clicked.connect(self.pagabastecer)
#         self.ui.btn_agregarproducto.clicked.connect(self.pagagregarproducto)
#         self.ui.btn_registrar.clicked.connect(self.panelClientes)
#         self.ui.btn_info.clicked.connect(self.paginfo)
#     # def paginicio(self):
#     #     self.ui.stackedWidget.setCurrentIndex(0)
#
#     def pagfactura(self):
#         self.ui.stackedWidget.setCurrentIndex(1)
#
#     def pagabastecer(self):
#         self.ui.stackedWidget.setCurrentIndex(2)
#
#     def pagagregarproducto(self):
#         self.ui.stackedWidget.setCurrentIndex(3)
#
# #-----------------------Obtecion de Datos Cliente---------------------------
#     def panelClientes(self):
#         self.ui.stackedWidget.setCurrentIndex(4)
#         self.tablaClientes()
#         self.llenarDatosClientes()
#
#     def obtencionDatosCliente(self):
#         id=self.ui.txtIdentificacion.text()
#         nombre=self.ui.txtNombres.text()
#         apellido=self.ui.txtApellidos.text()
#         direccion=self.ui.txtDireccion.text()
#         email=self.ui.txtEmail.text()
#         telefono=self.ui.txtTelefono.text()
#         if self.ui.radiobtn_siuser.isChecked():
#             socio=True
#         elif self.ui.radiobtn_nouser.isChecked():
#             socio=False
#
#         datos=(id,nombre,apellido,direccion,email,telefono,socio)
#         self.cliente=CtrlCliente(self.conexion)
#         self.cliente.guardarCliente(datos)
#
#     def buscarCliente(self):
#         id=self.ui.txtIdentificacion.text()
#         self.cliente=CtrlCliente(self.conexion)
#         datosCliente=self.cliente.cargarDatosCliente(id)
#         self.ui.txtNombres.setText(datosCliente[1])
#         self.ui.txtApellidos.setText(datosCliente[2])
#         self.ui.txtDireccion.setText(datosCliente[3])
#         self.ui.txtEmail.setText(datosCliente[4])
#         self.ui.txtTelefono.setText(datosCliente[5])
#         if datosCliente[6]:
#             self.ui.radiobtn_siuser.setChecked(True)
#         elif datosCliente[6]==False:
#             self.ui.radiobtn_nouser.setChecked(True)
#         self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
#                            self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True)
#
#     def eliminarCliente(self):
#         id=self.ui.txtIdentificacion.text()
#         self.cliente=CtrlCliente(self.conexion)
#         self.cliente.eliminarCliente(id)
#         self.vaciarCamposCliente()
#         self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
#                            self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
#
#     def modificarCliente(self):
#         id=self.ui.txtIdentificacion.text()
#         nombre=self.ui.txtNombres.text()
#         apellido=self.ui.txtApellidos.text()
#         direccion=self.ui.txtDireccion.text()
#         email=self.ui.txtEmail.text()
#         telefono=self.ui.txtTelefono.text()
#         if self.ui.radiobtn_siuser.isChecked():
#             socio=True
#         elif self.ui.radiobtn_nouser.isChecked():
#             socio=False
#
#         datos=(id,nombre,apellido,direccion,email,telefono,socio)
#         self.cliente=CtrlCliente(self.conexion)
#         self.cliente.modificarCliente(datos)
#         self.vaciarCamposCliente()
#         self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
#                            self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
#
#     def tablaClientes(self):
#         self.ui.tablaClientes.setColumnCount(7)
#         nombres_columnas = ["Cedula", "Nombres", "Apellidos", "Direccion", "Email", "Telefono", "Si es Socio"]
#         self.ui.tablaClientes.setHorizontalHeaderLabels(nombres_columnas)
#
#
#     def llenarDatosClientes(self):
#         self.cliente=CtrlCliente(self.conexion)
#         datosClientes=self.cliente.cargarTablaClientes()
#
#         for row_num, datos in enumerate(datosClientes):
#             self.ui.tablaClientes.insertRow(row_num)
#             for col_num, valor in enumerate(datos):
#                 item = QTableWidgetItem(str(valor))
#                 self.ui.tablaClientes.setItem(row_num, col_num, item)
#
#     def vaciarCamposCliente(self):
#         self.ui.txtIdentificacion.setText('')
#         self.ui.txtNombres.setText('')
#         self.ui.txtApellidos.setText('')
#         self.ui.txtDireccion.setText('')
#         self.ui.txtEmail.setText('')
#         self.ui.txtTelefono.setText('')
#         self.ui.radiobtn_siuser.setChecked(False)
#         self.ui.radiobtn_nouser.setChecked(False)
#
#
#     def paginfo(self):
#         self.ui.stackedWidget.setCurrentIndex(5)
#
#         #Probando
#         self.ui.btn_buscarUser.clicked.connect(lambda: self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True))
#
#     #-------------------------------SUCURSAL------------------------------------------#
#     def panelSucursal(self):
#         self.ui.stackedWidget.setCurrentIndex(0)
#         self.tablaSucursal()
#         self.llenarDatosSucursal()
#
#     def cargarCmbSucursal(self):
#         sucursal=
#
#
#     def obtencionDatosSucursal(self):
#         nombre=self.ui.txtNomSucur.text()
#         direccion=self.ui.txtDirSucur.text()
#         datos=(nombre,direccion)
#         self.sucursal=CtrlSucursal(self.conexion)
#         self.sucursal.guardarSucursal(datos)
#
#     def buscarSucursal(self):
#         nombre=self.ui.txtNomSucur.text()
#         self.sucursal=CtrlSucursal(self.conexion)
#         datosSucursal=self.sucursal.cargarDatosSucursal(nombre)
#         self.ui.txtDirSucur.setText(datosSucursal[2])
#
#     def modificarSucursal(self):
#         nombre=self.ui.txtNomSucur.text()
#         direccion=self.ui.txtDirSucur.text()
#         datos=(nombre,direccion)
#         self.sucursal=CtrlSucursal(self.conexion)
#         self.sucursal.modificarSucursal(datos)
#         self.vaciarCamposSucursal()
#
#     def eliminarSucursal(self):
#         nombre=self.ui.txtNomSucur.text()
#         self.sucursal=CtrlSucursal(self.conexion)
#         self.sucursal.eliminarSucursal(nombre)
#         self.vaciarCamposSucursal()
#
#     def tablaSucursal(self):
#         self.ui.tableWidget.setColumnCount(3)
#         nombres_columnas = ["Id", "Nombre", "Direccion"]
#         self.ui.tableWidget.setHorizontalHeaderLabels(nombres_columnas)
#
#
#     def llenarDatosSucursal(self):
#         self.sucursal=CtrlSucursal(self.conexion)
#         datosSucursal=self.sucursal.cargarTablaSucursal()
#
#         for row_num, datos in enumerate(datosSucursal):
#             self.ui.tableWidget.insertRow(row_num)
#             for col_num, valor in enumerate(datos):
#                 item = QTableWidgetItem(str(valor))
#                 self.ui.tableWidget.setItem(row_num, col_num, item)
#
#
#     def vaciarCamposSucursal(self):
#         self.ui.txtNomSucur.setText('')
#         self.ui.txtDirSucur.setText('')
#
# =======
        self.agregarTablaSucursal()
        #-------------------------------------- PAGINA1: PAGINA PRINCIPAL Y MANTENIMIENTO DE SUCURSAL -------------------------------------

        self.ui.btnAgrSuc.clicked.connect(self.agregarSucursal)
        self.ui.btnEditSuc.clicked.connect(self.editarSucursal)
        self.ui.btnElimSuc.clicked.connect(self.eliminarSucursal)
        self.ui.btn_cancelarSuc.clicked.connect(self.cancelarSucursal)
        self.ui.btnBuscSuc.clicked.connect(self.buscarSucursal)

        #-------------------------------------- PAGINA2: FACTURACION  -------------------------------------
        self.ui.btnBuscUserFact.clicked.connect(self.detallesClliente)
        self.ui.txtIdentificacion_3.setEnabled(True)
        self.ui.btnBuscProdFact.clicked.connect(self.buscarProductoFactura)
        #-------------------------------------- PAGINA3: ABASTECIMIENTO DEL SUPERMARKET -------------------------------------

        #-------------------------------------- PAGINA4: REGISTRO DE TODOS LOS DATOS  -------------------------------------

        self.ui.btnBuscFabri.clicked.connect(self.buscarFabricante)
        self.ui.btnAgrFabri.clicked.connect(self.agregarFabricante)
        self.ui.btnEditFabri.clicked.connect(self.editarFabricante)
        self.ui.btnElimFabri.clicked.connect(self.eliminarFabricante)
        self.ui.btn_cancelarfab.clicked.connect(self.cancelarFabricante)

        self.ui.btnBuscMarca.clicked.connect(self.buscarMarca)
        self.ui.btnAgrMarca.clicked.connect(self.agregarMarca)
        self.ui.btnEditMarca.clicked.connect(self.editarMarca)
        self.ui.btnElimMarca.clicked.connect(self.eliminarMarca)
        self.ui.btn_cancelarmarc.clicked.connect(self.cancelarMarca)

        self.ui.btnBuscCat.clicked.connect(self.buscarCategoria)
        self.ui.btnAgrCat.clicked.connect(self.agregarCategoria)
        self.ui.btnEditCat.clicked.connect(self.editarCategoria)
        self.ui.btnElimCat.clicked.connect(self.eliminarCategoria)
        self.ui.btn_cancelarcate.clicked.connect(self.cancelarCategoria)

        self.ui.btnBuscProduc.clicked.connect(self.buscarProducto)
        self.ui.btnAgrProd.clicked.connect(self.agregarProducto)
        self.ui.btnEditProd.clicked.connect(self.editarProducto)
        self.ui.btnElimProd.clicked.connect(self.eliminarProducto)
        self.ui.btn_cancelarpro.clicked.connect(self.cancelarProducto)

        self.ui.btnAgrCatProd.clicked.connect(self.agregarProductoCategoria)

        #-------------------------------------- PAGINA5: REGISTRO DE USUARIOS  -------------------------------------

        self.ui.btn_buscarUser.clicked.connect(self.buscarCliente)
        self.ui.btn_agregaruser.clicked.connect(self.agregarCliente)
        self.ui.btn_modificaruser.clicked.connect(self.editarCliente)
        self.ui.btn_eliminaruser.clicked.connect(self.eliminarCliente)
        self.ui.btn_cancelaruser.clicked.connect(self.cancelarCliente)

        #-------------------------------------- PAGINA6: INVENTARIO  -------------------------------------
        #-------------------------------------- PAGINA7: DETALLES DE VENTAS  -------------------------------------
        #-------------------------------------- PAGINA8: DETALLE DE ABASTECIMIENTOS -------------------------------------





    #--------------------------------- MANEJO DE CAMBIOS DE PESTAÑAS ------------------------------
    def paginicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.agregarTablaSucursal()
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)

# >>>>>>> origin/Alejandro
    def pagfactura(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.cargarFechaActual()
    def pagabastecer(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def pagagregarproducto(self):
        self.cargarComboFabricante()
        self.cargarComboCategoria()
        self.cargarComboMarca()
        self.cargarComboCategoriaProducto()
        self.cargarComboProductos()
        self.ui.stackedWidget.setCurrentIndex(3)
        self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri, False)
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca, False)
        self.manejoBotones(self.ui.btnBuscCat, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat, False)
        self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd, False)

    def pagregistrar(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
    def paginventario(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def pagventas(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def pagDetallesAbast(self):
        self.ui.stackedWidget.setCurrentIndex(7)
    def paginfo(self):
        self.ui.stackedWidget.setCurrentIndex(8)



    #-------------------------------------- PAGINA1: PAGINA PRINCIPAL Y MANTENIMIENTO DE SUCURSAL -------------------------------------
    def agregarTablaSucursal(self):
        self.sucursal=CtrlSucursal(self.conexion)
        datosSucursal=self.sucursal.cargarTablaSucursal()
        self.cargarDatosTabla(datosSucursal,['id','Nombre','Direccion'],self.ui.tableWidget)
    def buscarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        self.sucursal=CtrlSucursal(self.conexion)
        datosSucursal=self.sucursal.cargarDatosSucursal(nombre)
        self.ui.txtDirSucur.setText(datosSucursal[2])
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc,
                           self.ui.btnEditSuc, self.ui.btnElimSuc, True)

    def agregarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        if nombre!='' and direccion != '':
            datos=(nombre,direccion)
            self.sucursal=CtrlSucursal(self.conexion)
            self.sucursal.guardarSucursal(datos)
            QMessageBox.information(self, "Registro", "Sucursal agregada con éxito!")
            self.cancelarSucursal()
            self.agregarTablaSucursal()
            pass
        else:
            QMessageBox.information(self, "Sucursales", "Llene todos los campos!")

    def editarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        if nombre!= '' and direccion != '':
            datos=(nombre,direccion)
            self.sucursal=CtrlSucursal(self.conexion)
            self.sucursal.modificarSucursal(datos)
            QMessageBox.information(self, "Registro", "Sucursal modificada con éxito!")
            self.cancelarSucursal()
            self.agregarTablaSucursal()
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc,
                               self.ui.btnElimSuc, False)
            pass
        else:
            QMessageBox.information(self, "Sucursales", "Llene todos los campos!")

    def eliminarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.eliminarSucursal(nombre)
        QMessageBox.information(self, "Registro", "Sucursal eliminada con éxito!")
        self.cancelarSucursal()
        self.agregarTablaSucursal()
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc,
                           self.ui.btnEditSuc, self.ui.btnElimSuc, False)

    def cancelarSucursal(self):
        self.ui.txtNomSucur.setText("")
        self.ui.txtDirSucur.setText("")
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)


    #-------------------------------------- PAGINA2: FACTURACION  -------------------------------------
    def cargarFechaActual(self):
        fecha_actual = datetime.now().date()
        self.ui.lblFecha.setText(str(fecha_actual))

    def detallesClliente(self):
        id=self.ui.txtIdentificacion_3.text()
        self.cliente=CtrlCliente(self.conexion)
        datosCliente=self.cliente.cargarDatosCliente(id)
        self.ui.lblNombres.setText(datosCliente[1])
        self.ui.lblApellidos.setText(datosCliente[2])
        self.ui.lblDireccion.setText(datosCliente[3])
        self.ui.lblemail.setText(datosCliente[4])
        self.ui.lblTelefono.setText(datosCliente[5])
        if datosCliente[6]:
            self.ui.lblDescuento.setText('Si')
        elif datosCliente[6]==False:
            self.ui.lblDescuento.setText('No')

    def buscarProductoFactura(self):
        producto=CtrlProducto(self.conexion)
        nombre=producto.cargarNombreProducto(self.ui.txtbuscarProducto2.text())
        print('descr',nombre)
        self.ui.lblApellidos_2.setText(nombre[0])
    #-------------------------------------- PAGINA3: ABASTECIMIENTO DEL SUPERMARKET -------------------------------------
    #-------------------------------------- PAGINA4: REGISTRO DE TODOS LOS DATOS  -------------------------------------


    ###FABRICANTE
    def buscarFabricante(self):
        nombre=self.ui.txtNomFabri.text()
        fabricante=CtrlFabricante(self.conexion)
        datosFabricante=fabricante.cargarDatosFabricante(nombre)
        self.ui.txtDirFabri.setText(datosFabricante[2])
        self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri,
                           self.ui.btnElimFabri, True)
    def agregarFabricante(self):
        nombre=self.ui.txtNomFabri.text()
        direccion=self.ui.txtDirFabri.text()
        if nombre!='' and direccion != '':
            fabricanteDatos=(nombre,direccion)
            self.fabricante=CtrlFabricante(self.conexion)
            self.fabricante.guardarFabricante(fabricanteDatos)
            QMessageBox.information(self, "Registro", "Fabricante agregada con éxito!")
            self.cancelarFabricante()
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def editarFabricante(self):
        nombre=self.ui.txtNomFabri.text()
        direccion=self.ui.txtDirFabri.text()
        if nombre!= '' and direccion != '':
            datos=(nombre,direccion)
            self.fabricante=CtrlFabricante(self.conexion)
            self.fabricante.modificarFabricante(datos)
            QMessageBox.information(self, "Registro", "Fabricante modificada con éxito!")
            self.cancelarFabricante()
            self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri,
                               self.ui.btnEditFabri, self.ui.btnElimFabri,False)
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def eliminarFabricante(self):
        if True:
            nombre=self.ui.txtNomFabri.text()
            self.fabricante=CtrlFabricante(self.conexion)
            self.fabricante.eliminarFabricante(nombre)
            QMessageBox.information(self, "Registro", "Fabricante eliminada con éxito!")
            self.cancelarFabricante()
            self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri,
                               self.ui.btnEditFabri, self.ui.btnElimFabri, False)
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def cancelarFabricante(self):
        self.ui.txtNomFabri.setText("")
        self.ui.txtDirFabri.setText("")
        self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri,False)


    ##MARCA

    def buscarMarca(self):
        nombre=self.ui.txtNomMarca.text()
        marca=CtrlMarca(self.conexion)
        datosMarca=marca.cargarDatosMarca(nombre)
        self.ui.combFabric_Marca.setCurrentText(datosMarca[1])
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca,
                           self.ui.btnEditMarca, self.ui.btnElimMarca, True)

    def agregarMarca(self):
        fabricante=CtrlFabricante(self.conexion)
        marca=CtrlMarca(self.conexion)
        nombre=self.ui.txtNomMarca.text()
        idFabricante=fabricante.cargarIdFabricante(self.ui.combFabric_Marca.currentText())
        marcaDatos=(nombre,idFabricante)
        marca.guardarMarca(marcaDatos)
        self.cancelarMarca()
        QMessageBox.information(self, "Registro", "Marca agregada con éxito!")
        pass

    def editarMarca(self):
        nombreProveedor=self.ui.combFabric_Marca.currentText()
        nuevoNombreMarca=self.ui.txtNomMarca.text()
        marca=CtrlMarca(self.conexion)
        datos=(nombreProveedor,nuevoNombreMarca)
        marca.modificarMarca(datos)
        QMessageBox.information(self, "Registro", "Marca modificada con éxito!")
        self.cancelarMarca()
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca,
                           self.ui.btnEditMarca, self.ui.btnElimMarca,False)

    def eliminarMarca(self):
        nombre=self.ui.txtNomMarca.text()
        marca=CtrlMarca(self.conexion)
        marca.eliminarMarca(nombre)
        QMessageBox.information(self, "Registro", "Marca eliminada con éxito!")
        self.cancelarMarca()
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca,
                           self.ui.btnEditMarca, self.ui.btnElimMarca,False)


    def cancelarMarca(self):
        self.ui.txtNomMarca.setText("")
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca,
                           self.ui.btnEditMarca, self.ui.btnElimMarca,False)

    ##CATEGORIA

    def buscarCategoria(self):
        if True:
            nombre=self.ui.lineEditCat.text()
            categoria=CtrlCategoria(self.conexion)
            datosCategoria=categoria.cargarDatosCategoria(nombre)
            self.ui.combCatPadre.setCurrentText(datosCategoria[0])
            self.manejoBotones(self.ui.btnBuscCat, self.ui.btnAgrCat,
                               self.ui.btnEditCat, self.ui.btnElimCat, True)
        else:
            QMessageBox.warning(self, "ERROR", "No existe la Categoría!")

    def agregarCategoria(self):
        if True:
            categoria=CtrlCategoria(self.conexion)
            nombre=self.ui.lineEditCat.text()
            idCategoria=categoria.cargarIdCategoria(self.ui.combCatPadre.currentText())
            print('holaaaa',nombre,idCategoria)
            categoriaDatos=(nombre,idCategoria)
            categoria.guardarCategoria(categoriaDatos)
            self.cancelarCategoria()
            QMessageBox.information(self, "Registro", "Categoría agregada con éxito!")
        else:
            QMessageBox.information(self, "Categoría", "!")

    def editarCategoria(self):
        if True:
            nombreCategoriaCmb=self.ui.combCatPadre.currentText()
            nuevoNombreCategoria=self.ui.lineEditCat.text()
            categoria=CtrlCategoria(self.conexion)
            datos=(nombreCategoriaCmb,nuevoNombreCategoria)
            categoria.modificarCategoria(datos)
            QMessageBox.information(self, "Registro", "Categoria modificada con éxito!")
            self.cancelarCategoria()
            self.manejoBotones(self.ui.btnBuscCat, self.ui.btnAgrCat,
                               self.ui.btnEditCat, self.ui.btnElimCat,False)
            pass
        else:
            QMessageBox.information(self, "Categoría", "!")

    def eliminarCategoria(self):
        if True:
            nombre=self.ui.lineEditCat.text()
            categoria=CtrlCategoria(self.conexion)
            categoria.eliminarCategoria(nombre)
            QMessageBox.information(self, "Registro", "Marca eliminada con éxito!")
            self.cancelarCategoria()
            self.manejoBotones(self.ui.btnBuscCat, self.ui.btnAgrCat,
                               self.ui.btnEditCat, self.ui.btnElimCat,False)
        else:
            QMessageBox.information(self, "Categoría", "!")

    def cancelarCategoria(self):
        self.ui.lineEditCat.setText("")
        self.manejoBotones(self.ui.btnBuscCat, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat,False)

    ##PRODUCTO

    def buscarProducto(self):
        if True:
            nombre=self.ui.txtDescripcion.text()
            producto=CtrlProducto(self.conexion)
            datosProducto=producto.cargarDatosProducto(nombre)
            print('datososs: ',datosProducto)
            self.ui.txtTamanio.setText(datosProducto[0])
            self.ui.txtMedida.setText(datosProducto[1])
            self.ui.combMarcaProd.setCurrentText(datosProducto[2])
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd,
                               self.ui.btnEditProd, self.ui.btnElimProd, True)
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Producto!")

    def agregarProducto(self):
        if True:
            producto=CtrlProducto(self.conexion)
            marca=CtrlMarca(self.conexion)
            categoria=CtrlCategoria(self.conexion)

            nombre=self.ui.txtDescripcion.text()
            marcaId=marca.cargarIdMarca(self.ui.combMarcaProd.currentText())
            tamanio=self.ui.txtTamanio.text()
            medida=self.ui.txtMedida.text()
            categoriaId=categoria.cargarIdCategoria(self.ui.combCatProd.currentText())#otra tabla
            datos=(nombre,tamanio,medida,marcaId)
            producto.guardarProductp(datos)
            self.cancelarProducto()

            QMessageBox.information(self, "Registro", "Producto agregado con éxito!")
            pass
        else:
            QMessageBox.information(self, "Producto", "!")

    def editarProducto(self):
        if True:
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd,False)
            pass
        else:
            QMessageBox.information(self, "Producto", "!")

    def eliminarProducto(self):
        if True:
            nombre=self.ui.txtDescripcion.text()
            producto=CtrlProducto(self.conexion)
            producto.eliminarProducto(nombre)
            QMessageBox.information(self, "Registro", "Producto eliminado con éxito!")
            self.cancelarProducto()
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd,
                               self.ui.btnEditProd, self.ui.btnElimProd,False)
            pass
        else:
            QMessageBox.information(self, "Producto", "!")

    def agregarProductoCategoria(self):
        producto=CtrlProducto(self.conexion)
        categoria=CtrlCategoria(self.conexion)
        categoria_producto=CtrlCategoriaProducto(self.conexion)

        productoId=producto.cargarIdProducto(self.ui.combCatProd_2.currentText())
        categoriaId=categoria.cargarIdCategoria(self.ui.combCatProd.currentText())
        datos=(productoId,categoriaId)
        categoria_producto.guardarCategoriaProducto(datos)
        QMessageBox.information(self, "Registro", "Producto Categoria Agregado con éxito!")

    def cancelarProducto(self):
        self.ui.txtDescripcion.setText("")
        self.ui.txtTamanio.setText("")
        self.ui.txtMedida.setText("")
        self.ui.txtDescripcion.setText("")
        self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd,False)

    #-------------------------------------- PAGINA5: REGISTRO DE CLIENTES  -------------------------------------

    def buscarCliente(self):
        if True:
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
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Cliente!")

    def agregarCliente(self):
        if True:
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
            QMessageBox.information(self, "Registro", "Cliente agregado con éxito!")
            pass
        else:
            QMessageBox.information(self, "Clientes", "!")

    def editarCliente(self):
        if True:
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
            self.cancelarCliente()
            self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                               self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
            pass
        else:
            QMessageBox.information(self, "Clientes", "!")

    def eliminarCliente(self):
        if True:
            id=self.ui.txtIdentificacion.text()
            self.cliente=CtrlCliente(self.conexion)
            self.cliente.eliminarCliente(id)
            self.cancelarCliente()
            self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser,
                               self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
            pass
        else:
            QMessageBox.information(self, "Clientes", "!")

    def cancelarCliente(self):
        self.ui.txtIdentificacion.setText("")
        self.ui.txtNombres.setText("")
        self.ui.txtApellidos.setText("")
        self.ui.txtDireccion.setText("")
        self.ui.txtTelefono.setText("")
        self.ui.txtEmail.setText("")
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)



    #-------------------------------------- PAGINA6: INVENTARIO  -------------------------------------
    #-------------------------------------- PAGINA7: DETALLES DE VENTAS  -------------------------------------
    #-------------------------------------- PAGINA8: DETALLE DE ABASTECIMIENTOS -------------------------------------






    #--------------------------------------- CODIGOS EXTRA PARA TODAS LAS VENTANAS --------------------------------------
    def cargarComboProductos(self):
        self.ui.combCatProd_2.clear()
        producto=CtrlProducto(self.conexion)
        datos=producto.cargarTablaProducto()
        self.ui.combCatProd_2.addItems([item[1] for item in datos])
    def cargarComboMarca(self):
        self.ui.combMarcaProd.clear()
        marca=CtrlMarca(self.conexion)
        datos=marca.cargarTablaMarca()
        self.ui.combMarcaProd.addItems([item[1] for item in datos])
    def cargarComboCategoria(self):
        self.ui.combCatPadre.clear()
        categoria=CtrlCategoria(self.conexion)
        datos=categoria.cargarTablaCategoria()
        self.ui.combCatPadre.addItems([item[1] for item in datos])

    def cargarComboCategoriaProducto(self):
        self.ui.combCatProd.clear()
        categoria=CtrlCategoria(self.conexion)
        datos=categoria.cargarTablaCategoria()
        self.ui.combCatProd.addItems([item[1] for item in datos])
    def cargarComboFabricante(self):
        self.ui.combFabric_Marca.clear()
        fabricante=CtrlFabricante(self.conexion)
        datos=fabricante.cargarTablaFabricante()
        self.ui.combFabric_Marca.addItems([item[1] for item in datos])
    def cargarComboSucursal(self):
        self.ui.comboBox.clear()
        sucursal=CtrlSucursal(self.conexion)
        datos=sucursal.cargarTablaSucursal()
        for suc in datos:
            self.ui.comboBox.addItem(suc.nombre)
    def manejoBotones(self, buscar, agregar, modificar, eliminar, estado):
        buscar.setEnabled(not estado)
        agregar.setEnabled(not estado)
        modificar.setEnabled(estado)
        eliminar.setEnabled(estado)

    def cargarDatosTabla(self, lista, columnas, tabla):
        tabla.setColumnCount(len(columnas))
        tabla.setHorizontalHeaderLabels(columnas)

        for row_num, datos in enumerate(lista):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, valor in enumerate(datos):
                item = QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(row_num, col_num, item)



    def limpiaTabla(self, tabla):
        tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.clearContents()
        tabla.setRowCount(0)
