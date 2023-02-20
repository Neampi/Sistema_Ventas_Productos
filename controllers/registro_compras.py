
from datetime import datetime
from PySide2.QtWidgets import QWidget, QMainWindow
from views.ui_regCompras import *
from controllers.main_w import *
from db.conexion_sql import Conexion

class new_compra(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.new=Ui_registroCompras()
        self.new.setupUi(self)

        self.bd=Conexion()

        self.new.buscar_button_registro_compra.clicked.connect(self.busqueda_codigo)
        self.new.registrar_button_registro_compra.clicked.connect(self.registrar)

        fechanow=datetime.now()
        fecha=datetime.strftime(fechanow, '%d/%m/%Y')
        hora=datetime.strftime(fechanow, '%H:%M')
        self.new.fecha_wreg.setText(fecha)
        self.new.hora_wreg.setText(hora)

        self.new.preciocompra_compra.textChanged.connect(self.total_compra)
        self.new.stock_compra.textChanged.connect(self.total_compra)
        

    def busqueda_codigo(self):
        busqueda=self.new.codigo_compra.text()

        try:
            self.search=self.bd.busqueda_codigo_newbuy(busqueda)
            cod=self.search[0][4]
            cate=self.search[0][3]
            marca=self.search[0][6]
            modelo=self.search[0][7]
            desc=self.search[0][5]

            if cod==busqueda:
                self.new.categoria_compra.setText(cate)
                self.new.marca_compra.setText(marca)
                self.new.modelo_compra.setText(modelo)
                self.new.descripcion_compra.setText(desc)

        except Exception:
            print("ERROR")

                
    def total_compra(self):
        
        if self.new.preciocompra_compra.text()=='':
            pcom=0
        else:
            pcom=float(self.new.preciocompra_compra.text())

        if self.new.stock_compra.text()=='':
            stock=0
        else:
            stock=float(self.new.stock_compra.text())

        tot=pcom*stock

        return self.new.totalcompra_compra.setText(str(tot))


    def registrar(self):
        cod=self.new.codigo_compra.text()
        cat=self.new.categoria_compra.text()
        marc=self.new.marca_compra.text()
        mod=self.new.modelo_compra.text()
        descr=self.new.descripcion_compra.text()
        pc=self.new.preciocompra_compra.text()
        pv=self.new.precioventa_compra.text()
        stock=self.new.stock_compra.text()
        usu=self.new.codusu_wreg.text()
        tc=self.new.totalcompra_compra.text()

        if cod!='' and cat!='' and marc!='' and mod!='' and descr!='' and pc!='' and pv!='' and stock!='' and tc!='':
            self.bd.registro_producto(usu,cat,cod,descr,marc,mod,pc,pv,stock,tc)
            self.hide()
        else:
            print("ERROR")

                
        

