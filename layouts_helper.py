import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def configure_default_params(self):
    self.setupUi(self)
    self.setStyle(QtWidgets.QApplication.setStyle("Fusion"))
    # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


def close_event(object, event, title='Quit Warning', message='Are you sure you want to exit this application?'):
    choice = QtWidgets.QMessageBox.question(object, title,
        message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if choice == QtWidgets.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
