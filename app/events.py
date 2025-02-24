# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/events.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from models import session,events
import datetime
import dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
class Ui_MainWindow(QMainWindow,object):
    def home(self):
         pass
    def reg_event(self):
        e  = session.query(events).filter_by(id=1).first()
        if not e:
                if self.dateEdit.date() <= datetime.datetime.now():
                        new_event = events(title=self.title.text(),info=self.info.text(),dueDate=str(self.dateEdit.dateTime().toPyDateTime().date()))
                        session.add(new_event)
                        session.commit()
                        Dialog = QtWidgets.QDialog()
                        ui_dialog = dialog.Ui_Dialog()
                        ui_dialog.win_title = 'Message'
                        ui_dialog.title_="Successt"
                        ui_dialog.message_head=f"The event was added successfully."
                        ui_dialog.setupUi(Dialog)
                        Dialog.show() 
                        Dialog.exec_()   
        else:
                        e.title = self.title.text()
                        e.dueDate = self.dateEdit.dateTime().toPyDateTime().date()
                        e.info = self.info.text()
                        session.commit()
                        Dialog = QtWidgets.QDialog()
                        ui_dialog = dialog.Ui_Dialog()
                        ui_dialog.win_title = 'Message'
                        ui_dialog.title_="Successt"
                        ui_dialog.message_head=f"The event was added successfully."
                        ui_dialog.setupUi(Dialog)
                        Dialog.show() 
                        Dialog.exec_()   

            
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1021, 961))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/pexels-irina-iriser-1379636.jpg"))
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
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(50, 190, 711, 71))
        self.title.setStyleSheet("font: 20pt \"Segoe MDL2 Assets\";")
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 511, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_4.setObjectName("label_4")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(50, 670, 271, 51))
        self.submit.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.reg_event)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(510, 670, 271, 51))
        self.cancel.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(MainWindow.close)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 450, 511, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(50, 340, 621, 81))
        self.dateEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 9), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2100, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 9), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2024, 1, 9))
        self.dateEdit.setObjectName("dateEdit")
        self.info = QtWidgets.QLineEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(50, 490, 631, 161))
        self.info.setObjectName("info")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "EVENTS"))
        self.label_2.setText(_translate("MainWindow", "ADD NEW EVENT"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Date of Event"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_5.setText(_translate("MainWindow", "More info:"))
        self.info.setPlaceholderText(_translate("MainWindow",'A brief summary...'))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
