from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import layouts.change_password, layouts.login_box, layouts.query_user
import layouts_helper

class LoginWindow(QtWidgets.QDialog, layouts.login_box.Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyle(QtWidgets.QApplication.setStyle("Fusion"))
        self.setFixedSize(self.width(), self.height())
        self.phone_field.setInputMask('999-999-9999')
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cancel_button.clicked.connect(self.close_application)
        self.setSizeGripEnabled(False)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Quit Warning',
            "Are you sure you want to exit this application?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass



class ChangePassowrd(QtWidgets.QDialog, layouts.change_password.Ui_Dialog):
    def __init__(self, parent=None):
        super(ChangePassowrd, self).__init__(parent)
        self.setupUi(self)

class QueryUser(QtWidgets.QMainWindow, layouts.query_user.Ui_MainWindow):
    def __init__(self, parent=None):
        super(QueryUser, self).__init__(parent)
        self.setupUi(self)
