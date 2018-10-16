from PyQt5 import QtCore, QtGui, QtWidgets
import layouts_wrapper
import sys

def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    login_form = layouts_wrapper.LoginWindow()
    login_form.show()

    change_password_form = layouts_wrapper.ChangePassowrd()
    change_password_form.show()

    query_user_form = layouts_wrapper.QueryUser()
    query_user_form.show()

    app.exec_()

if __name__ == '__main__':
    main()