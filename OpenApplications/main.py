from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QButtonGroup
from OpenApplications import ButtonObjects as BO


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 300)
        self.setAcceptDrops(True)
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        self.button_show()
        app.setWindowIcon(QtGui.QIcon('logoImages/programming.png'))
        app.setApplicationName("Application Opener")


    def button_show(self):

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.buttonClicked[int].connect(self.button_clicked)

        self.button = BO.ButtonObject("league", 4.5, "L://Steam//Riot Games//Riot Client//RiotClientServices.exe", self)
        self.buttonGroup.addButton(self.button, 1)

        self.button = BO.ButtonObject("discord", 1.5, "C://Users//burak//AppData//Local//Discord//app-1.0.9005//Discord.exe", self)
        self.buttonGroup.addButton(self.button, 2)

        self.button = BO.ButtonObject("steam", 0, "L://Steam//steam.exe", self)
        self.buttonGroup.addButton(self.button, 3)

        self.button = BO.ButtonObject("chrome", 3, "C://Program Files (x86)//Google//Chrome//Application//chrome.exe", self)
        self.buttonGroup.addButton(self.button, 4)

        self.button = BO.ButtonObject("pycharm", 6, "L://Intellij//PyCharm 2022.1.2//bin//pycharm64.exe", self)
        self.buttonGroup.addButton(self.button, 5)

        self.eventLabel = QtWidgets.QLabel(self)
        self.eventLabel.setGeometry(QtCore.QRect(340, 20, 91, 41))
        self.eventLabel.setObjectName("eventLabel")


    def button_clicked(self, id):
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                button.execute()

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()
        for button in self.buttonGroup.buttons():
                if button.movement == 0:
                    pos = event.pos()
                    button.move(pos)
                    event.setDropAction(Qt.MoveAction)
                    event.accept()
                    button.movement = -1
                    return




app = QApplication(sys.argv)
attempt = AppDemo()
attempt.show()
sys.exit(app.exec_())