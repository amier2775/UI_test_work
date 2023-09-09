# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 661)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(410, 440, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 510, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(200, 50, 391, 70))
        self.textEdit.setObjectName("textEdit")
        self.LoginButton = QtWidgets.QPushButton(Form)
        self.LoginButton.setGeometry(QtCore.QRect(320, 570, 101, 51))
        self.LoginButton.setObjectName("LoginButton")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 500, 201, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 440, 201, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 130, 541, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("DSC2943_by_kcpru.jpg"))
        self.label.setObjectName("label")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(460, 580, 91, 41))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">欢迎使用铁路12306</span></p></body></html>"))
        self.LoginButton.setText(_translate("Form", "登录"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">密码</p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">用户名</p></body></html>"))
        self.exitButton.setText(_translate("Form", "退出"))

