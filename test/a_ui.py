# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.goButton = QtWidgets.QPushButton(Form)
        self.goButton.setGeometry(QtCore.QRect(140, 230, 89, 25))
        self.goButton.setObjectName("goButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.goButton.setText(_translate("Form", "PushButton"))

