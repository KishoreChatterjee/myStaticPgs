# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kishore_completeprofile(gui).ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1109, 834)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 1101, 831))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 261, 41))
        self.label_2.setStyleSheet("font: 20pt \"MS Serif\";\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 291, 51))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 81, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 270, 91, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 350, 91, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(240, 190, 341, 51))
        self.username.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.username.setText("")
        self.username.setObjectName("username")
        self.firstname = QtWidgets.QLineEdit(Dialog)
        self.firstname.setGeometry(QtCore.QRect(240, 270, 341, 51))
        self.firstname.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.firstname.setObjectName("firstname")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(640, 270, 91, 41))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lastname = QtWidgets.QLineEdit(Dialog)
        self.lastname.setGeometry(QtCore.QRect(740, 270, 341, 51))
        self.lastname.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.lastname.setObjectName("lastname")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(640, 350, 71, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(740, 360, 101, 31))
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(770, 190, 231, 28))
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.continue1 = QtWidgets.QPushButton(Dialog)
        self.continue1.setGeometry(QtCore.QRect(460, 500, 151, 51))
        self.continue1.setStyleSheet("color: black;\n"
"background-color: rgb(190, 159, 35);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px ;")
        self.continue1.setObjectName("continue1")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(240, 360, 341, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.error2 = QtWidgets.QLabel(Dialog)
        self.error2.setGeometry(QtCore.QRect(370, 440, 341, 51))
        self.error2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.error2.setText("")
        self.error2.setObjectName("error2")
        self.home3 = QtWidgets.QPushButton(Dialog)
        self.home3.setGeometry(QtCore.QRect(460, 590, 151, 51))
        self.home3.setStyleSheet("color: black;\n"
"background-color: rgb(190, 159, 35);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px ;")
        self.home3.setObjectName("home3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Fill in your profile</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Please complete your profile."))
        self.label_4.setText(_translate("Dialog", "Username"))
        self.label_5.setText(_translate("Dialog", "First Name"))
        self.label_6.setText(_translate("Dialog", "Birthday"))
        self.label_7.setText(_translate("Dialog", "Last Name"))
        self.label_8.setText(_translate("Dialog", "Gender"))
        self.comboBox.setItemText(0, _translate("Dialog", "Male"))
        self.comboBox.setItemText(1, _translate("Dialog", "Female"))
        self.comboBox.setItemText(2, _translate("Dialog", "Transgender"))
        self.pushButton.setText(_translate("Dialog", "Upload your photo"))
        self.continue1.setText(_translate("Dialog", "Continue"))
        self.continue1.clicked.connect(self.goTosignup)
        self.home3.setText(_translate("Dialog", "Home"))
        self.home3.clicked.connect(self.goToHome)

    def goTosignup(self):
        username = self.username.text()
        First_Name = self.firstname.text()
        Last_Name = self.lastname.text()

        if len(username) == 0 or len(First_Name) == 0 or len(Last_Name) == 0:
            self.error2.setText("Please in all the inputs")

        else:
            Dialog.close()
            os.system('python signpg.py')

    def goToHome(self):
        Dialog.close()
        os.system('python welcome.py')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
