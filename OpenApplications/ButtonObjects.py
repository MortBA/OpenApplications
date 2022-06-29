from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class ButtonObject(object):
    def __init__(self, appName, appNumber, executeLink):
        self.appName = appName
        self.appNumber = appNumber
        self.executeLink = executeLink

        self = QtWidgets.QPushButton(self.centralwidget)
        self.setGeometry(QtCore.QRect(appNumber*100 + 50 , 100, 100, 100))
        self.setAutoFillBackground(False)
        self.setStyleSheet("border-image : url(logoImages/"+appName+".png);")
        self.clicked.connect(self.execute)

    def execute(self):
        subprocess.Popen(self.executeLink)
