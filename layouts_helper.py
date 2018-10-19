import sys

from PyQt5 import QtCore, QtGui, QtWidgets


def configureDefaultParams(self):
    self.setupUi(self)
    self.setStyle(QtWidgets.QApplication.setStyle("Fusion"))

def closeEvent(Object, event, title='Quit Warning', message='Are you sure you want to exit this application?'):
    choice = QtWidgets.QMessageBox.question(Object, title,
        message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if choice == QtWidgets.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()


def which_browser(b):
   return{
       'Mozilla': 'firefox',
       'Chrome': 'google-chrome'
   }.get(b, 'firefox')
