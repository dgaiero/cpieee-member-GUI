# import sys
import datetime
import webbrowser

import requests
from ansi2html import Ansi2HTMLConverter
from colorama import Back, Fore, Style
from PyQt5 import QtCore, QtWidgets
import PyQt5.QtGui as QtGui
# from PyQt5.QtWidgets import QDialogButtonBox, QMessageBox

import layouts.change_password
import layouts.license
import layouts.login_box
import layouts.query_user
import layouts.query_user_simple
import layouts.user_lookup
import layouts_helper
import login_actions

# from colorama import init as coloramaInit

processes = set([])
TIME_UNTIL_LOGOUT = 3600 # 3600


class LoginWindow(QtWidgets.QDialog, layouts.login_box.Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        layouts_helper.configure_default_params(self)
        self.setFixedSize(self.width(), self.height())
        self.username_field.setInputMask('999-999-9999')
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cancel_button.clicked.connect(self.close)
        self.options_button.clicked.connect(self.showOptions)
        self.setSizeGripEnabled(False)
        self.login_button.setEnabled(False)
        self.password_field.textChanged.connect(self.enable_login_button)
        self.username_field.textChanged.connect(self.enable_login_button)
        self.login_button.clicked.connect(self.login)
        # if ((self.password_field.text() == "") or (self.username_field.text() == "")):
        #     self.login_button.setDisabled(True)

    def closeEvent(self, event, title="Cancel Operations", messgae="Do you really want to cancel this operation?"):
        layouts_helper.close_event(self, event, title, messgae)

    def showOptions(self):
        choice = QtWidgets.QMessageBox.question(self, 'Options Information',
                                                "Options not yet available",
                                                QtWidgets.QMessageBox.Ok)

    def login(self):
        # login_actions.bind_user(
        #     self.username_field.text(), self.password_field.text())
        self.login_button.setDisabled(True)
        self.cancel_button.setDisabled(True)
        self.options_button.setDisabled(True)
        success = True
        try:
            ldap_user = login_actions.bind_user(
                self.username_field.text(), self.password_field.text())
        except login_actions.PhoneNumberNotFoundException as e:
            self.password_field.setText("")
            self.username_field.setText("")
            self.username_field.setFocus()
            extended_text = f"The phone number: {e.phone_number} was not found."
            layouts_helper.show_dialog_detailed_text(
                self, "Error", f"Error: {e.message}", "", extended_text)
            self.login_button.setEnabled(True)
            self.cancel_button.setEnabled(True)
            self.options_button.setEnabled(True)
            success = False
        except login_actions.LoginErrorException as e:
            print("LoginErrorException")
            self.password_field.setText("")
            self.password_field.setFocus()
            extended_text = f"Error Code: {e.errors['result']}\nDescription: {e.errors['description']}"
            layouts_helper.show_dialog_detailed_text(
                self, "Error", f"Error: {e.message}", "", extended_text)
            self.login_button.setEnabled(True)
            self.cancel_button.setEnabled(True)
            self.options_button.setEnabled(True)
            success = False
        if success:
            print("Showing query form")
            # self.hide()
            query_user_form = layouts_helper.show_query(ldap_user)
            processes.add(query_user_form)
            self.hide()

    def enable_login_button(self):
        self.login_button.setEnabled(
            self.password_field.text() != "" and self.username_field.text() != "")


class ChangePassowrd(QtWidgets.QDialog, layouts.change_password.Ui_Dialog):
    def __init__(self, parent=None):
        super(ChangePassowrd, self).__init__(parent)
        layouts_helper.configure_default_params(self)
        self.phone_field.setInputMask('999-999-9999')
        self.old_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_field_confirm.setEchoMode(
            QtWidgets.QLineEdit.Password)
        self.cancel_button.clicked.connect(self.close)

    def closeEvent(self, event):
        layouts_helper.close_event(self, event)


class QueryUser(QtWidgets.QMainWindow, layouts.query_user.Ui_MainWindow):
    def __init__(self, parent=None):
        super(QueryUser, self).__init__(parent)
        layouts_helper.configure_default_params(self)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.close)

    def closeEvent(self, event):
        layouts_helper.close_event(self, event)


# def timerEvent():
#     global time
#     time = time.addSecs(1)
#     print(time.toString("hh:mm:ss"))

class QueryUserSimple(QtWidgets.QMainWindow, layouts.query_user_simple.Ui_QueryUserSimple):
    def __init__(self, ldap_user, parent=None):
        super(QueryUserSimple, self).__init__(parent)
        layouts_helper.configure_default_params(self)
        self.ldap = ldap_user
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.close)
        # self.member_since_field.setDisabled(True)
        self.export_query.setDisabled(True)
        self.query_user.setEnabled(False)
        self.first_name_field.textChanged.connect(
            self.enable_query_button)
        self.last_name_field.textChanged.connect(
            self.enable_query_button)
        self.email_field.textChanged.connect(
            self.enable_query_button)
        self.login_user_text = QtWidgets.QLabel(self.layoutWidget)
        self.login_user_text.setObjectName("login_user_text")
        self.login_user_text.setText(
            f"Authenticated as: {self.ldap.bind_user}")
        self.statusBar.addPermanentWidget(self.login_user_text, 1)
        self.time_in_session = QtWidgets.QLabel(self.layoutWidget)
        self.time_in_session.setObjectName("time_in_session")
        self.time_in_session.setText("Time left in session: {time_in_session}")
        self.time_in_session.setAlignment(QtCore.Qt.AlignRight)
        self.statusBar.addPermanentWidget(self.time_in_session, 1)
        license_view_dialog = LicenseWindow()
        processes.add(license_view_dialog)
        # print(license_view_dialog)
        # license_view_dialog.show()
        self.actionAbout.triggered.connect(license_view_dialog.show)
        self.actionLogout.triggered.connect(self.logout)
        self.query_user.clicked.connect(self.query)
        self.timer_start_logout()
        self.update_time_left()
        self.first_name_field.installEventFilter(self)
        self.last_name_field.installEventFilter(self)
        self.email_field.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress):
            key = event.key()
            if (key == QtCore.Qt.Key_Return):
                self.query()
        return QtWidgets.QMainWindow.eventFilter(self, source, event)

    def closeEvent(self, event):
        layouts_helper.close_event(self, event)

    def enable_query_button(self):
        self.query_user.setEnabled(
            self.first_name_field.text() != "" or
            self.last_name_field.text() != "" or
            self.email_field.text() != "")

    def timer_start_logout(self):
        self.time_until_logout_int = TIME_UNTIL_LOGOUT

        self.timer_logout = QtCore.QTimer(self)
        self.timer_logout.timeout.connect(self.logout_timer_timeout)
        self.timer_logout.start(1000)

        self.update_time_left()

    def logout_timer_timeout(self):
        self.time_until_logout_int -= 1
        self.time_check()
        self.update_time_left()
        

    def time_check(self):
        extend_session_flag = False
        if self.time_until_logout_int == 0:
            logout_action = layouts_helper.show_dialog_detailed_text(
                self, "Expired Session", "Expired Session.", "You must login again if you need to extend your session.", "Your session has expired. Press any button to logout.", icon=QtWidgets.QMessageBox.Information)
            if logout_action == QtWidgets.QMessageBox.Ok:
                self.timer_logout.stop()
                self.logout()
            else:
                self.timer_logout.stop()
                self.logout()
        elif self.time_until_logout_int == 900:  # 900
            if not(extend_session_flag):
                extend_session_action = layouts_helper.show_dialog_non_informative_text(
                    self, "Session Information", "Your session is about to expire.", "Do you want to extend your session by 15 minutes?", buttons=QtWidgets.QMessageBox.Yes |
                    QtWidgets.QMessageBox.No, icon=QtWidgets.QMessageBox.Information)
                if extend_session_action == QtWidgets.QMessageBox.Yes:
                    self.time_until_logout_int += 5
                else:
                    pass
                extend_session_flag = True
        # self.update_time_left()

    def update_time_left(self):
        self.time_in_session.setText(
            f"Time left in session: {str(datetime.timedelta(seconds=self.time_until_logout_int))}")

    def logout(self):
        self.ldap.unbind()
        self.hide()
        login_window = LoginWindow()
        processes.add(login_window)
        login_window.show()

    def query(self):
        first_name = self.first_name_field.text()
        last_name = self.last_name_field.text()
        email = self.email_field.text()
        search_parameters = []
        if first_name != "":
            search_parameters.append(f"(givenName={first_name}*)")
        if last_name != "":
            search_parameters.append(f"(sn={last_name}*)")
        if email != "":
            search_parameters.append(f"(mail={email}*)")
        inner_search_string = ""
        # inner_search_string.join
        for search_parameter in search_parameters:
            inner_search_string += search_parameter
        search_string = (f"(&(ObjectClass=ieeeUser)(|{inner_search_string}))")
        print("Search Query: " + search_string)

        search_result = self.ldap.search(search_string)
        search_print = ""
        if len(search_result) > 0:
            for user in search_result:
                user_data = user.entry_attributes_as_dict
                if "cn=activeMembers,dc=calpolyieee,dc=com" in user_data['member']:
                    status = Back.GREEN + Fore.BLACK + "ACTIVE" + Style.RESET_ALL
                elif "cn=arrearsMembers,dc=calpolyieee,dc=com" in user_data["member"]:
                    status = Back.RED + "ARREARS" + Style.RESET_ALL
                elif "cn=inactiveMembers,dc=calpolyieee,dc=com" in user_data["member"]:
                    status = Back.RED + "INACTIVE" + Style.RESET_ALL
                else:
                    status = Back.RED + "UNKNOWN"
                first_name = user_data["displayName"][0]
                email_address = user_data["mail"][0]
                member_number = user_data["ieeeMemberNumber"][0]
                search_print += f"{Back.CYAN}{Fore.BLACK}  NAME:{Style.RESET_ALL} {first_name}\n"
                search_print += f"{Back.CYAN}{Fore.BLACK} EMAIL:{Style.RESET_ALL} {email_address.upper()}\n"
                search_print += f"{Back.CYAN}{Fore.BLACK}MBR NO:{Style.RESET_ALL} {member_number}\n"
                search_print += f"{Back.CYAN}{Fore.BLACK}STATUS:{Style.RESET_ALL} {status}\n"
                search_print += "                " + Style.RESET_ALL + "\n"
        else:
            search_print += "NO RESULT FOUND."
        
        # search_print_html = ascii
        print("Query Result: \n" + search_print)
        conv = Ansi2HTMLConverter()
        ansi = search_print
        html = conv.convert(ansi)
        self.data_view.setHtml(html)


        
class UserLookup(QtWidgets.QDialog, layouts.user_lookup.Ui_Dialog):
    def __init__(self, parent=None):
        super(UserLookup, self).__init__(parent)
        layouts_helper.configure_default_params(self)


class LicenseWindow(QtWidgets.QDialog, layouts.license.Ui_Dialog):
    def __init__(self, parent=None):
        super(LicenseWindow, self).__init__(parent)
        layouts_helper.configure_default_params(self)
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

    def viewWebsite(self):
        title = "View Website"
        message = f"You are about to open the Cal Poly IEEE website in your default webrowser.  Do you want to continue?"
        choice = QtWidgets.QMessageBox.question(self, title,
                                                message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            webbrowser.open_new_tab("https://calpolyieee.com")

    # def show(self):
    #     self.show()
