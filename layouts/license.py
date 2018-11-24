# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'license.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(702, 505)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(702, 505))
        Dialog.setMaximumSize(QtCore.QSize(702, 505))
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 10, 481, 121))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.licenseText = QtWidgets.QTextBrowser(Dialog)
        self.licenseText.setGeometry(QtCore.QRect(20, 130, 661, 311))
        self.licenseText.setObjectName("licenseText")
        self.visitWebsiteButton = QtWidgets.QPushButton(Dialog)
        self.visitWebsiteButton.setGeometry(QtCore.QRect(580, 460, 101, 20))
        self.visitWebsiteButton.setObjectName("visitWebsiteButton")
        self.viewLicenseOnlineButton = QtWidgets.QPushButton(Dialog)
        self.viewLicenseOnlineButton.setGeometry(QtCore.QRect(430, 460, 141, 20))
        self.viewLicenseOnlineButton.setObjectName("viewLicenseOnlineButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 181, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logoHeaders/image_assets/logo_license_back_small.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label.setText(_translate("Dialog", "The configuration file for this software is not to be redistributed.\n"
"Copyright (C) Cal Poly IEEE Student Branch 2018\n"
"\n"
"Developed and Designed by Dominic Gaiero\n"
"This program is licensed under the GNU General Public License v3.0.\n"
"This license is shown below and is generated from the online version.\n"
"For an online version, click the button below.\n"
"To visit the Cal Poly IEEE Website, click the Visit Website button below. "))
        self.licenseText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Fira Code Medium\'; font-size:10pt;\"><br /></p></body></html>"))
        self.visitWebsiteButton.setText(_translate("Dialog", "Visit website"))
        self.viewLicenseOnlineButton.setText(_translate("Dialog", "View License Online"))

import main_images_rc
