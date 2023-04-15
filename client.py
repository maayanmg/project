import socket
import sys

import gui
import login
from login import Ui_LoginD
from PyQt5 import QtCore, QtGui, QtWidgets

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 8080
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
#gui.first()
#login.start()
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_LoginD()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
