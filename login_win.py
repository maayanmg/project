# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sign_up_win

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginD(object):
    def setupUi(self, Dialog, ClientMultiSocket):
        Dialog.setObjectName("Dialog")
        Dialog.resize(853, 709)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 220, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 16pt\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 211, 111))
        self.label_2.setStyleSheet("color: rgb(14, 154, 175);\n"
"font-size: 42pt ")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 120, 351, 31))
        self.label_6.setStyleSheet("color: rgb(0, 209, 255);\n"
"font-size: 20pt \n"
"")
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(660, 130, 141, 91))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("books3.png"))
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 170, 151, 61))
        self.pushButton_5.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 170, 151, 61))
        self.pushButton_6.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 170, 151, 61))
        self.pushButton_7.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255,255,255);\n"
"font-size: 14pt\n"
"")
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(520, 30, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo1.png"))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(170, 240, 471, 461))
        self.frame_2.setStyleSheet("background-color: rgb(202,202,202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 441))
        self.frame.setStyleSheet("background-color: rgb(54,54,54);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(70, 240, 131, 17))
        self.checkBox.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 270, 121, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 18pt\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 100, 111, 21))
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 16pt")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 130, 171, 31))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 221, 71))
        self.label_3.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 200, 171, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 170, 111, 21))
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 16pt")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 350, 261, 51))
        self.pushButton_3.setStyleSheet("\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(140, 140, 140);\n"
"font-size: 18pt\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: self.try_login(ClientMultiSocket, Dialog))
        self.pushButton_3.clicked.connect(lambda: self.open_sign_up_win(ClientMultiSocket, Dialog))


    def try_login(self, ClientMultiSocket, Dialog):
        Dialog.close()
        print(ClientMultiSocket)
        username = self.lineEdit_4.text()
        password = self.lineEdit_3.text()
        message = 'login\r\n' + username + '\r\n' + password
        ClientMultiSocket.send(message)
        res = ClientMultiSocket.recv(1024)

        # self.dialog = QtWidgets.QDialog()
        # self.ui = sign_up_win.Ui_Dialog()
        # self.ui.setupUi(self.dialog, ClientMultiSocket)
        # self.dialog.show()

    def open_sign_up_win(self, ClientMultiSocket, Dialog):
        Dialog.close()
        is_connected = False
        if not is_connected:
            self.dialog = QtWidgets.QDialog()
            self.ui = sign_up_win.Ui_Dialog()
            self.ui.setupUi(self.dialog, ClientMultiSocket)
            self.dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Login System"))
        self.label_2.setText(_translate("Dialog", "DeTECh"))
        self.label_6.setText(_translate("Dialog", "Best way to detect disesases"))
        self.pushButton_5.setText(_translate("Dialog", "user history"))
        self.pushButton_6.setText(_translate("Dialog", "about DeTECh"))
        self.pushButton_7.setText(_translate("Dialog", "X-rays detection"))
        self.checkBox.setText(_translate("Dialog", "Remember me"))
        self.pushButton_2.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_3.setText(_translate("Dialog", "Login System:"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.pushButton_3.setText(_translate("Dialog", "First time in the app"))