"""
    with connect_ldap(authentication=SIMPLE, user=user_dn, password=old_pass) as c:
        c.bind()
        c.extend.standard.modify_password(user_dn, old_pass, new_pass)
"""

import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox

import layouts.configuration
import layouts_helper
import keyring

import ctypes
import os
import sys

# print(__name__)

# class LoginWindow(QtWidgets.QDialog, layouts.login_box.Ui_Dialog):
#     def __init__(self, parent=None):
#         super(LoginWindow, self).__init__(parent)
#         layouts_helper.configure_default_params(self)
#         self.setFixedSize(self.width(), self.height())
#         # self.phone_field.setInputMask('999-999-9999')
#         self.setWindowTitle("Set Admin Bind DN and Password")
#         self.username_label.setText("Admin Bind DN")
#         self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.cancel_button.clicked.connect(self.close)
#         self.options_button.setDisabled(True)
#         self.setSizeGripEnabled(False)
#         self.login_button.clicked.connect(self.set_bind_password_keystore)

#     def closeEvent(self, event, title="Cancel Operations", messgae="Do you really want to cancel this operation?"):
#         layouts_helper.close_event(self, event, title, messgae)

#     def set_bind_password_keystore(self):
#         username = self.username_field.text()
#         password = self.password_field.text()
#         keyring.set_password('LDAP', username, password) #TODO: Change LDAP to a config variable

class ConfigurationWindow(QtWidgets.QWizard, layouts.configuration.Ui_Wizard):
    def __init__(self, parent=None):
        super(ConfigurationWindow, self).__init__(parent)
        layouts_helper.configure_default_params(self)
        self.default_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.field_registration()
        # self.can
        # .clicked.connect(self.close)
        # self.cancel_button.clicked.connect(self.close)

    def closeEvent(self, event, title="Cancel Operations", messgae="Do you really want to cancel this operation?"):
        layouts_helper.close_event(self, event, title, messgae)

    def set_bind_password_keystore(self):
        username = self.username_field.text()
        password = self.password_field.text()
        # TODO: Change LDAP to a config variable
        keyring.set_password('LDAP', username, password)

    def field_registration(self):
        # about wizard page
        # self.about_wizard.registerField("licsen_ack*", self.license_ack)
        # self.about_wizard.registerField("view_license_button*", self.view_license_button)
        self.bind_page.registerField(
            "default_password_field*", self.default_password_field)

    # def isComplete(self, completeStatus):
    #     self.

    # def run_configuration(self):
    #     if ctypes.windll.shell32.IsUserAnAdmin():
    #         # Code of your program here
    #         # open("C:/Program Files/Adobe/test.txt", "w")
    #         # raise NotImplementedError
    #         self.setWindowTitle(
    #             "ADMIN: LDAP Parameter Setup Wizard")
    #         self.show()
    #     else:
    #         # Re-run the program with admin rights
    #         title = 'Elevation Warning'
    #         message = 'Do you want to generate a configuration file for the system or for the user? If you want to generate a configuration file for the system, you will need to provide administartor credentials. Press Yes to generate a system configuration, or No to generate a user configuration.'
    #         choice = QtWidgets.QMessageBox.question(self, title,
    #                                                 message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    #         if choice == QtWidgets.QMessageBox.Yes:
    #             ctypes.windll.shell32.ShellExecuteW(
    #                 None, "runas", sys.executable, __file__, None, 1)
    #         else:
    #             self.show()


# def is_admin():
#     return ctypes.windll.shell32.IsUserAnAdmin()
    # try:
    #     return ctypes.windll.shell32.IsUserAnAdmin()
    # except:
    #     return False

def check_password_in_keystore():
    raise NotImplementedError

class CheckConfigLocation(QtWidgets.QWidget):
    def check_config_event(self, event, title='Elevation Warning', message='Do you want to generate a configuration file for the system or for the user? If you want to generate a configuration file for the system, you will need to provide administartor credentials. Press Yes to generate a system configuration, or No to generate a user configuration.'):
        choice = QtWidgets.QMessageBox.question(self, title,
                                                message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, __file__, None, 1)
        else:
            pass
            



# def main():

#     myappid = 'cpieee.memberconnect.v2.GUI'
#     ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#     script_dir = os.path.dirname(os.path.realpath(__file__))

#     if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#         QtWidgets.QApplication.setAttribute(
#             QtCore.Qt.AA_EnableHighDpiScaling, True)

#     if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#         QtWidgets.QApplication.setAttribute(
#             QtCore.Qt.AA_UseHighDpiPixmaps, True)
#     app = QtWidgets.QApplication(sys.argv)
#     app.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'logo.png'))

    # configuration_wizard = ConfigurationWindow()
    # configuration_wizard.run_configuration()
    # run_configuration(configuration_wizard)

    # if is_admin():
    #     # Code of your program here
    #     # open("C:/Program Files/Adobe/test.txt", "w")
    #     # raise NotImplementedError
    #     configuration_wizard.setWindowTitle("ADMIN: LDAP Parameter Setup Wizard")
    #     configuration_wizard.show()
    # else:
    #     # Re-run the program with admin rights
    #     title = 'Elevation Warning'
    #     message = 'Do you want to generate a configuration file for the system or for the user? If you want to generate a configuration file for the system, you will need to provide administartor credentials. Press Yes to generate a system configuration, or No to generate a user configuration.'
    #     choice = QtWidgets.QMessageBox.question(configuration_wizard, title,
    #             message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    #     if choice == QtWidgets.QMessageBox.Yes:
    #         ctypes.windll.shell32.ShellExecuteW(
    #             None, "runas", sys.executable, __file__, None, 1)
    #     else:
    #         configuration_wizard.show()
    #     # configuration_location = CheckConfigLocation()
    #     # configuration_location.show()


    
    

    # sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()
