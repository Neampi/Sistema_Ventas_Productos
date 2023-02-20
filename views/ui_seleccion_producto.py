# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seleccion_productoHamnbd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sell_w(object):
    def setupUi(self, sell_w):
        if not sell_w.objectName():
            sell_w.setObjectName(u"sell_w")
        sell_w.resize(792, 432)
        self.centralwidget = QWidget(sell_w)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(345, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.cod_seleccion = QLineEdit(self.frame_2)
        self.cod_seleccion.setObjectName(u"cod_seleccion")
        self.cod_seleccion.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.cod_seleccion)

        self.buscar_cod_sel = QPushButton(self.frame_2)
        self.buscar_cod_sel.setObjectName(u"buscar_cod_sel")
        self.buscar_cod_sel.setMaximumSize(QSize(16777215, 40))
        self.buscar_cod_sel.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_cod_sel)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cat_cbx_seleccion = QComboBox(self.frame_2)
        self.cat_cbx_seleccion.setObjectName(u"cat_cbx_seleccion")
        self.cat_cbx_seleccion.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.cat_cbx_seleccion)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.mar_cbx_seleccion = QComboBox(self.frame_2)
        self.mar_cbx_seleccion.setObjectName(u"mar_cbx_seleccion")
        self.mar_cbx_seleccion.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.mar_cbx_seleccion)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.mod_cbx_seleccion = QComboBox(self.frame_2)
        self.mod_cbx_seleccion.setObjectName(u"mod_cbx_seleccion")
        self.mod_cbx_seleccion.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.mod_cbx_seleccion)

        self.buscar_mod_sel = QPushButton(self.frame_2)
        self.buscar_mod_sel.setObjectName(u"buscar_mod_sel")
        self.buscar_mod_sel.setMaximumSize(QSize(16777215, 40))
        self.buscar_mod_sel.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.buscar_mod_sel)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tabla_seleccion = QTableWidget(self.frame)
        if (self.tabla_seleccion.columnCount() < 7):
            self.tabla_seleccion.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_seleccion.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_seleccion.setObjectName(u"tabla_seleccion")
        self.tabla_seleccion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_seleccion.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tabla_seleccion)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.dscto_seleccion = QLineEdit(self.frame_4)
        self.dscto_seleccion.setObjectName(u"dscto_seleccion")
        self.dscto_seleccion.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.dscto_seleccion)

        self.horizontalSpacer_2 = QSpacerItem(212, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.cantidad_seleccion = QLineEdit(self.frame_4)
        self.cantidad_seleccion.setObjectName(u"cantidad_seleccion")
        self.cantidad_seleccion.setMinimumSize(QSize(150, 0))
        self.cantidad_seleccion.setMaximumSize(QSize(155, 16777215))

        self.horizontalLayout_3.addWidget(self.cantidad_seleccion)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_4.addWidget(self.label_8)

        self.total_seleccion = QLineEdit(self.frame_5)
        self.total_seleccion.setObjectName(u"total_seleccion")
        self.total_seleccion.setMaximumSize(QSize(200, 16777215))
        self.total_seleccion.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.total_seleccion)

        self.horizontalSpacer_3 = QSpacerItem(213, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.aceptar_seleccion = QPushButton(self.frame_5)
        self.aceptar_seleccion.setObjectName(u"aceptar_seleccion")
        self.aceptar_seleccion.setMaximumSize(QSize(16777215, 40))
        self.aceptar_seleccion.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.aceptar_seleccion)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        sell_w.setCentralWidget(self.centralwidget)

        self.retranslateUi(sell_w)

        QMetaObject.connectSlotsByName(sell_w)
    # setupUi

    def retranslateUi(self, sell_w):
        sell_w.setWindowTitle(QCoreApplication.translate("sell_w", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("sell_w", u"SELECCIONAR PRODUCTO", None))
        self.pushButton.setText(QCoreApplication.translate("sell_w", u"X", None))
        self.label.setText(QCoreApplication.translate("sell_w", u"CODIGO:", None))
        self.buscar_cod_sel.setText(QCoreApplication.translate("sell_w", u"BUSCAR", None))
        self.label_3.setText(QCoreApplication.translate("sell_w", u"CATEGORIA:", None))
        self.label_4.setText(QCoreApplication.translate("sell_w", u"MARCA:", None))
        self.label_5.setText(QCoreApplication.translate("sell_w", u"MODELO:", None))
        self.buscar_mod_sel.setText(QCoreApplication.translate("sell_w", u"BUSCAR", None))
        ___qtablewidgetitem = self.tabla_seleccion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sell_w", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_seleccion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sell_w", u"CODIGO", None));
        ___qtablewidgetitem2 = self.tabla_seleccion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sell_w", u"DESCRIPCION", None));
        ___qtablewidgetitem3 = self.tabla_seleccion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sell_w", u"TIPO", None));
        ___qtablewidgetitem4 = self.tabla_seleccion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("sell_w", u"MARCA", None));
        ___qtablewidgetitem5 = self.tabla_seleccion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("sell_w", u"MODELO", None));
        ___qtablewidgetitem6 = self.tabla_seleccion.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("sell_w", u"PRECIO", None));
        self.label_6.setText(QCoreApplication.translate("sell_w", u"DESCUENTO:", None))
        self.label_7.setText(QCoreApplication.translate("sell_w", u"CANTIDAD:", None))
        self.label_8.setText(QCoreApplication.translate("sell_w", u"TOTAL:", None))
        self.aceptar_seleccion.setText(QCoreApplication.translate("sell_w", u"ACEPTAR", None))
    # retranslateUi

