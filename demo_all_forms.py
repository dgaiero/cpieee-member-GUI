import ctypes
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import layouts_wrapper


def main():

    myappid = 'cpieee.memberconnect.v2.GUI'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    script_dir = os.path.dirname(os.path.realpath(__file__))

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'logo.png'))

    # login_form = layouts_wrapper.LoginWindow()
    # login_form.show()

    # change_password_form = layouts_wrapper.ChangePassowrd()
    # change_password_form.show()

    license_view_dialog = layouts_wrapper.LicenseWindow()
    # license_view_dialog.show()

    query_user_form = layouts_wrapper.QueryUser()
    query_user_form.actionAbout.triggered.connect(license_view_dialog.show)
    query_user_form.show()

    # user_lookup_form = layouts_wrapper.UserLookup()
    # user_lookup_form.show()

    sys.exit(app.exec_())  

if __name__ == '__main__':
    main()
