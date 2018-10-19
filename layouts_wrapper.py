import sys
import webbrowser

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox

import layouts.change_password
import layouts.license
import layouts.login_box
import layouts.query_user
import layouts.user_lookup
import layouts_helper


class LoginWindow(QtWidgets.QDialog, layouts.login_box.Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        layouts_helper.configureDefaultParams(self)
        self.setFixedSize(self.width(), self.height())
        self.phone_field.setInputMask('999-999-9999')
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cancel_button.clicked.connect(self.close)
        self.options_button.clicked.connect(self.showOptions)
        self.setSizeGripEnabled(False)

    def closeEvent(self, event, title="Cancel Operations", messgae="Do you really want to cancel this operation?"):
        layouts_helper.closeEvent(self, event, title, messgae)

    def showOptions(self):
        choice = QtWidgets.QMessageBox.question(self, 'Options Information',
            "Options not yet available",
            QtWidgets.QMessageBox.Ok)

class ChangePassowrd(QtWidgets.QDialog, layouts.change_password.Ui_Dialog):
    def __init__(self, parent=None):
        super(ChangePassowrd, self).__init__(parent)
        layouts_helper.configureDefaultParams(self)
        self.phone_field.setInputMask('999-999-9999')
        self.old_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_field_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cancel_button.clicked.connect(self.close)

    def closeEvent(self, event):
        layouts_helper.closeEvent(self, event)

class QueryUser(QtWidgets.QMainWindow, layouts.query_user.Ui_MainWindow):
    def __init__(self, parent=None):
        super(QueryUser, self).__init__(parent)
        layouts_helper.configureDefaultParams(self)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.close)
        # self.actionExit.clicked.connect(self.close)

    def closeEvent(self, event):
        layouts_helper.closeEvent(self, event)

class UserLookup(QtWidgets.QDialog, layouts.user_lookup.Ui_Dialog):
    def __init__(self, parent=None):
        super(UserLookup, self).__init__(parent)
        layouts_helper.configureDefaultParams(self)

class LicenseWindow(QtWidgets.QDialog, layouts.license.Ui_Dialog):
    def __init__(self, parent=None):
        super(LicenseWindow, self).__init__(parent)
        layouts_helper.configureDefaultParams(self)
        self.viewLicenseOnlineButton.clicked.connect(self.viewLicense)
        self.visitWebsiteButton.clicked.connect(self.viewWebsite)
        self.license_url = 'https://raw.githubusercontent.com/dgaiero/cpieee-member-GUI/master/LICENSE'
        license_text = requests.get(self.license_url)

        self.licenseText.setPlainText(license_text.text)

    def viewLicense(self):
        title = "View License"
        message = f"You are about to open the license in your default webrowser.  Do you want to continue?"
        choice = QtWidgets.QMessageBox.question(self, title,
                                                message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            webbrowser.open_new_tab(self.license_url)
        else:
            pass

    def viewWebsite(self):
        title = "View Website"
        message = f"You are about to open the Cal Poly IEEE website in your default webrowser.  Do you want to continue?"
        choice = QtWidgets.QMessageBox.question(self, title,
                                                message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            webbrowser.open_new_tab("https://calpolyieee.com")
        else:
            pass
