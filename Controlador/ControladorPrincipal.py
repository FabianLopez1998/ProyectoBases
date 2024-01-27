import sys

from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt6.uic.properties import QtWidgets

from Vista.ventana import Ui_MainWindow
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal

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

        #-------------------------------------- PAGINA1: PAGINA PRINCIPAL Y MANTENIMIENTO DE SUCURSAL -------------------------------------

        self.ui.btnAgrSuc.clicked.connect(self.agregarSucursal)
        self.ui.btnEditSuc.clicked.connect(self.editarSucursal)
        self.ui.btnElimSuc.clicked.connect(self.eliminarSucursal)
        self.ui.btn_cancelarSuc.clicked.connect(self.cancelarSucursal)
        self.ui.btnBuscSuc.clicked.connect(self.buscarSucursal)

        #-------------------------------------- PAGINA2: FACTURACION  -------------------------------------
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

        #self.ui.btnBuscCat.clicked.connect(self.buscarCategoria)
        self.ui.btnAgrCat.clicked.connect(self.agregarCategoria)
        self.ui.btnEditCat.clicked.connect(self.editarCategoria)
        self.ui.btnElimCat.clicked.connect(self.eliminarCategoria)
        self.ui.btn_cancelarcate.clicked.connect(self.cancelarCategoria)

        self.ui.btnBuscProduc.clicked.connect(self.buscarProducto)
        self.ui.btnAgrProd.clicked.connect(self.agregarProducto)
        self.ui.btnEditProd.clicked.connect(self.editarProducto)
        self.ui.btnElimProd.clicked.connect(self.eliminarProducto)
        self.ui.btn_cancelarpro.clicked.connect(self.cancelarProducto)

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
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)
        ### esto es para probar
        columnas = ["Laboratorio", "Fecha", "Hora", "Estado"]
        miLista = [{'Laboratorio': 'Lab1', 'Fecha': '2024-01-26', 'Hora': '10:00', 'Estado': True},
                   {'Laboratorio': 'Lab2', 'Fecha': '2024-01-27', 'Hora': '11:30', 'Estado': False}]
        self.cargarDatosTabla(miLista, columnas, self.ui.tableWidget)
    def pagfactura(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def pagabastecer(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def pagagregarproducto(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri, False)
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca, False)
        self.manejoBotones(self.ui.btnBuscMarca_2, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat, False)
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

    def buscarSucursal(self):
        if True:
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe la sucursal!")

    def agregarSucursal(self):
        if True:
            QMessageBox.information(self, "Registro", "Sucursal agregada con éxito!")
            pass
        else:
            QMessageBox.information(self, "Sucursales", "!")

    def editarSucursal(self):
        if True:
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)
            pass
        else:
            QMessageBox.information(self, "Sucursales", "!")

    def eliminarSucursal(self):
        if True:
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)
            pass
        else:
            QMessageBox.information(self, "Sucursales", "!")

    def cancelarSucursal(self):
        self.ui.txtNomSucur.setText("")
        self.ui.txtDirSucur.setText("")
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)


    #-------------------------------------- PAGINA2: FACTURACION  -------------------------------------
    #-------------------------------------- PAGINA3: ABASTECIMIENTO DEL SUPERMARKET -------------------------------------
    #-------------------------------------- PAGINA4: REGISTRO DE TODOS LOS DATOS  -------------------------------------


    ###FABRICANTE
    def buscarFabricante(self):
        if True:
            self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Fabricante!")

    def agregarFabricante(self):
        if True:
            QMessageBox.information(self, "Registro", "Fabricante agregado con éxito!")
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def editarFabricante(self):
        if True:
            self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri,False)
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def eliminarFabricante(self):
        if True:
            self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri, False)
            pass
        else:
            QMessageBox.information(self, "Fabricante", "!")

    def cancelarFabricante(self):
        self.ui.txtNomFabri.setText("")
        self.ui.txtDirFabri.setText("")
        self.manejoBotones(self.ui.btnBuscFabri, self.ui.btnAgrFabri, self.ui.btnEditFabri, self.ui.btnElimFabri,False)


    ##MARCA

    def buscarMarca(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe la Marca!")

    def agregarMarca(self):
        if True:
            QMessageBox.information(self, "Registro", "Marca agregada con éxito!")
            pass
        else:
            QMessageBox.information(self, "Marca", "!")

    def editarMarca(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca,False)
            pass
        else:
            QMessageBox.information(self, "Marca", "!")

    def eliminarMarca(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca,False)
            pass
        else:
            QMessageBox.information(self, "Marca", "!")

    def cancelarMarca(self):
        self.ui.txtNomMarca.setText("")
        self.manejoBotones(self.ui.btnBuscMarca, self.ui.btnAgrMarca, self.ui.btnEditMarca, self.ui.btnElimMarca,False)

    ##CATEGORIA

    def buscarCategoria(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca_2, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe la Categoría!")

    def agregarCategoria(self):
        if True:
            QMessageBox.information(self, "Registro", "Categoría agregada con éxito!")
            pass
        else:
            QMessageBox.information(self, "Categoría", "!")

    def editarCategoria(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca_2, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat,False)
            pass
        else:
            QMessageBox.information(self, "Categoría", "!")

    def eliminarCategoria(self):
        if True:
            self.manejoBotones(self.ui.btnBuscMarca_2, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat,False)
            pass
        else:
            QMessageBox.information(self, "Categoría", "!")

    def cancelarCategoria(self):
        self.ui.lineEditCat.setText("")
        self.manejoBotones(self.ui.btnBuscMarca_2, self.ui.btnAgrCat, self.ui.btnEditCat, self.ui.btnElimCat,False)

    ##PRODUCTO

    def buscarProducto(self):
        if True:
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Producto!")

    def agregarProducto(self):
        if True:
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
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd,False)
            pass
        else:
            QMessageBox.information(self, "Producto", "!")

    def cancelarProducto(self):
        self.ui.txtDescripcion.setText("")
        self.ui.txtTamanio.setText("")
        self.ui.txtMedida.setText("")
        self.ui.txtDescripcion.setText("")
        self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd, self.ui.btnEditProd, self.ui.btnElimProd,False)

    #-------------------------------------- PAGINA5: REGISTRO DE CLIENTES  -------------------------------------

    def buscarCliente(self):
        if True:
            self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True)
            pass
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Cliente!")

    def agregarCliente(self):
        if True:
            QMessageBox.information(self, "Registro", "Cliente agregado con éxito!")
            pass
        else:
            QMessageBox.information(self, "Clientes", "!")

    def editarCliente(self):
        if True:
            self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
            pass
        else:
            QMessageBox.information(self, "Clientes", "!")

    def eliminarCliente(self):
        if True:
            self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
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
    def manejoBotones(self, buscar, agregar, modificar, eliminar, estado):
        buscar.setEnabled(not estado)
        agregar.setEnabled(not estado)
        modificar.setEnabled(estado)
        eliminar.setEnabled(estado)

    def cargarDatosTabla(self, lista, columnas, tabla):
        #self.limpiaTabla(tabla)
        tabla.setColumnCount(len(columnas))
        tabla.setHorizontalHeaderLabels(columnas)

        row = 0
        for item in lista:
            tabla.insertRow(row)
            col = 0
            for key in columnas:
                celda = QTableWidgetItem(str(item.get(key, '')))
                tabla.setItem(row, col, celda)
                col += 1
            row += 1

    def limpiaTabla(self, tabla):
        tabla.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.clearContents()
        tabla.setRowCount(0)
