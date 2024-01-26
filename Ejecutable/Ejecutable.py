import sys

from PyQt6.QtWidgets import QApplication

from Controlador.ControladorPrincipal import ControladorPrincipal
from conection import DataBaseConection
if __name__=="__main__":
    app = QApplication(sys.argv)
    conexion=DataBaseConection()
    puntero=conexion.StarConection()
    controlador = ControladorPrincipal(puntero)

    controlador.setWindowTitle("Sistema de Facturacion")
    controlador.show()

    sys.exit(app.exec())
    conexion.EndConection()



