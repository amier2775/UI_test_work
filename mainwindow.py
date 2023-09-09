import sys
from PyQt5 import QtCore, QtWidgets, QtCore

# 导入 Qt designer 设计的页面
from hello import Ui_Form as Hello_Ui 
from login import Ui_Form as Login_Ui
from operate import Ui_Form as Operate_Ui
# 主窗口
class HelloWindow(QtWidgets.QMainWindow, Hello_Ui):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号
    switch_window2 = QtCore.pyqtSignal() # 跳转信号
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)
        self.operateButton.clicked.connect(self.goOperate)
        self.LoginButton.clicked.connect(self.goLogin)
    def goLogin(self):
        self.switch_window1.emit()
    def goOperate(self):
        self.switch_window2.emit()

# 登录窗口
class LoginWindow(QtWidgets.QMainWindow, Login_Ui):
    switch_window = QtCore.pyqtSignal() # 跳转信号
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exitHello)
        
    def exitHello(self):
        self.switch_window.emit()
    

# 操作窗口
class OperateWindow(QtWidgets.QMainWindow, Operate_Ui):
    switch_window = QtCore.pyqtSignal() # 跳转信号
    def __init__(self):
        super(OperateWindow, self).__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exitHello)
        
    def exitHello(self):
        self.switch_window.emit()
# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到 hello 窗口
    def show_hello(self):
        self.hello = HelloWindow()
        self.login = LoginWindow()
        self.operate = OperateWindow()
        self.login.close()
        self.operate.close()
        self.hello.switch_window1.connect(self.show_login)
        self.hello.switch_window2.connect(self.show_operate)
        self.hello.show()
    # 跳转到 login 窗口, 注意关闭原页面
    def show_login(self):
        
        self.login.switch_window.connect(self.show_hello)
        self.hello.close()
        self.login.show()
    # 跳转到 operate 窗口, 注意关闭原页面
    def show_operate(self):
        
        self.operate.switch_window.connect(self.show_hello)
        self.hello.close()
        self.operate.show()
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller() 
    controller.show_hello()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
