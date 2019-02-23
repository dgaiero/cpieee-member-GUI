import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

# import layouts_helper
import layouts_wrapper

global app
global script_dir
global login_form
global query_user_form
global license_view_dialog

app = QtWidgets.QApplication(sys.argv)
script_dir = os.path.dirname(os.path.realpath(__file__))
# app.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'logo.png'))
# layouts_helper.show_query()
# license_view_dialog = layouts_wrapper.LicenseWindow()
login_form = layouts_wrapper.LoginWindow()
query_user_form = layouts_wrapper.QueryUserSimple()
license_view_dialog = layouts_wrapper.LicenseWindow()
# query_user_form.actionAbout.triggered.connect(license_view_dialog.show)
# # query_user_form.show()
# login_form.show()
# login_form.login_button.clicked.connect(login_form.login)
