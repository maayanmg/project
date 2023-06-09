# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from select_file import Ui_FileD
from sign_up import Ui_SignUpD
import select_file


class Ui_ErrorLoginD(object):
    def setupUi(self, Dialog, ClientMultiSocket, public_key):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 388)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 111))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 28pt ")
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 190, 171, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 140, 171, 31))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 240, 101, 41))
        self.pushButton.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(70, 300, 121, 17))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 320, 91, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog, ClientMultiSocket, public_key)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, ClientMultiSocket, public_key):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login System:"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Username"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.checkBox.setText(_translate("Dialog", "Remember me"))
        self.pushButton_2.setText(_translate("Dialog", "Register"))



        self.pushButton.clicked.connect(lambda: self.open_select_file(ClientMultiSocket, Dialog, public_key))
        self.pushButton_2.clicked.connect(self.open_sign_up)

    def open_select_file(self, ClientMultiSocket, Dialog, public_key):
        Dialog.close()
        print(ClientMultiSocket)
        username = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        message = 'login\r\n' + username + '\r\n' + password
        message = bytes(message, 'utf-8')
        encrypted_message = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("encrypted:  " + str(encrypted_message))
        #print("regular:  " + message)
        ClientMultiSocket.send(encrypted_message)
        res = ClientMultiSocket.recv(1024)


        print(res.decode('utf-8'))
        print(username)
        if not res == 'False':
            self.dialog = QtWidgets.QDialog()
            self.ui = Ui_FileD()
            self.ui.setupUi(self.dialog)
            self.dialog.show()
        else

        #QtCore.QCoreApplication.instance().quit()
        #Dialog.destroy()

    def open_sign_up(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_SignUpD()
        self.ui.setupUi(self.dialog)
        self.dialog.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LoginD()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



def start():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LoginD()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())