import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import json
import sqlite3

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("kishore_Welcome(Gui).ui",self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("kishore_login(gui).ui",self)
        self.login.clicked.connect(self.loginfunction)
        self.home.clicked.connect(self.welcomefunction)
    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()

        if len(username)==0 or len(password)==0:
            self.error.setText("Please input all Fields")

        else:
            with open('login.json') as f:
                data = json.load(f)

            for users in data['user_login']:
                if users['username'] == username and users['password'] == password:
                    print("logedin succesfully")
                    self.error.setText("Succesfully loged in.")
                    self.login.clicked.connect(self.welcomefunction)
                    break
            else:
                print("logedin not succesfully")
                self.error.setText("Invalid user name or password.")

    def welcomefunction(self):
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen,self).__init__()
        loadUi("kishore_signup_page(gui).ui",self)
        self.signup.clicked.connect(self.signupfunction)
        self.home2.clicked.connect(self.welcomefunction)

    def welcomefunction(self):
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupfunction(self):
        username = self.username.text()
        password = self.password.text()
        confirmpassword = self.confirmpassword.text()

        if len(username)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error1.setText("Please Fill in all the inputs")

        elif password != confirmpassword:
            self.error1.setText("Password did not matched")

        else:
            with open('login.json', "r+") as file:
                data = json.load(file)
                list1 = data['user_login']
                for users in data['user_login']:
                    if users['username'] == username:
                        self.error1.setText("User name is already exists")
                        break
                else:
                    list1.extend([{'username':username,'password':password}])
                    data['user_login'] = list1
                    file.seek(0)
                    json.dump(data, file)

                    fillprofile = FillProfileScreen()
                    widget.addWidget(fillprofile)
                    widget.setCurrentIndex(widget.currentIndex()+1)

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen,self).__init__()
        loadUi("kishore_completeprofile(gui).ui",self)
        self.continue1.clicked.connect(self.fillupfunction)
        self.home3.clicked.connect(self.welcomefunction)

    def fillupfunction(self):
        username = self.username.text()
        First_Name = self.firstname.text()
        Last_Name = self.lastname.text()

        if len(username)==0 or len(First_Name)==0 or len(Last_Name)==0:
            self.error2.setText("Please in all the inputs")

        else:
            self.continue1.clicked.connect(self.welcomefunction)

    def welcomefunction(self):
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")