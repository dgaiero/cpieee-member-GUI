# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 250)
        Dialog.setMinimumSize(QtCore.QSize(430, 200))
        Dialog.setMaximumSize(QtCore.QSize(430, 250))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 411, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.new_password_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.new_password_field.setAutoFillBackground(False)
        self.new_password_field.setObjectName("new_password_field")
        self.gridLayout.addWidget(self.new_password_field, 2, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.old_password_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.old_password_field.setAutoFillBackground(False)
        self.old_password_field.setObjectName("old_password_field")
        self.gridLayout.addWidget(self.old_password_field, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.phone_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.phone_field.setObjectName("phone_field")
        self.gridLayout.addWidget(self.phone_field, 0, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.new_password_field_confirm = QtWidgets.QLineEdit(self.layoutWidget)
        self.new_password_field_confirm.setAutoFillBackground(False)
        self.new_password_field_confirm.setObjectName("new_password_field_confirm")
        self.gridLayout.addWidget(self.new_password_field_confirm, 4, 1, 1, 3)
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_button.setMinimumSize(QtCore.QSize(0, 33))
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 6, 3, 1, 1)
        self.change_password_button = QtWidgets.QPushButton(self.layoutWidget)
        self.change_password_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_password_button.sizePolicy().hasHeightForWidth())
        self.change_password_button.setSizePolicy(sizePolicy)
        self.change_password_button.setMinimumSize(QtCore.QSize(0, 33))
        self.change_password_button.setObjectName("change_password_button")
        self.gridLayout.addWidget(self.change_password_button, 6, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.phone_field, self.old_password_field)
        Dialog.setTabOrder(self.old_password_field, self.new_password_field)
        Dialog.setTabOrder(self.new_password_field, self.new_password_field_confirm)
        Dialog.setTabOrder(self.new_password_field_confirm, self.change_password_button)
        Dialog.setTabOrder(self.change_password_button, self.cancel_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Password"))
        self.new_password_field.setProperty("EchoMode", _translate("Dialog", "Passowrd"))
        self.label.setText(_translate("Dialog", "Phone Number"))
        self.old_password_field.setProperty("EchoMode", _translate("Dialog", "Passowrd"))
        self.label_3.setText(_translate("Dialog", "Old Password"))
        self.label_4.setText(_translate("Dialog", "New Password"))
        self.label_5.setText(_translate("Dialog", "Confirmation"))
        self.new_password_field_confirm.setProperty("EchoMode", _translate("Dialog", "Passowrd"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.change_password_button.setText(_translate("Dialog", "Change Password"))
        self.label_2.setText(_translate("Dialog", "Change Password"))

