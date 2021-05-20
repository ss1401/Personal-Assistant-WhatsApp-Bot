import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
#from PyQt5.uic import loadUi
import pandas as pd # pip install pandas
import pyodbc
import attendance_rc

#connection
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-8UVAR6B;"
    "Database=PPAP;"
    "Trusted_Connection=yes;"
)

class Tt(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tt,self).__init__()
        uic.loadUi('UI/attendance.ui', self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Dell\\Downloads', 'CSV (*.csv)')
        #self.filename.setText(fname[0])
        file=fname[0]
        self.browse.setText(file)
        
        df = pd.read_csv(file)

        columns = ['Date', 'Roll_No', 'Slot_ID','Attd']
        
        df_data = df[columns]
        records = df_data.values.tolist()
        print(records)

        """
        cursor=conn.cursor()
        x=len(records)
        for i in range(x):
            cursor.execute("INSERT into Attendance values (?,?,?,?)", (records[i][0],records[i][1],records[i][2],records[i][3]))
            conn.commit()
        """
    
    


gui = QtWidgets.QApplication(sys.argv)
UIwindow = Tt()
UIwindow.show()
#widget=QtWidgets.QStackedWidget()
gui.exec_()