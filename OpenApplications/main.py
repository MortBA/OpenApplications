from PyQt5 import QtCore, QtGui, QtWidgets

from OpenApplications import ButtonObjects as BO


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Application Opener")
        MainWindow.resize(800, 300)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QtGui.QIcon('logoImages/programming.png'))

        self.leagueButton = BO.ButtonObject("league", 4.5, "L://Steam//Riot Games//Riot Client//RiotClientServices.exe", self.centralwidget)
        self.leagueButton.clicked.connect(lambda : self.leagueButton.execute())

        self.discordButton = BO.ButtonObject("discord", 1.5, "C://Users//burak//AppData//Local//Discord//app-1.0.9005//Discord.exe", self.centralwidget)
        self.discordButton.clicked.connect(lambda : self.discordButton.execute())

        self.steamButton = BO.ButtonObject("steam", 0, "L://Steam//steam.exe", self.centralwidget)
        self.steamButton.clicked.connect(lambda : self.steamButton.execute())

        self.chromeButton = BO.ButtonObject("chrome", 3, "C://Program Files (x86)//Google//Chrome//Application//chrome.exe", self.centralwidget)
        self.chromeButton.clicked.connect(lambda : self.chromeButton.execute())

        self.pycharmButton = BO.ButtonObject("pycharm", 6, "L://Intellij//PyCharm 2022.1.2//bin//pycharm64.exe", self.centralwidget)
        self.leagueButton.clicked.connect(lambda: self.pycharmButton.execute())

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