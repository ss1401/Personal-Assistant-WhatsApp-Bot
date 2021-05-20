from announcement import Announcement
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
#from PyQt5.uic import loadUi
import pandas as pd
import Login_rc
import register_rc
import attendance_rc
import pyodbc

conn=pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-8UVAR6B;"
                "Database=PPAP;"
                "Trusted_Connection=yes;"
            ) #connection

cursor=conn.cursor()

"""
def gotoTimetable():
        page2=Timetable()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)
"""
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
            print("Correct pass ", corrpass_list[0][0], " INPUT ENROLL: ", password)

            if corrpass_list[0][0]==password: # checks password
                print("LOGIN SUCCESFULL")
                self.loginbutton.clicked.connect(self.gotoAttd())

            else:
                self.warning.setText("Invalid Password!")
        
        except:
            self.warning.setText("Invalid Email!")
    
    def gotoregister(self):
        page2=Register()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def gotoAttd(self):
        page5=Attendance()
        widget.addWidget(page5)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Register,self).__init__()
        uic.loadUi('UI/register.ui', self)
        print("In register class")
        self.show()
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

    def gotologin(self):
        page1=Login()
        widget.addWidget(page1)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Attendance(QtWidgets.QMainWindow):
    def __init__(self):
        super(Attendance,self).__init__()
        uic.loadUi('UI/attendance.ui', self)
        self.browse.clicked.connect(self.browsefiles)
        self.assignmentbutton.clicked.connect(self.gotoassignment)
        self.announcementbutton.clicked.connect(self.gotoannouncement)
        self.announcementbutton.clicked.connect(self.gotoannouncement)


    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\Dell\\Downloads', 'CSV (*.csv)')
        #self.filename.setText(fname[0])
        file=fname[0]
        
        df = pd.read_csv(file)

        columns = ['Date', 'Roll_No', 'Slot_ID','Attd']
        
        df_data = df[columns]
        records = df_data.values.tolist()
        print(records)


        cursor=conn.cursor()
        x=len(records)
        for i in range(x):
            cursor.execute("INSERT into Attendance values (?,?,?,?)", (records[i][0],records[i][1],records[i][2],records[i][3]))
            conn.commit()

        self.registerbutton.clicked.connect(self.registerfunction)


class Announcement(QtWidgets.QMainWindow):
    def __init__(self):
        super(Announcement,self).__init__()
        uic.loadUi('UI/announcement.ui', self)
        self.postbutton.clicked.connect(self.Postfunction)

    def Postfunction(self):
        announcement = self.announcement.text()
        name = self.name.text()
        print("Successfully registerd in with announcement: ", announcement, "and name:", name,)



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
