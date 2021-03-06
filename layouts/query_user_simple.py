# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_user_simple.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QueryUserSimple(object):
    def setupUi(self, QueryUserSimple):
        QueryUserSimple.setObjectName("QueryUserSimple")
        QueryUserSimple.resize(800, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QueryUserSimple.sizePolicy().hasHeightForWidth())
        QueryUserSimple.setSizePolicy(sizePolicy)
        QueryUserSimple.setMinimumSize(QtCore.QSize(800, 330))
        QueryUserSimple.setMaximumSize(QtCore.QSize(800, 330))
        QueryUserSimple.setDocumentMode(False)
        QueryUserSimple.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(QueryUserSimple)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 271))
        self.groupBox.setObjectName("groupBox")
        self.query_user = QtWidgets.QPushButton(self.groupBox)
        self.query_user.setGeometry(QtCore.QRect(100, 240, 91, 23))
        self.query_user.setAutoDefault(True)
        self.query_user.setDefault(True)
        self.query_user.setObjectName("query_user")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.label_4.setObjectName("label_4")
        self.export_query = QtWidgets.QPushButton(self.groupBox)
        self.export_query.setGeometry(QtCore.QRect(10, 240, 81, 23))
        self.export_query.setObjectName("export_query")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 76, 181, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.first_name_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.first_name_field.setObjectName("first_name_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.first_name_field)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.last_name_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.last_name_field.setObjectName("last_name_field")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.last_name_field)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.email_field = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_field.setObjectName("email_field")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.email_field)
        self.data_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.data_view.setGeometry(QtCore.QRect(215, 11, 581, 271))
        self.data_view.setObjectName("data_view")
        QueryUserSimple.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(QueryUserSimple)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        self.viewHelp = QtWidgets.QMenu(self.menuBar)
        self.viewHelp.setObjectName("viewHelp")
        QueryUserSimple.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(QueryUserSimple)
        self.statusBar.setObjectName("statusBar")
        QueryUserSimple.setStatusBar(self.statusBar)
        self.actionLogout = QtWidgets.QAction(QueryUserSimple)
        self.actionLogout.setObjectName("actionLogout")
        self.actionExit = QtWidgets.QAction(QueryUserSimple)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(QueryUserSimple)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOptions.addAction(self.actionLogout)
        self.menuOptions.addAction(self.actionExit)
        self.viewHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.viewHelp.menuAction())

        self.retranslateUi(QueryUserSimple)
        QtCore.QMetaObject.connectSlotsByName(QueryUserSimple)
        QueryUserSimple.setTabOrder(self.first_name_field, self.last_name_field)
        QueryUserSimple.setTabOrder(self.last_name_field, self.email_field)
        QueryUserSimple.setTabOrder(self.email_field, self.export_query)
        QueryUserSimple.setTabOrder(self.export_query, self.query_user)
        QueryUserSimple.setTabOrder(self.query_user, self.data_view)

    def retranslateUi(self, QueryUserSimple):
        _translate = QtCore.QCoreApplication.translate
        QueryUserSimple.setWindowTitle(_translate("QueryUserSimple", "User Query"))
        self.groupBox.setTitle(_translate("QueryUserSimple", "Query Parameters"))
        self.query_user.setText(_translate("QueryUserSimple", "Query"))
        self.label_4.setText(_translate("QueryUserSimple", "The query is set as:\n"
"(fieldAttribute=textEntered*).\n"
"You may enter the first part of\n"
"any parameter"))
        self.export_query.setText(_translate("QueryUserSimple", "Export"))
        self.label.setText(_translate("QueryUserSimple", "First Name"))
        self.label_2.setText(_translate("QueryUserSimple", "Last Name"))
        self.label_3.setText(_translate("QueryUserSimple", "Email"))
        self.menuOptions.setTitle(_translate("QueryUserSimple", "Options"))
        self.viewHelp.setTitle(_translate("QueryUserSimple", "Help"))
        self.actionLogout.setText(_translate("QueryUserSimple", "Logout"))
        self.actionExit.setText(_translate("QueryUserSimple", "Exit"))
        self.actionAbout.setText(_translate("QueryUserSimple", "About"))

