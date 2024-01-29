import sys
from datetime import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel
from Controlador.CtrlAbastecer import CtrlAbastecer
from Controlador.CtrlCategoria import CtrlCategoria
from Controlador.CtrlCategoriaProducto import CtrlCategoriaProducto
from Controlador.CtrlFabricante import CtrlFabricante
from Controlador.CtrlFactura import CtrlFactura
from Controlador.CtrlFacturaProducto import CtrlFacturaProducto
from Controlador.CtrlMarca import CtrlMarca
from Controlador.CtrlProducto import CtrlProducto
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox, QHeaderView

from Modelo import Validaciones

from Vista.ventana import Ui_MainWindow
from conection import DataBaseConection
from Controlador.CtrlSucursal import CtrlSucursal
from Controlador.CtrlClientes import CtrlCliente

class ControladorPrincipal(QMainWindow):

    def __init__(self,conexion):
        super().__init__()
        self.variableGlobal=None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conexion=conexion
        self.cargarComboSucursal()
        self.actualizar_label()
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

        self.agregarTablaSucursal()
        self.ui.comboBox.currentIndexChanged.connect(self.actualizar_label)
        self.ui.btnAgrSuc.clicked.connect(self.agregarSucursal)
        self.ui.btnEditSuc.clicked.connect(self.editarSucursal)
        self.ui.btnElimSuc.clicked.connect(self.eliminarSucursal)
        self.ui.btn_cancelarSuc.clicked.connect(self.cancelarSucursal)
        self.ui.btnBuscSuc.clicked.connect(self.buscarSucursal)

        #-------------------------------------- PAGINA2: FACTURACION  -------------------------------------
        self.ui.btnBuscUserFact.clicked.connect(self.detallesClliente)
        self.ui.txtIdentificacion_3.setEnabled(True)
        self.ui.btnBuscProdFact.clicked.connect(self.buscarProductoFactura)
        self.ui.btn_agregarfact.clicked.connect(self.agregarTablaDetalleFactura)
        self.ui.btn_quitarAbast_2.clicked.connect(self.QuitarProductoFactura)
        self.ui.btn_pagarfac.clicked.connect(self.generarFactura)
        self.listaTablaFactura = []
        #self.agregarCabeceraTablaDetalleFactura()

        #-------------------------------------- PAGINA3: ABASTECIMIENTO DEL SUPERMARKET -------------------------------------
        self.ui.btnBuscProdAbast.clicked.connect(self.buscarProductoAbastecimiento)
        self.ui.btn_agregarAbast.clicked.connect(self.AgregarAlInventario)
        self.ui.btn_quitarAbast.clicked.connect(self.QuitarAlInventario)
        self.ui.btn_agregarAbast_2.clicked.connect(self.Abastecer)
        self.ui.comboProvAbast.currentIndexChanged.connect(self.cargarTablaProductosAbastecimieto)
        self.lista = []
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



    def actualizar_label(self):
        texto_seleccionado = self.ui.comboBox.currentText()
        self.ui.lblSucursal.setText(texto_seleccionado)

    #--------------------------------- MANEJO DE CAMBIOS DE PESTAÑAS ------------------------------
    def paginicio(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.agregarTablaSucursal()
        self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc, self.ui.btnElimSuc, False)

    # >>>>>>> origin/Alejandro
    def pagfactura(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.cargarFechaActual()
        self.cargarIdFactura()
    def pagabastecer(self):
        self.ui.btn_agregarAbast.setEnabled(False)
        self.ui.btn_quitarAbast.setEnabled(False)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.cargarComboFabricante(self.ui.comboProvAbast)
    def pagagregarproducto(self):
        self.cargarComboFabricante(self.ui.combFabric_Marca)
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
        self.agregarTablaCliente()
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
        self.cargarComboSucursal()
    def buscarSucursal(self):
        self.variableGlobal=self.ui.txtNomSucur.text()
        nombre=self.ui.txtNomSucur.text()
        self.sucursal=CtrlSucursal(self.conexion)
        datosSucursal=self.sucursal.cargarDatosSucursal(nombre)
        if datosSucursal != None:
            self.ui.txtDirSucur.setText(datosSucursal[2])
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc,
                               self.ui.btnEditSuc, self.ui.btnElimSuc, True)
        else:
            QMessageBox.warning(self, "ERROR", "No existe la sucursal!")

    def agregarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        if nombre!='' and direccion != '':
            datos=(nombre,direccion)
            self.sucursal=CtrlSucursal(self.conexion)
            if self.sucursal.guardarSucursal(datos):
                QMessageBox.information(self, "Registro", "Sucursal agregada con éxito!")
                self.cancelarSucursal()
                self.agregarTablaSucursal()
            else:
                QMessageBox.warning(self, "ERROR", "Ya existe la sucursal con ese nombre!")
        else:
            QMessageBox.information(self, "Sucursales", "Llene todos los campos!")

    def editarSucursal(self):
        nombre=self.ui.txtNomSucur.text()
        direccion=self.ui.txtDirSucur.text()
        if nombre!= '' and direccion != '':
            self.sucursal=CtrlSucursal(self.conexion)
            idSucursal=self.sucursal.cargarIdSucursal(self.variableGlobal)
            datos=(idSucursal,nombre,direccion)
            self.sucursal.modificarSucursal(datos)
            QMessageBox.information(self, "Registro", "Sucursal modificada con éxito!")
            self.cancelarSucursal()
            self.agregarTablaSucursal()
            self.manejoBotones(self.ui.btnBuscSuc, self.ui.btnAgrSuc, self.ui.btnEditSuc,
                               self.ui.btnElimSuc, False)
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
    def agregarTablaDetalleFactura(self):
        codigo=self.ui.txtbuscarProducto2.text()
        descripcion=self.ui.lblApellidos_2.text()
        cantidad=self.ui.box_cantidadfact.value()
        precioUnitario=self.ui.doubleSpinBoxAbast_3.value()
        precioTotal=str(float(cantidad) * float(precioUnitario))
        self.listaTablaFactura.append((codigo, descripcion, cantidad, precioUnitario,precioTotal))
        self.cargarDatosTabla(self.listaTablaFactura,['Codigo', 'Descripcion','Cantidad',
                                          'Precio Uni','Precio Tot'],self.ui.tabla_productosfac)
        self.calcularCostos(True,False)
    def calcularCostos(self,suma,resta):
        self.suma=suma
        self.resta=resta
        subtotal=0
        iva=0
        if self.suma:
            for tupla in self.listaTablaFactura:
                subtotal+=float(tupla[-1])
            iva=0.12*(subtotal)
            ivaItem=QTableWidgetItem(str(round(iva,2)))

            subTotalItem=QTableWidgetItem(str(subtotal))

            self.ui.tabla_facturafac.setItem(0,0,subTotalItem)
            self.ui.tabla_facturafac.setItem(1,0,ivaItem)

            if self.ui.lblDescuento.text() == 'Si':
                descuento=0.15*(subtotal)
                descuentoItem=QTableWidgetItem(str(descuento))
                self.ui.tabla_facturafac.setItem(2,0,descuentoItem)
                total=subtotal+iva-descuento
                totalItem=QTableWidgetItem(str(round(total,2)))
                self.ui.tabla_facturafac.setItem(3,0,totalItem)
            else:
                descuentoItem=QTableWidgetItem('0')
                self.ui.tabla_facturafac.setItem(2,0,descuentoItem)
                total=subtotal+iva
                totalItem=QTableWidgetItem(str(round(total,2)))
                self.ui.tabla_facturafac.setItem(3,0,totalItem)
        if self.resta:
            None
    def QuitarProductoFactura(self):
        self.listaTablaFactura = [tupla for tupla in self.listaTablaFactura if tupla[0] != self.ui.txtbuscarProducto2.text()]
        self.cargarDatosTabla(self.listaTablaFactura,['Codigo', 'Descripcion','Cantidad',
                                          'Precio Uni','Precio Tot'],self.ui.tabla_productosfac)
        self.calcularCostos(True,False )

    def cargarIdFactura(self):
        self.ui.lblNumeroFactura_2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        factura=CtrlFactura(self.conexion)
        idFactura=factura.cargarIdUltimaFactura()
        self.ui.lblNumeroFactura_2.setText(str(int(idFactura+1)))

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
        abastecer=CtrlAbastecer(self.conexion)
        producto=CtrlProducto(self.conexion)

        nombre=producto.cargarNombreProducto(self.ui.txtbuscarProducto2.text())
        precioBase=abastecer.cargarPrecioBase(self.ui.txtbuscarProducto2.text())
        self.ui.doubleSpinBoxAbast_3.setValue(precioBase[0])
        self.ui.lblApellidos_2.setText(nombre[0])
    #-------------------------------------- PAGINA3: ABASTECIMIENTO DEL SUPERMARKET -------------------------------------

    def cargarTablaProductosAbastecimieto(self):
        abastecer=CtrlAbastecer(self.conexion)
        datos = abastecer.cargarTablaProductosProveedor(self.ui.comboProvAbast.currentText())
        self.cargarDatosTabla(datos,['ID producto', 'Descripción','Marca','Tamaño', 'Medida'],self.ui.tablaProductos)

    def cargarTablaInventario(self):
        abastecer=CtrlAbastecer(self.conexion)
        datos = abastecer.cargarTablaProductosProveedor(self.ui.comboProvAbast.currentText())
        self.cargarDatosTabla(datos,['ID producto', 'Descripción','Marca','Tamaño', 'Medida'],self.ui.tabla_inventario)

    def limpiarAbastecimiento(self):
        self.ui.txt_idproductoabastecimiento_2.setText("")
        self.ui.lblDescripcion.setText("")
        self.ui.lblMarca.setText("")
        self.ui.lblTamanio.setText("")
        self.ui.lblMedida.setText("")
        self.ui.btn_agregarAbast.setEnabled(False)
        self.ui.btn_quitarAbast.setEnabled(False)
    def buscarProductoAbastecimiento(self):
        if True:
            nombre=self.ui.txt_idproductoabastecimiento_2.text()
            producto=CtrlProducto(self.conexion)
            datosProducto=producto.extraerProductoPorId(nombre)
            print('datososs: ',datosProducto)
            self.ui.lblDescripcion.setText(datosProducto[0])
            self.ui.lblMarca.setText(datosProducto[1])
            self.ui.lblTamanio.setText(datosProducto[2])
            self.ui.lblMedida.setText(datosProducto[3])
            self.ui.btn_agregarAbast.setEnabled(True)
            self.ui.btn_quitarAbast.setEnabled(True)
        else:
            QMessageBox.warning(self, "ERROR", "No existe el Producto!")


    def AgregarAlInventario(self):
        sucursal=CtrlSucursal(self.conexion)
        suc = sucursal.cargarDatosSucursal(self.ui.lblSucursal.text())
        id_suc = suc[0]
        id_pro = self.ui.txt_idproductoabastecimiento_2.text()
        cantidad = self.ui.box_cantidadabast.text()
        precio = self.ui.doubleSpinBoxAbast.value()
        fecha = datetime.now().date()
        self.lista.append((id_suc, id_pro, cantidad, precio, fecha))
        self.cargarDatosTabla(self.lista,['ID', 'Descripcion','cantidad','precio'],self.ui.tabla_inventario)
        self.limpiarAbastecimiento()
        pass
    def QuitarAlInventario(self):
        self.lista = [tupla for tupla in self.lista if tupla[1] != self.ui.txt_idproductoabastecimiento_2.text()]
        self.cargarDatosTabla(self.lista,['ID', 'Descripcion','cantidad','precio'],self.ui.tabla_inventario)
        self.limpiarAbastecimiento()


    def Abastecer(self):
        abastecer=CtrlAbastecer(self.conexion)
        print('Abastece ',self.lista)
        for datos in self.lista:
             abastecer.guardarAbastecer(datos)
        self.limpiarAbastecimiento()

    def generarFactura(self):
        facturaProducto=CtrlFacturaProducto(self.conexion)
        factura=CtrlFactura(self.conexion)
        sucursal=CtrlSucursal(self.conexion)
        fecha=self.ui.lblFecha.text()
        idSucursal=sucursal.cargarIdSucursal(self.ui.lblSucursal.text())
        idCliente=self.ui.txtIdentificacion_3.text()
        datos=(fecha,idSucursal,idCliente)
        factura.guardarFactura(datos)
        nuevaLista=[(tupla[0], tupla[2], tupla[3],self.ui.lblNumeroFactura_2.text()) for tupla in self.listaTablaFactura]
        for data in nuevaLista:
            facturaProducto.guardarFacturaProducto(data)






    #-------------------------------------- PAGINA4: REGISTRO DE TODOS LOS DATOS  -------------------------------------


    ###FABRICANTE
    def buscarFabricante(self):
        self.variableGlobal=self.ui.txtNomFabri.text()
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
            self.fabricante=CtrlFabricante(self.conexion)
            idFabricante=self.fabricante.cargarIdFabricante(self.variableGlobal)
            datos=(idFabricante,nombre,direccion)
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
        self.variableGlobal=self.ui.txtNomMarca.text()
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
        marca=CtrlMarca(self.conexion)
        nuevoNombreMarca=self.ui.txtNomMarca.text()
        idMarca=marca.cargarIdMarca(self.variableGlobal)
        datos=(idMarca,nuevoNombreMarca)
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
            self.variableGlobal=self.ui.lineEditCat.text()
            nombre=self.ui.lineEditCat.text()
            categoria=CtrlCategoria(self.conexion)
            datosCategoria=categoria.cargarDatosCategoria(nombre)
            print(datosCategoria)
            self.ui.combCatPadre.setCurrentText(datosCategoria)
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
            categoria=CtrlCategoria(self.conexion)

            idCategoriaPadre=categoria.cargarIdCategoria(self.ui.combCatPadre.currentText())
            nuevoNombreCategoria=self.ui.lineEditCat.text()
            idCategoria=categoria.cargarIdCategoria(self.variableGlobal)
            datos=(idCategoria,idCategoriaPadre,nuevoNombreCategoria)
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
            self.variableGlobal=self.ui.txtDescripcion.text()
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
            producto=CtrlProducto(self.conexion)
            marca=CtrlMarca(self.conexion)
            idProducto=producto.cargarIdProducto(self.variableGlobal)
            nombre=self.ui.txtDescripcion.text()
            idMarca=marca.cargarIdMarca(self.ui.combMarcaProd.currentText())
            tamanio=self.ui.txtTamanio.text()
            medida=self.ui.txtMedida.text()
            datos=(idProducto,nombre,tamanio,medida,idMarca)
            producto.modificarProducto(datos)
            self.manejoBotones(self.ui.btnBuscProduc, self.ui.btnAgrProd,
                               self.ui.btnEditProd, self.ui.btnElimProd,False)
            QMessageBox.information(self, "Registro", "Producto modificado con éxito!")
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
    def Validaciones(self, cedula_Ruc, nombre, apellido, direccion, telefono, correo, socio):
        validar = Validaciones.validar()
        if not validar.validarVacios(cedula_Ruc, nombre, direccion, telefono, correo) :
            QMessageBox.warning(self, "ERROR", "Llene todos los campos!")
            return False
        if socio == None:
            QMessageBox.warning(self, "ERROR", "Seleccione si tiene o no tarjeta de descuento!")
            return False

        if not validar.validarCedulaRuc(cedula_Ruc):
            QMessageBox.warning(self, "ERROR", "Cedula o Ruc no validos!")
            return False

        if not validar.ValidaSoloLetras(nombre):
            QMessageBox.warning(self, "ERROR", "Nombre o apellidos no validos!")
            return False

        if not (validar.ValidaSoloLetras(apellido)):
            QMessageBox.warning(self, "ERROR", "Apellidos no válidos!")
            return False

        if not telefono.isdigit():
            QMessageBox.warning(self, "ERROR", "Telefono no valido!")
            return False

        if not validar.es_correo_valido(correo):
            QMessageBox.warning(self, "ERROR", "Correo no valido!")
            return False

        return True

    def agregarTablaCliente(self):
        self.entidad=CtrlCliente(self.conexion)
        datos=self.entidad.cargarTablaClientes()
        print(list(datos))
        self.cargarDatosTabla(datos,['id','Nombre','Apellido','Dirección','Email', 'Teléfono', 'Descuento'],self.ui.tablaClientes)
    def buscarCliente(self):
        id=self.ui.txtIdentificacion.text()
        self.cliente=CtrlCliente(self.conexion)
        if not id.isdigit():
            QMessageBox.warning(self, "ERROR", "No existe el Cliente!")
            print("Hola")
            return
        datosCliente=self.cliente.cargarDatosCliente(id)
        if datosCliente!=None:
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

        else:
            QMessageBox.warning(self, "ERROR", "No existe el Cliente!")

    def agregarCliente(self):
        id=self.ui.txtIdentificacion.text()
        nombre=self.ui.txtNombres.text()
        apellido=self.ui.txtApellidos.text()
        direccion=self.ui.txtDireccion.text()
        email=self.ui.txtEmail.text()
        telefono=self.ui.txtTelefono.text()
        if self.ui.radiobtn_siuser.isChecked(): socio=True
        elif self.ui.radiobtn_nouser.isChecked(): socio=False
        else:socio = None
        if self.Validaciones(id, nombre, apellido, direccion, telefono, email, socio):
            datos=(id,nombre,apellido,direccion,email,telefono,socio)
            self.cliente=CtrlCliente(self.conexion)
            if self.cliente.guardarCliente(datos): #Validar existencia
                QMessageBox.information(self, "Registro", "Cliente agregado con éxito!")
                self.cancelarCliente()
                self.agregarTablaCliente()
                self.agregarTablaCliente()
                pass
            else:
                QMessageBox.information(self, "Clientes", "El cliente ya existe!")

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
            self.agregarTablaCliente()
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
            self.agregarTablaCliente()
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
        self.ui.radiobtn_siuser.setChecked(False)
        self.ui.radiobtn_nouser.setChecked(False)
        self.manejoBotones(self.ui.btn_buscarUser, self.ui.btn_agregaruser, self.ui.btn_modificaruser, self.ui.btn_eliminaruser, False)



    #-------------------------------------- PAGINA6: INVENTARIO  -------------------------------------
    #-------------------------------------- PAGINA7: DETALLES DE VENTAS  -------------------------------------
    #-------------------------------------- PAGINA8: DETALLE DE ABASTECIMIENTOS -------------------------------------





#=============================================================================================================================================================
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
    def cargarComboFabricante(self, combo):
        combo.clear()
        fabricante=CtrlFabricante(self.conexion)
        datos=fabricante.cargarTablaFabricante()
        combo.addItems([item[1] for item in datos])
    def cargarComboSucursal(self):
        self.ui.comboBox.clear()
        sucursal=CtrlSucursal(self.conexion)
        datos=sucursal.cargarTablaSucursal()
        self.ui.comboBox.addItems([item[1] for item in datos])

    def manejoBotones(self, buscar, agregar, modificar, eliminar, estado):
        buscar.setEnabled(not estado)
        agregar.setEnabled(not estado)
        modificar.setEnabled(estado)
        eliminar.setEnabled(estado)

    def cargarDatosTabla(self, lista, columnas, tabla):  ##Cambios en la tabla ya funciona correctamente
        self.limpiaTabla(tabla)
        tabla.setColumnCount(len(columnas))
        tabla.setHorizontalHeaderLabels(columnas)
        tabla.verticalHeader().setVisible(False)
        for row_num, datos in enumerate(lista):
            tabla.insertRow(row_num)
            for col_num, valor in enumerate(datos):
                item = QTableWidgetItem(str(valor))
                tabla.setItem(row_num, col_num, item)



    def limpiaTabla(self, tabla):
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.clearContents()
        tabla.setRowCount(0)