# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.resize(811, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Wizard.sizePolicy().hasHeightForWidth())
        Wizard.setSizePolicy(sizePolicy)
        self.about_wizard = QtWidgets.QWizardPage()
        self.about_wizard.setObjectName("about_wizard")
        self.information_text = QtWidgets.QLabel(self.about_wizard)
        self.information_text.setGeometry(QtCore.QRect(0, 10, 771, 71))
        self.information_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.information_text.setWordWrap(True)
        self.information_text.setObjectName("information_text")
        self.view_license_button = QtWidgets.QPushButton(self.about_wizard)
        self.view_license_button.setGeometry(QtCore.QRect(640, 180, 131, 31))
        self.view_license_button.setObjectName("view_license_button")
        self.license_ack = QtWidgets.QCheckBox(self.about_wizard)
        self.license_ack.setGeometry(QtCore.QRect(640, 220, 131, 16))
        self.license_ack.setCheckable(False)
        self.license_ack.setObjectName("license_ack")
        Wizard.addPage(self.about_wizard)
        self.load_configuration = QtWidgets.QWizardPage()
        self.load_configuration.setObjectName("load_configuration")
        self.load_configration_label = QtWidgets.QLabel(self.load_configuration)
        self.load_configration_label.setGeometry(QtCore.QRect(0, 0, 771, 131))
        self.load_configration_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.load_configration_label.setWordWrap(True)
        self.load_configration_label.setObjectName("load_configration_label")
        self.load_configuration_button = QtWidgets.QPushButton(self.load_configuration)
        self.load_configuration_button.setGeometry(QtCore.QRect(640, 180, 131, 31))
        self.load_configuration_button.setObjectName("load_configuration_button")
        Wizard.addPage(self.load_configuration)
        self.set_ldap_parameters = QtWidgets.QWizardPage()
        self.set_ldap_parameters.setObjectName("set_ldap_parameters")
        self.ldap_server_hostname_label = QtWidgets.QLabel(self.set_ldap_parameters)
        self.ldap_server_hostname_label.setGeometry(QtCore.QRect(1, 1, 132, 16))
        self.ldap_server_hostname_label.setObjectName("ldap_server_hostname_label")
        self.ldap_server_hostname_field = QtWidgets.QLineEdit(self.set_ldap_parameters)
        self.ldap_server_hostname_field.setGeometry(QtCore.QRect(1, 20, 261, 31))
        self.ldap_server_hostname_field.setObjectName("ldap_server_hostname_field")
        self.port_field = QtWidgets.QLineEdit(self.set_ldap_parameters)
        self.port_field.setGeometry(QtCore.QRect(270, 20, 41, 31))
        self.port_field.setObjectName("port_field")
        self.port_label = QtWidgets.QLabel(self.set_ldap_parameters)
        self.port_label.setGeometry(QtCore.QRect(270, 1, 27, 16))
        self.port_label.setObjectName("port_label")
        self.default_search_base_field = QtWidgets.QLineEdit(self.set_ldap_parameters)
        self.default_search_base_field.setGeometry(QtCore.QRect(1, 73, 261, 31))
        self.default_search_base_field.setObjectName("default_search_base_field")
        self.search_base_label = QtWidgets.QLabel(self.set_ldap_parameters)
        self.search_base_label.setGeometry(QtCore.QRect(1, 54, 126, 16))
        self.search_base_label.setObjectName("search_base_label")
        self.search_filte_label = QtWidgets.QLabel(self.set_ldap_parameters)
        self.search_filte_label.setGeometry(QtCore.QRect(0, 111, 126, 16))
        self.search_filte_label.setObjectName("search_filte_label")
        self.search_filter_field = QtWidgets.QLineEdit(self.set_ldap_parameters)
        self.search_filter_field.setGeometry(QtCore.QRect(0, 130, 261, 31))
        self.search_filter_field.setObjectName("search_filter_field")
        Wizard.addPage(self.set_ldap_parameters)
        self.bind_page = QtWidgets.QWizardPage()
        self.bind_page.setObjectName("bind_page")
        self.default_password_label = QtWidgets.QLabel(self.bind_page)
        self.default_password_label.setGeometry(QtCore.QRect(0, 50, 126, 16))
        self.default_password_label.setObjectName("default_password_label")
        self.default_password_field = QtWidgets.QLineEdit(self.bind_page)
        self.default_password_field.setGeometry(QtCore.QRect(0, 69, 261, 31))
        self.default_password_field.setObjectName("default_password_field")
        self.default_bind_field = QtWidgets.QLineEdit(self.bind_page)
        self.default_bind_field.setGeometry(QtCore.QRect(0, 19, 261, 31))
        self.default_bind_field.setFrame(True)
        self.default_bind_field.setObjectName("default_bind_field")
        self.default_bind_label = QtWidgets.QLabel(self.bind_page)
        self.default_bind_label.setGeometry(QtCore.QRect(0, 0, 132, 16))
        self.default_bind_label.setObjectName("default_bind_label")
        Wizard.addPage(self.bind_page)
        self.connection_status_page = QtWidgets.QWizardPage()
        self.connection_status_page.setObjectName("connection_status_page")
        self.connection_status_image = QtWidgets.QLabel(self.connection_status_page)
        self.connection_status_image.setGeometry(QtCore.QRect(30, 20, 16, 16))
        self.connection_status_image.setText("")
        self.connection_status_image.setPixmap(QtGui.QPixmap(":/generalAssets/image_assets/success_small.png"))
        self.connection_status_image.setScaledContents(True)
        self.connection_status_image.setObjectName("connection_status_image")
        self.connection_status_short_info = QtWidgets.QLabel(self.connection_status_page)
        self.connection_status_short_info.setGeometry(QtCore.QRect(50, 20, 451, 16))
        self.connection_status_short_info.setObjectName("connection_status_short_info")
        self.more_information_text = QtWidgets.QTextBrowser(self.connection_status_page)
        self.more_information_text.setGeometry(QtCore.QRect(35, 50, 691, 181))
        self.more_information_text.setObjectName("more_information_text")
        Wizard.addPage(self.connection_status_page)
        self.parameters_to_show_page = QtWidgets.QWizardPage()
        self.parameters_to_show_page.setObjectName("parameters_to_show_page")
        self.fields_to_show_label = QtWidgets.QLabel(self.parameters_to_show_page)
        self.fields_to_show_label.setGeometry(QtCore.QRect(10, 11, 211, 16))
        self.fields_to_show_label.setObjectName("fields_to_show_label")
        self.fields_to_show_description = QtWidgets.QTextBrowser(self.parameters_to_show_page)
        self.fields_to_show_description.setGeometry(QtCore.QRect(550, 30, 211, 231))
        self.fields_to_show_description.setObjectName("fields_to_show_description")
        self.paramter_edit = QtWidgets.QTextEdit(self.parameters_to_show_page)
        self.paramter_edit.setGeometry(QtCore.QRect(0, 30, 541, 271))
        self.paramter_edit.setObjectName("paramter_edit")
        self.update_preview_button = QtWidgets.QPushButton(self.parameters_to_show_page)
        self.update_preview_button.setGeometry(QtCore.QRect(550, 270, 211, 31))
        self.update_preview_button.setObjectName("update_preview_button")
        Wizard.addPage(self.parameters_to_show_page)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "LDAP Parameter Setup Wizard"))
        self.information_text.setText(_translate("Wizard", "Welcome to the Cal Poly IEEE LDAP connection and configuration wizard. This wizard will  setup the default parameters required to connect to the LDAP member server.\n"
"\n"
"This wizard will only run if a configuration file is not found in the installation directory. If you would like to load an existing configuration file, please click the load configuration button on the next page.\n"
"\n"
"To use this application, you must agree to the license. Press the \'View License\" button below to view, accept, and acknowledge the license for this application."))
        self.view_license_button.setText(_translate("Wizard", "View License"))
        self.license_ack.setText(_translate("Wizard", "I acknowledge the License"))
        self.load_configration_label.setText(_translate("Wizard", "If you have a configuration file that you would like to load, click the \"Load Configuration\" button below. This will autopopulate the fields on the next pages of this wizard.\n"
"\n"
"If you do not have a configuration file and would like to setup this terminal for the first time, click \"Next\"."))
        self.load_configuration_button.setText(_translate("Wizard", "Load Configuration"))
        self.ldap_server_hostname_label.setText(_translate("Wizard", "LDAP Server Hostname"))
        self.port_field.setInputMask(_translate("Wizard", "999"))
        self.port_field.setText(_translate("Wizard", "389"))
        self.port_label.setText(_translate("Wizard", "Port"))
        self.search_base_label.setText(_translate("Wizard", "Default Search Base"))
        self.search_filte_label.setText(_translate("Wizard", "Search Filter"))
        self.default_password_label.setText(_translate("Wizard", "Password"))
        self.default_bind_label.setText(_translate("Wizard", "Default BIND DN"))
        self.connection_status_short_info.setText(_translate("Wizard", "Connection to LDAP server <<ldap.server.hostname>> was successful."))
        self.fields_to_show_label.setText(_translate("Wizard", "Fields to Show in Table"))
        self.fields_to_show_description.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt;\">Input parameter data as RFC 4627 JSON. An example is shown in the text area to the left. It is also duplicated below for reference. Certain parameters that are not in the LDAP system can be inputted, and their value will be calculated based off of the values placed in NLDAP.</span></p></body></html>"))
        self.paramter_edit.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">   {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">      &quot;LDAP_parameters&quot;:[</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Attribute Name&quot;:&quot;givenName&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Friendly Name&quot;:&quot;First Name&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         },</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Attribute Name&quot;:&quot;surname&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Friendly Name&quot;:&quot;Last Name&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         },</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Attribute Name&quot;:&quot;mail&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Friendly Name&quot;:&quot;Email&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         },</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Attribute Name&quot;:&quot;[NLDAP]status&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;Friendly Name&quot;:&quot;Status&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">      ],</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">      &quot;NLDAP&quot;:[</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;active_field&quot;:&quot;ieeeExpiration&quot;,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            &quot;member_field&quot;:&quot;member&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">      ]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">   }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">]</span></p></body></html>"))
        self.update_preview_button.setText(_translate("Wizard", "Update Preview"))

import main_images_rc
