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


    def Iniciar(self):
        self.Sucursal()

    def Sucursal(self):
        self.sucursal=CtrlSucursal(self.conexion)
        self.sucursal.Iniciar()
