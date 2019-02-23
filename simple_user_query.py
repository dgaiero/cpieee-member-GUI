import ctypes
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

# import configuration_wizard
import layouts_wrapper
from configuration_wizard import ConfigurationWindow
from read_common_config import CommonConfig, NoConfigFoundError
import layouts_helper
from colorama import init as coloramaInit
# from setup_forms import *

def main():
    setup_parameters()
    coloramaInit()
    app = QtWidgets.QApplication(sys.argv)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'logo.png'))
    # query_user_form = layouts_helper.show_query()


    # license_view_dialog = layouts_wrapper.LicenseWindow()
    # license_view_dialog.show()
    login_form = layouts_wrapper.LoginWindow()
    login_form.show()
    sys.exit(app.exec_())

def setup_parameters():
    app_id = 'cpieee.memberconnect.v2.GUI'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True)

if __name__ == "__main__":
    main()
