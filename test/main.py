from a_ui import Ui_MainWindow as A_Ui # a界面的库
from b_ui import Ui_MainWindow as B_Ui # b界面的库

from PyQt5 import QtCore, QtWidgets
import sys

class AUi(QtWidgets.QMainWindow, A_Ui):
    def __init__(self):
        super(AUi, self).__init__()
        self.setupUi(self)

class BUi(QtWidgets.QMainWindow, B_Ui):
    def __init__(self):
        super(BUi, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = AUi()
    a.show()
    b = BUi()
    # button是你定义的按钮
    a.goButton.clicked.connect(
    	lambda:{a.close(), b.show()}
   	)
    sys.exit(app.exec_())
