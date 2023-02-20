# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principalWindowBgTQfb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_principal_w(object):
    def setupUi(self, principal_w):
        if not principal_w.objectName():
            principal_w.setObjectName(u"principal_w")
        principal_w.resize(1269, 639)
        self.centralwidget = QWidget(principal_w)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 2, 0, 2)
        self.titulos_button = QFrame(self.frame)
        self.titulos_button.setObjectName(u"titulos_button")
        self.titulos_button.setMinimumSize(QSize(0, 42))
        self.titulos_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")
        self.titulos_button.setFrameShape(QFrame.StyledPanel)
        self.titulos_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titulos_button)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.home_b = QPushButton(self.titulos_button)
        self.home_b.setObjectName(u"home_b")
        self.home_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.home_b)

        self.inventario_b = QPushButton(self.titulos_button)
        self.inventario_b.setObjectName(u"inventario_b")
        self.inventario_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.inventario_b)

        self.compras_b = QPushButton(self.titulos_button)
        self.compras_b.setObjectName(u"compras_b")
        self.compras_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.compras_b)

        self.ventas_b = QPushButton(self.titulos_button)
        self.ventas_b.setObjectName(u"ventas_b")
        self.ventas_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.ventas_b)

        self.reportes_b = QPushButton(self.titulos_button)
        self.reportes_b.setObjectName(u"reportes_b")
        self.reportes_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.reportes_b)

        self.avanzado_b = QPushButton(self.titulos_button)
        self.avanzado_b.setObjectName(u"avanzado_b")
        self.avanzado_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.avanzado_b)

        self.configuracion_b = QPushButton(self.titulos_button)
        self.configuracion_b.setObjectName(u"configuracion_b")
        self.configuracion_b.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.configuracion_b)

        self.op_ventana = QFrame(self.titulos_button)
        self.op_ventana.setObjectName(u"op_ventana")
        self.op_ventana.setMinimumSize(QSize(0, 0))
        self.op_ventana.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.op_ventana.setFrameShape(QFrame.StyledPanel)
        self.op_ventana.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.op_ventana)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.salir_b = QPushButton(self.op_ventana)
        self.salir_b.setObjectName(u"salir_b")
        self.salir_b.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.salir_b)

        self.minimizar_b = QPushButton(self.op_ventana)
        self.minimizar_b.setObjectName(u"minimizar_b")
        self.minimizar_b.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.minimizar_b)


        self.horizontalLayout.addWidget(self.op_ventana)


        self.verticalLayout_2.addWidget(self.titulos_button)

        self.contenido = QFrame(self.frame)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(61, 61, 61);\n"
"	color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"")
        self.contenido.setFrameShape(QFrame.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contenido)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.paginas_forbutton = QStackedWidget(self.contenido)
        self.paginas_forbutton.setObjectName(u"paginas_forbutton")
        self.paginas_forbutton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.compras_w = QWidget()
        self.compras_w.setObjectName(u"compras_w")
        self.verticalLayout_5 = QVBoxLayout(self.compras_w)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.compras_w)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 8pt \"MS Sans Serif\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.frame_2 = QFrame(self.compras_w)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.cbx_categoria_compras = QComboBox(self.frame_2)
        self.cbx_categoria_compras.setObjectName(u"cbx_categoria_compras")
        self.cbx_categoria_compras.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.cbx_categoria_compras)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_9)

        self.cbx_marca_compras = QComboBox(self.frame_2)
        self.cbx_marca_compras.setObjectName(u"cbx_marca_compras")
        self.cbx_marca_compras.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.cbx_marca_compras)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_2.addWidget(self.label_10)

        self.cbx_modelo_compras = QComboBox(self.frame_2)
        self.cbx_modelo_compras.setObjectName(u"cbx_modelo_compras")
        self.cbx_modelo_compras.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.cbx_modelo_compras)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.fecha_inicio_buscar = QDateEdit(self.frame_2)
        self.fecha_inicio_buscar.setObjectName(u"fecha_inicio_buscar")
        self.fecha_inicio_buscar.setMinimumDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.fecha_inicio_buscar)

        self.fecha_final_buscar = QDateEdit(self.frame_2)
        self.fecha_final_buscar.setObjectName(u"fecha_final_buscar")
        self.fecha_final_buscar.setMinimumDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_2.addWidget(self.fecha_final_buscar)

        self.buscar_compras_button = QPushButton(self.frame_2)
        self.buscar_compras_button.setObjectName(u"buscar_compras_button")
        self.buscar_compras_button.setMinimumSize(QSize(60, 20))
        self.buscar_compras_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_compras_button)

        self.buscar_compras_fecha = QPushButton(self.frame_2)
        self.buscar_compras_fecha.setObjectName(u"buscar_compras_fecha")
        self.buscar_compras_fecha.setMinimumSize(QSize(60, 20))
        self.buscar_compras_fecha.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_compras_fecha)

        self.buscar_compras_categoria = QPushButton(self.frame_2)
        self.buscar_compras_categoria.setObjectName(u"buscar_compras_categoria")
        self.buscar_compras_categoria.setMinimumSize(QSize(60, 20))
        self.buscar_compras_categoria.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_compras_categoria)

        self.buscar_compras_marca = QPushButton(self.frame_2)
        self.buscar_compras_marca.setObjectName(u"buscar_compras_marca")
        self.buscar_compras_marca.setMinimumSize(QSize(60, 20))
        self.buscar_compras_marca.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_compras_marca)

        self.actualizar_compras_button = QPushButton(self.frame_2)
        self.actualizar_compras_button.setObjectName(u"actualizar_compras_button")
        self.actualizar_compras_button.setMinimumSize(QSize(80, 20))
        self.actualizar_compras_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.actualizar_compras_button)

        self.registrar_producto_button = QPushButton(self.frame_2)
        self.registrar_producto_button.setObjectName(u"registrar_producto_button")
        self.registrar_producto_button.setMinimumSize(QSize(115, 20))
        self.registrar_producto_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.registrar_producto_button)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.compras_tabla = QTableWidget(self.compras_w)
        if (self.compras_tabla.columnCount() < 12):
            self.compras_tabla.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.compras_tabla.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.compras_tabla.setObjectName(u"compras_tabla")
        self.compras_tabla.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.compras_tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.compras_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_5.addWidget(self.compras_tabla)

        self.paginas_forbutton.addWidget(self.compras_w)
        self.inventario_w = QWidget()
        self.inventario_w.setObjectName(u"inventario_w")
        self.verticalLayout_6 = QVBoxLayout(self.inventario_w)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.inventario_w)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.inventario_w)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.cbx_categoria_inventario = QComboBox(self.frame_3)
        self.cbx_categoria_inventario.setObjectName(u"cbx_categoria_inventario")

        self.horizontalLayout_3.addWidget(self.cbx_categoria_inventario)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.cbx_marca_inventario = QComboBox(self.frame_3)
        self.cbx_marca_inventario.setObjectName(u"cbx_marca_inventario")

        self.horizontalLayout_3.addWidget(self.cbx_marca_inventario)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.cbx_modelo_inventario = QComboBox(self.frame_3)
        self.cbx_modelo_inventario.setObjectName(u"cbx_modelo_inventario")
        self.cbx_modelo_inventario.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.cbx_modelo_inventario)

        self.horizontalSpacer_2 = QSpacerItem(500, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.buscar_inventario_button = QPushButton(self.frame_3)
        self.buscar_inventario_button.setObjectName(u"buscar_inventario_button")
        self.buscar_inventario_button.setMinimumSize(QSize(0, 20))
        self.buscar_inventario_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.buscar_inventario_button)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.inventario_w)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.inventario_tabla = QTableWidget(self.frame_4)
        if (self.inventario_tabla.columnCount() < 8):
            self.inventario_tabla.setColumnCount(8)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.inventario_tabla.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        self.inventario_tabla.setObjectName(u"inventario_tabla")
        self.inventario_tabla.setMaximumSize(QSize(802, 16777215))
        self.inventario_tabla.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.inventario_tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inventario_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_4.addWidget(self.inventario_tabla)

        self.lado_derecho = QFrame(self.frame_4)
        self.lado_derecho.setObjectName(u"lado_derecho")
        self.lado_derecho.setFrameShape(QFrame.StyledPanel)
        self.lado_derecho.setFrameShadow(QFrame.Raised)
        self.btn_actualizar_inventario = QPushButton(self.lado_derecho)
        self.btn_actualizar_inventario.setObjectName(u"btn_actualizar_inventario")
        self.btn_actualizar_inventario.setGeometry(QRect(110, 20, 151, 23))
        self.btn_actualizar_inventario.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.lado_derecho)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.paginas_forbutton.addWidget(self.inventario_w)
        self.home_w = QWidget()
        self.home_w.setObjectName(u"home_w")
        self.frame_5 = QFrame(self.home_w)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 400, 158))
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(20, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bienvenida = QLabel(self.frame_6)
        self.bienvenida.setObjectName(u"bienvenida")
        self.bienvenida.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_7.addWidget(self.bienvenida)

        self.bienvenida_2 = QLabel(self.frame_6)
        self.bienvenida_2.setObjectName(u"bienvenida_2")
        self.bienvenida_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_7.addWidget(self.bienvenida_2)

        self.bienvenida_3 = QLabel(self.frame_6)
        self.bienvenida_3.setObjectName(u"bienvenida_3")
        self.bienvenida_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_7.addWidget(self.bienvenida_3)

        self.bienvenida_4 = QLabel(self.frame_6)
        self.bienvenida_4.setObjectName(u"bienvenida_4")
        self.bienvenida_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_7.addWidget(self.bienvenida_4)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(80, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.user_text = QLabel(self.frame_7)
        self.user_text.setObjectName(u"user_text")
        self.user_text.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_8.addWidget(self.user_text)

        self.codigo_text = QLabel(self.frame_7)
        self.codigo_text.setObjectName(u"codigo_text")
        self.codigo_text.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_8.addWidget(self.codigo_text)

        self.nombre_text = QLabel(self.frame_7)
        self.nombre_text.setObjectName(u"nombre_text")
        self.nombre_text.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_8.addWidget(self.nombre_text)

        self.cargo_text = QLabel(self.frame_7)
        self.cargo_text.setObjectName(u"cargo_text")
        self.cargo_text.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"")

        self.verticalLayout_8.addWidget(self.cargo_text)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.paginas_forbutton.addWidget(self.home_w)
        self.ventas_w = QWidget()
        self.ventas_w.setObjectName(u"ventas_w")
        self.ventas_w.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.ventas_w)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.ventas_w)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_11.addWidget(self.label_2)

        self.frame_8 = QFrame(self.ventas_w)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.cliente_venta = QLineEdit(self.frame_9)
        self.cliente_venta.setObjectName(u"cliente_venta")

        self.horizontalLayout_6.addWidget(self.cliente_venta)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.documento_venta = QLineEdit(self.frame_9)
        self.documento_venta.setObjectName(u"documento_venta")

        self.horizontalLayout_6.addWidget(self.documento_venta)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.telf_venta = QLineEdit(self.frame_9)
        self.telf_venta.setObjectName(u"telf_venta")

        self.horizontalLayout_6.addWidget(self.telf_venta)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.buscar_producto_venta = QPushButton(self.frame_10)
        self.buscar_producto_venta.setObjectName(u"buscar_producto_venta")
        self.buscar_producto_venta.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_7.addWidget(self.buscar_producto_venta)

        self.horizontalSpacer = QSpacerItem(700, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.label_15)

        self.comprobante_venta = QComboBox(self.frame_10)
        self.comprobante_venta.setObjectName(u"comprobante_venta")
        self.comprobante_venta.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.comprobante_venta)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.tabla_venta = QTableWidget(self.ventas_w)
        if (self.tabla_venta.columnCount() < 10):
            self.tabla_venta.setColumnCount(10)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(9, __qtablewidgetitem29)
        self.tabla_venta.setObjectName(u"tabla_venta")
        self.tabla_venta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_venta.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_11.addWidget(self.tabla_venta)

        self.frame_11 = QFrame(self.ventas_w)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setPointSize(48)
        self.label_16.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.total_venta = QLineEdit(self.frame_11)
        self.total_venta.setObjectName(u"total_venta")
        self.total_venta.setMaximumSize(QSize(800, 85))
        font2 = QFont()
        font2.setFamily(u"Microsoft Yi Baiti")
        font2.setPointSize(48)
        self.total_venta.setFont(font2)
        self.total_venta.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.total_venta)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(200, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.eliminar_producto_venta = QPushButton(self.frame_12)
        self.eliminar_producto_venta.setObjectName(u"eliminar_producto_venta")
        self.eliminar_producto_venta.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_10.addWidget(self.eliminar_producto_venta)

        self.procesar_venta = QPushButton(self.frame_12)
        self.procesar_venta.setObjectName(u"procesar_venta")
        self.procesar_venta.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_10.addWidget(self.procesar_venta)


        self.horizontalLayout_8.addWidget(self.frame_12)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.paginas_forbutton.addWidget(self.ventas_w)
        self.reportes_w = QWidget()
        self.reportes_w.setObjectName(u"reportes_w")
        self.paginas_forbutton.addWidget(self.reportes_w)
        self.avanzado_w = QWidget()
        self.avanzado_w.setObjectName(u"avanzado_w")
        self.paginas_forbutton.addWidget(self.avanzado_w)
        self.configuracion_w = QWidget()
        self.configuracion_w.setObjectName(u"configuracion_w")
        self.paginas_forbutton.addWidget(self.configuracion_w)

        self.verticalLayout_4.addWidget(self.paginas_forbutton)


        self.verticalLayout_2.addWidget(self.contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        principal_w.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal_w)

        self.paginas_forbutton.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(principal_w)
    # setupUi

    def retranslateUi(self, principal_w):
        principal_w.setWindowTitle(QCoreApplication.translate("principal_w", u"MainWindow", None))
        self.home_b.setText(QCoreApplication.translate("principal_w", u"HOME", None))
        self.inventario_b.setText(QCoreApplication.translate("principal_w", u"INVENTARIO", None))
        self.compras_b.setText(QCoreApplication.translate("principal_w", u"COMPRAS", None))
        self.ventas_b.setText(QCoreApplication.translate("principal_w", u"VENTAS", None))
        self.reportes_b.setText(QCoreApplication.translate("principal_w", u"REPORTES", None))
        self.avanzado_b.setText(QCoreApplication.translate("principal_w", u"AVANZADO", None))
        self.configuracion_b.setText(QCoreApplication.translate("principal_w", u"CONFIGURACION", None))
        self.salir_b.setText(QCoreApplication.translate("principal_w", u"X", None))
        self.minimizar_b.setText(QCoreApplication.translate("principal_w", u"-", None))
        self.label.setText(QCoreApplication.translate("principal_w", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">COMPRAS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("principal_w", u"CATEGORIA:", None))
        self.label_9.setText(QCoreApplication.translate("principal_w", u"MARCA:", None))
        self.label_10.setText(QCoreApplication.translate("principal_w", u"MODELO:", None))
        self.label_3.setText(QCoreApplication.translate("principal_w", u"FECHA:", None))
        self.buscar_compras_button.setText(QCoreApplication.translate("principal_w", u"BUSCAR TOTAL", None))
        self.buscar_compras_fecha.setText(QCoreApplication.translate("principal_w", u"FECHA", None))
        self.buscar_compras_categoria.setText(QCoreApplication.translate("principal_w", u"CATEGORIA", None))
        self.buscar_compras_marca.setText(QCoreApplication.translate("principal_w", u"MARCA", None))
        self.actualizar_compras_button.setText(QCoreApplication.translate("principal_w", u"ACTUALIZAR", None))
        self.registrar_producto_button.setText(QCoreApplication.translate("principal_w", u"REGISTRAR NUEVO", None))
        ___qtablewidgetitem = self.compras_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("principal_w", u"ID", None));
        ___qtablewidgetitem1 = self.compras_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("principal_w", u"Fecha", None));
        ___qtablewidgetitem2 = self.compras_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("principal_w", u"Usuario", None));
        ___qtablewidgetitem3 = self.compras_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("principal_w", u"Categoria", None));
        ___qtablewidgetitem4 = self.compras_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("principal_w", u"Codigo", None));
        ___qtablewidgetitem5 = self.compras_tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("principal_w", u"Descripcion", None));
        ___qtablewidgetitem6 = self.compras_tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("principal_w", u"Marca", None));
        ___qtablewidgetitem7 = self.compras_tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("principal_w", u"Modelo", None));
        ___qtablewidgetitem8 = self.compras_tabla.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("principal_w", u"Precio Compra", None));
        ___qtablewidgetitem9 = self.compras_tabla.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("principal_w", u"Precio Venta", None));
        ___qtablewidgetitem10 = self.compras_tabla.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("principal_w", u"Cantidad", None));
        ___qtablewidgetitem11 = self.compras_tabla.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("principal_w", u"Total Compra", None));
        self.label_4.setText(QCoreApplication.translate("principal_w", u"INVENTARIO", None))
        self.label_5.setText(QCoreApplication.translate("principal_w", u"CATEGORIA:", None))
        self.label_6.setText(QCoreApplication.translate("principal_w", u"MARCA:", None))
        self.label_7.setText(QCoreApplication.translate("principal_w", u"MODELO:", None))
        self.buscar_inventario_button.setText(QCoreApplication.translate("principal_w", u"BUSCAR", None))
        ___qtablewidgetitem12 = self.inventario_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("principal_w", u"ID", None));
        ___qtablewidgetitem13 = self.inventario_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("principal_w", u"Codigo", None));
        ___qtablewidgetitem14 = self.inventario_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("principal_w", u"Descripcion", None));
        ___qtablewidgetitem15 = self.inventario_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("principal_w", u"Categoria", None));
        ___qtablewidgetitem16 = self.inventario_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("principal_w", u"Marca", None));
        ___qtablewidgetitem17 = self.inventario_tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("principal_w", u"Modelo", None));
        ___qtablewidgetitem18 = self.inventario_tabla.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("principal_w", u"Precio Venta", None));
        ___qtablewidgetitem19 = self.inventario_tabla.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("principal_w", u"Stock", None));
        self.btn_actualizar_inventario.setText(QCoreApplication.translate("principal_w", u"ACTUALIZAR", None))
        self.bienvenida.setText(QCoreApplication.translate("principal_w", u"USER", None))
        self.bienvenida_2.setText(QCoreApplication.translate("principal_w", u"CODIGO:", None))
        self.bienvenida_3.setText(QCoreApplication.translate("principal_w", u"NOMBRE:", None))
        self.bienvenida_4.setText(QCoreApplication.translate("principal_w", u"CARGO:", None))
        self.user_text.setText("")
        self.codigo_text.setText("")
        self.nombre_text.setText("")
        self.cargo_text.setText("")
        self.label_2.setText(QCoreApplication.translate("principal_w", u"VENTA", None))
        self.label_11.setText(QCoreApplication.translate("principal_w", u"CLIENTE:", None))
        self.label_12.setText(QCoreApplication.translate("principal_w", u"DOCUMENTO:", None))
        self.label_13.setText(QCoreApplication.translate("principal_w", u"TELEFONO:", None))
        self.label_14.setText(QCoreApplication.translate("principal_w", u"PRODUCTO:", None))
        self.buscar_producto_venta.setText(QCoreApplication.translate("principal_w", u"BUSCAR", None))
        self.label_15.setText(QCoreApplication.translate("principal_w", u"TIPO DE PAGO:", None))
        ___qtablewidgetitem20 = self.tabla_venta.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("principal_w", u"ID", None));
        ___qtablewidgetitem21 = self.tabla_venta.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("principal_w", u"CODIGO", None));
        ___qtablewidgetitem22 = self.tabla_venta.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("principal_w", u"TIPO", None));
        ___qtablewidgetitem23 = self.tabla_venta.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("principal_w", u"DESCRIPCION", None));
        ___qtablewidgetitem24 = self.tabla_venta.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("principal_w", u"MARCA", None));
        ___qtablewidgetitem25 = self.tabla_venta.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("principal_w", u"MODELO", None));
        ___qtablewidgetitem26 = self.tabla_venta.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("principal_w", u"PRECIO", None));
        ___qtablewidgetitem27 = self.tabla_venta.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("principal_w", u"DESCUENTO", None));
        ___qtablewidgetitem28 = self.tabla_venta.horizontalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("principal_w", u"CANTIDAD", None));
        ___qtablewidgetitem29 = self.tabla_venta.horizontalHeaderItem(9)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("principal_w", u"TOTAL", None));
        self.label_16.setText(QCoreApplication.translate("principal_w", u"TOTAL", None))
        self.total_venta.setText("")
        self.eliminar_producto_venta.setText(QCoreApplication.translate("principal_w", u"ELIMINAR", None))
        self.procesar_venta.setText(QCoreApplication.translate("principal_w", u"PROCESAR", None))
    # retranslateUi

