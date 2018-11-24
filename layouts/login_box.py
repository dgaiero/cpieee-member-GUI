# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_box.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(430, 209)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(430, 204))
        Dialog.setBaseSize(QtCore.QSize(430, 200))
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 431, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logoHeaders/image_assets/header_background_logo.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 411, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.username_label = QtWidgets.QLabel(self.layoutWidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)
        self.username_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_field.setObjectName("username_field")
        self.gridLayout.addWidget(self.username_field, 0, 1, 1, 3)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)
        self.password_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_field.setAutoFillBackground(False)
        self.password_field.setObjectName("password_field")
        self.gridLayout.addWidget(self.password_field, 1, 1, 1, 3)
        self.login_button = QtWidgets.QPushButton(self.layoutWidget)
        self.login_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 2, 1, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 2, 2, 1, 1)
        self.options_button = QtWidgets.QPushButton(self.layoutWidget)
        self.options_button.setObjectName("options_button")
        self.gridLayout.addWidget(self.options_button, 2, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.username_field, self.password_field)
        Dialog.setTabOrder(self.password_field, self.login_button)
        Dialog.setTabOrder(self.login_button, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.options_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OIC Login"))
        self.username_label.setText(_translate("Dialog", "Phone Number"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.password_field.setProperty("EchoMode", _translate("Dialog", "Passowrd"))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.options_button.setText(_translate("Dialog", "Options"))

import main_images_rc
