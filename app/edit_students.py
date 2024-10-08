
from models import Classroom,Teachers,Students,Subjects,Parents,session
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from dialog import Ui_Dialog
from datetime import datetime
import sys

class Ui_MainWindow(QMainWindow,object):
    def __init__(self):
        pass
    def canceled(self):
        pass
    def register(self):
        student = session.query(Students).filter_by(index_no=self.adm_no.text()).first()
        if student:
            student.full_name = self.full_name.text().upper()
            student.admission_date = self.full_name.text()
            student.classroom = self.comboBox.currentText()
            student.dob = self.dob.text()
            student.guardian = self.guardian.text().upper()
            student.index_no = int(self.adm_no.text())
            session.commit()
            s = session.query(Students).filter_by(index_no=int(self.adm_no.text())).first()
            for i in s:
                #uSE A QDIALOG BOX           
                Dialog = QtWidgets.QDialog()
                ui_dialog = Ui_Dialog()
                ui_dialog.win_title = 'Success'
                ui_dialog.title = f'USER {i.full_name} HAS BEEN UPDATED'
                ui_dialog.message_head='SOME INFO:'
                ui_dialog.info = 'Name:'
                ui_dialog.info_2 = i.full_name
                ui_dialog.more_info_1 = f"Adm no: {i.index_no}"
                ui_dialog.more_info_2=f"Class room: {i.classroom}"
                ui_dialog.setupUi(Dialog)
                Dialog.show() 
                Dialog.exec_()
                
                    
        else:
                Dialog = QtWidgets.QDialog()
                ui_dialog = Ui_Dialog()
                ui_dialog.win_title='Error'
                ui_dialog.title=f'STUDENT DOES NOT EXISTS'
                ui_dialog.message_head='The student you are trying to enter into the database DOES NOT exists!'            
                ui_dialog.setupUi(Dialog)
                Dialog.show()
                Dialog.exec_()   
                
             #CLEAR THE TEXT  
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/660921-84.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 1021, 961))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/pexels-francesco-ungaro-1526713.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 40, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 87 22pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 191, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_3.setObjectName("label_3")
        self.full_name = QtWidgets.QLineEdit(self.centralwidget)
        self.full_name.setGeometry(QtCore.QRect(50, 190, 711, 71))
        self.full_name.setStyleSheet("font: 20pt \"Segoe MDL2 Assets\";")
        self.full_name.setObjectName("full_name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 511, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_4.setObjectName("label_4")
        self.adm_no = QtWidgets.QLineEdit(self.centralwidget)
        self.adm_no.setGeometry(QtCore.QRect(50, 350, 711, 71))
        self.adm_no.setStyleSheet("font: 20pt \"Segoe MDL2 Assets\";")
        self.adm_no.setObjectName("adm_no")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 450, 411, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_5.setObjectName("label_5")
        self.guardian = QtWidgets.QLineEdit(self.centralwidget)
        self.guardian.setGeometry(QtCore.QRect(50, 500, 711, 71))
        self.guardian.setStyleSheet("font: 20pt \"Segoe MDL2 Assets\";")
        self.guardian.setText("")
        self.guardian.setObjectName("guardian")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 610, 191, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_6.setObjectName("label_6")
        self.dob = QtWidgets.QLineEdit(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(50, 660, 711, 71))
        self.dob.setStyleSheet("font: 20pt \"Segoe MDL2 Assets\";")
        self.dob.setObjectName("dob")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 760, 191, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 810, 691, 51))
        self.comboBox.setObjectName("comboBox")
        classrooms = session.query(Classroom).all()
        for classroom in classrooms:
             self.comboBox.addItem(f"{classroom.form} {classroom.stream}")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(50, 890, 271, 51))
        self.submit.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.register)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(510, 890, 271, 51))
        self.cancel.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit Student"))
        self.label_2.setText(_translate("MainWindow", "EDIT STUDENT"))
        self.label_3.setText(_translate("MainWindow", "Full Name:"))
        self.label_4.setText(_translate("MainWindow", "Admission number:"))
        self.label_5.setText(_translate("MainWindow", "Guardian\'s name:"))
        self.label_6.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_7.setText(_translate("MainWindow", "Class Assigned:"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
