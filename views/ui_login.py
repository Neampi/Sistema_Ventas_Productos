# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logincPPjhN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(363, 381)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, 1, 344, 479))
        self.label.setPixmap(QPixmap(u"../assets/ICONS/fondo.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 30, 101, 101))
        self.label_2.setPixmap(QPixmap(u"../assets/ICONS/icon.png"))
        self.label_2.setScaledContents(True)
        self.exit_button = QPushButton(self.frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(304, 10, 31, 23))
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
        self.usuLine = QLineEdit(self.frame)
        self.usuLine.setObjectName(u"usuLine")
        self.usuLine.setGeometry(QRect(60, 160, 221, 31))
        self.usuLine.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(125, 131, 71);\n"
"padding-bottom:7px;")
        self.usuLine.setAlignment(Qt.AlignCenter)
        self.usuLine.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.passLine = QLineEdit(self.frame)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(60, 220, 221, 31))
        self.passLine.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(125, 131, 71);\n"
"padding-bottom:7px;")
        self.passLine.setAlignment(Qt.AlignCenter)
        self.logButton = QPushButton(self.frame)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(60, 290, 221, 31))
        self.logButton.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.error = QLabel(self.frame)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(60, 270, 221, 16))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.frame)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.exit_button.setText(QCoreApplication.translate("login", u"X", None))
        self.usuLine.setPlaceholderText(QCoreApplication.translate("login", u"Usuario", None))
        self.passLine.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
        self.logButton.setText(QCoreApplication.translate("login", u"Log in", None))
        self.error.setText("")
    # retranslateUi

