from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

from PyQt5.QtWidgets import *


class ButtonObject(QPushButton):
    def __init__(self, appName, appNumber, executeLink, ui):
        super().__init__(ui)

        self.appName = appName
        self.appNumber = appNumber
        self.executeLink = executeLink

        self.setGeometry(QtCore.QRect(appNumber * 100 + 50, 100, 100, 100))
        self.setAutoFillBackground(False)
        self.setStyleSheet("border-image : url(logoImages/" + appName + ".png);")

    def execute(self):
        subprocess.Popen(self.executeLink)