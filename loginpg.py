import json
from PyQt5 import QtCore, QtGui, QtWidgets
import os
class Login_Ui_Dialog(object):

    def homeButtonClick(self, MainWindow):
        Dialog.close()
        os.system('python welcome.py')

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
                   # self.login.clicked.connect(self.welcomefunction)
                    break
            else:
                print("logedin not succesfully")
                self.error.setText("Invalid user name or password.")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login Page")
        MainWindow.resize(1087, 775)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 1091, 771))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(410, 110, 171, 61))
        self.label_2.setStyleSheet("font: 20pt \"MS Serif\";\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(330, 170, 331, 61))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(330, 260, 71, 31))
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(MainWindow)
        self.username.setGeometry(QtCore.QRect(330, 290, 341, 51))
        self.username.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(MainWindow)
        self.password.setGeometry(QtCore.QRect(330, 390, 341, 51))
        self.password.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(330, 360, 71, 31))
        self.label_5.setObjectName("label_5")
        self.login = QtWidgets.QPushButton(MainWindow)
        self.login.setGeometry(QtCore.QRect(390, 510, 201, 51))
        self.login.setStyleSheet("color: black;\n"
"background-color: rgb(190, 159, 35);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px ;")
        self.login.setObjectName("login")
        self.error = QtWidgets.QLabel(MainWindow)
        self.error.setGeometry(QtCore.QRect(330, 450, 371, 51))
        self.error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.error.setText("")
        self.error.setObjectName("error")
        self.home = QtWidgets.QPushButton(MainWindow)
        self.home.setGeometry(QtCore.QRect(390, 610, 201, 51))
        self.home.setStyleSheet("color: black;\n"
"background-color: rgb(190, 159, 35);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px ;")
        self.home.setObjectName("home")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login Page", "LoginPage"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Login</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sign in to your existing account</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.login.setText(_translate("MainWindow", "Log in"))
        self.login.clicked.connect(self.loginfunction)
        self.home.setText(_translate("MainWindow", "Home"))
        self.home.clicked.connect(self.homeButtonClick)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Login_Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
