
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-38, -8, 841, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/black.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.jarvisai = QtWidgets.QLabel(self.centralwidget)
        self.jarvisai.setGeometry(QtCore.QRect(420, 20, 351, 231))
        self.jarvisai.setText("")
        self.jarvisai.setPixmap(QtGui.QPixmap("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/processing.gif"))
        self.jarvisai.setScaledContents(True)
        self.jarvisai.setObjectName("jarvisai")
        self.voice_gui = QtWidgets.QLabel(self.centralwidget)
        self.voice_gui.setGeometry(QtCore.QRect(20, 150, 241, 181))
        self.voice_gui.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.voice_gui.setText("")
        self.voice_gui.setPixmap(QtGui.QPixmap("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/voice.gif"))
        self.voice_gui.setScaledContents(True)
        self.voice_gui.setObjectName("voice_gui")
        self.gif_int = QtWidgets.QLabel(self.centralwidget)
        self.gif_int.setGeometry(QtCore.QRect(10, 10, 311, 121))
        self.gif_int.setText("")
        self.gif_int.setPixmap(QtGui.QPixmap("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/initialize.gif"))
        self.gif_int.setScaledContents(True)
        self.gif_int.setObjectName("gif_int")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(260, 410, 91, 31))
        self.start_btn.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(85, 0, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.start_btn.setObjectName("start_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(360, 410, 91, 31))
        self.exit_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.exit_btn.setObjectName("exit_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 280, 311, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Manan V. Vaishnav/OneDrive/Pictures/project images/lines.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 340, 221, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.textBrowser.setToolTip(_translate("MainWindow", "<html><head/><body><p>time 12:12</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
