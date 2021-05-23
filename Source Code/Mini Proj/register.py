import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
#from PyQt5.uic import loadUi
import register_rc
import pyodbc

conn=pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-8UVAR6B;"
                "Database=PPAP;"
                "Trusted_Connection=yes;"
            ) #connection

cursor=conn.cursor()

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
        self.show_popup()
        

    def show_popup(self):
        msg = QMessageBox()
        msg.setText("Successfully Registered!")
        msg.setIcon(QMessageBox.Information)
    
        msg.setStandardButtons(QMessageBox.Ok) 
        msg.setDefaultButton(QMessageBox.Ok)

        msg.buttonClicked.connect(self.gotologin)
        x = msg.exec_()  # this will show our messagebox

     #   def popup_button(self, i):
        #	print(i.text())
        

    
    


    def gotologin(self):
        from main import Login
        self.close()
        createacc = Login()

gui = QtWidgets.QApplication(sys.argv)
UIwindow = Register()
#UIwindow.show()
#widget=QtWidgets.QStackedWidget()
gui.exec_()
#sys.exit(gui.exec_())


