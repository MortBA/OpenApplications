from PyQt5 import QtCore, QtGui, QtWidgets

import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Application Opener")
        MainWindow.resize(800, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QtGui.QIcon('logoImages/programming.png'))

        self.steamButton = QtWidgets.QPushButton(self.centralwidget)
        self.steamButton.setGeometry(QtCore.QRect(50, 100, 100, 100))
        self.steamButton.setAutoFillBackground(False)
        self.steamButton.setStyleSheet("border-image : url(logoImages/steam.png);")
        self.steamButton.clicked.connect(self.steam)

        self.discordButton = QtWidgets.QPushButton(self.centralwidget)
        self.discordButton.setGeometry(QtCore.QRect(200, 100, 100, 100))
        self.discordButton.setAutoFillBackground(False)
        self.discordButton.setStyleSheet("border-image : url(logoImages/discord.png);")
        self.discordButton.clicked.connect(self.discord)

        self.chromeButton = QtWidgets.QPushButton(self.centralwidget)
        self.chromeButton.setGeometry(QtCore.QRect(350, 100, 100, 100))
        self.chromeButton.setAutoFillBackground(False)
        self.chromeButton.setStyleSheet("border-image : url(logoImages/chrome.png);")
        self.chromeButton.clicked.connect(self.chrome)

        self.leagueButton = QtWidgets.QPushButton(self.centralwidget)
        self.leagueButton.setGeometry(QtCore.QRect(500, 100, 100, 100))
        self.leagueButton.setAutoFillBackground(False)
        self.leagueButton.setStyleSheet("border-image : url(logoImages/league.png);")
        self.leagueButton.clicked.connect(self.league)

        self.pycharmButton = QtWidgets.QPushButton(self.centralwidget)
        self.pycharmButton.setGeometry(QtCore.QRect(650, 100, 100, 100))
        self.pycharmButton.setAutoFillBackground(False)
        self.pycharmButton.setStyleSheet("border-image : url(logoImages/pycharm.png);")
        self.pycharmButton.clicked.connect(self.pycharm)



        self.eventLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventLabel.setGeometry(QtCore.QRect(340, 20, 91, 41))
        self.eventLabel.setObjectName("eventLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def discord(self):
        subprocess.Popen("C://Users//burak//AppData//Local//Discord//app-1.0.9005//Discord.exe")
        self.eventLabel.setText("You've Changed!")

    def steam(self):
        subprocess.Popen("L://Steam//steam.exe")
        self.eventLabel.setText("You should not do this!")
        self.eventLabel.adjustSize()

    def chrome(self):
        subprocess.Popen("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")
        self.eventLabel.setText("Chrome Opened!")
        self.eventLabel.adjustSize()

    def league(self):
        subprocess.Popen("L://Steam//Riot Games//Riot Client//RiotClientServices.exe")
        self.eventLabel.setText("League Opened!")
        self.eventLabel.adjustSize()

    def pycharm(self):
        subprocess.Popen("L://Intellij//PyCharm 2022.1.2//bin//pycharm64.exe")
        self.eventLabel.setText("Pycharm Opened!")
        self.eventLabel.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application Opener"))
        self.eventLabel.setText(_translate("MainWindow", "Your Applications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
