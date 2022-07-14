from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QMimeData, Qt


class ButtonObject(QPushButton):
    def __init__(self, appName, appNumber, executeLink, ui):
        super().__init__(ui)

        self.movement = None
        self.appName = appName
        self.appNumber = appNumber
        self.executeLink = executeLink

        self.setGeometry(QtCore.QRect(appNumber * 100 + 50, 100, 100, 100))
        self.setAutoFillBackground(False)
        self.setStyleSheet("border-image : url(logoImages/" + appName + ".png);")

    def execute(self):
        subprocess.Popen(self.executeLink)

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.RightButton:
            return
        if event.buttons() == Qt.RightButton:
            self.movement = 0
        mime_data = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)