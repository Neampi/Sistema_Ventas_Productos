import sys
from PySide2 import QtWidgets
from controllers.logi import *

def loguear():
    window=loginUsu()
    return window

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    global lg
    lg=loguear()
    lg.show()
    sys.exit(app.exec_())

