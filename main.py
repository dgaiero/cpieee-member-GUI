import ctypes
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

import layouts_wrapper
import configuration_wizard
from configuration_wizard import ConfigurationWindow
from read_common_config import CommonConfig, NoConfigFoundError
# from configuration_wizard import LoginWindow as SetBindPassword


def main():

    setup_parameters()
    app = QtWidgets.QApplication(sys.argv)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'logo.png'))

    try:
        config = CommonConfig()
    except NoConfigFoundError:
        config_wizard = ConfigurationWindow()
        run_configuration(config_wizard)
        

    # login_form = layouts_wrapper.LoginWindow()
    # login_form.show()

    # change_password_form = layouts_wrapper.ChangePassowrd()
    # change_password_form.show()
    

    # license_view_dialog = layouts_wrapper.LicenseWindow()
    # license_view_dialog.show()

    # query_user_form = layouts_wrapper.QueryUser()
    # query_user_form.actionAbout.triggered.connect(license_view_dialog.show)
    # query_user_form.show()

    # user_lookup_form = layouts_wrapper.UserLookup()
    # user_lookup_form.show()

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


def run_configuration(wizard):
        if ctypes.windll.shell32.IsUserAnAdmin():
            # Code of your program here
            # open("C:/Program Files/Adobe/test.txt", "w")
            # raise NotImplementedError
            wizard.setWindowTitle(
                "ADMIN: LDAP Parameter Setup Wizard")
            # wizard.show()
        else:
            # Re-run the program with admin rights
            title = 'Elevation Warning'
            message = 'Do you want to generate a configuration file for the system or for the user? If you want to generate a configuration file for the system, you will need to provide administartor credentials. Press Yes to generate a system configuration, or No to generate a user configuration.'
            choice = QtWidgets.QMessageBox.question(wizard, title,
                                                    message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, __file__, None, 1)
            # else:
            #     wizard.show()
        
        # wizard.NextButton.IsUserAnAdmin
        # wizard.wizardPage_2.registerField("default_password_field*", wizard.default_password_field)
        license_view_dialog = layouts_wrapper.LicenseWindow()
        wizard.show()
        wizard.view_license_button.clicked.connect(license_view_dialog.show)



        # wizard.default_password_field.setValidator(QtGui.QValidator.Invalid)
        # QtGui.QValidator.Invalid
        # wizard.setOptions()
        # wizard.default_password_field.isRe
        # wizard.next()
        
        # print(type(wizard.about_wizard.isComplete()))
        # wizard.setPage(0, wizard.about_wizard)
@pyqtSlot()
def show_window(window):
    print(window)
    # license_view_dialog = layouts_wrapper.LicenseWindow(parent)
    window.show()
    # print("testtetst")

if __name__ == "__main__":
    main()
