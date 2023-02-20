
import sys
from PyQt5.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMainWindow, QTableWidgetItem
from controllers.seleccion_prod import *
from db.conexion_sql import Conexion

from views.ui_principalWindow import *
from controllers.logi import *
from controllers.registro_compras import *

class principal_process(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.prin=Ui_principal_w()
        self.prin.setupUi(self)

       
        #INSTANCIAR CONEXION DE BASE DE DATOS 
        self.bd=Conexion()

        #CONEXION DE BOTONES CON VENTANAS WIDGET
        self.prin.paginas_forbutton.setCurrentWidget(self.prin.home_w)
        self.prin.home_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.home_w))
        self.prin.inventario_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.inventario_w))
        self.prin.compras_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.compras_w))
        self.prin.ventas_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.ventas_w))
        self.prin.reportes_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.reportes_w))
        self.prin.avanzado_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.avanzado_w))
        self.prin.configuracion_b.clicked.connect(lambda: self.prin.paginas_forbutton.setCurrentWidget(self.prin.configuracion_w))
        
     
        #BOTONES AUXILIARES
        self.prin.salir_b.clicked.connect(self.salir)
        self.prin.minimizar_b.clicked.connect(self.min)

        #INICIALIZAR COMBOBOX Y TABLAS
            #INVENTARIO
        self.cbx_categoria()
        self.cbx_marca()
        self.invent()
            #COMPRAS
        self.cbx_categoria_compra()
        self.cbx_marca_compra()
        self.compras_inventario()

        #DETECCION DE SELECCION DE DATOS EN COMBOBOX DE INVENTARIO Y COMPRAS
        self.prin.cbx_categoria_inventario.currentTextChanged.connect(self.seleccion_categoria)
        self.prin.cbx_categoria_compras.currentTextChanged.connect(self.seleccion_categoria_compras)

    #VENTANA HOME

    
    #VENTANA INVENTARIO
        #BOTONES
        self.prin.btn_actualizar_inventario.clicked.connect(self.invent)
        self.prin.buscar_inventario_button.clicked.connect(self.searchinventario_cbx)
        self.prin.registrar_producto_button.clicked.connect(self.openregis)

    #VENTANA COMPRAS
        #BOTONES
        self.prin.actualizar_compras_button.clicked.connect(self.compras_inventario)
        self.prin.buscar_compras_button.clicked.connect(self.searchcompras_cbx_date_total)
        self.prin.buscar_compras_fecha.clicked.connect(self.searchcompras_cbx_date)
        self.prin.buscar_compras_categoria.clicked.connect(self.searchcompra_cbx_categoria)
        self.prin.buscar_compras_marca.clicked.connect(self.searchcompra_cbx_marca)
        
    #VENTANA VENTA
        #BOTONES
        self.prin.buscar_producto_venta.clicked.connect(self.open_seleccion)
        self.prin.eliminar_producto_venta.clicked.connect(self.eliminar_seleccion)
        self.prin.tabla_venta.itemChanged.connect(self.suma_venta)
        self.prin.procesar_venta.clicked.connect(self.procesar_sell)
        self.cbx_tipopago()

        
        
        #INVENTARIO TABLA
    def invent(self):
        datos=self.bd.inventario()
        i=len(datos)
        self.prin.inventario_tabla.setRowCount(i)
        tablerow=0
        for row in datos:
            self.prin.inventario_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.inventario_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.inventario_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.inventario_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.inventario_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.inventario_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.inventario_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.inventario_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            tablerow+=1

        
        #CAMBIO AL SELECCIONAR ELEMENTO EN CATEGORIA
    def seleccion_categoria(self):
        self.prin.cbx_marca_inventario.clear()
        self.cbx_marca()


        #COMBOBOX CATEGORIA
    def cbx_categoria(self):
        datos=self.bd.combobd_categoria_inventario()

        for categorias in datos:
            self.prin.cbx_categoria_inventario.addItem(categorias[1])

        #DETECCION DE SELECCION DE DATOS EN COMBOBOX MARCA | INVENTARIO
        self.prin.cbx_marca_inventario.currentTextChanged.connect(self.seleccion_marca)


        #CAMBIO AL SELECCIONAR ELEMENTO EN MARCA
    def seleccion_marca(self):
        self.prin.cbx_modelo_inventario.clear()
        self.cbx_modelo()

        #COMBOBOX MARCA
    def cbx_marca(self):
        index=self.prin.cbx_categoria_inventario.currentText()
        datosmarca=self.bd.combobd_marca_inventario(index)
        
        for marcas in datosmarca:
            self.prin.cbx_marca_inventario.addItem(marcas[0])

        #COMBOBOX MODELO
    def cbx_modelo(self):
        indexx=self.prin.cbx_categoria_inventario.currentText()
        indexy=self.prin.cbx_marca_inventario.currentText()
        datosmodelo=self.bd.combobd_modelo_inventario(indexx,indexy)

        for modelos in datosmodelo:
            self.prin.cbx_modelo_inventario.addItem(modelos[0])


        #BUSQUEDA POR COMBOBOXS
    def searchinventario_cbx(self):
        self.prin.inventario_tabla.clearContents()
        indexx=self.prin.cbx_categoria_inventario.currentText()
        indexy=self.prin.cbx_marca_inventario.currentText()
        indexz=self.prin.cbx_modelo_inventario.currentText()
        busqueda=self.bd.busqueda_producto_cbx(indexx, indexy, indexz)
        i=len(busqueda)
        self.prin.inventario_tabla.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.prin.inventario_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.inventario_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.inventario_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.inventario_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.inventario_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.inventario_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.inventario_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.inventario_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            tablerow+=1
    
    #VENTANA COMPRAS
        #COMPRAS TABLA
    def compras_inventario(self):
        datos=self.bd.compras_inventario()
        i=len(datos)
        self.prin.compras_tabla.setRowCount(i)
        tablerow=0
        for row in datos:
            self.prin.compras_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.compras_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.compras_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.compras_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.compras_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.compras_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.compras_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.compras_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            self.prin.compras_tabla.setItem(tablerow,8,QTableWidgetItem(str(row[8])))
            self.prin.compras_tabla.setItem(tablerow,9,QTableWidgetItem(str(row[9])))
            self.prin.compras_tabla.setItem(tablerow,10,QTableWidgetItem(str(row[10])))
            self.prin.compras_tabla.setItem(tablerow,11,QTableWidgetItem(str(row[11])))
            tablerow+=1
    
        #CAMBIO AL SELECCIONAR ELEMENTO EN CATEGORIA
    def seleccion_categoria_compras(self):
        self.prin.cbx_marca_compras.clear()
        self.cbx_marca_compra()

        #COMBOBOX CATEGORIA
    def cbx_categoria_compra(self):
        datos=self.bd.combobd_categoria_inventario()

        for categorias in datos:
            self.prin.cbx_categoria_compras.addItem(categorias[1])

        #DETECCION DE SELECCION DE DATOS EN COMBOBOX MARCA | COMPRAS
        self.prin.cbx_marca_compras.currentTextChanged.connect(self.seleccion_marca_compras)

        #CAMBIO AL SELECCIONAR ELEMENTO EN MARCA
    def seleccion_marca_compras(self):
        self.prin.cbx_modelo_compras.clear()
        self.cbx_modelo_compra()

        #COMBOBOX MARCA
    def cbx_marca_compra(self):
        index=self.prin.cbx_categoria_compras.currentText()
        datosmarca=self.bd.combobd_marca_inventario(index)
        
        for marcas in datosmarca:
            self.prin.cbx_marca_compras.addItem(marcas[0])

        #COMBOBOX MODELO
    def cbx_modelo_compra(self):
        indexx=self.prin.cbx_categoria_compras.currentText()
        indexy=self.prin.cbx_marca_compras.currentText()
        datosmodelo=self.bd.combobd_modelo_inventario(indexx,indexy)

        for modelos in datosmodelo:
            self.prin.cbx_modelo_compras.addItem(modelos[0])

        #BUSQUEDA POR COMBOBOXS Y FECHA
    def searchcompras_cbx_date_total(self):
        self.prin.compras_tabla.clearContents()
        indexx=self.prin.cbx_categoria_compras.currentText()
        indexy=self.prin.cbx_marca_compras.currentText()
        indexz=self.prin.cbx_modelo_compras.currentText()

        date1=self.prin.fecha_inicio_buscar.date()
        date1_string = date1.toString("dd/MM/yyyy")

        
        date2=self.prin.fecha_final_buscar.date()
        date2_string=date2.toString("dd/MM/yyyy")


        busqueda=self.bd.busqueda_compras_fecha_total(indexx,indexy,indexz,date1_string, date2_string)
        i=len(busqueda)
        self.prin.compras_tabla.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.prin.compras_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.compras_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.compras_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.compras_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.compras_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.compras_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.compras_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.compras_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            self.prin.compras_tabla.setItem(tablerow,8,QTableWidgetItem(str(row[8])))
            self.prin.compras_tabla.setItem(tablerow,9,QTableWidgetItem(str(row[9])))
            self.prin.compras_tabla.setItem(tablerow,10,QTableWidgetItem(str(row[10])))
            self.prin.compras_tabla.setItem(tablerow,11,QTableWidgetItem(str(row[11])))
            tablerow+=1

        #BUSQUEDA POR FECHA
    def searchcompras_cbx_date(self):
        self.prin.compras_tabla.clearContents()
        
        date1=self.prin.fecha_inicio_buscar.date()
        date1_string = date1.toString("dd/MM/yyyy")

        date2=self.prin.fecha_final_buscar.date()
        date2_string=date2.toString("dd/MM/yyyy")

        busqueda=self.bd.busqueda_compras_fecha(date1_string, date2_string)
        i=len(busqueda)
        self.prin.compras_tabla.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.prin.compras_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.compras_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.compras_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.compras_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.compras_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.compras_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.compras_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.compras_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            self.prin.compras_tabla.setItem(tablerow,8,QTableWidgetItem(str(row[8])))
            self.prin.compras_tabla.setItem(tablerow,9,QTableWidgetItem(str(row[9])))
            self.prin.compras_tabla.setItem(tablerow,10,QTableWidgetItem(str(row[10])))
            self.prin.compras_tabla.setItem(tablerow,11,QTableWidgetItem(str(row[11])))
            tablerow+=1

    def searchcompra_cbx_categoria(self):
        self.prin.compras_tabla.clearContents()
        indexx=self.prin.cbx_categoria_compras.currentText()

        busqueda=self.bd.busqueda_compras_categoria(indexx)
        i=len(busqueda)
        self.prin.compras_tabla.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.prin.compras_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.compras_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.compras_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.compras_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.compras_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.compras_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.compras_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.compras_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            self.prin.compras_tabla.setItem(tablerow,8,QTableWidgetItem(str(row[8])))
            self.prin.compras_tabla.setItem(tablerow,9,QTableWidgetItem(str(row[9])))
            self.prin.compras_tabla.setItem(tablerow,10,QTableWidgetItem(str(row[10])))
            self.prin.compras_tabla.setItem(tablerow,11,QTableWidgetItem(str(row[11])))
            tablerow+=1

    def searchcompra_cbx_marca(self):
        self.prin.compras_tabla.clearContents()
        indexx=self.prin.cbx_categoria_compras.currentText()
        indexy=self.prin.cbx_marca_compras.currentText()

        busqueda=self.bd.busqueda_compras_marca(indexx,indexy)
        i=len(busqueda)
        self.prin.compras_tabla.setRowCount(i)
        tablerow=0
        for row in busqueda:
            self.prin.compras_tabla.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.prin.compras_tabla.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.prin.compras_tabla.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.prin.compras_tabla.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.prin.compras_tabla.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.prin.compras_tabla.setItem(tablerow,5,QTableWidgetItem(str(row[5])))
            self.prin.compras_tabla.setItem(tablerow,6,QTableWidgetItem(str(row[6])))
            self.prin.compras_tabla.setItem(tablerow,7,QTableWidgetItem(str(row[7])))
            self.prin.compras_tabla.setItem(tablerow,8,QTableWidgetItem(str(row[8])))
            self.prin.compras_tabla.setItem(tablerow,9,QTableWidgetItem(str(row[9])))
            self.prin.compras_tabla.setItem(tablerow,10,QTableWidgetItem(str(row[10])))
            self.prin.compras_tabla.setItem(tablerow,11,QTableWidgetItem(str(row[11])))
            tablerow+=1



    def openregis(self):
        self.nw=new_compra()
        self.nw.show()
        self.nw.new.usuario_compra.setText(self.prin.user_text.text())
        self.nw.new.usuario_wreg.setText(self.prin.user_text.text())
        self.nw.new.codusu_wreg.setText(self.prin.codigo_text.text())

    #VENTANA VENTA

    def cbx_tipopago(self):
        datos=self.bd.tipo_pago()

        for tipo in datos:
            self.prin.comprobante_venta.addItem(tipo[0])

    def open_seleccion(self):
        self.sel=ventana_seleccion()
        self.sel.show()
        
        self.sel.sp.aceptar_seleccion.clicked.connect(self.datos_seleccion)

    def datos_seleccion(self):
        
        selected_item = self.sel.sp.tabla_seleccion.selectedItems()[0]
        item_row = selected_item.row()
    
        global ide, cod, descrip, tipo, marca, modelo, precio, dscto, cantidad, total
        ide=self.sel.sp.tabla_seleccion.item(item_row,0).text()
        cod=self.sel.sp.tabla_seleccion.item(item_row,1).text()
        descrip=self.sel.sp.tabla_seleccion.item(item_row,2).text()
        tipo=self.sel.sp.tabla_seleccion.item(item_row,3).text()
        marca=self.sel.sp.tabla_seleccion.item(item_row,4).text()
        modelo=self.sel.sp.tabla_seleccion.item(item_row,5).text()
        precio=self.sel.sp.tabla_seleccion.item(item_row,6).text()
        dscto=self.sel.sp.dscto_seleccion.text()
        cantidad=self.sel.sp.cantidad_seleccion.text()
        total=self.sel.sp.total_seleccion.text()
        
        tablerow=self.prin.tabla_venta.rowCount()
        self.prin.tabla_venta.insertRow(tablerow)
        self.prin.tabla_venta.setItem(tablerow, 0, QTableWidgetItem(ide))
        self.prin.tabla_venta.setItem(tablerow, 1, QTableWidgetItem(cod))
        self.prin.tabla_venta.setItem(tablerow, 2, QTableWidgetItem(tipo))
        self.prin.tabla_venta.setItem(tablerow, 3, QTableWidgetItem(descrip))
        self.prin.tabla_venta.setItem(tablerow, 4, QTableWidgetItem(marca))
        self.prin.tabla_venta.setItem(tablerow, 5, QTableWidgetItem(modelo))
        self.prin.tabla_venta.setItem(tablerow, 6, QTableWidgetItem(precio))
        self.prin.tabla_venta.setItem(tablerow, 7, QTableWidgetItem(dscto))
        self.prin.tabla_venta.setItem(tablerow, 8, QTableWidgetItem(cantidad))
        self.prin.tabla_venta.setItem(tablerow, 9, QTableWidgetItem(total))

        self.sel.hide()
        

    def suma_venta(self):
        suma = 0
        for fila in range(self.prin.tabla_venta.rowCount()):
            item = self.prin.tabla_venta.item(fila, 9)
            if item:
                suma += float(item.text())
        self.prin.total_venta.setText(str(suma))

    def eliminar_seleccion(self):
        selected_row=self.prin.tabla_venta.currentRow()
        self.prin.tabla_venta.removeRow(selected_row)
        self.suma_venta()

    def procesar_sell(self):

        print("EXITO")

        for row in range(self.prin.tabla_venta.rowCount()):

            cod = self.prin.tabla_venta.item(row, 1).text()
            tipo = self.prin.tabla_venta.item(row, 2).text()
            descrip = self.prin.tabla_venta.item(row, 3).text()
            marca = self.prin.tabla_venta.item(row, 4).text()
            modelo = self.prin.tabla_venta.item(row, 5).text()
            precio = self.prin.tabla_venta.item(row, 6).text()
            dscto = self.prin.tabla_venta.item(row, 7).text()
            cantidad = self.prin.tabla_venta.item(row, 8).text()
            total = self.prin.tabla_venta.item(row, 9).text()
            cod_v = self.bd.obtener_ultimo_id_venta() + 1

            self.bd.proceso_detalle_venta(cod,tipo,descrip,marca,modelo,precio,dscto,cantidad,total,cod_v)


        cliente=self.prin.cliente_venta.text()
        doc=self.prin.documento_venta.text()
        tel=self.prin.telf_venta.text()
        tp=self.prin.comprobante_venta.currentText()
        tot=self.prin.total_venta.text()
        user=self.prin.codigo_text.text()

        self.bd.proceso_venta(cod_v,cliente,doc,tel,tot,tp,user)
        self.prin.tabla_venta.setRowCount(0)
        self.prin.tabla_venta.clearContents()
        self.prin.cliente_venta.clear()
        self.prin.documento_venta.clear()
        self.prin.telf_venta.clear()
        self.prin.total_venta.clear()

    


    def salir(self):
        sys.exit()
    
    def min(self):
        self.showMinimized()
