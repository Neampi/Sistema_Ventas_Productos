import sys
from PyQt5.QtCore import Qt
from PySide2.QtWidgets import QWidget, QMainWindow
from db.conexion_sql import Conexion

from views.ui_login import *
from controllers.main_w import *



class loginUsu(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ln=Ui_login()
        self.ln.setupUi(self)
        self.bd=Conexion()

        

        #CONEXION DE BOTONES
        self.ln.logButton.clicked.connect(self.login_activate)
        self.ln.exit_button.clicked.connect(self.salir)
        

    def login_activate(self):
        
        user=self.ln.usuLine.text()
        password=self.ln.passLine.text()

        if len(user)==0 or len(password)==0:
            self.ln.error.setText("Ingrese Datos")
        else:
            try:
                self.funcion=self.bd.inicio_sesion(user, password)
                #CODIGO
                cod=self.funcion[0][0]
                #NOMBRE
                nom=self.funcion[0][4]
                us=self.funcion[0][1]
                ps=self.funcion[0][3]
                #CARGO
                carg=self.funcion[0][9]
                
                if (us==user and ps==password):
                    self.hide()
                    self.pr=principal_process()
                    self.pr.show()
                    self.pr.prin.user_text.setText(us)
                    self.pr.prin.codigo_text.setText(str(cod))
                    self.pr.prin.nombre_text.setText(nom)
                    self.pr.prin.cargo_text.setText(self.bd.cargo_usu(carg))
                    
                    
                
            except Exception:
                self.ln.error.setText("Datos Incorrectos")

        
    def salir(self):
        sys.exit()

        
        
