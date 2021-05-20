import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
import pyodbc
import timetable_rc

conn=pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-8UVAR6B;"
                "Database=PPAP;"
                "Trusted_Connection=yes;"
            ) #connection

cursor=conn.cursor()


class MainWindow(QtWidgets.QMainWindow):

    
    def __init__(self):
            super(MainWindow,self).__init__()
            uic.loadUi('UI/timetable.ui', self)
            show=self.ShowTT()
            self.searchbutton.clicked.connect(self.Searchfunction)
            self.updatebutton.clicked.connect(self.Updatefunction)


    
    def Searchfunction(self):
            slot=self.slot.text()
            lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=(?)",(slot))
            lec_slot_list=lec_slot.fetchall()
            self.subject.setText(lec_slot_list[0][0])
            
            lec_link=cursor.execute("select Link from Lecture_Slot where Slot_ID=(?)",(slot))
            lec_link_list=lec_link.fetchall()
            self.link.setText(lec_link_list[0][0])
    
    
    def Updatefunction(self):
        slot=self.slot.text()
        link = self.link.text()
        subject = self.subject.text()
        up1=cursor.execute("update Lecture_Slot set Subject_Name = (?) where Slot_ID= (?)",(subject,slot))
        up2=cursor.execute("update Lecture_Slot set Link = (?) where Slot_ID= (?)",(link,slot))
        conn.commit()
        self.ShowTT()
        


    def ShowTT(self):        
        
        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=1")
        lec_slot_list=lec_slot.fetchall()
        self.l1.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=2")
        lec_slot_list=lec_slot.fetchall()
        self.l2.setText(lec_slot_list[0][0])
        
        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=3")
        lec_slot_list=lec_slot.fetchall()
        self.l3.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=4")
        lec_slot_list=lec_slot.fetchall()
        self.l4.setText(lec_slot_list[0][0])

        
        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=5")
        lec_slot_list=lec_slot.fetchall()
        self.l5.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=6")
        lec_slot_list=lec_slot.fetchall()
        self.l6.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=7")
        lec_slot_list=lec_slot.fetchall()
        self.l7.setText(lec_slot_list[0][0])
        
        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=8")
        lec_slot_list=lec_slot.fetchall()
        self.l8.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=9")
        lec_slot_list=lec_slot.fetchall()
        self.l9.setText(lec_slot_list[0][0])
        
        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=10")
        lec_slot_list=lec_slot.fetchall()
        self.l10.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=11")
        lec_slot_list=lec_slot.fetchall()
        self.l11.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=12")
        lec_slot_list=lec_slot.fetchall()
        self.l12.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=13")
        lec_slot_list=lec_slot.fetchall()
        self.l13.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=14")
        lec_slot_list=lec_slot.fetchall()
        self.l14.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=15")
        lec_slot_list=lec_slot.fetchall()
        self.l15.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=16")
        lec_slot_list=lec_slot.fetchall()
        self.l16.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=17")
        lec_slot_list=lec_slot.fetchall()
        self.l17.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=18")
        lec_slot_list=lec_slot.fetchall()
        self.l18.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=19")
        lec_slot_list=lec_slot.fetchall()
        self.l19.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=20")
        lec_slot_list=lec_slot.fetchall()
        self.l20.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=21")
        lec_slot_list=lec_slot.fetchall()
        self.l21.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=22")
        lec_slot_list=lec_slot.fetchall()
        self.l22.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=23")
        lec_slot_list=lec_slot.fetchall()
        self.l23.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=24")
        lec_slot_list=lec_slot.fetchall()
        self.l24.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=25")
        lec_slot_list=lec_slot.fetchall()
        self.l25.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=26")
        lec_slot_list=lec_slot.fetchall()
        self.l26.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=27")
        lec_slot_list=lec_slot.fetchall()
        self.l27.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=28")
        lec_slot_list=lec_slot.fetchall()
        self.l28.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=29")
        lec_slot_list=lec_slot.fetchall()
        self.l29.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=30")
        lec_slot_list=lec_slot.fetchall()
        self.l30.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=31")
        lec_slot_list=lec_slot.fetchall()
        self.l31.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=32")
        lec_slot_list=lec_slot.fetchall()
        self.l32.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=33")
        lec_slot_list=lec_slot.fetchall()
        self.l33.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=34")
        lec_slot_list=lec_slot.fetchall()
        self.l34.setText(lec_slot_list[0][0])

        lec_slot=cursor.execute("select Subject_Name from Lecture_Slot where Slot_ID=35")
        lec_slot_list=lec_slot.fetchall()
        self.l35.setText(lec_slot_list[0][0])
        
    


#main

app = QApplication(sys.argv)
mainwindow = MainWindow()

widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.show()


app.exec_()
#sys.exit(gui.exec_())





