import sys

from PyQt6.QtWidgets import QMainWindow

from Vista.ventana import Ui_MainWindow
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal

class ControladorPrincipal(QMainWindow):

    def __init__(self,conexion):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conexion=conexion
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)
        #--------------------------Pagina princpal--------------------------
        self.ui.btn_inicio.clicked.connect(self.paginicio)
        self.ui.btn_factura.clicked.connect(self.pagfactura)
        self.ui.btn_abastecer.clicked.connect(self.pagabastecer)
        self.ui.btn_agregarproducto.clicked.connect(self.pagagregarproducto)
        self.ui.btn_registrar.clicked.connect(self.pagregistrar)
        self.ui.btn_info.clicked.connect(self.paginfo)


        #Probando

        self.ui.btn_buscarUser.clicked.connect(lambda: self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, True))
    def paginicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)
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
