# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regComprasfYBHzj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_registroCompras(object):
    def setupUi(self, registroCompras):
        if not registroCompras.objectName():
            registroCompras.setObjectName(u"registroCompras")
        registroCompras.resize(800, 600)
        self.centralwidget = QWidget(registroCompras)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(61, 61, 61);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(504, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exit_button = QPushButton(self.frame_9)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(30, 30))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 50px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.exit_button)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_11)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(23)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.codigo_compra = QLineEdit(self.frame_3)
        self.codigo_compra.setObjectName(u"codigo_compra")

        self.verticalLayout.addWidget(self.codigo_compra)

        self.categoria_compra = QLineEdit(self.frame_3)
        self.categoria_compra.setObjectName(u"categoria_compra")

        self.verticalLayout.addWidget(self.categoria_compra)

        self.marca_compra = QLineEdit(self.frame_3)
        self.marca_compra.setObjectName(u"marca_compra")

        self.verticalLayout.addWidget(self.marca_compra)

        self.modelo_compra = QLineEdit(self.frame_3)
        self.modelo_compra.setObjectName(u"modelo_compra")

        self.verticalLayout.addWidget(self.modelo_compra)

        self.descripcion_compra = QLineEdit(self.frame_3)
        self.descripcion_compra.setObjectName(u"descripcion_compra")

        self.verticalLayout.addWidget(self.descripcion_compra)

        self.preciocompra_compra = QLineEdit(self.frame_3)
        self.preciocompra_compra.setObjectName(u"preciocompra_compra")

        self.verticalLayout.addWidget(self.preciocompra_compra)

        self.precioventa_compra = QLineEdit(self.frame_3)
        self.precioventa_compra.setObjectName(u"precioventa_compra")

        self.verticalLayout.addWidget(self.precioventa_compra)

        self.stock_compra = QLineEdit(self.frame_3)
        self.stock_compra.setObjectName(u"stock_compra")

        self.verticalLayout.addWidget(self.stock_compra)

        self.usuario_compra = QLineEdit(self.frame_3)
        self.usuario_compra.setObjectName(u"usuario_compra")
        self.usuario_compra.setReadOnly(True)

        self.verticalLayout.addWidget(self.usuario_compra)

        self.totalcompra_compra = QLineEdit(self.frame_3)
        self.totalcompra_compra.setObjectName(u"totalcompra_compra")
        self.totalcompra_compra.setReadOnly(True)

        self.verticalLayout.addWidget(self.totalcompra_compra)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.buscar_button_registro_compra = QPushButton(self.frame_5)
        self.buscar_button_registro_compra.setObjectName(u"buscar_button_registro_compra")
        self.buscar_button_registro_compra.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.buscar_button_registro_compra)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_14)

        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_16)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.fecha_wreg = QLabel(self.frame_7)
        self.fecha_wreg.setObjectName(u"fecha_wreg")
        self.fecha_wreg.setFont(font1)

        self.verticalLayout_5.addWidget(self.fecha_wreg)

        self.hora_wreg = QLabel(self.frame_7)
        self.hora_wreg.setObjectName(u"hora_wreg")
        self.hora_wreg.setFont(font1)

        self.verticalLayout_5.addWidget(self.hora_wreg)

        self.usuario_wreg = QLabel(self.frame_7)
        self.usuario_wreg.setObjectName(u"usuario_wreg")
        self.usuario_wreg.setMaximumSize(QSize(16777215, 41))
        self.usuario_wreg.setFont(font1)

        self.verticalLayout_5.addWidget(self.usuario_wreg)

        self.codusu_wreg = QLabel(self.frame_7)
        self.codusu_wreg.setObjectName(u"codusu_wreg")
        self.codusu_wreg.setMaximumSize(QSize(16777215, 41))
        self.codusu_wreg.setFont(font1)

        self.verticalLayout_5.addWidget(self.codusu_wreg)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.registrar_button_registro_compra = QPushButton(self.frame_5)
        self.registrar_button_registro_compra.setObjectName(u"registrar_button_registro_compra")
        self.registrar_button_registro_compra.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.registrar_button_registro_compra)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame)

        registroCompras.setCentralWidget(self.centralwidget)

        self.retranslateUi(registroCompras)

        QMetaObject.connectSlotsByName(registroCompras)
    # setupUi

    def retranslateUi(self, registroCompras):
        registroCompras.setWindowTitle(QCoreApplication.translate("registroCompras", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("registroCompras", u"REGISTRO COMPRAS", None))
        self.exit_button.setText(QCoreApplication.translate("registroCompras", u"X", None))
        self.label_2.setText(QCoreApplication.translate("registroCompras", u"CODIGO:", None))
        self.label_3.setText(QCoreApplication.translate("registroCompras", u"CATEGORIA:", None))
        self.label_4.setText(QCoreApplication.translate("registroCompras", u"MARCA:", None))
        self.label_5.setText(QCoreApplication.translate("registroCompras", u"MODELO:", None))
        self.label_6.setText(QCoreApplication.translate("registroCompras", u"DESCRIPCION:", None))
        self.label_7.setText(QCoreApplication.translate("registroCompras", u"PRECIO COMPRA:", None))
        self.label_8.setText(QCoreApplication.translate("registroCompras", u"PRECIO VENTA:", None))
        self.label_9.setText(QCoreApplication.translate("registroCompras", u"STOCK:", None))
        self.label_10.setText(QCoreApplication.translate("registroCompras", u"USUARIO:", None))
        self.label_11.setText(QCoreApplication.translate("registroCompras", u"TOTAL COMPRA:", None))
        self.buscar_button_registro_compra.setText(QCoreApplication.translate("registroCompras", u"BUSCAR", None))
        self.label_12.setText(QCoreApplication.translate("registroCompras", u"FECHA:", None))
        self.label_14.setText(QCoreApplication.translate("registroCompras", u"HORA:", None))
        self.label_16.setText(QCoreApplication.translate("registroCompras", u"USUARIO:", None))
        self.fecha_wreg.setText(QCoreApplication.translate("registroCompras", u"FECHA:", None))
        self.hora_wreg.setText(QCoreApplication.translate("registroCompras", u"HORA:", None))
        self.usuario_wreg.setText(QCoreApplication.translate("registroCompras", u"USU", None))
        self.codusu_wreg.setText(QCoreApplication.translate("registroCompras", u"COD_USU", None))
        self.registrar_button_registro_compra.setText(QCoreApplication.translate("registroCompras", u"REGISTRAR", None))
    # retranslateUi

