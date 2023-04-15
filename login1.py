# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Dialog, client, main_win):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 313)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        Dialog.setModal(True)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 471, 461))
        self.frame_2.setStyleSheet("background-color: rgb(202,202,202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 351))
        self.frame.setStyleSheet("background-color: rgb(54,54,54);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 260, 130, 37))
        self.pushButton_3.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 18pt\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 16pt")
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 120, 291, 31))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 221, 71))
        self.label_3.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 190, 291, 31))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 111, 21))
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 16pt")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 221, 21))
        self.label_6.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 230, 221, 21))
        self.label_11.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")

        self.label_6.hide()
        self.label_11.hide()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_3.clicked.connect(lambda: self.try_login(Dialog, client, main_win))

    def try_login(self, Dialog, client, main_win):
        username = self.lineEdit_5.text()
        password = self.lineEdit_6.text()
        if username == '' or password == '':
            self.label_11.show()
            self.label_11.raise_()
            return
        res = client.login(username, password)
        print(res)
        res = client.handle_res(res, "login")
        # res ="True"
        if res != None:
            main_win.turn_into_logged_in_mode(username, res)
            main_win.fill_table(client)
            Dialog.close()
        else:
            self.label_6.show()
            self.label_6.raise_()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "Sign in"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.label_6.setText(_translate("Dialog", "username or password are wrong!"))
        self.label_11.setText(_translate("Dialog", "please fill all the fields!"))
