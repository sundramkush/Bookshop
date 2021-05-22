import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

connection = sqlite3.connect('BookStore.db')
cur = connection.cursor()

class Ui_Dialog(object):

    def displayMsg(self,msg,title='Information'):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setText(msg)
        MsgBox.setWindowTitle(title)
        MsgBox.setIcon(QtWidgets.QMessageBox.Information)
        MsgBox.exec()


    def findPrice(self):
        title = self.lineEdit.text()
        result = cur.execute("SELECT * FROM books WHERE title='"+title+"';")
        book = result.fetchone()
        if book == None:
            self.displayMsg("Sorry, we don't have that book")
            return None
        else:
            self.displayMsg("Yes, we have that book.\n\nTitle: {}\nAuthor: {}\nPrice: {}".format(book[0],book[1],book[2]))
            self.label_4.setText(str(book[2]))
            return book[2]

    def findTotal(self):
        quantity = int(self.lineEdit_2.text()) if self.lineEdit_2.text() != "" else 0
        price = self.findPrice()
        if price != None:
            self.label_6.setText(str(price*quantity))
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(306, 205)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        regexp = QtCore.QRegExp('^\d+$')
        validator = QtGui.QRegExpValidator(regexp)
        self.lineEdit_2.setValidator(validator)
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #Slots
        self.pushButton.clicked.connect(self.findPrice)
        self.pushButton_2.clicked.connect(self.findTotal)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Book Selling System"))
        self.label.setText(_translate("Dialog", "Book Title:"))
        self.pushButton.setText(_translate("Dialog", "Find Price"))
        self.label_3.setText(_translate("Dialog", "Price: "))
        self.label_2.setText(_translate("Dialog", "Quantity:"))
        self.pushButton_2.setText(_translate("Dialog", "Find Total"))
        self.label_5.setText(_translate("Dialog", "Total: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

