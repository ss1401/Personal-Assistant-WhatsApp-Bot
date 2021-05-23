import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
#from PyQt5.uic import loadUi
import pandas as pd # pip install pandas
import pyodbc
import assignment_rc

#connection
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-8UVAR6B;"
    "Database=PPAP;"
    "Trusted_Connection=yes;"
)

class Assignment(QtWidgets.QMainWindow):
    def __init__(self):
        super(Assignment,self).__init__()
        uic.loadUi('UI/assignment.ui', self)
        self.addbutton.clicked.connect(self.Addfunction)

    def Addfunction(self):
        acode = self.acode.text()
        aname = self.aname.text()
        duedate = self.duedate.text()
        subjectname = self.subjectname.text()
        print("Successfully registerd in with acode: ", acode, "and aname:", aname, " duedate:", duedate, " and subname:", subjectname)
        cursor=conn.cursor()
        cursor.execute("INSERT into Assignment values (?,?,?,?)",(acode,aname,duedate,subjectname))
        conn.commit()
    
    
    


gui = QtWidgets.QApplication(sys.argv)
UIwindow = Assignment()
UIwindow.show()
#widget=QtWidgets.QStackedWidget()
gui.exec_()
