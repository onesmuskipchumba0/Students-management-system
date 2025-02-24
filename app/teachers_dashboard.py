# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teachers_dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from models import Teachers,session
import dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
class Ui_Form(QMainWindow,object):
    def search_(self):
        students = session.query(Teachers).filter_by(full_name=self.search.text().upper()).all()
        if len(students)>0:
            for i, student in enumerate(students):
                    self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(str(student.id)))
                    self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(student.full_name))
                    self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(student.contacts))
                    self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(student.subjects))
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(student.location))
                    self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(student.date_hired))
        else:
                Dialog = QtWidgets.QDialog()
                ui_dialog = dialog.Ui_Dialog()
                ui_dialog.win_title='Error'
                ui_dialog.title_='Name search error'
                ui_dialog.message_head='This is because: '
                ui_dialog.more_info_1 = ''' You may have entered only one name and not the full name, You may have mispelled the name, You entered a name without a space.eg,onesmusbett instead of onesmus bett
                '''
                ui_dialog.setupUi(Dialog)
                Dialog.show()
                Dialog.exec_() 
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1900, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/660921-84.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 1841, 900))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 226, 232);")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.search = QtWidgets.QLineEdit(Form)
        self.search.setGeometry(QtCore.QRect(20, 20, 391, 71))
        self.search.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.search.setObjectName("search")
        self.search_btn = QtWidgets.QPushButton(Form)
        self.search_btn.setGeometry(QtCore.QRect(430, 20, 161, 71))
        self.search_btn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/sign-out-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search_)
        self.home = QtWidgets.QPushButton(Form)
        self.home.setGeometry(QtCore.QRect(670, 20, 201, 71))
        self.home.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 85, 0);")
        self.home.clicked.connect(Form.close)
        self.home.setObjectName("home")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Teachers Database"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Contacts"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Subjects Taught"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Home"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Day Hired"))
        students = session.query(Teachers).all()
        self.tableWidget.setRowCount(len(students))

        for i, student in enumerate(students):
            self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(str(student.id)))
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(student.full_name))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(student.contacts))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(student.subjects))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(student.location))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(student.date_hired))
        self.search.setPlaceholderText(_translate("Form", "Search full name..."))
        self.search_btn.setText(_translate("Form", "search"))
        self.home.setText(_translate("Form", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
