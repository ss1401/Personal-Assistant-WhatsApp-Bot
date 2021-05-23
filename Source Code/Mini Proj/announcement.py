import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
#from PyQt5.uic import loadUi
import pandas as pd # pip install pandas
import pyodbc
import announcement_rc


class Announcement(QtWidgets.QMainWindow):
    def __init__(self):
        super(Announcement,self).__init__()
        uic.loadUi('UI/announcement.ui', self)
        self.postbutton.clicked.connect(self.Postfunction)

    def Postfunction(self):
        announcement = self.announcement.text()
        name = self.name.text()
        print("Successfully registerd in with announcement: ", announcement, "and name:", name,)
        


gui = QtWidgets.QApplication(sys.argv)
UIwindow = Announcement()
UIwindow.show()
#widget=QtWidgets.QStackedWidget()
gui.exec_()
