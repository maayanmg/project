# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_case.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import calendar_win


class Ui_Report_case(object):
    def setupUi(self, Dialog, client, main_win):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 603)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        Dialog.setModal(True)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.label_7.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 210, 111, 21))
        self.label_9.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 290, 391, 31))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 230, 391, 31))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 331, 71))
        self.label_3.setStyleSheet("background-color: rgb(54,54,54);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 111, 21))
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 330, 181, 21))
        self.label_8.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 170, 391, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 110, 391, 31))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 350, 491, 111))
        self.textEdit.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 540, 171, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(14, 154, 175);\n"
"color: rgb(255,255,255);\n"
"font-size: 18pt\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 470, 301, 21))
        self.label_10.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 12pt")
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 490, 391, 31))
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet("background-color: rgb(197,197,197);\n"
"color: rgb(42, 42, 42);\n"
"font-size: 12pt")
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        widget = QtWidgets.QLineEdit
        widget.mouseDoubleClickEvent = self.open_calendar()
        self.lineEdit_6.mouseDoubleClickEvent

    def open_calendar(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = calendar_win.Ui_Calendar()
        self.ui.setupUi(self.dialog, self)
        self.dialog.show()

    def set_date(self, selected_date):
        self.lineEdit_6.setText(selected_date)

    def report(self, Dialog, client, main_win):
        full_name = self.lineEdit_4.text()
        ID = self.lineEdit_3.text()
        email = self.lineEdit_5.text()
        date = self.lineEdit_6.text()
        description = self.textEdit


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Date:"))
        self.label_9.setText(_translate("Dialog", "Patinet\'s e-mail:"))
        self.label_3.setText(_translate("Dialog", "Report a new case:"))
        self.label_5.setText(_translate("Dialog", "Patient\'s ID:"))
        self.label_8.setText(_translate("Dialog", "Description of the case:"))
        self.label_4.setText(_translate("Dialog", "Patient's full name:"))
        self.pushButton_2.setText(_translate("Dialog", "Submit report"))
        self.label_10.setText(_translate("Dialog", "Add X-ray photo for detection (Optional):"))