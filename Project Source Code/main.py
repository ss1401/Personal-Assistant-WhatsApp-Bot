import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
#from PyQt5.uic import loadUi
import Login_rc
import pyodbc

conn=pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-8UVAR6B;"
                "Database=PPAP;"
                "Trusted_Connection=yes;"
            ) #connection

cursor=conn.cursor()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi('UI/login.ui', self)
        print("In login class")
        self.show()
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
                #cursor.execute('update enroll set enrollid = (?) where faltu = 1;',(enrollmentid))
                #conn.commit()
                self.loginbutton.clicked.connect(self.gotoTimetalbe())

            else:
                self.warning.setText("Invalid Password!")
                #print("Invalid Password!")
        
        except:
            #print("Invalid Email!")
            self.warning.setText("Invalid Email!")
    
    
    def gotoregister(self):
        from register import Register
        self.close()

        createacc = Register()
        

    def gotoTimetalbe(self):
        print("im in gotogroup before import")
        from timetable import MainWindow
        print("im in gotogroup")
        self.close()

        tt = MainWindow()

    def gotoregister(self):
        from register import Register
        self.close()
        createacc = Register()
        #Mywindow1.createaccfunction(Mywindow1)

        #widget.addWidget(createacc)
        #widget.setCurrentIndex(widget.currentIndex()+1)





gui = QtWidgets.QApplication(sys.argv)
UIwindow = Login()
#UIwindow.show()
#widget=QtWidgets.QStackedWidget()
gui.exec_()
#sys.exit(gui.exec_())
