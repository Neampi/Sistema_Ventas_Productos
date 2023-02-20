import sys
from PySide2.QtWidgets import QWidget, QMainWindow, QTableWidgetItem
from db.conexion_sql import Conexion
from views.ui_seleccion_producto import Ui_sell_w
from controllers.main_w import *
seleccion_precio=0
class ventana_seleccion(QMainWindow):

    
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.sp=Ui_sell_w()
        self.sp.setupUi(self)

        self.bd=Conexion()

        self.sp.buscar_cod_sel.clicked.connect(self.busqueda_codigo)
        self.sp.buscar_mod_sel.clicked.connect(self.busqueda_cbx)

        self.cbx_categoria()
        self.cbx_marca()

        self.sp.cat_cbx_seleccion.currentTextChanged.connect(self.seleccion_categoria)

        self.sp.tabla_seleccion.itemClicked.connect(self.click_fila_precio)
        self.sp.tabla_seleccion.cellClicked.connect(self.calculo_total)
        self.sp.dscto_seleccion.textChanged.connect(self.calculo_total)
        self.sp.cantidad_seleccion.textChanged.connect(self.calculo_total)

        



    def click_fila_precio(self, item):
        global seleccion_precio
        seleccion_precio=self.sp.tabla_seleccion.item(item.row(),6).text()    

    def calculo_total(self):
        if self.sp.dscto_seleccion.text()=='':
            dscto=0
        else: 
            dscto=float(self.sp.dscto_seleccion.text())

        if self.sp.cantidad_seleccion.text()=='':
            cant=0
        else:
            cant=float(self.sp.cantidad_seleccion.text())

        
        pre=float(seleccion_precio)

        total=(pre*cant)-dscto

        return self.sp.total_seleccion.setText(str(total))


        #CAMBIO AL SELECCIONAR ELEMENTO EN CATEGORIA
    def seleccion_categoria(self):
        self.sp.mar_cbx_seleccion.clear()
        self.cbx_marca()


        #COMBOBOX CATEGORIA
    def cbx_categoria(self):
        datos=self.bd.combobd_categoria_inventario()

        for categorias in datos:
            self.sp.cat_cbx_seleccion.addItem(categorias[1])

        #DETECCION DE SELECCION DE DATOS EN COMBOBOX MARCA | INVENTARIO
        self.sp.mar_cbx_seleccion.currentTextChanged.connect(self.seleccion_marca)


        #CAMBIO AL SELECCIONAR ELEMENTO EN MARCA
    def seleccion_marca(self):
        self.sp.mod_cbx_seleccion.clear()
        self.cbx_modelo()

        #COMBOBOX MARCA
    def cbx_marca(self):
        index=self.sp.cat_cbx_seleccion.currentText()
        datosmarca=self.bd.combobd_marca_inventario(index)
        
        for marcas in datosmarca:
            self.sp.mar_cbx_seleccion.addItem(marcas[0])

        #COMBOBOX MODELO
    def cbx_modelo(self):
        indexx=self.sp.cat_cbx_seleccion.currentText()
        indexy=self.sp.mar_cbx_seleccion.currentText()
        datosmodelo=self.bd.combobd_modelo_inventario(indexx,indexy)

        for modelos in datosmodelo:
            self.sp.mod_cbx_seleccion.addItem(modelos[0])


    def busqueda_codigo(self):
        codigo=self.sp.cod_seleccion.text()
        try:
            self.search=self.bd.busqueda_codigo_seleccion(codigo)
            if self.search[0][1]==codigo:
                i=len(self.search)
                self.sp.tabla_seleccion.setRowCount(i)
                tablerow=0
                for row in self.search:
                    self.sp.tabla_seleccion.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
                    self.sp.tabla_seleccion.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
                    self.sp.tabla_seleccion.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
                    self.sp.tabla_seleccion.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
                    self.sp.tabla_seleccion.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
                    self.sp.tabla_seleccion.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
                    self.sp.tabla_seleccion.setItem(tablerow,6,QTableWidgetItem(str(row[6])))

                    tablerow+=1

        except Exception:
            print("ERROR")

    def busqueda_cbx(self):
        indexx=self.sp.cat_cbx_seleccion.currentText()
        indexy=self.sp.mar_cbx_seleccion.currentText()
        indexz=self.sp.mod_cbx_seleccion.currentText()
        busqueda=self.bd.busqueda_producto_venta_cbx(indexx,indexy,indexz)
        i=len(busqueda)
        self.sp.tabla_seleccion.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.sp.tabla_seleccion.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.sp.tabla_seleccion.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.sp.tabla_seleccion.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.sp.tabla_seleccion.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.sp.tabla_seleccion.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.sp.tabla_seleccion.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.sp.tabla_seleccion.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            tablerow+=1

    

        
