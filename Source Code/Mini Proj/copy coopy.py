import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox
#from PyQt5.uic import loadUi
import pandas as pd
import Login_rc
import register_rc
import attendance_rc
import announcement_rc
import assignment_rc
import timetable_rc
import pyodbc
import time
from selenium import webdriver
records=list()



conn=pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-8UVAR6B;"
                "Database=PPAP;"
                "Trusted_Connection=yes;"
            ) #connection

cursor=conn.cursor()


def gotoAttendance():
        page=Attendance()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

def gotoAssignment():
        page=Assignment()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

def gotoAnnouncement():
        page=Announcement()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

def gotoTimetable():
        page=Timetable()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi('UI/login.ui', self)
        print("In login class")
        #self.show()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.registerbutton.clicked.connect(self.gotoregister)
        

    def loginfunction(self):
        
        email = self.email.text()
        password = self.password.text()
        print("Successfully logged in with email: ", email, "and enrollment id:", password)
        cursor = conn.cursor()

        try:
            corrpass = cursor.execute("select Password from Teacher where Teacher_Email = (?)", (email))
            corrpass_list = corrpass.fetchall()
            print("Correct pass ", corrpass_list[0][0], " INPUT password: ", password)

            if corrpass_list[0][0]==password: # checks password
                print("LOGIN SUCCESFULL")
                gotoTimetable()

            else:
                self.warning.setText("Invalid Password!")
        
        except:
            self.warning.setText("Invalid Email!")
    
    def gotoregister(self):
        page2=Register()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Register,self).__init__()
        uic.loadUi('UI/register.ui', self)
        print("In register class")
        #self.show()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerbutton.clicked.connect(self.registerfunction)
        self.loginbutton.clicked.connect(self.gotologin)
      
    def registerfunction(self):
        email = self.email.text()
        password = self.password.text()
        name = self.name.text()
        number = self.number.text()

        cursor.execute("insert into Teacher values (?,?,?,?)",(email,name,number,password))
        print("Successfully registerd in with email: ", email, "and password:", password, " and name:", name, " and number:", number)

        conn.commit()
        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Successfully Registered!")
        msg.setIcon(QMessageBox.Information)
    
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(self.gotologin)
        x = msg.exec_()

    def gotologin(self):
        page1=Login()
        widget.addWidget(page1)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Attendance(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Attendance,self).__init__()
        uic.loadUi('UI/attendance.ui', self)
        
        self.browse.clicked.connect(self.browsefiles)

        self.timetalblebutton.clicked.connect(gotoTimetable)
        self.announcementbutton.clicked.connect(gotoAnnouncement)
        self.assignmentbutton.clicked.connect(gotoAssignment)
        self.attendancebutton.clicked.connect(gotoAttendance)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Dell\\Downloads', 'CSV (*.csv)')
        #self.filename.setText(fname[0])
        file=fname[0]
        self.browse.setText(file)
        df = pd.read_csv(file)

        columns = ['Date', 'Roll_No', 'Slot_ID','Attd']
        
        df_data = df[columns]
        global records
        records = df_data.values.tolist()
        self.uploadbutton.clicked.connect(self.update)

    def update(self):
        
        print(type(records))
        
        
        cursor=conn.cursor()
        x=len(records)
        for i in range(x):
            cursor.execute("INSERT into Attendance values (?,?,?,?)", (records[i][0],records[i][1],records[i][2],records[i][3]))
            conn.commit()

        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Attendance Updated!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(gotoAttendance)
        x = msg.exec_()
        

class Announcement(QtWidgets.QMainWindow):
    def __init__(self):
        super(Announcement,self).__init__()
        uic.loadUi('UI/announcement.ui', self)
        self.postbutton.clicked.connect(self.Postfunction)

        self.timetalblebutton.clicked.connect(gotoTimetable)
        self.announcementbutton.clicked.connect(gotoAnnouncement)
        self.assignmentbutton.clicked.connect(gotoAssignment)
        self.attendancebutton.clicked.connect(gotoAttendance)


    def Postfunction(self):
        announcement = self.announcement.text()
        name = self.name.text()
        print("Successfully announcement: ", announcement, "and name:", name,)
        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Announcement Sent!")
        msg.setIcon(QMessageBox.Information)
        #msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(gotoAnnouncement)
        x = msg.exec_()


class Assignment(QtWidgets.QMainWindow):
    def __init__(self):
        super(Assignment,self).__init__()
        uic.loadUi('UI/assignment.ui', self)
        self.addbutton.clicked.connect(self.Addfunction)

        self.timetalblebutton.clicked.connect(gotoTimetable)
        self.announcementbutton.clicked.connect(gotoAnnouncement)
        self.assignmentbutton.clicked.connect(gotoAssignment)
        self.attendancebutton.clicked.connect(gotoAttendance)

    def Addfunction(self):
        acode = self.acode.text()
        aname = self.aname.text()
        duedate = self.duedate.text()
        subjectname = self.subjectname.text()
        print("Successfully registerd in with acode: ", acode, "and aname:", aname, " duedate:", duedate, " and subname:", subjectname)
        cursor=conn.cursor()
        cursor.execute("INSERT into Assignment values (?,?,?,?)",(acode,aname,duedate,subjectname))
        conn.commit()
        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Assignment Added!")
        msg.setIcon(QMessageBox.Information)
        #msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(gotoAssignment)
        x = msg.exec_()


class Timetable(QtWidgets.QMainWindow):

    
    def __init__(self):
            super(Timetable,self).__init__()
            uic.loadUi('UI/timetable.ui', self)
            show=self.ShowTT()
            self.searchbutton.clicked.connect(self.Searchfunction)
            self.updatebutton.clicked.connect(self.Updatefunction)

            self.timetalblebutton.clicked.connect(gotoTimetable)
            self.announcementbutton.clicked.connect(gotoAnnouncement)
            self.assignmentbutton.clicked.connect(gotoAssignment)
            self.attendancebutton.clicked.connect(gotoAttendance)


    
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
        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Timetable Updated!")
        msg.setIcon(QMessageBox.Information)
        #msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(gotoTimetable)
        x = msg.exec_()
        


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

gui = QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
page1=Login()
widget.addWidget(page1)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.setCurrentIndex(widget.currentIndex())
widget.show()
sys.exit(gui.exec_())
